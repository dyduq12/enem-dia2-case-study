import json
import re
import os

with open('text_stats.json', 'r', encoding='utf-8') as f:
    stats = json.load(f)

with_text = [s for s in stats if s.get('total_chars', 0) >= 500]

print(f"Total files with text: {len(with_text)}")

# Let's inspect filenames to create canonical exam groups
def get_exam_key(filename):
    fn = filename
    # Remove extension
    name = os.path.splitext(fn)[0]
    
    # Check duplicate marks like (1), _2
    name_clean = re.sub(r'\s*\([0-9]+\)$', '', name)
    name_clean = re.sub(r'_[0-9]+$', '', name_clean)
    
    # Check color suffixes (AMARELO, AZUL, BRANCO, VERDE, ROSA, CINZA)
    color_pattern = r'\s*-\s*(AMARELO|AZUL|BRANCO|VERDE|ROSA|CINZA)\s*'
    name_clean = re.sub(color_pattern, ' ', name_clean, flags=re.IGNORECASE)
    name_clean = re.sub(r'\b(AMARELO|AZUL|BRANCO|VERDE|ROSA|CINZA)\b', '', name_clean, flags=re.IGNORECASE)
    
    # Check GABARITO / RESOLUCAO vs PROVA
    is_gab_or_res = bool(re.search(r'(gabarito|resolu[cç][aã]o|resol|gab\b)', name_clean, flags=re.IGNORECASE))
    
    return name_clean.strip(), is_gab_or_res

groups = {}
for item in with_text:
    fn = item['filename']
    clean_name, is_gab = get_exam_key(fn)
    groups.setdefault(clean_name, []).append((fn, item['pages'], item['total_chars'], is_gab))

print(f"Grouped into {len(groups)} distinct exam bases/titles.")

with open('exam_groups.json', 'w', encoding='utf-8') as f:
    json.dump({k: v for k, v in sorted(groups.items())}, f, ensure_ascii=False, indent=2)

print("\nSample groups:")
for k, v in list(groups.items())[:20]:
    print(f"Key: '{k}' ({len(v)} files)")
    for f, p, c, g in v:
        print(f"    {'GAB/RES' if g else 'PROVA  '} | {p:2d} pgs | {c:6d} chars | {f}")
