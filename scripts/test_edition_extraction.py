import os, json, re, pypdf

base = 'BERNOULLI-20261110T151947Z-1-001'

with open('classified_gamma.json', 'r', encoding='utf-8') as f:
    classified = json.load(f)

valid = [c for c in classified if c['status'] == 'VALIDO_DIA2']

editions = {}
for c in valid:
    ed = c['edition']
    if not ed or 'VESTGEEK' in ed or 'Prova 2.pdf' in ed:
        continue
    if ed not in editions:
        editions[ed] = []
    editions[ed].append(c)

print(f"Total editions to test: {len(editions)}")

edition_source_map = {}

for ed, files in sorted(editions.items()):
    # Prefer RESOLUCAO, then PROVA with largest pages/size
    res_files = [f for f in files if f['type'] == 'RESOLUCAO']
    prova_files = [f for f in files if f['type'] == 'PROVA']
    
    selected = None
    if res_files:
        selected = max(res_files, key=lambda x: x['pages'])
    elif prova_files:
        selected = max(prova_files, key=lambda x: x['pages'])
    else:
        selected = files[0]
        
    edition_source_map[ed] = selected

for ed, s in sorted(edition_source_map.items()):
    rel = s['path']
    full = os.path.join(base, rel)
    reader = pypdf.PdfReader(full)
    # Check question numbers
    text = ""
    for p in range(len(reader.pages)):
        text += f"\n[P{p+1}]\n" + (reader.pages[p].extract_text() or "")
    
    q_matches = re.findall(r'(?:QUEST[ÃA]O|Quest[ãa]o)\s+(\d{1,3})', text)
    q_set = set(int(q) for q in q_matches if 45 <= int(q) <= 180)
    print(f"{ed:18s} | file: {rel[:55]:55s} | pgs: {len(reader.pages):2d} | qs: {len(q_set):2d} (min={min(q_set) if q_set else None}, max={max(q_set) if q_set else None})")
