import pypdf

files = [
    r'BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2021\7º\7- Gabarito Segundo dia.pdf',
    r'BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2021\7º\7- Segundo Dia.pdf',
    r'BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2021\7º\GABARITO SIMU 7- PROVA 2.pdf',
    r'BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2021\7º\PROVA 2° DIA (7° BERNOULLI).pdf',
    r'BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2021\7º\[GABARITO DIA 2] - 7 BERNOULLI 2021.pdf',
    r'BERNOULLI-20261110T151947Z-1-001\BERNOULLI\2021\7º\[PROVA DIA 2] - 7 BERNOULLI 2021.pdf'
]

for f in files:
    r = pypdf.PdfReader(f)
    print(f, len(r.pages), 'pages')
    print('  p1:', (r.pages[0].extract_text() or '')[:100].replace('\n', ' '))
    if len(r.pages) > 1:
        print('  p2:', (r.pages[1].extract_text() or '')[:100].replace('\n', ' '))
