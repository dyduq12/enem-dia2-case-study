import os
import hashlib

def get_file_hash(path):
    h = hashlib.md5()
    with open(path, 'rb') as f:
        # Read first 64KB and last 64KB for fast hashing of large files
        chunk = f.read(65536)
        h.update(chunk)
        size = os.path.getsize(path)
        if size > 65536:
            f.seek(max(0, size - 65536))
            h.update(f.read(65536))
        h.update(str(size).encode())
    return h.hexdigest()

def check_duplicates():
    base_dirs = ['APEIRON-20261110T152018Z-1-001', 'BERNOULLI-20261110T151947Z-1-001', 'ENEM', 'POLIEDRO', 'SAS', '_ENEM_DIA_2_BRUTO']
    hashes = {}
    duplicates = []
    total_files = 0
    
    for b in base_dirs:
        for root, dirs, files in os.walk(b):
            for f in files:
                p = os.path.join(root, f)
                total_files += 1
                fh = get_file_hash(p)
                if fh in hashes:
                    duplicates.append((hashes[fh], p))
                else:
                    hashes[fh] = p
                    
    print(f"Total files checked: {total_files}")
    print(f"Unique files by hash: {len(hashes)}")
    print(f"Duplicate instances: {len(duplicates)}")
    
    # Check duplicates involving _ENEM_DIA_2_BRUTO
    bruto_dups = [d for d in duplicates if '_ENEM_DIA_2_BRUTO' in d[0] or '_ENEM_DIA_2_BRUTO' in d[1]]
    print(f"Duplicates involving _ENEM_DIA_2_BRUTO: {len(bruto_dups)}")

if __name__ == '__main__':
    check_duplicates()
