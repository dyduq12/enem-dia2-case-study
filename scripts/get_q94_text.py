import os, pypdf, re

path = r'BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2019\1º conjunto\Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf'
reader = pypdf.PdfReader(path)
full_text = ''
for p in range(len(reader.pages)):
    full_text += f'\n[P{p+1}]\n' + (reader.pages[p].extract_text() or '')

m = re.search(r'(?:QUEST[ÃA]O|Quest[ãa]o)\s+94\b(.*?)(?=(?:QUEST[ÃA]O|Quest[ãa]o)\s+95\b|\Z)', full_text, re.DOTALL | re.IGNORECASE)
if m:
    print("Full Q94 text:\n", m.group(1))
