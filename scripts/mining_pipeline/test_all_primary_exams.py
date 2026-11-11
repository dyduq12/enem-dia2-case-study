import json
import pypdf
import os
import re

with open("delta_primary_exams.json", "r", encoding="utf-8") as f:
    primary_exams = json.load(f)

print(f"Testing text extraction across all {len(primary_exams)} primary exams...\n")

results = []
for exam in primary_exams:
    name = exam["exam_name"]
    prim = exam["primary"]
    rel = prim["rel"]
    full_path = os.path.join("BERNOULLI-20261110T151947Z-1-001", rel)
    
    pages = 0
    q_count = 0
    text_len = 0
    error = None
    
    try:
        reader = pypdf.PdfReader(full_path)
        pages = len(reader.pages)
        full_text = ""
        for p in reader.pages:
            full_text += (p.extract_text() or "") + "\n"
        text_len = len(full_text)
        
        # Check questions found
        pattern = re.compile(r"(?:QUEST[ÃA]O|Quest[ãa]o)\s+(\d{2,3})")
        found = set()
        for m in pattern.finditer(full_text):
            num = int(m.group(1))
            if 91 <= num <= 180:
                found.add(num)
        q_count = len(found)
        
        # If primary has 0 questions or small text, check if any associated file has text
        if q_count < 40 and exam.get("associated_files"):
            for assoc in exam["associated_files"]:
                if assoc["rel"] != rel:
                    assoc_full = os.path.join("BERNOULLI-20261110T151947Z-1-001", assoc["rel"])
                    r_assoc = pypdf.PdfReader(assoc_full)
                    txt_assoc = ""
                    for p in r_assoc.pages:
                        txt_assoc += (p.extract_text() or "") + "\n"
                    found_assoc = set()
                    for m in pattern.finditer(txt_assoc):
                        num = int(m.group(1))
                        if 91 <= num <= 180:
                            found_assoc.add(num)
                    if len(found_assoc) > q_count:
                        print(f"  Swapping to richer associated file for {name}: {assoc['rel']} ({len(found_assoc)} qs vs {q_count})")
                        rel = assoc["rel"]
                        full_path = assoc_full
                        full_text = txt_assoc
                        text_len = len(txt_assoc)
                        pages = len(r_assoc.pages)
                        q_count = len(found_assoc)
                        
    except Exception as e:
        error = str(e)
        
    results.append({
        "exam_name": name,
        "selected_file": rel,
        "pages": pages,
        "text_len": text_len,
        "q_count": q_count,
        "error": error
    })
    print(f"Exam: {name:25} | Qs: {q_count:2} | Pages: {pages:2} | Chars: {text_len:6} | File: {os.path.basename(rel)}")

with open("delta_exams_extract_status.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
