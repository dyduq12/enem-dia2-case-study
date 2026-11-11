import os
import re

def inspect_all_filenames():
    base_dirs = ['APEIRON-20261110T152018Z-1-001', 'BERNOULLI-20261110T151947Z-1-001', 'ENEM', 'POLIEDRO', 'SAS', '_ENEM_DIA_2_BRUTO']
    
    for b in base_dirs:
        print(f"==================================================")
        print(f"ANALYZING: {b}")
        print(f"==================================================")
        files = []
        for root, dirs, fnames in os.walk(b):
            for f in fnames:
                files.append(os.path.join(root, f))
        
        print(f"Total files: {len(files)}")
        # Print first 20 filenames
        for f in files[:20]:
            rel = os.path.relpath(f, b)
            print(" ", rel)
        if len(files) > 20:
            print(f" ... and {len(files)-20} more")
        print()

if __name__ == '__main__':
    inspect_all_filenames()
