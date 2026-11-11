import json
import os
import re

with open("delta_files_hashed.json", "r", encoding="utf-8") as f:
    files = json.load(f)

print(f"Loaded {len(files)} files.")

paulistas_kw = ["fuvest", "unicamp", "unesp", "uerj", "uece", "olimpiada", "paulista"]

catalog = []
for item in files:
    rel = item["rel"]
    rel_lower = rel.lower()
    sample = item["sample"].lower()
    ext = item["ext"]
    pages = item["pages"]
    sz_mb = item["sz_mb"]
    sha256 = item.get("sha256", "")
    
    status = ""
    justification = ""
    
    # 1. Non-pdf
    if ext != ".pdf":
        status = "DESCARTADO"
        justification = f"Arquivo em formato não-PDF ({ext}) / Anexo de imagem ou índice corrompido"
    # 2. Corrupted / 0 bytes
    elif sz_mb == 0 or pages == 0 and sz_mb < 0.01:
        status = "DESCARTADO"
        justification = "Arquivo vazio (0 bytes) ou corrompido"
    # 3. Trilhas / Didático modular
    elif "trilhas" in rel_lower:
        status = "DESCARTADO"
        justification = "Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM)"
    # 4. Paulistas / Outros vestibulares
    elif any(kw in rel_lower for kw in paulistas_kw) or any(kw in sample for kw in ["fuvest", "unicamp", "unesp", "uerj"]):
        status = "DESCARTADO"
        matched = [kw.upper() for kw in paulistas_kw if kw in rel_lower]
        vest_name = matched[0] if matched else "Paulista/Estadual"
        justification = f"Descartado: Caderno de outro vestibular ({vest_name})"
    # 5. Scanned without OCR
    elif "res - 1º simulado bernoulli.pdf" in rel_lower:
        status = "DESCARTADO"
        justification = "Descartado: Arquivo rasterizado/scaneado sem camada OCR (o conteúdo correspondente do 1º Simulado 2024 Dia 2 está presente no arquivo digital irmão 'SIMULADO 1 - GABARITO COMENTADO.pdf')"
    # 6. Dia 1
    elif any(k in rel_lower for k in ["dia 1", "dia 01", "dia1", "1º dia", "1° dia", "1ºdia", "prova 1", "prova i", "prova1", " d1", "- d1", "-d1"]):
        # Check if it also says Dia 2
        if not any(k in rel_lower for k in ["dia 2", "dia 02", "dia2", "2º dia", "2° dia", "2ºdia", "prova 2", "prova ii", "prova2", " d2", "- d2", "-d2"]):
            status = "DESCARTADO"
            justification = "Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação)"
    # 7. Check by sample if it's Dia 1
    elif ("linguagens" in sample and "ciências humanas" in sample) and not ("ciências da natureza" in sample or "matemática" in sample):
        status = "DESCARTADO"
        justification = "Descartado: Conteúdo identificado como 1º Dia do ENEM (Linguagens e Ciências Humanas)"
    
    # If still not discarded:
    if not status:
        status = "VALIDO_DIA2"
        justification = "Válido: Caderno / Gabarito Comentado do ENEM Dia 2 (Ciências da Natureza e Matemática)"

    catalog.append({
        "rel": rel,
        "pages": pages,
        "sz_mb": sz_mb,
        "sha256": sha256,
        "status": status,
        "justification": justification
    })

valid_list = [c for c in catalog if c["status"] == "VALIDO_DIA2"]
discard_list = [c for c in catalog if c["status"] == "DESCARTADO"]

print(f"Total scanned: {len(catalog)}")
print(f"Total Válidos Dia 2: {len(valid_list)}")
print(f"Total Descartados: {len(discard_list)}")

with open("delta_catalog.json", "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)
print("Saved delta_catalog.json")
