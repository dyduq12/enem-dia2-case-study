import hashlib
import json
import os

with open("delta_files_info.json", "r", encoding="utf-8") as f:
    files = json.load(f)

def get_hash(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        while chunk := f.read(65536):
            h.update(chunk)
    return h.hexdigest()

print("Calculating hashes...")
hash_map = {}
for item in files:
    full = os.path.join("BERNOULLI-20261110T151947Z-1-001", item["rel"])
    try:
        fhash = get_hash(full)
    except Exception as e:
        fhash = f"ERROR_{e}"
    item["sha256"] = fhash
    hash_map.setdefault(fhash, []).append(item["rel"])

print(f"Total files: {len(files)}")
print(f"Unique file hashes: {len(hash_map)}")

dup_count = 0
for h, flist in hash_map.items():
    if len(flist) > 1:
        dup_count += (len(flist) - 1)
        print(f"\nExact Hash Duplicate ({len(flist)} files):")
        for f in flist:
            print(f"  {f}")

print(f"\nTotal duplicate files by exact binary hash: {dup_count}")

with open("delta_files_hashed.json", "w", encoding="utf-8") as f:
    json.dump(files, f, ensure_ascii=False, indent=2)
