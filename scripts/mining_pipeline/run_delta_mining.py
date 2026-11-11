import json
import os
import re
from collections import Counter, defaultdict
import pypdf
import semantic_engine as se

# Load primary exams status
with open("delta_exams_extract_status.json", "r", encoding="utf-8") as f:
    exam_statuses = json.load(f)

# Load catalog of all 185 files
with open("delta_final_classified.json", "r", encoding="utf-8") as f:
    all_files_catalog = json.load(f)

print(f"Loaded {len(exam_statuses)} exam entries and {len(all_files_catalog)} cataloged files.")

# Filter out duplicate exam 2025/3 (which is identical to 2025/2)
unique_exams = []
seen_hashes = set()
duplicates_noted = []

for item in exam_statuses:
    rel = item["selected_file"]
    full_path = os.path.join("BERNOULLI-20261110T151947Z-1-001", rel)
    
    # Check sha256 from catalog
    cat_entry = next((c for c in all_files_catalog if c["rel"] == rel), None)
    fhash = cat_entry["sha256"] if cat_entry else ""
    
    if fhash in seen_hashes:
        duplicates_noted.append((item["exam_name"], rel, fhash))
        print(f"Skipping identical exam duplicate: {item['exam_name']} ({rel})")
        continue
        
    seen_hashes.add(fhash)
    unique_exams.append(item)

print(f"\nProcessing {len(unique_exams)} unique exams (deduplicated)...")

# Question extraction helper
def extract_exam_questions(pdf_path):
    reader = pypdf.PdfReader(pdf_path)
    full_text = ""
    for p in reader.pages:
        full_text += (p.extract_text() or "") + "\n"
        
    q_indices = []
    pattern = re.compile(r"(?:QUEST[ÃA]O|Quest[ãa]o)\s+(\d{2,3})")
    for m in pattern.finditer(full_text):
        q_num = int(m.group(1))
        if 91 <= q_num <= 180:
            q_indices.append((q_num, m.start(), m.end()))
            
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
        questions.append((q_num, block))
    return questions

# Accumulators
total_questions = 0
discipline_counts = Counter()
discipline_topics = defaultdict(Counter)
discipline_skills = defaultdict(Counter)
topic_skills_map = defaultdict(lambda: Counter())
interdisciplinary_counts = Counter()
exam_level_stats = []

for idx, ex in enumerate(unique_exams):
    exam_name = ex["exam_name"]
    rel_path = ex["selected_file"]
    full_path = os.path.join("BERNOULLI-20261110T151947Z-1-001", rel_path)
    
    qs = extract_exam_questions(full_path)
    print(f"[{idx+1}/{len(unique_exams)}] {exam_name:25} -> {len(qs)} questions extracted")
    
    ex_disc_counts = Counter()
    
    for q_num, q_text in qs:
        res = se.classify_question(q_num, q_text)
        disc = res["discipline"]
        topic = res["topic"]
        skill = res["skill"]
        interdisc = res["interdisciplinary"]
        
        total_questions += 1
        discipline_counts[disc] += 1
        ex_disc_counts[disc] += 1
        discipline_topics[disc][topic] += 1
        discipline_skills[disc][skill] += 1
        topic_skills_map[topic][skill] += 1
        
        for item in interdisc:
            interdisciplinary_counts[item] += 1
            
    exam_level_stats.append({
        "exam_name": exam_name,
        "file": rel_path,
        "total_qs": len(qs),
        "disciplines": dict(ex_disc_counts)
    })

print(f"\n==========================================")
print(f"Total Unique Questions Analyzed: {total_questions}")
print(f"Distribution by Discipline:")
for d, cnt in discipline_counts.most_common():
    pct = (cnt / total_questions) * 100
    print(f"  {d:12}: {cnt:4} ({pct:5.2f}%)")

# Save raw mining results to json
mining_data = {
    "total_questions": total_questions,
    "unique_exams_count": len(unique_exams),
    "discipline_counts": dict(discipline_counts),
    "discipline_topics": {d: dict(cnt) for d, cnt in discipline_topics.items()},
    "discipline_skills": {d: dict(cnt) for d, cnt in discipline_skills.items()},
    "topic_skills_map": {t: dict(cnt) for t, cnt in topic_skills_map.items()},
    "interdisciplinary_counts": dict(interdisciplinary_counts),
    "exam_level_stats": exam_level_stats,
    "duplicates_noted": duplicates_noted
}

with open("delta_mining_results.json", "w", encoding="utf-8") as f:
    json.dump(mining_data, f, ensure_ascii=False, indent=2)

print("\nSaved delta_mining_results.json successfully!")
