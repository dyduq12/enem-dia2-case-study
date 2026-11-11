import os
import re
import sys
import pypdf

def classify_file(filepath):
    relpath = os.path.relpath(filepath, '.')
    fname = os.path.basename(filepath)
    fname_lower = fname.lower()
    path_lower = relpath.lower()
    ext = os.path.splitext(filepath)[1].lower()

    # Determine Provider / Banca
    provider = "OUTROS"
    if "apeiron" in path_lower:
        provider = "APEIRON"
    elif "bernoulli" in path_lower:
        provider = "BERNOULLI"
    elif "poliedro" in path_lower:
        provider = "POLIEDRO"
    elif "sas" in path_lower:
        provider = "SAS"
    elif "enem" in path_lower:
        provider = "ENEM_OFICIAL"
    elif "_enem_dia_2_bruto" in path_lower:
        # Check if filename indicates provider
        if "bernoulli" in fname_lower:
            provider = "BERNOULLI"
        elif "sas" in fname_lower:
            provider = "SAS"
        elif "poliedro" in fname_lower:
            provider = "POLIEDRO"
        elif "apeiron" in fname_lower:
            provider = "APEIRON"
        elif "enem" in fname_lower:
            provider = "ENEM_OFICIAL"
        elif "ap2" in fname_lower or "ag2" in fname_lower or "cnst" in fname_lower:
            provider = "SAS" # AP2/AG2 CNST-MST are SAS Avaliações Periódicas / Simulados
        else:
            provider = "SIMULADOS_GERAIS"

    # Determine Year
    year = None
    year_match = re.search(r'(200[9]|201[0-9]|202[0-6])', path_lower)
    if year_match:
        year = year_match.group(1)
    else:
        # Check short 2-digit years like -19_, -20_, -21_, -22_
        short_match = re.search(r'[-_](1[89]|2[0-6])[-_ ]', fname_lower)
        if short_match:
            year = "20" + short_match.group(1)

    # Determine Type: Caderno vs Gabarito vs Resolução
    doc_type = "OUTRO"
    if any(k in fname_lower for k in ["resolucao", "resolução", "comentada", "comentadas"]):
        doc_type = "RESOLUCAO_COMENTADA"
    elif any(k in fname_lower for k in ["gabarito", "gab", "ag2"]):
        doc_type = "GABARITO"
    elif any(k in fname_lower for k in ["prova", "caderno", "simulado", "ap2", "cnst"]):
        doc_type = "CADERNO_QUESTOES"
    elif ext == ".pdf":
        doc_type = "CADERNO_QUESTOES" # Default for exam pdfs if not gabarito

    # Determine Day / Subjects: Dia 1 vs Dia 2
    # Dia 2 signals: d2, dia 2, 2º dia, 2° dia, prova 2, prova ii, 2ºdia, 2°dia, dia_2, cnst-mst, natureza, matematica
    # Dia 1 signals: d1, dia 1, 1º dia, 1° dia, prova 1, prova i, 1ºdia, 1°dia, dia_1, humanas, linguagens, redacao
    day = "DESCONHECIDO"
    
    is_d2 = False
    is_d1 = False
    
    # Explicit D2 patterns
    if re.search(r'(\bd2\b|\bd-2\b|dia\s*2|2[º°\s_-]*dia|prova\s*(2|ii)|segundo\s*dia|cnst[-_ ]*mst|matem[aá]tica|natureza)', fname_lower):
        is_d2 = True
    if re.search(r'(\bd2\b|\bd-2\b|dia\s*2|2[º°\s_-]*dia|prova\s*(2|ii)|segundo\s*dia|cnst[-_ ]*mst)', path_lower):
        is_d2 = True

    # Explicit D1 patterns
    if re.search(r'(\bd1\b|\bd-1\b|dia\s*1|1[º°\s_-]*dia|prova\s*(1|i)|primeiro\s*dia|ch[-_ ]*lc|humanas|linguagens|reda[cç][aã]o)', fname_lower):
        is_d1 = True
    if re.search(r'(\bd1\b|\bd-1\b|dia\s*1|1[º°\s_-]*dia|prova\s*(1|i)|primeiro\s*dia)', path_lower):
        is_d1 = True

    # If both or neither, we can inspect PDF text
    return {
        'path': relpath,
        'filename': fname,
        'ext': ext,
        'size': os.path.getsize(filepath),
        'provider': provider,
        'year': year,
        'doc_type': doc_type,
        'is_d1_name': is_d1,
        'is_d2_name': is_d2
    }

def main():
    base_dirs = ['APEIRON-20261110T152018Z-1-001', 'BERNOULLI-20261110T151947Z-1-001', 'ENEM', 'POLIEDRO', 'SAS', '_ENEM_DIA_2_BRUTO']
    records = []
    for b in base_dirs:
        for root, dirs, files in os.walk(b):
            for f in files:
                full = os.path.join(root, f)
                records.append(classify_file(full))

    print(f"Total files mapped: {len(records)}")
    
    # Stats
    pdf_count = sum(1 for r in records if r['ext'] == '.pdf')
    print(f"PDF count: {pdf_count}")
    
    # Providers
    providers = {}
    for r in records:
        providers[r['provider']] = providers.get(r['provider'], 0) + 1
    print("\nProviders:")
    for p, c in sorted(providers.items(), key=lambda x: -x[1]):
        print(f"  {p}: {c}")

    # Doc Types
    dtypes = {}
    for r in records:
        dtypes[r['doc_type']] = dtypes.get(r['doc_type'], 0) + 1
    print("\nDoc Types (heuristic):")
    for dt, c in sorted(dtypes.items(), key=lambda x: -x[1]):
        print(f"  {dt}: {c}")

    # Day name heuristics
    d2_only = sum(1 for r in records if r['is_d2_name'] and not r['is_d1_name'])
    d1_only = sum(1 for r in records if r['is_d1_name'] and not r['is_d2_name'])
    both = sum(1 for r in records if r['is_d1_name'] and r['is_d2_name'])
    neither = sum(1 for r in records if not r['is_d1_name'] and not r['is_d2_name'])
    print(f"\nDay detection by filename/path:")
    print(f"  Dia 2 only: {d2_only}")
    print(f"  Dia 1 only: {d1_only}")
    print(f"  Both matched: {both}")
    print(f"  Neither matched: {neither}")

if __name__ == '__main__':
    main()
