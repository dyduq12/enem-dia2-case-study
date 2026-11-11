import json
import os

with open("delta_files_info.json", "r", encoding="utf-8") as f:
    files = json.load(f)

# Load deep_classify results
import deep_classify

valid_files = [f for f in deep_classify.results if f["is_valid"]]
print(f"Total valid files: {len(valid_files)}")

# Group valid files by folder/exam edition
by_subfolder = {}
for f in valid_files:
    rel = f["rel"]
    parts = rel.split(os.sep)
    # folder e.g. 2022/7º, 2022/8º, 2023/2º, etc.
    edition_key = os.path.join(*parts[1:-1]) if len(parts) > 2 else parts[1]
    by_subfolder.setdefault(edition_key, []).append(f)

print(f"\nGrouped into {len(by_subfolder)} exam edition folders:")
for edition, flist in sorted(by_subfolder.items()):
    print(f"\n--- Edition: {edition} ({len(flist)} valid Dia 2 files) ---")
    for f in flist:
        print(f"  {os.path.basename(f['rel'])} | Pages: {f['pages']} | Size: {f['sz_mb']:.2f} MB")
