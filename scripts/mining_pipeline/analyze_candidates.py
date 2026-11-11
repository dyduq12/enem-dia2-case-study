import pypdf
import os
import json

target = '_ENEM_DIA_2_BRUTO'
with open('file_analysis.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

valid = [x for x in data if x['status'] == 'VALIDO_DIA_2']
stats = []

for item in valid:
    fn = item['filename']
    fp = os.path.join(target, fn)
    try:
        reader = pypdf.PdfReader(fp)
        num_pages = len(reader.pages)
        total_chars = 0
        pages_with_text = 0
        for p in reader.pages:
            t = p.extract_text() or ''
            total_chars += len(t)
            if len(t.strip()) > 30:
                pages_with_text += 1
        stats.append({
            'filename': fn,
            'pages': num_pages,
            'pages_with_text': pages_with_text,
            'total_chars': total_chars,
            'avg_chars_per_page': round(total_chars / max(1, num_pages), 1)
        })
    except Exception as e:
        stats.append({'filename': fn, 'error': str(e), 'total_chars': 0, 'pages': 0})

with open('text_stats.json', 'w', encoding='utf-8') as f:
    json.dump(stats, f, ensure_ascii=False, indent=2)

no_text = [s for s in stats if s.get('total_chars', 0) < 500]
print(f'Total candidates analyzed: {len(stats)}')
print(f'Files with little or no text (< 500 chars): {len(no_text)}')
for nt in no_text:
    print(f'  {nt.get("pages", 0)} pgs | {nt.get("total_chars", 0)} chars | {nt["filename"]}')
