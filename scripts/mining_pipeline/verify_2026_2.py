import pypdf

p1 = r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2026\2º\Gabarito simulado Enem .pdf"
p2 = r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2026\2º\2° BERNOULLI 2026 - D2 - GABARITO.pdf"

r1 = pypdf.PdfReader(p1)
r2 = pypdf.PdfReader(p2)

print("P1 page 2 text:", (r1.pages[1].extract_text() or "")[:300].replace("\n", " "))
print("P2 page 2 text:", (r2.pages[1].extract_text() or "")[:300].replace("\n", " "))
