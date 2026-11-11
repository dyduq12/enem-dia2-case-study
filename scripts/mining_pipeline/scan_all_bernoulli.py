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
print(f"Total files found in {base}: {len(all_files)}")
print(f"Total size: {sum(x[1] for x in all_files)/(1024*1024):.2f} MB")

# Print top-level folders
top_level = sorted(os.listdir(os.path.join(base, "BERNOULLI")))
print("\nTop-level subfolders inside BERNOULLI-20261110T151947Z-1-001/BERNOULLI:")
for idx, d in enumerate(top_level):
    count = sum(1 for rel, _, _ in all_files if rel.startswith(os.path.join("BERNOULLI", d)))
    print(f"  [{idx}] {d}: {count} files")

print("\nAll files list (first 20):")
for r, s, _ in all_files[:20]:
    print(f"  {r} ({s/(1024*1024):.2f} MB)")

print("\nAll files list (around the middle):")
mid = len(all_files) // 2
for r, s, _ in all_files[max(0, mid-10):mid+10]:
    print(f"  {r} ({s/(1024*1024):.2f} MB)")

print("\nAll files list (last 20):")
for r, s, _ in all_files[-20:]:
    print(f"  {r} ({s/(1024*1024):.2f} MB)")
