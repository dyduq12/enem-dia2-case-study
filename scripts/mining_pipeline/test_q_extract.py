import pypdf
import os
import re

target = '_ENEM_DIA_2_BRUTO'

def test_extract_questions(filename):
    fp = os.path.join(target, filename)
    reader = pypdf.PdfReader(fp)
    full_text = ''
    for i, p in enumerate(reader.pages):
        txt = p.extract_text() or ''
        full_text += f"\n--- PAGE {i+1} ---\n" + txt

    # Let's search for QUESTÃO patterns
    matches = list(re.finditer(r'(QUEST[ÃA]O\s+(\d+))', full_text, flags=re.IGNORECASE))
    print(f"File: {filename} ({len(reader.pages)} pages)")
    print(f"  Found {len(matches)} occurrences of 'QUESTÃO XX'")
    if matches:
        q_nums = [m.group(2) for m in matches]
        print(f"  First 10 question numbers: {q_nums[:10]}")
        print(f"  Last 5 question numbers: {q_nums[-5:]}")
    return len(matches)

test_files = [
    '1º SIMULADO SAS ENEM - 2026 -  D2 - AMARELO.pdf',
    'Prova - Simulado Autoral 1 - 2º Dia (2025).pdf',
    '1° BERNOULLI EXTRA 2026 - D2.pdf',
    '2017SASENEM1DIA2prova.pdf',
    '1139-21 - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf',
    'ENEM 2021 DIA 2.pdf'
]

for tf in test_files:
    test_extract_questions(tf)
    print()
