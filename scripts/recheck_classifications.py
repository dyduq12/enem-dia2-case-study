import os, json, re, pypdf

base = 'BERNOULLI-20261110T151947Z-1-001'

with open('classified_gamma.json', 'r', encoding='utf-8') as f:
    classified = json.load(f)

# Re-check and fix any misclassified files based on page text
for c in classified:
    rel = c['path']
    if '2020\\4º\\SIMULADO 4(2°Dia)BERNOULLI 2020.pdf' in rel:
        c['status'] = 'DESCARTADO'
        c['justification'] = 'Descartado: Caderno do 1º Dia do ENEM (apesar do nome conter 2ºDia, o conteúdo interno é Linguagens e Humanas)'
        c['edition'] = ''
        c['type'] = ''

with open('classified_gamma.json', 'w', encoding='utf-8') as f:
    json.dump(classified, f, indent=2, ensure_ascii=False)

valid = [c for c in classified if c['status'] == 'VALIDO_DIA2']
print(f"Total valid Dia 2 files after content verification: {len(valid)}")
print(f"Total discarded files: {len(classified) - len(valid)}")

# Group valid files by edition
editions = {}
for c in valid:
    ed = c['edition']
    if ed not in editions:
        editions[ed] = []
    editions[ed].append(c)

print(f"\nTotal unique editions: {len(editions)}")
for ed in sorted(editions.keys()):
    files = editions[ed]
    print(f"Edition {ed:20s}: {len(files)} files")
