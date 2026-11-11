import pypdf

reader = pypdf.PdfReader(r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2024\1º\RES - 1º SIMULADO BERNOULLI.pdf")
print("Num pages:", len(reader.pages))
total_text = ""
for i, page in enumerate(reader.pages):
    t = page.extract_text() or ""
    if t.strip():
        print(f"Page {i+1} has text: {t[:100]}")
    total_text += t
print(f"Total text extracted: {len(total_text)} chars")
