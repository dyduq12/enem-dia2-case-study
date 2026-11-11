import json
import os
import re

with open("delta_files_hashed.json", "r", encoding="utf-8") as f:
    files = json.load(f)

paulistas_kw = ["fuvest", "unicamp", "unesp", "uerj", "uece", "olimpiada", "paulista"]

final_classified = []
for item in files:
    rel = item["rel"]
    rel_lower = rel.lower().replace("_", " ").replace("-", " ")
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
        justification = f"Descartado: Arquivo em formato não-PDF ({ext}) / Anexo inválido"
    # 2. Corrupted / 0 bytes
    elif sz_mb == 0 or (pages == 0 and sz_mb < 0.01):
        status = "DESCARTADO"
        justification = "Descartado: Arquivo vazio (0 bytes) ou corrompido"
    # 3. Trilhas / Didático modular
    elif "trilhas" in item["rel"].lower():
        status = "DESCARTADO"
        justification = "Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM)"
    # 4. Paulistas / Outros vestibulares
    elif any(kw in item["rel"].lower() for kw in paulistas_kw) or any(kw in sample for kw in ["fuvest", "unicamp", "unesp", "uerj"]):
        matched = [kw.upper() for kw in paulistas_kw if kw in item["rel"].lower()]
        vest_name = matched[0] if matched else "Paulista/Estadual"
        status = "DESCARTADO"
        justification = f"Descartado: Caderno de outro vestibular ({vest_name})"
    # 5. Scanned without OCR
    elif "res - 1º simulado bernoulli.pdf" in item["rel"].lower():
        status = "DESCARTADO"
        justification = "Descartado: Arquivo rasterizado/escaneado sem camada OCR (o conteúdo correspondente do 1º Simulado 2024 Dia 2 está presente de forma digital nativa no arquivo irmão 'SIMULADO 1 - GABARITO COMENTADO.pdf')"
    # 6. Dia 1 indicators in relative path or filename
    elif any(d1 in rel_lower for d1 in ["dia 1", "dia 01", "dia1", "1º dia", "1° dia", "1ºdia", "1o dia", "1o. dia", "prova 1", "prova i", "prova1", " d1", "d1."]):
        # Double check if it explicitly mentions Dia 2
        if not any(d2 in rel_lower for d2 in ["dia 2", "dia 02", "dia2", "2º dia", "2° dia", "2ºdia", "2o dia", "prova 2", "prova ii", "prova2", " d2", "d2."]):
            status = "DESCARTADO"
            justification = "Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação)"
    # Check duplicate of a Dia 1 file by hash
    elif sha256 == "43d93bfbb6e257dbda6e1ee76964a27fe878c9d2fbeadabce5a5931215442fb8": # Gabarito simulado Enem .pdf
        status = "DESCARTADO"
        justification = "Descartado: Caderno do 1º Dia do ENEM (hash idêntico a 2° BERNOULLI 2026 - D1 - GABARITO.pdf)"
    elif "3_conj._2020_-_prova_i_-_resolucao_comentada.pdf" in item["rel"].lower():
        status = "DESCARTADO"
        justification = "Descartado: Caderno do 1º Dia do ENEM (Prova I - Resolução Comentada / Linguagens e Humanas)"
    elif "bernoulli0-1ºdia 2024.pdf" in item["rel"].lower() or "bernoulli2024zero.pdf" in item["rel"].lower():
        status = "DESCARTADO"
        justification = "Descartado: Caderno do 1º Dia do ENEM (Bernoulli 0 - Dia 1)"
    
    # 7. Check if not yet discarded
    if not status:
        if ("linguagens" in sample and "ciências humanas" in sample) and not ("ciências da natureza" in sample or "matemática" in sample):
            status = "DESCARTADO"
            justification = "Descartado: Conteúdo identificado como 1º Dia do ENEM (Linguagens e Ciências Humanas)"
        else:
            status = "VALIDO_DIA2"
            justification = "Válido: Simulado ENEM Dia 2 (Ciências da Natureza e Matemática)"

    final_classified.append({
        "rel": item["rel"],
        "pages": pages,
        "sz_mb": sz_mb,
        "sha256": sha256,
        "status": status,
        "justification": justification
    })

valid = [f for f in final_classified if f["status"] == "VALIDO_DIA2"]
discarded = [f for f in final_classified if f["status"] == "DESCARTADO"]

print(f"Total files: {len(final_classified)}")
print(f"Válidos Dia 2: {len(valid)}")
print(f"Descartados: {len(discarded)}")

with open("delta_final_classified.json", "w", encoding="utf-8") as f:
    json.dump(final_classified, f, ensure_ascii=False, indent=2)
