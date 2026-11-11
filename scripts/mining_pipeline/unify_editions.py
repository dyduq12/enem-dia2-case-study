import json
import re

with open('canonical_editions.json', 'r', encoding='utf-8') as f:
    editions = json.load(f)

# Unify matching pairs (e.g. 1241/1242, 1373/1378, 2096/2097, 2348/2349, 2017SASENEM1 prova/gabarito)
unified = {}

for name, files in editions.items():
    # Normalize name
    u_name = name
    # Remove AP2/AG2 code variations to match pairs
    m_ap = re.search(r'(\d{4})[-_](\d{2})[_\s-]+(RESOLUCAO\s+)?(AP\d|AG\d)[_\s-]+([A-Z0-9_-]+)', name, re.IGNORECASE)
    if m_ap:
        code, year, _, typ, rest = m_ap.groups()
        # Pair codes like 1241/1242, 1373/1378, 2096/2097, 2348/2349, 4009/4228, 5023/5150, 6377/6378, 6919/6919
        clean_rest = re.sub(r'WILL.*', 'WILL', rest, flags=re.IGNORECASE).strip(' _-')
        u_name = f"AP/AG_{year}_{typ}_{clean_rest}"
        
    m_sas = re.search(r'(\d{4})SASENEM(\d)DIA2(prova|gabarito)', name, re.IGNORECASE)
    if m_sas:
        yr, num, _ = m_sas.groups()
        u_name = f"SAS_{yr}_SIMULADO_{num}_DIA2"
        
    m_ber = re.search(r'(\d+)[°º]?\s*BERNOULLI\s*(EXTRA)?\s*(\d{4})?', name, re.IGNORECASE)
    if m_ber:
        num, extra, yr = m_ber.groups()
        extra_str = "_EXTRA" if extra else ""
        yr_str = f"_{yr}" if yr else ""
        u_name = f"BERNOULLI{extra_str}{yr_str}_SIMULADO_{num}_DIA2"
        
    m_aut = re.search(r'Simulado Autoral (\d+) - 2º Dia \((\d{4})\)', name, re.IGNORECASE)
    if m_aut:
        num, yr = m_aut.groups()
        u_name = f"SIMULADO_AUTORAL_{yr}_NUM_{num}_DIA2"
        
    m_enem_oficial = re.search(r'ENEM\s+(\d{4})\s+DIA\s+2', name, re.IGNORECASE)
    if m_enem_oficial:
        yr = m_enem_oficial.group(1)
        u_name = f"ENEM_OFICIAL_{yr}_DIA2"

    unified.setdefault(u_name, []).extend(files)

print(f"Total unified unique exam editions: {len(unified)}")

with open('unified_editions.json', 'w', encoding='utf-8') as f:
    json.dump(unified, f, ensure_ascii=False, indent=2)

print("\nSample unified editions:")
for k, v in list(unified.items())[:25]:
    fnames = [x['filename'] for x in v]
    print(f"[{len(v):2d} files] {k} -> {fnames[0]}")
