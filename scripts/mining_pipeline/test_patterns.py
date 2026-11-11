import pypdf
import os
import re

sample_paths = [
    r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2022\7º\[GABARITO DIA 2] SÉTIMO BERNOULLI 2022.pdf",
    r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2023\1º\SIMULADO 1 - 2020 - BERNOULLI.pdf",
    r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2024\3º\SIMULADO 3 - GABARITO COMENTADO.pdf",
    r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2025\1\GABARITO - 1º BERNOULLI 2025 - D2.pdf",
    r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2026\1°\BERNOULLI  - SIMULADO 1 - 2026 - 2° DIA - GABARITO.pdf",
]

for p in sample_paths:
    print(f"\n==========================================")
    print(f"Testing {os.path.basename(p)}...")
    reader = pypdf.PdfReader(p)
    print(f"Total pages: {len(reader.pages)}")
    
    # Check pages 2 and 3
    for pno in [1, 2, min(len(reader.pages)-1, 35)]:
        txt = reader.pages[pno].extract_text() or ""
        print(f"--- Page {pno+1} snippet ---")
        lines = [line.strip() for line in txt.split("\n") if line.strip()]
        for l in lines[:10]:
            print("  ", l)
