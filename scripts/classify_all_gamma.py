import os
import re
import json
import pypdf

base = 'BERNOULLI-20261110T151947Z-1-001'
all_files = sorted([os.path.relpath(os.path.join(root, f), base) for root, dirs, files in os.walk(base) for f in files])
gamma_files = all_files[:185]

with open('file_diagnostics_gamma.json', 'r', encoding='utf-8') as f:
    diags = json.load(f)

print(f"Loaded {len(diags)} diagnostics.")

# Detailed classification logic for every file
classified = []

for d in diags:
    idx = d['index']
    rel = d['path']
    pages = d['pages']
    err = d['error']
    sub = d['subject_mentions']
    q_range = d['question_range']
    
    status = 'UNKNOWN'
    justification = ''
    edition_key = ''
    file_type = '' # 'PROVA', 'RESOLUCAO', 'GABARITO_FOLHA', 'OUTRO'
    
    lower_path = rel.lower()
    
    # 1. Error / Corrupt / Non-PDF
    if err:
        status = 'DESCARTADO'
        justification = f"Arquivo inválido ou ilegível ({err})"
        classified.append({'index': idx, 'path': rel, 'status': status, 'justification': justification, 'edition': '', 'pages': pages})
        continue

    # 2. Outros Vestibulares
    if d['is_vestibular_outro'] or 'poliedro' in lower_path:
        status = 'DESCARTADO'
        justification = "Descartado: Caderno de outro vestibular/sistema (não pertence ao modelo ENEM Dia 2 Bernoulli)"
        classified.append({'index': idx, 'path': rel, 'status': status, 'justification': justification, 'edition': '', 'pages': pages})
        continue

    # 3. Gabarito puro de 1 folha (apenas tabela de letras)
    if pages <= 3 and not d['has_questions']:
        status = 'DESCARTADO'
        justification = "Descartado: Gabarito preliminar sintético (tabela de letras sem enunciados de questões)"
        classified.append({'index': idx, 'path': rel, 'status': status, 'justification': justification, 'edition': '', 'pages': pages})
        continue

    # 4. Check whether it is Dia 1 or Dia 2 based on content
    # Let's check text extraction from page 1 and page 2
    path = os.path.join(base, rel)
    reader = pypdf.PdfReader(path)
    sample_text = ""
    for p in range(min(4, len(reader.pages))):
        sample_text += "\n" + (reader.pages[p].extract_text() or "")
    sample_text_lower = sample_text.lower()
    
    # Check for question numbers in text
    q_nums = [int(m) for m in re.findall(r'(?:QUEST[ÃA]O|Quest[ãa]o)\s+(\d{1,3})', sample_text)]
    min_q = min(q_nums) if q_nums else None
    
    # Dia 1 detection
    is_dia1 = False
    is_dia2 = False
    
    if 'ciências humanas' in sample_text_lower and 'linguagens' in sample_text_lower:
        is_dia1 = True
    elif 'ciências humanas' in sample_text_lower and not ('matemática' in sample_text_lower or 'natureza' in sample_text_lower):
        is_dia1 = True
    elif 'linguagens' in sample_text_lower and not ('matemática' in sample_text_lower or 'natureza' in sample_text_lower):
        is_dia1 = True
    elif min_q is not None and min_q < 90 and not ('matemática' in sample_text_lower or 'natureza' in sample_text_lower):
        is_dia1 = True
    elif 'ciências da natureza' in sample_text_lower or 'matemática e suas tecnologias' in sample_text_lower:
        is_dia2 = True
    elif min_q is not None and min_q >= 91:
        is_dia2 = True
        
    # Check year 2014/2015 old format
    if '2015\\simulado 2014.pdf' in lower_path:
        # SIMULADO 2014.pdf has CH on pages 1-20, CN on pages 21-39, Gabarito CH/CN on 40-68
        is_dia2 = True
        justification = "Válido: Simulado modelo anterior contendo caderno e resolução de Ciências da Natureza (Questões 46 a 90)"
        status = 'VALIDO_DIA2'
        edition_key = '2014_SIMULADO_1'
        file_type = 'MISTO_COM_NATUREZA'
        classified.append({'index': idx, 'path': rel, 'status': status, 'justification': justification, 'edition': edition_key, 'pages': pages, 'type': file_type})
        continue

    if is_dia1 and not is_dia2:
        status = 'DESCARTADO'
        justification = "Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas)"
    elif is_dia2:
        status = 'VALIDO_DIA2'
        justification = "Válido: Caderno / Resolução do 2º Dia do ENEM (Ciências da Natureza e Matemática)"
        
        # Determine edition key
        # Extract year and set/number
        parts = rel.split(os.sep)
        year = parts[1]
        subset = parts[2] if len(parts) > 2 else ''
        edition_key = f"{year}_{subset}"
        if 'resolução' in lower_path or 'comentada' in lower_path or 'book_provaii' in lower_path:
            file_type = 'RESOLUCAO'
        else:
            file_type = 'PROVA'
    else:
        # Check if title explicitly says dia 1 or dia 2
        if any(w in lower_path for w in ['1º dia', '1ºdia', 'dia 1', 'prova 1', 'prova i', 'primeiro dia']):
            status = 'DESCARTADO'
            justification = "Descartado: Caderno/Gabarito do 1º Dia do ENEM"
        elif any(w in lower_path for w in ['2º dia', '2ºdia', 'dia 2', 'prova 2', 'prova ii', 'segundo dia']):
            status = 'VALIDO_DIA2'
            justification = "Válido: Caderno / Resolução do 2º Dia do ENEM (Ciências da Natureza e Matemática)"
            parts = rel.split(os.sep)
            year = parts[1]
            subset = parts[2] if len(parts) > 2 else ''
            edition_key = f"{year}_{subset}"
            file_type = 'PROVA'
        else:
            status = 'DESCARTADO'
            justification = "Descartado: Material sem conteúdo válido de Matemática ou Ciências da Natureza do Dia 2"
            
    classified.append({
        'index': idx,
        'path': rel,
        'status': status,
        'justification': justification,
        'edition': edition_key,
        'pages': pages,
        'type': file_type
    })

with open('classified_gamma.json', 'w', encoding='utf-8') as f:
    json.dump(classified, f, indent=2, ensure_ascii=False)

valid_dia2 = [c for c in classified if c['status'] == 'VALIDO_DIA2']
discarded = [c for c in classified if c['status'] == 'DESCARTADO']

print(f"Total files: {len(classified)}")
print(f"Válidos Dia 2: {len(valid_dia2)}")
print(f"Descartados: {len(discarded)}")

# Let's count unique editions among valid
editions = {}
for v in valid_dia2:
    ed = v['edition']
    editions[ed] = editions.get(ed, 0) + 1

print("\nEdições únicas válidas do Dia 2:")
for ed, count in sorted(editions.items()):
    print(f"  {ed}: {count} arquivos válidos")
