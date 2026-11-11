import pypdf

fpath = r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2024\1º\SIMULADO 1 - GABARITO COMENTADO.pdf"
reader = pypdf.PdfReader(fpath)
print(f"Num pages: {len(reader.pages)}")
for i in [0, 1, 2, 3]:
    txt = reader.pages[i].extract_text() or ""
    print(f"=== PAGE {i+1} ===")
    print(txt[:1000])
