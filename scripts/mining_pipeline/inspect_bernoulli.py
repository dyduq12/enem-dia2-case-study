import os
import sys

base_dir = "BERNOULLI-20261110T151947Z-1-001"
print(f"Inspecting {base_dir}...")

entries = os.listdir(base_dir)
print(f"Top-level entries in {base_dir}: {entries}")

for e in sorted(entries):
    full_path = os.path.join(base_dir, e)
    if os.path.isdir(full_path):
        sub_entries = sorted(os.listdir(full_path))
        print(f"\nDirectory '{e}' contains {len(sub_entries)} items:")
        for se in sub_entries:
            sub_full = os.path.join(full_path, se)
            if os.path.isdir(sub_full):
                count_deep = len(os.listdir(sub_full))
                print(f"  [DIR] {se} ({count_deep} items inside)")
            else:
                sz = os.path.getsize(sub_full) / (1024*1024)
                print(f"  [FILE] {se} ({sz:.2f} MB)")
    else:
        sz = os.path.getsize(full_path) / (1024*1024)
        print(f"  [FILE] {e} ({sz:.2f} MB)")
