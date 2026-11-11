import os, re

with open('FINAL/TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md', 'r', encoding='utf-8') as f:
    text = f.read()

paths = re.findall(r'`([^`]+\.pdf|[^`]+\.xlsx)`', text)
print(f"Total paths in trilha: {len(paths)}")
unique_paths = sorted(set(paths))
print(f"Unique paths in trilha: {len(unique_paths)}")

missing = [p for p in unique_paths if not os.path.exists(p)]
print(f"Missing paths in trilha: {len(missing)}")
for m in missing:
    print(f"  MISSING: {m}")

if not missing:
    print("ALL PATHS IN TRILHA PHYSICALLY EXIST ON DISK!")
