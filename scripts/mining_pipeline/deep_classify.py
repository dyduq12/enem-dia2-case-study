import json
import os

with open("delta_files_info.json", "r", encoding="utf-8") as f:
    files = json.load(f)

print(f"Total delta files: {len(files)}")

# Let's inspect each folder and file
paulistas_kw = ["fuvest", "unicamp", "unesp", "uerj", "uece", "olimpiada", "paulista"]

results = []
for idx, item in enumerate(files):
    rel = item["rel"]
    rel_lower = rel.lower()
    sample = item["sample"].lower()
    ext = item["ext"]
    pages = item["pages"]
    sz_mb = item["sz_mb"]
    
    # Classification rules
    cat = ""
    discard_reason = ""
    is_valid = False
    
    if ext != ".pdf":
        cat = "DESCARTADO"
        discard_reason = f"Arquivo com formato não-PDF ({ext}) / Anexo inválido"
    elif sz_mb == 0:
        cat = "DESCARTADO"
        discard_reason = "Arquivo corrompido / 0 bytes"
    elif "trilhas" in rel_lower:
        cat = "DESCARTADO"
        discard_reason = "Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM)"
    elif any(kw in rel_lower for kw in paulistas_kw) or any(kw in sample for kw in ["fuvest", "unicamp", "unesp", "uerj"]):
        cat = "DESCARTADO"
        matched = [kw for kw in paulistas_kw if kw in rel_lower]
        if matched:
            discard_reason = f"Caderno de outro vestibular ({matched[0].upper()})"
        else:
            discard_reason = "Caderno de outro vestibular (Paulista/Estadual identificado no texto)"
    elif any(k in rel_lower for k in ["dia 1", "dia 01", "dia1", "1º dia", "1° dia", "1ºdia", "prova 1", "prova i", "prova1", " d1", "- d1", "-d1"]):
        if not any(k in rel_lower for k in ["dia 2", "dia 02", "dia2", "2º dia", "2° dia", "2ºdia", "prova 2", "prova ii", "prova2", " d2", "- d2", "-d2"]):
            cat = "DESCARTADO"
            discard_reason = "ENEM 1º Dia (Linguagens, Códigos e Ciências Humanas / Redação)"
    
    if not cat:
        # Check if it has indicators of Dia 2
        # Either in filename or in sample
        is_dia2_name = any(k in rel_lower for k in ["dia 2", "dia 02", "dia2", "2º dia", "2° dia", "2ºdia", "prova 2", "prova ii", "prova2", " d2", "- d2", "-d2"])
        starts_at_91 = "91 -" in item["sample"] or "91 b" in item["sample"].lower() or "questões de 91" in item["sample"].lower() or "questão 91" in item["sample"].lower() or "ciências da natureza" in sample or "matemática" in sample
        starts_at_1 = "questões de 1 a 45" in sample or "questão 1" in sample or "linguagens" in sample or "ciências humanas" in sample
        
        if is_dia2_name or starts_at_91:
            cat = "VALIDO_DIA2"
            is_valid = True
        elif starts_at_1:
            cat = "DESCARTADO"
            discard_reason = "ENEM 1º Dia (identificado no texto: questões 1 a 90 / Linguagens / Humanas)"
        else:
            # Let's see what is inside
            cat = "A_DETERMINAR"
            discard_reason = "Necessário verificar páginas intermediárias"
            
    results.append({
        "rel": rel,
        "cat": cat,
        "is_valid": is_valid,
        "discard_reason": discard_reason,
        "pages": pages,
        "sz_mb": sz_mb
    })

valid = [r for r in results if r["is_valid"]]
discarded = [r for r in results if not r["is_valid"]]
to_determine = [r for r in results if r["cat"] == "A_DETERMINAR"]

print(f"Valid Dia 2: {len(valid)}")
print(f"Discarded: {len(discarded)}")
print(f"To Determine: {len(to_determine)}")

for td in to_determine:
    print(f"  TD: {td['rel']} (pages: {td['pages']}, sz: {td['sz_mb']:.2f} MB)")
