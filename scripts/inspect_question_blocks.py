import os, pypdf, re

def show_questions(rel, sample_q_nums=[91, 92, 105, 120, 136, 150]):
    path = os.path.join('BERNOULLI-20261110T151947Z-1-001', rel)
    reader = pypdf.PdfReader(path)
    full_text = ''
    for p in range(len(reader.pages)):
        full_text += f'\n[P{p+1}]\n' + (reader.pages[p].extract_text() or '')
        
    for q in sample_q_nums:
        # Search for QUESTÃO <q>
        pattern = rf'(QUEST[ÃA]O\s+{q}\b.*?)(?=QUEST[ÃA]O\s+\d{{1,3}}\b|\Z)'
        m = re.search(pattern, full_text, re.DOTALL | re.IGNORECASE)
        if m:
            block = m.group(1).strip()
            print(f"=== {rel} - Q{q} ===")
            print(block[:400] + ('...' if len(block) > 400 else ''))
            print()

show_questions(r'BERNOULLI\2019\1º conjunto\Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf')
show_questions(r'BERNOULLI\2021\1º\2021_v01_BOOK_PROVAII_TE_reduzido.pdf')
show_questions(r'BERNOULLI\2022\1º\RESOLUÇÃO 2° DIA (1° BERNOULLI 2022).pdf')
