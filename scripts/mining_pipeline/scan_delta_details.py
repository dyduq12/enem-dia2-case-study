import os
import pypdf

base = "BERNOULLI-20261110T151947Z-1-001"
all_files = []
for root, dirs, files in os.walk(base):
    for f in files:
        full = os.path.join(root, f)
        rel = os.path.relpath(full, base)
        sz = os.path.getsize(full)
        all_files.append((rel, sz, full))

all_files.sort(key=lambda x: x[0])
mid = len(all_files) // 2
delta_files = all_files[mid:]

print(f"Scanning {len(delta_files)} Delta files...")

results = []
for idx, (rel, sz, full) in enumerate(delta_files):
    ext = os.path.splitext(rel)[1].lower()
    num_pages = 0
    sample_text = ""
    error = None
    if ext == ".pdf":
        try:
            reader = pypdf.PdfReader(full)
            num_pages = len(reader.pages)
            # Sample text from first 2 pages
            for p in range(min(2, num_pages)):
                sample_text += reader.pages[p].extract_text() or ""
        except Exception as e:
            error = str(e)
    results.append({
        "index": mid + idx,
        "delta_idx": idx,
        "rel": rel,
        "sz_mb": sz / (1024*1024),
        "ext": ext,
        "pages": num_pages,
        "sample": sample_text[:300].replace("\n", " "),
        "error": error
    })

print(f"Successfully processed info for {len(results)} files.")

# Write results to a json file for easy processing
import json
with open("delta_files_info.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print("Saved delta_files_info.json")
