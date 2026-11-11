import json

with open('classified_gamma.json', 'r', encoding='utf-8') as f:
    classified = json.load(f)

for c in classified:
    if c['edition'] in ['2022_2º', '2021_7º', '2020_3º']:
        print(f"{c['edition']} [{c['type']}]: {c['path']}")
