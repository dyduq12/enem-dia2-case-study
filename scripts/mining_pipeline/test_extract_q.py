import pypdf
import re

def test_extract_questions(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    full_text = ""
    for p in reader.pages:
        full_text += (p.extract_text() or "") + "\n---PAGE---\n"
        
    # Match questions from 91 to 180
    q_matches = list(re.finditer(r"(?:QUEST[ÃA]O|Quest[ãa]o)\s+(\d{2,3})", full_text))
    found_nums = sorted(list(set(int(m.group(1)) for m in q_matches if 91 <= int(m.group(1)) <= 180)))
    print(f"File: {pdf_path}")
    print(f"Total pages: {len(reader.pages)}, text length: {len(full_text)}")
    print(f"Questions found: {len(found_nums)} (min: {min(found_nums) if found_nums else 'None'}, max: {max(found_nums) if found_nums else 'None'})")
    return len(found_nums)

test_extract_questions(r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2024\1º\SIMULADO 1 - GABARITO COMENTADO.pdf")
test_extract_questions(r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2025\1\GABARITO - 1º BERNOULLI 2025 - D2.pdf")
test_extract_questions(r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2026\1°\BERNOULLI  - SIMULADO 1 - 2026 - 2° DIA - GABARITO.pdf")
test_extract_questions(r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2022\7º\[GABARITO DIA 2] SÉTIMO BERNOULLI 2022.pdf")
test_extract_questions(r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2023\1º\SIMULADO 1 - 2020 - BERNOULLI.pdf")
