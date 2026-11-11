import os
import sys
import re
import json
import zipfile
import hashlib
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

try:
    import pypdf
except ImportError:
    print("pypdf is required")
    sys.exit(1)

def hash_file(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        while chunk := f.read(8192):
            h.update(chunk)
    return h.hexdigest()

def parse_xlsx(path):
    with zipfile.ZipFile(path) as z:
        ss = []
        if 'xl/sharedStrings.xml' in z.namelist():
            tree = ET.fromstring(z.read('xl/sharedStrings.xml'))
            for elem in tree.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}si'):
                text = ''.join(t.text for t in elem.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}t') if t.text)
                ss.append(text)
        sheet_tree = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        rows = []
        for r in sheet_tree.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
            row_data = []
            for c in r.findall('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                v = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                t = c.get('t')
                val = v.text if v is not None else ''
                if t == 's' and val.isdigit():
                    val = ss[int(val)]
                row_data.append(val)
            if any(row_data):
                rows.append(row_data)
        return rows

print("Helper functions defined successfully.")
