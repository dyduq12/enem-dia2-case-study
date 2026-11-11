import os
import sys

def explore():
    base_dirs = ['APEIRON-20261110T152018Z-1-001', 'BERNOULLI-20261110T151947Z-1-001', 'ENEM', 'POLIEDRO', 'SAS', '_ENEM_DIA_2_BRUTO']
    for d in base_dirs:
        print(f"=== {d} ===")
        file_count = 0
        dir_count = 0
        subdirs = {}
        for root, dirs, files in os.walk(d):
            rel = os.path.relpath(root, d)
            first_level = rel.split(os.sep)[0] if rel != '.' else '.'
            subdirs[first_level] = subdirs.get(first_level, 0) + len(files)
            file_count += len(files)
            dir_count += len(dirs)
        print(f"Total files: {file_count}, Subdirs: {dir_count}")
        print("First level distribution:")
        for k, v in sorted(subdirs.items(), key=lambda x: -x[1])[:10]:
            print(f"  {k}: {v} files")
        print()

if __name__ == '__main__':
    explore()
