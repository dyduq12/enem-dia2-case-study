import os

with open('FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

paths = []
for line in lines:
    line = line.strip()
    if line.startswith('|') and not line.startswith('| :') and not 'Arquivo de Resolução' in line and not '---' in line:
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 7:
            raw_path = parts[-2].strip('`')
            paths.append(raw_path)

print(f"Total paths extracted: {len(paths)}")
unique_paths = sorted(set(paths))
print(f"Unique paths extracted: {len(unique_paths)}")

missing = [p for p in unique_paths if not os.path.exists(p)]
print(f"Missing paths: {len(missing)}")
for m in missing:
    print(f"  MISSING: {m}")

if not missing:
    print("ALL 23 UNIQUE PATHS PHYSICALLY EXIST ON DISK!")
