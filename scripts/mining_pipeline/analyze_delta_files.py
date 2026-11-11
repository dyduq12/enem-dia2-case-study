import os

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
print(f"Total files in dataset: {len(all_files)}")
print(f"Delta files (index {mid} to {len(all_files)-1}): {len(delta_files)}")

# Group by folder / category
categories = {}
for rel, sz, full in delta_files:
    parts = rel.split(os.sep)
    # e.g. BERNOULLI, 2023, ...
    folder = parts[1] if len(parts) > 1 else "ROOT"
    categories.setdefault(folder, []).append((rel, sz, full))

for folder, flist in sorted(categories.items()):
    total_sz = sum(x[1] for x in flist) / (1024*1024)
    print(f"\nFolder: {folder} ({len(flist)} files, {total_sz:.2f} MB)")
    for rel, sz, _ in flist:
        print(f"  {rel} ({sz/(1024*1024):.2f} MB)")
