import os

with open('FINAL/CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

paths = []
for line in lines:
    line = line.strip()
    if line.startswith('|') and not line.startswith('| :') and not 'Caminho Relativo' in line and not '---' in line and not 'Métrica Global' in line and not 'Plataforma / Provedor' in line:
        parts = [p.strip() for p in line.split('|')]
        if len(parts) >= 7:
            raw_path = parts[-2].strip('`')
            paths.append(raw_path)

print(f"Total paths in catalog: {len(paths)}")
unique_paths = sorted(set(paths))
print(f"Unique paths in catalog: {len(unique_paths)}")

missing = [p for p in unique_paths if not os.path.exists(p)]
print(f"Missing paths in catalog: {len(missing)}")
for m in missing:
    print(f"  MISSING: {m}")

if not missing:
    print("ALL PATHS IN CATALOG PHYSICALLY EXIST ON DISK!")
