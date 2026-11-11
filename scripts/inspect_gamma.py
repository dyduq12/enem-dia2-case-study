import os
import pypdf

base = 'BERNOULLI-20261110T151947Z-1-001'
all_files = sorted([os.path.relpath(os.path.join(root, f), base) for root, dirs, files in os.walk(base) for f in files])
gamma_files = all_files[:185]

results = []
for i, rel in enumerate(gamma_files):
    path = os.path.join(base, rel)
    size_kb = os.path.getsize(path) / 1024
    ext = os.path.splitext(rel)[1].lower()
    num_pages = 0
    first_page_text = ''
    error = None
    if ext == '.pdf':
        try:
            reader = pypdf.PdfReader(path)
            num_pages = len(reader.pages)
            if num_pages > 0:
                first_page_text = (reader.pages[0].extract_text() or '')[:300].replace('\n', ' ')
        except Exception as e:
            error = str(e)
    else:
        error = f'Non-pdf: {ext}'
    results.append({
        'index': i,
        'rel': rel,
        'size_kb': size_kb,
        'pages': num_pages,
        'error': error,
        'sample': first_page_text[:120]
    })

print(f'Total scanned: {len(results)}')
errors = [r for r in results if r['error']]
print(f'Files with errors/non-pdf: {len(errors)}')
for e in errors:
    print(f"{e['index']:03d}: {e['rel']} - {e['error']}")

with open('inspect_gamma_out.txt', 'w', encoding='utf-8') as out:
    for r in results:
        out.write(f"[{r['index']:03d}] {r['rel']} | {r['size_kb']:.1f} KB | {r['pages']} pgs | err: {r['error']} | sample: {r['sample']}\n")
print('Saved inspection to inspect_gamma_out.txt')
