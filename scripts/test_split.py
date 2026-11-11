import os, json, re, pypdf

# Let's write an initial classifier to test on 1 edition
edition_file = r'BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2021\1º\2021_v01_BOOK_PROVAII_TE_reduzido.pdf'
reader = pypdf.PdfReader(edition_file)
full_text = ''
for p in range(len(reader.pages)):
    full_text += f'\n[PAGE {p+1}]\n' + (reader.pages[p].extract_text() or '')

# Split questions 91 to 180
questions = {}
for q in range(91, 181):
    next_q = q + 1
    pattern = rf'(?:QUEST[ÃA]O|Quest[ãa]o)\s+{q}\b(.*?)(?=(?:QUEST[ÃA]O|Quest[ãa]o)\s+{next_q}\b|\Z)'
    m = re.search(pattern, full_text, re.DOTALL | re.IGNORECASE)
    if m:
        questions[q] = m.group(1).strip()
    else:
        # Fallback search
        p_fallback = rf'(?:QUEST[ÃA]O|Quest[ãa]o)\s+{q}\b(.*)'
        m2 = re.search(p_fallback, full_text, re.DOTALL | re.IGNORECASE)
        if m2:
            questions[q] = m2.group(1)[:2000].strip()

print(f"Extracted {len(questions)} questions from 2021 Volume 1.")
for q in [91, 95, 100, 110, 125, 135, 136, 145, 160, 175]:
    if q in questions:
        snippet = questions[q][:150].replace('\n', ' ')
        print(f"Q{q}: {snippet}")
