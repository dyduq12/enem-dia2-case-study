import json
import os

with open("delta_catalog.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

valid = [c for c in catalog if c["status"] == "VALIDO_DIA2"]
print(f"Total valid files: {len(valid)}")

# Let's see all valid files and how they group by edition/folder
editions = {}
for c in valid:
    rel = c["rel"]
    parts = rel.split(os.sep)
    # Year/Simulado folder
    if len(parts) >= 3:
        year = parts[1]
        simu = parts[2]
        key = f"{year}/{simu}"
    else:
        key = parts[0]
    editions.setdefault(key, []).append(c)

print(f"\nUnique Exam Edition Keys: {len(editions)}")
for k, flist in sorted(editions.items()):
    print(f"\nKey: {k} ({len(flist)} files)")
    for f in flist:
        print(f"  {f['rel']} (pages: {f['pages']}, {f['sz_mb']:.2f} MB)")
