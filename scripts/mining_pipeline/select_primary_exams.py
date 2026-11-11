import json
import os
import pypdf
import re

with open("delta_final_classified.json", "r", encoding="utf-8") as f:
    classified = json.load(f)

valid = [c for c in classified if c["status"] == "VALIDO_DIA2"]

# Group by edition key
editions = {}
for c in valid:
    rel = c["rel"]
    parts = rel.split(os.sep)
    # Year/Simulado folder
    year = parts[1]
    simu = parts[2]
    key = f"{year}/{simu}"
    editions.setdefault(key, []).append(c)

print(f"Total unique edition keys: {len(editions)}")

# For each edition, pick the primary file
primary_sources = []
for key, flist in sorted(editions.items()):
    # Preference order:
    # 1. Contains "gabarito" or "resolução" or "resolucao" or "comentado"
    # 2. Most pages
    def score_file(item):
        name = item["rel"].lower()
        score = 0
        if "gabarito" in name: score += 100
        if "comentado" in name or "comentdado" in name: score += 50
        if "resolução" in name or "resolucao" in name or "res_" in name: score += 80
        if "prova" in name and "gabarito" not in name: score += 10
        score += item["pages"]
        # avoid 1st page only or short gabarito
        if item["pages"] < 10: score -= 500
        return score
    
    sorted_flist = sorted(flist, key=score_file, reverse=True)
    best = sorted_flist[0]
    
    # Check if there are other distinct exams in the same folder (e.g. EXTRA vs Regular)
    # Check if flist has both "EXTRA" and non-extra
    extras = [f for f in flist if "extra" in f["rel"].lower()]
    non_extras = [f for f in flist if "extra" not in f["rel"].lower()]
    
    if extras and non_extras:
        # We have TWO distinct exams in this folder!
        best_extra = sorted(extras, key=score_file, reverse=True)[0]
        best_reg = sorted(non_extras, key=score_file, reverse=True)[0]
        primary_sources.append((f"{key} (Regular)", best_reg, [f for f in non_extras if f != best_reg]))
        primary_sources.append((f"{key} (Extra)", best_extra, [f for f in extras if f != best_extra]))
    else:
        primary_sources.append((key, best, [f for f in flist if f != best]))

print(f"\nTotal Primary Unique Exam Sources identified: {len(primary_sources)}")
for exam_name, prim, others in primary_sources:
    print(f"\nExam: {exam_name}")
    print(f"  Primary: {prim['rel']} ({prim['pages']} pages, {prim['sz_mb']:.2f} MB)")
    if others:
        print(f"  Paired/Duplicate files ({len(others)}):")
        for o in others:
            print(f"    - {o['rel']} ({o['pages']} pages)")

with open("delta_primary_exams.json", "w", encoding="utf-8") as f:
    json.dump([
        {
            "exam_name": name,
            "primary": prim,
            "associated_files": [prim] + others
        }
        for name, prim, others in primary_sources
    ], f, ensure_ascii=False, indent=2)
