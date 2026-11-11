import pypdf
import re
import json

def extract_questions_from_pdf(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    full_text = ""
    for p in reader.pages:
        full_text += (p.extract_text() or "") + "\n"
        
    # Find all question blocks
    # Questions from 91 to 180
    # In Bernoulli gabaritos, questions appear as:
    # QUESTÃO 91 ... QUESTÃO 92 ...
    # Alternativa ... Resolução: ...
    q_indices = []
    pattern = re.compile(r"(?:QUEST[ÃA]O|Quest[ãa]o)\s+(\d{2,3})")
    for m in pattern.finditer(full_text):
        q_num = int(m.group(1))
        if 91 <= q_num <= 180:
            q_indices.append((q_num, m.start(), m.end()))
            
    # Remove duplicates if any question header appears twice (keep first or last)
    unique_q = {}
    for q_num, start, end in q_indices:
        if q_num not in unique_q:
            unique_q[q_num] = (start, end)
            
    sorted_q_nums = sorted(unique_q.keys())
    questions = []
    for i, q_num in enumerate(sorted_q_nums):
        start_pos = unique_q[q_num][0]
        end_pos = unique_q[sorted_q_nums[i+1]][0] if i + 1 < len(sorted_q_nums) else len(full_text)
        block = full_text[start_pos:end_pos].strip()
        questions.append({
            "num": q_num,
            "text": block
        })
    return questions

sample_pdf = r"BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2024\1º\SIMULADO 1 - GABARITO COMENTADO.pdf"
qs = extract_questions_from_pdf(sample_pdf)
print(f"Extracted {len(qs)} questions from {sample_pdf}")
print(f"First question (Q{qs[0]['num']}):\n{qs[0]['text'][:300]}...\n")
print(f"Natureza/Math transition (Q135 & Q136):")
q135 = next((q for q in qs if q["num"] == 135), None)
q136 = next((q for q in qs if q["num"] == 136), None)
if q135: print(f"Q135:\n{q135['text'][:200]}...\n")
if q136: print(f"Q136:\n{q136['text'][:200]}...\n")
