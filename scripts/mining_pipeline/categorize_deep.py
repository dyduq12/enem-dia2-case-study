import json

with open('file_analysis.json', 'r', encoding='utf-8') as f:
    file_analysis = json.load(f)

with open('text_stats.json', 'r', encoding='utf-8') as f:
    text_stats = {x['filename']: x for x in json.load(f)}

categorized = {
    'descartado_dia_1': [],
    'descartado_olimpiada': [],
    'descartado_material_didatico': [],
    'descartado_gabarito_isolado': [],
    'descartado_corrompido_ou_sem_texto': [],
    'valido_dia_2_cadernos': []
}

for item in file_analysis:
    fn = item['filename']
    status = item['status']
    pages = item['pages']
    reason = item['reason']
    ts = text_stats.get(fn, {})
    chars = ts.get('total_chars', None)
    
    if status == 'DESCARTADO_DIA_1':
        categorized['descartado_dia_1'].append((fn, pages, reason))
    elif status == 'DESCARTADO_OLIMPIADA':
        categorized['descartado_olimpiada'].append((fn, pages, reason))
    elif status == 'DESCARTADO_MATERIAL_DIDATICO':
        categorized['descartado_material_didatico'].append((fn, pages, reason))
    elif status == 'DESCARTADO_GABARITO_ISOLADO':
        categorized['descartado_gabarito_isolado'].append((fn, pages, reason))
    elif status == 'DESCARTADO_CORROMPIDO':
        categorized['descartado_corrompido_ou_sem_texto'].append((fn, pages, reason))
    else:
        # VALIDO_DIA_2 in file_analysis
        if chars is not None and chars < 500:
            categorized['descartado_corrompido_ou_sem_texto'].append((fn, pages, f'Sem texto extraível ({chars} caracteres / arquivo escaneado em imagem ou vazio)'))
        else:
            categorized['valido_dia_2_cadernos'].append((fn, pages, chars))

print("=== CONTAGEM GERAL DE ARQUIVOS CORRIGIDA ===")
print("Total de arquivos:", len(file_analysis))
for k, v in categorized.items():
    print(f"  {k}: {len(v)}")

with open('detailed_file_categories.json', 'w', encoding='utf-8') as f:
    json.dump(categorized, f, ensure_ascii=False, indent=2)
