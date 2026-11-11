import json
import re

with open('detailed_file_categories.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

valid_files = data['valido_dia_2_cadernos']

print(f"Total valid Dia 2 files: {len(valid_files)}")

# Let's inspect the files to classify their provider/series
series = {
    'SAS': [],
    'BERNOULLI': [],
    'SIMULADO_AUTORAL': [],
    'AP2_AG2_CNST_MST': [],
    'ENEM_OFICIAL': [],
    'APEIRON': [],
    'OUTROS': []
}

for item in valid_files:
    fn = item[0]
    pages = item[1]
    chars = item[2]
    fn_lower = fn.lower()
    
    if 'autoral' in fn_lower:
        series['SIMULADO_AUTORAL'].append((fn, pages, chars))
    elif 'sas' in fn_lower:
        series['SAS'].append((fn, pages, chars))
    elif 'bernoulli' in fn_lower:
        series['BERNOULLI'].append((fn, pages, chars))
    elif 'ap2' in fn_lower or 'ag2' in fn_lower:
        series['AP2_AG2_CNST_MST'].append((fn, pages, chars))
    elif 'enem 20' in fn_lower or 'enem_20' in fn_lower or 'enem oficial' in fn_lower:
        series['ENEM_OFICIAL'].append((fn, pages, chars))
    elif 'apeiron' in fn_lower:
        series['APEIRON'].append((fn, pages, chars))
    else:
        series['OUTROS'].append((fn, pages, chars))

print("\nDistribution by series/collection:")
for k, v in series.items():
    print(f"  {k}: {len(v)} files")

print("\nFiles in OUTROS:")
for f, p, c in series['OUTROS']:
    print(f"  {p} pgs | {c} chars | {f}")
