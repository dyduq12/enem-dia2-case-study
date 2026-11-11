import pypdf

fpath = r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2024\1º\RES - 1º SIMULADO BERNOULLI.pdf"
reader = pypdf.PdfReader(fpath)
print(f"Num pages: {len(reader.pages)}")
for i in range(min(5, len(reader.pages))):
    txt = reader.pages[i].extract_text() or ""
    print(f"--- Page {i+1} (len {len(txt)}) ---")
    print(txt[:300])
