import re, pypdf

def check_bank_codes(path):
    reader = pypdf.PdfReader(path)
    full_text = ''
    for p in range(len(reader.pages)):
        full_text += f'\n[P{p+1}]\n' + (reader.pages[p].extract_text() or '')
    
    # Search for codes like ...SE...BIO... or FIS or QUI or MAT
    matches = re.findall(r'([A-Z0-9_]{3,10}(?:BIO|FIS|QUI|MAT)[A-Z0-9_]{3,15})', full_text)
    print(path)
    print(f"Found {len(matches)} bank codes with discipline indicators. Sample: {matches[:10]}")

check_bank_codes(r'BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2019\1º conjunto\Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf')
check_bank_codes(r'BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2021\1º\2021_v01_BOOK_PROVAII_TE_reduzido.pdf')
check_bank_codes(r'BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2022\1º\RESOLUÇÃO 2° DIA (1° BERNOULLI 2022).pdf')
