import json
import re
import os

with open('detailed_file_categories.json', 'r', encoding='utf-8') as f:
    cat = json.load(f)

valid_files = [x[0] for x in cat['valido_dia_2_cadernos']]

# Let's inspect all valid filenames and identify exact canonical editions
print(f"Total valid files to analyze: {len(valid_files)}")

# Build edition clustering
editions = {}

for fn in sorted(valid_files):
    name = os.path.splitext(fn)[0]
    
    # Clean duplicates like (1), _2
    clean = re.sub(r'\s*\([0-9]+\)$', '', name)
    clean = re.sub(r'_[0-9]+$', '', clean)
    
    # Normalize spaces
    clean = ' '.join(clean.split())
    
    # Detect colors
    color = None
    for c in ['AMARELO', 'AZUL', 'BRANCO', 'VERDE', 'ROSA', 'CINZA']:
        if re.search(r'\b' + c + r'\b', clean, re.IGNORECASE):
            color = c
            clean = re.sub(r'\s*-\s*' + c + r'\b', '', clean, flags=re.IGNORECASE)
            clean = re.sub(r'\b' + c + r'\b', '', clean, flags=re.IGNORECASE)
            clean = ' '.join(clean.split())
            break
            
    # Detect type: Gabarito/Resolução vs Prova
    is_res = bool(re.search(r'(resolu[cç][aã]o|resol|gabarito|gab\b)', clean, re.IGNORECASE))
    
    # Base edition key
    base_key = clean
    base_key = re.sub(r'^\s*\[(PROVA DIA 2|PROVA AMARELA|GABARITO DIA 2|GABARITO|RESOLUÇÃOV2)\]\s*-?\s*', '', base_key, flags=re.IGNORECASE)
    base_key = re.sub(r'\b(RESOLUCAO|RESOLUÇÃO|GABARITO|GAB|PROVA)\b', '', base_key, flags=re.IGNORECASE)
    base_key = re.sub(r'\s*-\s*$', '', base_key)
    base_key = re.sub(r'^\s*-\s*', '', base_key)
    base_key = ' '.join(base_key.split())
    
    editions.setdefault(base_key, []).append({
        'filename': fn,
        'color': color,
        'is_res': is_res,
        'raw_clean': clean
    })

print(f"Clustered into {len(editions)} canonical exam editions.")

with open('canonical_editions.json', 'w', encoding='utf-8') as f:
    json.dump(editions, f, ensure_ascii=False, indent=2)

for i, (k, v) in enumerate(list(editions.items())[:30]):
    print(f"{i+1:2d}. Edition '{k}': {len(v)} files")
    for f in v:
        print(f"     [{'RES' if f['is_res'] else 'PRV'} | {f['color'] or 'STD'}] {f['filename']}")
