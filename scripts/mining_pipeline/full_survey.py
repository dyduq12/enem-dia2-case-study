import os
import sys
import re
import json
import logging
import pypdf

logging.getLogger("pypdf").setLevel(logging.ERROR)

BASE_DIRS = [
    'APEIRON-20261110T152018Z-1-001',
    'BERNOULLI-20261110T151947Z-1-001',
    'ENEM',
    'POLIEDRO',
    'SAS',
    '_ENEM_DIA_2_BRUTO'
]

def detect_provider(path_lower, fname_lower):
    if "apeiron" in path_lower or "apeiron" in fname_lower:
        return "APEIRON"
    if "bernoulli" in path_lower or "bernoulli" in fname_lower or "ber_" in fname_lower:
        return "BERNOULLI"
    if "poliedro" in path_lower or "poliedro" in fname_lower or "edros" in fname_lower:
        return "POLIEDRO"
    if "sas" in path_lower or "sas" in fname_lower or "ap2" in fname_lower or "ag2" in fname_lower or "cnst" in fname_lower:
        return "SAS"
    if "enem" in path_lower or "enem" in fname_lower:
        return "ENEM_OFICIAL"
    if "exercício" in fname_lower or "exercicio" in fname_lower:
        return "LISTA_EXERCICIOS"
    return "OUTROS"

def detect_year(path_lower, fname_lower):
    m = re.search(r'(200[9]|201[0-9]|202[0-7])', path_lower + ' ' + fname_lower)
    if m:
        return int(m.group(1))
    m2 = re.search(r'[-_](1[0-9]|2[0-7])[-_ ]', fname_lower)
    if m2:
        return 2000 + int(m2.group(1))
    return None

def detect_doc_type(fname_lower, path_lower):
    if any(k in fname_lower for k in ["resolucao", "resolução", "comentada", "comentadas", "resol"]):
        return "RESOLUCAO_COMENTADA"
    if any(k in fname_lower for k in ["gabarito", "gab", "ag2", "modelo gab"]):
        return "GABARITO"
    if "ficha mapa" in fname_lower or "mapa" in fname_lower:
        return "FICHA_MAPA"
    if "redacao" in fname_lower or "redação" in fname_lower:
        return "REDACAO"
    if any(k in fname_lower for k in ["prova", "caderno", "simulado", "ap2", "cnst", "book"]):
        return "CADERNO_QUESTOES"
    return "OUTRO"

def inspect_pdf_header(filepath):
    """Inspect first 2 pages of PDF to extract text and detect Day / Subjects."""
    text_snippet = ""
    page_count = 0
    try:
        reader = pypdf.PdfReader(filepath)
        page_count = len(reader.pages)
        pages_to_check = min(3, page_count)
        for i in range(pages_to_check):
            t = reader.pages[i].extract_text() or ""
            text_snippet += " " + t
    except Exception as e:
        return page_count, "", f"ERR: {str(e)[:50]}"
    return page_count, text_snippet[:3000], "OK"

def classify_day_and_subjects(fname_lower, path_lower, text_snippet, year):
    combined = (fname_lower + " " + path_lower + " " + text_snippet).lower()
    
    # Non-ENEM exams detection
    is_fuvest = "fuvest" in combined
    is_unicamp = "unicamp" in combined
    is_olimpiada = "olimpiada" in combined or "olimpíada" in combined
    is_ufrgs = "ufrgs" in combined or "ufrs" in combined
    is_uerj = "uerj" in combined
    is_pasunb = "pasunb" in combined

    category = "ENEM"
    if is_olimpiada:
        category = "OLIMPIADA"
    elif is_fuvest:
        category = "FUVEST"
    elif is_unicamp:
        category = "UNICAMP"
    elif is_ufrgs:
        category = "UFRGS"
    elif is_uerj:
        category = "UERJ"
    elif is_pasunb:
        category = "PAS_UNB"

    # Subject signals
    has_cn = any(k in combined for k in [
        "ciências da natureza", "ciencias da natureza", "cnst", "física", "fisica", "química", "quimica", "biologia"
    ])
    has_mat = any(k in combined for k in [
        "matemática e suas tecnologias", "matematica e suas tecnologias", "mst", "matemática", "matematica"
    ])
    has_ch = any(k in combined for k in [
        "ciências humanas", "ciencias humanas", "chst", "história", "geografia", "filosofia", "sociologia"
    ])
    has_lc = any(k in combined for k in [
        "linguagens, códigos", "linguagens e códigos", "lcst", "redação", "língua portuguesa"
    ])

    # Day determination
    # Explicit dia 2 signs
    dia_2_signs = bool(re.search(r'(\bd2\b|\bd-2\b|dia\s*2|2[º°\s_-]*dia|prova\s*(2|ii)|segundo\s*dia|cnst[-_ ]*mst)', fname_lower + ' ' + path_lower))
    # Explicit dia 1 signs
    dia_1_signs = bool(re.search(r'(\bd1\b|\bd-1\b|dia\s*1|1[º°\s_-]*dia|prova\s*(1|i)|primeiro\s*dia|chst[-_ ]*lcst)', fname_lower + ' ' + path_lower))

    # Older ENEM (2009-2016):
    # Dia 1 was Natureza + Humanas
    # Dia 2 was Matemática + Linguagens/Redação
    # Modern ENEM (2017+):
    # Dia 1 is Humanas + Linguagens + Redação
    # Dia 2 is Natureza + Matemática
    
    classification = "OUTRO"
    if year and year < 2017 and "enem" in (fname_lower + path_lower):
        if dia_1_signs or (has_cn and has_ch and not has_mat):
            classification = "ENEM_ANTIGO_D1_CN_CH" # Contains Natureza!
        elif dia_2_signs or (has_mat and has_lc and not has_cn):
            classification = "ENEM_ANTIGO_D2_MAT_LC" # Contains Matemática!
    else:
        if dia_2_signs or (has_cn and has_mat and not has_ch and not has_lc):
            classification = "DIA_2_CN_MAT"
        elif dia_1_signs or (has_ch and has_lc and not has_mat and not has_cn):
            classification = "DIA_1_CH_LC"
        elif has_cn and has_mat:
            classification = "DIA_2_CN_MAT"
        elif has_ch or has_lc:
            classification = "DIA_1_CH_LC"
        elif dia_2_signs:
            classification = "DIA_2_CN_MAT"
        elif dia_1_signs:
            classification = "DIA_1_CH_LC"

    return {
        'category': category,
        'classification': classification,
        'has_cn': has_cn,
        'has_mat': has_mat,
        'has_ch': has_ch,
        'has_lc': has_lc
    }

def main():
    print("Iniciando varredura profunda de todos os arquivos...")
    records = []
    
    for b in BASE_DIRS:
        if not os.path.exists(b):
            continue
        print(f"Varrendo pasta: {b} ...")
        for root, dirs, files in os.walk(b):
            for f in files:
                p = os.path.join(root, f)
                rel = os.path.relpath(p, '.')
                fname = f
                fname_lower = fname.lower()
                path_lower = rel.lower()
                ext = os.path.splitext(f)[1].lower()
                size = os.path.getsize(p)
                
                provider = detect_provider(path_lower, fname_lower)
                year = detect_year(path_lower, fname_lower)
                doc_type = detect_doc_type(fname_lower, path_lower)
                
                pages = 0
                snippet = ""
                status = "SKIPPED_NOT_PDF"
                
                if ext == '.pdf':
                    pages, snippet, status = inspect_pdf_header(p)
                
                day_info = classify_day_and_subjects(fname_lower, path_lower, snippet, year)
                
                records.append({
                    'path': rel,
                    'filename': fname,
                    'ext': ext,
                    'size': size,
                    'provider': provider,
                    'year': year,
                    'doc_type': doc_type,
                    'pages': pages,
                    'status': status,
                    'category': day_info['category'],
                    'classification': day_info['classification'],
                    'has_cn': day_info['has_cn'],
                    'has_mat': day_info['has_mat'],
                    'snippet': snippet[:300]
                })

    print(f"\nVarredura concluída. Total de arquivos: {len(records)}")
    
    # Save full survey to json
    with open('full_survey_raw.json', 'w', encoding='utf-8') as f:
        json.dump(records, f, ensure_ascii=False, indent=2)
    print("Salvo full_survey_raw.json com sucesso.")

if __name__ == '__main__':
    main()
