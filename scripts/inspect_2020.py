import os, pypdf

base = 'BERNOULLI-20261110T151947Z-1-001'
all_files = sorted([os.path.relpath(os.path.join(root, f), base) for root, dirs, files in os.walk(base) for f in files])
gamma_files = [f for f in all_files[:185] if '2020' in f]

for f in gamma_files:
    full = os.path.join(base, f)
    ext = os.path.splitext(f)[1].lower()
    if ext == '.pdf':
        r = pypdf.PdfReader(full)
        sample = (r.pages[0].extract_text() or '')[:120].replace('\n', ' ')
        print(f"{f} | {len(r.pages)} pgs | {sample}")
    else:
        print(f"{f} | NON-PDF")
