import pypdf

f1 = r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2026\5º\5° BERNOULLI - 2026 - Dia 02.pdf"
f2 = r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2026\5º\d3d4ebf36fc4f39bb474847b5928558207be3c0eBer_SE2026_V05_BOOK_PROVAII.pdf"

r1 = pypdf.PdfReader(f1)
r2 = pypdf.PdfReader(f2)

print("F1 pages:", len(r1.pages), "sample:", (r1.pages[1].extract_text() or "")[:200].replace("\n", " "))
print("F2 pages:", len(r2.pages), "sample:", (r2.pages[1].extract_text() or "")[:200].replace("\n", " "))
