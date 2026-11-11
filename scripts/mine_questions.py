import os
import sys
import re
import json
import zipfile
import xml.etree.ElementTree as ET
from collections import Counter, defaultdict

try:
    import pypdf
except ImportError:
    print("pypdf required")
    sys.exit(1)

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

def extract_pdf_text(path):
    r = pypdf.PdfReader(path)
    pages_text = []
    for p in r.pages:
        pages_text.append(p.extract_text() or '')
    return pages_text

print("Miner script scaffolding ready.")
