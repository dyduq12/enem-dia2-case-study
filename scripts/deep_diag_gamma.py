import os
import re
import hashlib
import json
import pypdf

base = 'BERNOULLI-20261110T151947Z-1-001'
all_files = sorted([os.path.relpath(os.path.join(root, f), base) for root, dirs, files in os.walk(base) for f in files])
gamma_files = all_files[:185]

file_diagnostics = []

def get_file_hash(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

for i, rel in enumerate(gamma_files):
    path = os.path.join(base, rel)
    size_kb = os.path.getsize(path) / 1024
    ext = os.path.splitext(rel)[1].lower()
    
    diag = {
        'index': i,
        'path': rel,
        'size_kb': round(size_kb, 1),
        'ext': ext,
        'pages': 0,
        'error': None,
        'is_dia1': False,
        'is_dia2': False,
        'is_vestibular_outro': False,
        'is_gabarito_puro': False,
        'has_questions': False,
        'subject_mentions': {},
        'question_range': None,
        'notes': ''
    }
    
    if ext != '.pdf':
        diag['error'] = f'Formato não PDF ({ext})'
        file_diagnostics.append(diag)
        continue
        
    try:
        reader = pypdf.PdfReader(path)
        diag['pages'] = len(reader.pages)
        if diag['pages'] == 0:
            diag['error'] = 'PDF vazio (0 páginas)'
            file_diagnostics.append(diag)
            continue
            
        full_sample_text = ""
        # Read text from first 5 pages, middle page, and last 2 pages
        sample_pages = set(list(range(min(5, len(reader.pages)))) + 
                           [len(reader.pages)//2] + 
                           list(range(max(0, len(reader.pages)-2), len(reader.pages))))
        
        for p_idx in sorted(sample_pages):
            try:
                p_text = reader.pages[p_idx].extract_text() or ""
                full_sample_text += f"\n--- PAGE {p_idx+1} ---\n" + p_text
            except Exception:
                pass
                
        # Anti-vestibular check
        lower_sample = full_sample_text.lower()
        if any(v in lower_sample for v in ['fuvest', 'unicamp', 'unesp', 'uerj', 'uece', 'olimpíada', 'prova paulista']):
            # check if it is exclusively or primarily that vestibular
            # Sometimes ENEM mentions "Adaptado de FUVEST" in a question source. We need to distinguish!
            # Caderno de vestibular usually has it on title/header
            if any(v in lower_sample[:1000] for v in ['fuvest', 'unicamp', 'unesp', 'uerj', 'uece', 'prova paulista']):
                diag['is_vestibular_outro'] = True
                
        # Subject detection
        has_mat = bool(re.search(r'matem[áa]tica', lower_sample))
        has_nat = bool(re.search(r'ci[êe]ncias da natureza', lower_sample))
        has_hum = bool(re.search(r'ci[êe]ncias humanas', lower_sample))
        has_ling = bool(re.search(r'linguagens', lower_sample))
        
        diag['subject_mentions'] = {
            'matematica': has_mat,
            'natureza': has_nat,
            'humanas': has_hum,
            'linguagens': has_ling
        }
        
        # Detect question numbers
        q_nums = [int(m) for m in re.findall(r'(?:QUEST[ÃA]O|Quest[ãa]o)\s+(\d{1,3})', full_sample_text)]
        if q_nums:
            diag['has_questions'] = True
            diag['question_range'] = [min(q_nums), max(q_nums)]
            
        # Check pure gabarito: 1 or 2 pages, high density of "01 - A", "91 - B", etc.
        if diag['pages'] <= 3 and not diag['has_questions']:
            diag['is_gabarito_puro'] = True
            
        # Check Dia 1 vs Dia 2
        # Dia 2 standard ENEM: Questions 91 to 180, Natureza & Matemática
        # Note: In 2012-2016, ENEM Dia 1 was Humanas + Natureza (1-90) and Dia 2 was Linguagens + Redação + Matemática (91-180)!
        # BUT since 2017: Dia 1 is Linguagens + Humanas + Redação (1-90), Dia 2 is Natureza + Matemática (91-180).
        # Let's inspect carefully how Bernoulli 2012 and 2015 are structured!
        
        if diag['has_questions']:
            q_min, q_max = diag['question_range']
            if q_min >= 91 or (has_nat and has_mat and not has_ling and not has_hum):
                diag['is_dia2'] = True
            elif q_max <= 90 and (has_ling or has_hum) and not (has_nat and has_mat):
                diag['is_dia1'] = True
            elif has_nat and not has_ling and not has_hum:
                diag['is_dia2'] = True
            elif has_ling and has_hum and not has_nat and not has_mat:
                diag['is_dia1'] = True
                
        # Also check pure gabarito sheets
        if diag['is_gabarito_puro']:
            if 'segundo' in lower_sample or 'dia 2' in lower_sample or 'prova ii' in lower_sample:
                diag['is_dia2'] = True
            elif 'primeiro' in lower_sample or 'dia 1' in lower_sample or 'prova i' in lower_sample:
                diag['is_dia1'] = True
                
    except Exception as e:
        diag['error'] = str(e)
        
    file_diagnostics.append(diag)

with open('file_diagnostics_gamma.json', 'w', encoding='utf-8') as f:
    json.dump(file_diagnostics, f, indent=2, ensure_ascii=False)

print('Diagnostic finished for all 185 files.')
