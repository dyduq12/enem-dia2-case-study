import json
import re

with open("delta_files_info.json", "r", encoding="utf-8") as f:
    files = json.load(f)

print(f"Total files loaded: {len(files)}")

paulistas_kw = ["fuvest", "unicamp", "unesp", "uerj", "uece", "olimpiada", "paulista"]
dia1_kw = ["dia 1", "dia 01", "dia1", "1º dia", "1° dia", "1ºdia", "prova 1", "prova i", "prova1", "d1"]
dia2_kw = ["dia 2", "dia 02", "dia2", "2º dia", "2° dia", "2ºdia", "prova 2", "prova ii", "prova2", "d2"]

classified = []
for item in files:
    rel = item["rel"]
    rel_lower = rel.lower()
    sample = item["sample"].lower()
    ext = item["ext"]
    pages = item["pages"]
    
    status = None
    reason = None
    
    # Check non-pdf or zero size
    if ext != ".pdf":
        status = "DESCARTADO"
        reason = f"Arquivo não-PDF ({ext}) / Anexo auxiliar"
    elif item["sz_mb"] == 0:
        status = "DESCARTADO"
        reason = "Arquivo corrompido / 0 bytes"
    # Check Trilhas
    elif "trilhas" in rel_lower:
        status = "DESCARTADO"
        reason = "Material didático modular / Trilha pedagógica (não é simulado ENEM)"
    # Check Paulistas / Outros Vestibulares
    elif any(kw in rel_lower for kw in paulistas_kw) or any(kw in sample for kw in ["fuvest", "unicamp", "unesp", "uerj"]):
        status = "DESCARTADO"
        for kw in paulistas_kw:
            if kw in rel_lower:
                reason = f"Caderno de outro vestibular ({kw.upper()})"
                break
        if not reason:
            reason = "Caderno de outro vestibular (Paulista/Estadual)"
    # Check Dia 1
    elif any(k in rel_lower for k in ["dia 1", "dia 01", "dia1", "1º dia", "1° dia", "1ºdia", "prova 1", "prova i", "prova1", " d1", "- d1", "-d1"]):
        # Make sure it's not Dia 2
        if not any(k in rel_lower for k in ["dia 2", "dia 02", "dia2", "2º dia", "2° dia", "2ºdia", "prova 2", "prova ii", "prova2", " d2", "- d2", "-d2"]):
            status = "DESCARTADO"
            reason = "ENEM 1º Dia (Linguagens, Códigos e Ciências Humanas)"
    
    # If not yet discarded, check Dia 2 indications or sample content
    if not status:
        if any(k in rel_lower for k in ["dia 2", "dia 02", "dia2", "2º dia", "2° dia", "2ºdia", "prova 2", "prova ii", "prova2", " d2", "- d2", "-d2"]):
            status = "VALIDO_DIA2"
            reason = "Caderno / Gabarito Comentado ENEM Dia 2 (Matemática e Ciências da Natureza)"
        else:
            # Ambiguous filename, inspect sample text and path
            if "ciências da natureza" in sample or "matemática" in sample or "matematica" in sample:
                status = "VALIDO_DIA2"
                reason = "Identificado via conteúdo como ENEM Dia 2 (Matemática e Ciências da Natureza)"
            elif "linguagens" in sample or "ciências humanas" in sample or "redação" in sample:
                status = "DESCARTADO"
                reason = "Identificado via conteúdo como ENEM 1º Dia (Linguagens/Humanas)"
            else:
                status = "A_REVISAR"
                reason = "Requer inspeção manual de páginas e texto"
                
    classified.append({
        "rel": rel,
        "sz_mb": item["sz_mb"],
        "pages": pages,
        "status": status,
        "reason": reason,
        "sample": item["sample"][:150]
    })

val_count = sum(1 for c in classified if c["status"] == "VALIDO_DIA2")
desc_count = sum(1 for c in classified if c["status"] == "DESCARTADO")
rev_count = sum(1 for c in classified if c["status"] == "A_REVISAR")

print(f"\nClassificação Preliminar:")
print(f"  Válidos Dia 2: {val_count}")
print(f"  Descartados: {desc_count}")
print(f"  A revisar: {rev_count}")

if rev_count > 0:
    print("\nArquivos A REVISAR:")
    for c in classified:
        if c["status"] == "A_REVISAR":
            print(f"  {c['rel']} (pages: {c['pages']}, sz: {c['sz_mb']:.2f} MB)")
            print(f"    sample: {c['sample']}")
