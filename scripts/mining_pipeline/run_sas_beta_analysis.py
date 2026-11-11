import os
import re
import json
import zipfile
import xml.etree.ElementTree as ET
import pypdf
from semantic_classifier import classify_text_semantics

WORKSPACE = r"c:\Users\Eduardo\Documents\02_Estudos & Academico\ENEM DIA 2"
SAS_DIR = os.path.join(WORKSPACE, "SAS")
PROG_DIR = os.path.join(SAS_DIR, "PROGRAMÁTICA")
COLEGIO_DIR = os.path.join(SAS_DIR, "SAS ENEM COLEGIO")

stats = {
    'total_valid_questions': 0,
    'by_discipline': {
        'Matemática': 0,
        'Física': 0,
        'Química': 0,
        'Biologia': 0
    },
    'by_topic': {
        'Matemática': {},
        'Física': {},
        'Química': {},
        'Biologia': {}
    },
    'interdisciplinary_pairs': {},
    'processed_files': [],
    'discarded_files': []
}

# 1. Record Discarded Non-ENEM & Day 1 Folders
all_files = sorted([os.path.relpath(os.path.join(root, f), SAS_DIR) for root, _, fnames in os.walk(SAS_DIR) for f in fnames])
beta_files = all_files[261:]

for f in beta_files:
    if f.startswith('OLIMPÍADAS'):
        stats['discarded_files'].append({
            'file': f,
            'reason': 'Descarte sumário: material de Olimpíadas científicas internas SAS, fora da matriz de competências do ENEM Dia 2.'
        })
    elif f.startswith('UERJ'):
        stats['discarded_files'].append({
            'file': f,
            'reason': 'Descarte sumário: vestibular estadual da UERJ / caderno de Humanas, fora do ENEM Dia 2.'
        })
    elif f.startswith('UFRS'):
        stats['discarded_files'].append({
            'file': f,
            'reason': 'Descarte sumário: vestibular regional da UFRGS (modelo tradicional de 4 dias), fora do ENEM Dia 2.'
        })
    elif f.startswith('UNICAMP'):
        stats['discarded_files'].append({
            'file': f,
            'reason': 'Descarte sumário: vestibular paulista UNICAMP (1ª e 2ª Fase dissertativa), fora do ENEM Dia 2.'
        })

# 2. Process PROGRAMÁTICA
prog_files = sorted(os.listdir(PROG_DIR))
day2_docx_provas = [
  '1746460211238_2020PROGRAMATICAS32aSERIECNMATprova.docx',
  '1748344913564_2025PROGRAMATICAS2_ETAPA1_SERIEMTCNPROVA.docx',
  '1749832546041_2025PROGRAMATICAS1_ETAPA2_SERIEMTCNPROVA.docx',
  '1749832546367_2025PROGRAMATICAS2_ETAPA2_SERIEMTCNPROVA.docx',
  '1755279226423_2025PROGRAMATICAS3_ETAPA1_SERIEMTCNPROVA.docx',
  '1755279302269_2025PROGRAMATICAS3_ETAPA2_SERIEMTCNPROVA.docx',
  '1759774118897_2025PROGRAMATICAS4_ETAPA1_SERIEMTCNPROVA.docx',
  '1759774497217_2025PROGRAMATICAS4_ETAPA2_SERIEMTCNPROVA.docx',
  '1773056619665_PROVA_2026Programaticas1_Etapa1SerieMatematica_e_Ciencias_da_Natureza.docx',
  '1773057060163_PROVA_2026Programaticas1_Etapa2SerieMatematica_e_Ciencias_da_Natureza.docx'
]

for pf in prog_files:
    pf_path = f"PROGRAMÁTICA/{pf}"
    pf_upper = pf.upper()
    if any(k in pf_upper for k in ['LGCH', 'REDACAO', 'LINGUAGENS', 'HUMANAS', 'LCCH']):
        stats['discarded_files'].append({
            'file': pf_path,
            'reason': 'Descarte sumário: Caderno do 1º Dia do ENEM (Linguagens, Códigos, Redação ou Ciências Humanas).'
        })
    elif pf not in day2_docx_provas:
        stats['processed_files'].append({
            'file': pf_path,
            'type': 'Gabarito Oficial SAS Programática Dia 2',
            'status': 'Correlacionado com Prova'
        })

def extract_docx_paras(path):
    with zipfile.ZipFile(path) as z:
        tree = ET.fromstring(z.read('word/document.xml'))
        ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}
        paras = []
        for p in tree.findall('.//w:p', ns):
            texts = [t.text for t in p.findall('.//w:t', ns) if t.text]
            if texts:
                paras.append(''.join(texts).strip())
        return paras

for pf in day2_docx_provas:
    path = os.path.join(PROG_DIR, pf)
    paras = extract_docx_paras(path)
    
    current_area = None
    q_text_buffer = []
    q_num = None
    file_questions = 0
    
    for p in paras:
        pu = p.upper()
        if 'CIÊNCIAS DA NATUREZA' in pu:
            current_area = 'CN'
        elif 'MATEMÁTICA' in pu:
            current_area = 'MAT'
            
        m = re.match(r'^(?:Quest[ãa]o\s+)?(\d{1,2})[\.\)]\s*(.*)', p, re.IGNORECASE)
        if m:
            if q_text_buffer and q_num:
                text_block = ' '.join(q_text_buffer)
                if current_area == 'MAT':
                    allowed = ['Matemática']
                else:
                    allowed = ['Física', 'Química', 'Biologia']
                disc, topic, inter = classify_text_semantics(text_block, allowed_disciplines=allowed)
                stats['total_valid_questions'] += 1
                stats['by_discipline'][disc] += 1
                stats['by_topic'][disc][topic] = stats['by_topic'][disc].get(topic, 0) + 1
                if inter:
                    pair = f"{disc} x {inter}"
                    stats['interdisciplinary_pairs'][pair] = stats['interdisciplinary_pairs'].get(pair, 0) + 1
                file_questions += 1
            q_num = m.group(1)
            q_text_buffer = [m.group(2)]
        else:
            q_text_buffer.append(p)
            
    if q_text_buffer and q_num:
        text_block = ' '.join(q_text_buffer)
        if current_area == 'MAT':
            allowed = ['Matemática']
        else:
            allowed = ['Física', 'Química', 'Biologia']
        disc, topic, inter = classify_text_semantics(text_block, allowed_disciplines=allowed)
        stats['total_valid_questions'] += 1
        stats['by_discipline'][disc] += 1
        stats['by_topic'][disc][topic] = stats['by_topic'][disc].get(topic, 0) + 1
        if inter:
            pair = f"{disc} x {inter}"
            stats['interdisciplinary_pairs'][pair] = stats['interdisciplinary_pairs'].get(pair, 0) + 1
        file_questions += 1
        
    stats['processed_files'].append({
        'file': f"PROGRAMÁTICA/{pf}",
        'type': 'Prova Programática SAS Dia 2 (.docx)',
        'questions_extracted': file_questions
    })

# 3. Process SAS ENEM COLEGIO
colegio_files = sorted(os.listdir(COLEGIO_DIR))
dups = {
    '1139-21 - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL_2.pdf',
    '1452-21 - RESOLUCAO - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL_2.pdf',
    '1925-21 - AG2 DE CNST e MST - 3a SERIE - 1a ETAPA_2.pdf',
    '2125-21 - RESOLUCAO AG2 - MST-CNST - 3a SERIE - 1a ETAPA_2.pdf'
}
for d in dups:
    stats['discarded_files'].append({
        'file': f"SAS ENEM COLEGIO/{d}",
        'reason': 'Descarte: cópia idêntica binária (arquivo duplicado _2.pdf no repositório).'
    })

stats['discarded_files'].append({
    'file': 'SAS ENEM COLEGIO/9183a9_ce9c73fee68d4d13b7d48d7bf776b583.pdf',
    'reason': 'Descarte: PDF escaneado rasterizado sem camada de texto ou gabarito estruturado.'
})

unique_colegio = [f for f in colegio_files if f not in dups and f != '9183a9_ce9c73fee68d4d13b7d48d7bf776b583.pdf']
resolucoes = [f for f in unique_colegio if any(k in f.upper() for k in ['RESOLU', 'COMENTARIO', 'GABARITO'])]
provas = [f for f in unique_colegio if f not in resolucoes]

for rf in resolucoes:
    stats['processed_files'].append({
        'file': f"SAS ENEM COLEGIO/{rf}",
        'type': 'Resolução Comentada / Gabarito Analítico SAS Colégio',
        'status': 'Correlacionado com Prova / Mapeamento Conceitual'
    })

for pf in provas:
    path = os.path.join(COLEGIO_DIR, pf)
    r = pypdf.PdfReader(path)
    full_text = '\n'.join(p.extract_text() or '' for p in r.pages)
    
    fu = pf.upper()
    is_cn_mst = ('CNST' in fu and ('MST' in fu or 'MAT' in fu)) or ('MST' in fu and 'CNST' in fu)
    is_ch_cn = ('CHST' in fu or 'CHS' in fu) and ('CNST' in fu or 'CNT' in fu or 'CNHT' in fu)
    is_vp3_other = 'vp3_2a-etapa_5o-simulado_prova.pdf' in pf
    
    q_blocks = re.split(r'\n\s*QUEST[ÃA]O\s+(\d{1,2})\b', full_text, flags=re.IGNORECASE)
    
    file_questions = 0
    discarded_ch = 0
    
    if len(q_blocks) > 1:
        for i in range(1, len(q_blocks), 2):
            q_num = int(q_blocks[i])
            q_text = q_blocks[i+1]
            
            if is_cn_mst:
                if q_num >= 46:
                    allowed = ['Matemática']
                else:
                    allowed = ['Física', 'Química', 'Biologia']
                disc, topic, inter = classify_text_semantics(q_text, allowed_disciplines=allowed)
                stats['total_valid_questions'] += 1
                stats['by_discipline'][disc] += 1
                stats['by_topic'][disc][topic] = stats['by_topic'][disc].get(topic, 0) + 1
                if inter:
                    pair = f"{disc} x {inter}"
                    stats['interdisciplinary_pairs'][pair] = stats['interdisciplinary_pairs'].get(pair, 0) + 1
                file_questions += 1
            elif is_ch_cn or is_vp3_other:
                if q_num <= 45:
                    discarded_ch += 1
                else:
                    allowed = ['Física', 'Química', 'Biologia']
                    disc, topic, inter = classify_text_semantics(q_text, allowed_disciplines=allowed)
                    stats['total_valid_questions'] += 1
                    stats['by_discipline'][disc] += 1
                    stats['by_topic'][disc][topic] = stats['by_topic'][disc].get(topic, 0) + 1
                    if inter:
                        pair = f"{disc} x {inter}"
                        stats['interdisciplinary_pairs'][pair] = stats['interdisciplinary_pairs'].get(pair, 0) + 1
                    file_questions += 1
    else:
        q_fallback = re.findall(r'(?:^|\n)\s*(\d{1,2})\.\s+(.*?)(?=(?:\n\s*\d{1,2}\.|\Z))', full_text, re.DOTALL)
        if q_fallback:
            for q_num_str, q_text in q_fallback:
                q_num = int(q_num_str)
                if is_cn_mst:
                    if q_num >= 46:
                        allowed = ['Matemática']
                    else:
                        allowed = ['Física', 'Química', 'Biologia']
                    disc, topic, inter = classify_text_semantics(q_text, allowed_disciplines=allowed)
                    stats['total_valid_questions'] += 1
                    stats['by_discipline'][disc] += 1
                    stats['by_topic'][disc][topic] = stats['by_topic'][disc].get(topic, 0) + 1
                    if inter:
                        pair = f"{disc} x {inter}"
                        stats['interdisciplinary_pairs'][pair] = stats['interdisciplinary_pairs'].get(pair, 0) + 1
                    file_questions += 1
                elif is_ch_cn or is_vp3_other:
                    if q_num <= 45:
                        discarded_ch += 1
                    else:
                        allowed = ['Física', 'Química', 'Biologia']
                        disc, topic, inter = classify_text_semantics(q_text, allowed_disciplines=allowed)
                        stats['total_valid_questions'] += 1
                        stats['by_discipline'][disc] += 1
                        stats['by_topic'][disc][topic] = stats['by_topic'][disc].get(topic, 0) + 1
                        if inter:
                            pair = f"{disc} x {inter}"
                            stats['interdisciplinary_pairs'][pair] = stats['interdisciplinary_pairs'].get(pair, 0) + 1
                        file_questions += 1
                        
    stats['processed_files'].append({
        'file': f"SAS ENEM COLEGIO/{pf}",
        'type': 'Caderno de Prova SAS ENEM Colégio (.pdf)',
        'valid_dia2_questions': file_questions,
        'discarded_dia1_ch_questions': discarded_ch
    })

# Save JSON results
with open(os.path.join(WORKSPACE, "sas_beta_results.json"), "w", encoding="utf-8") as f:
    json.dump(stats, f, indent=2, ensure_ascii=False)

print(f"Extraction complete!")
print(f"Total Valid Day 2 Questions: {stats['total_valid_questions']}")
print(f"By Discipline: {stats['by_discipline']}")
print(f"Processed Files: {len(stats['processed_files'])}")
print(f"Discarded Files: {len(stats['discarded_files'])}")
