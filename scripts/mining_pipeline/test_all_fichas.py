import zipfile, xml.etree.ElementTree as ET, re, os

def col_letter_to_index(col_str):
    col = 0
    for c in col_str:
        col = col * 26 + (ord(c.upper()) - ord('A') + 1)
    return col - 1

def parse_sheet_proper(path):
    with zipfile.ZipFile(path) as z:
        shared = []
        if 'xl/sharedStrings.xml' in z.namelist():
            tree = ET.fromstring(z.read('xl/sharedStrings.xml'))
            for elem in tree:
                shared.append(''.join(elem.itertext()))
        sheet_tree = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        rows_dict = {}
        for row in sheet_tree.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
            for c in row.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                coord = c.attrib.get('r', '')
                m = re.match(r'([A-Z]+)(\d+)', coord)
                if not m:
                    continue
                col_letters, row_num = m.groups()
                col_idx = col_letter_to_index(col_letters)
                row_idx = int(row_num)
                
                t = c.attrib.get('t')
                v = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                val = v.text if v is not None else ''
                if t == 's' and val:
                    try:
                        val = shared[int(val)]
                    except Exception:
                        pass
                
                if row_idx not in rows_dict:
                    rows_dict[row_idx] = {}
                rows_dict[row_idx][col_idx] = val
        return rows_dict

poliedro_files = [
    'POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx',
    'POLIEDRO/2024/2º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx',
    'POLIEDRO/2024/3º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx',
    'POLIEDRO/2024/4º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx',
    'POLIEDRO/2024/2024_5_poliedro_enem_3serie_e_pv_ficha_mapa_geral_dia02.xlsx'
]

for p in poliedro_files:
    rows = parse_sheet_proper(p)
    h_idx = None
    q_col = None
    for r_idx, r in sorted(rows.items()):
        for c_idx, val in r.items():
            if 'QUEST' in str(val).upper():
                h_idx = r_idx
                q_col = c_idx
                break
        if h_idx is not None:
            break
            
    header = rows.get(h_idx, {})
    col_by_name = {str(v).strip().upper(): k for k, v in header.items()}
    
    q_count = 0
    q_nums = []
    for r_idx in sorted(rows.keys()):
        if r_idx <= h_idx:
            continue
        r = rows[r_idx]
        q_val = str(r.get(q_col, '')).strip()
        if q_val.isdigit() and 91 <= int(q_val) <= 180:
            q_count += 1
            q_nums.append(int(q_val))
            
    print(f"{os.path.basename(p)}: header at row {h_idx}, col {q_col}, questions count={q_count}, range=({min(q_nums) if q_nums else 0} to {max(q_nums) if q_nums else 0})")
