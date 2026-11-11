import os
import re
import json
import pypdf
from collections import Counter

base = 'BERNOULLI-20261110T151947Z-1-001'

with open('classified_gamma.json', 'r', encoding='utf-8') as f:
    classified = json.load(f)

valid = [c for c in classified if c['status'] == 'VALIDO_DIA2']

editions = {}
for c in valid:
    ed = c['edition']
    if not ed or 'VESTGEEK' in ed or 'Prova 2.pdf' in ed:
        continue
    if ed not in editions:
        editions[ed] = []
    editions[ed].append(c)

edition_source_map = {}
for ed, files in sorted(editions.items()):
    res_files = [f for f in files if f['type'] == 'RESOLUCAO']
    prova_files = [f for f in files if f['type'] == 'PROVA']
    if res_files:
        selected = max(res_files, key=lambda x: x['pages'])
    elif prova_files:
        selected = max(prova_files, key=lambda x: x['pages'])
    else:
        selected = files[0]
    edition_source_map[ed] = selected

print(f"Refining classification for {len(edition_source_map)} editions.")

# Refined regex patterns for disciplines
DISC_PATTERNS = {
    'Fisica': re.compile(r'\b(velocidade|acelera[çc][ãa]o|cinem[áa]tica|movimento|trajet[óo]ria|lan[çc]amento|radar|quil[ôo]metro|km/h|m/s|newton|for[çc]a|atrito|energia cin[ée]tica|energia potencial|trabalho mec[âa]nico|pot[êe]ncia mec[âa]nica|press[ãa]o hidrost[áa]tica|empuxo|hidrost[áa]tica|densidade|stevin|pascal|arquimedes|flutua|vasos comunicantes|termodin[âa]mica|calorimetria|calor espec[íi]fico|calor latente|temperatura|trocas de calor|condu[çc][ãa]o|convec[çc][ãa]o|irradia[çc][ãa]o|dilata[çc][ãa]o|circuito|resistor|resist[êe]ncia el[ée]trica|voltagem|tens[ãa]o el[ée]trica|corrente el[ée]trica|ddp|diferen[çc]a de potencial|pot[êe]ncia el[ée]trica|kwh|quilowatt|l[âa]mpada|fus[íi]vel|disjuntor|ohm|leis de ohm|onda|frequ[êe]ncia|hertz|comprimento de onda|ac[úu]stica|som|resson[âa]ncia|doppler|difra[çc][ãa]o|interfer[êe]ncia|refra[çc][ãa]o da luz|reflex[ãa]o|espelho|lente|[óo]ptic[ao]|[óo]tic[ao]|miopia|hipermetropia|eletromagnetismo|campo magn[ée]tico|[íi]m[ãa]|indux|faraday|espiras|transformador|gravita[çc][ãa]o|kepler|sat[ée]lite|f[óo]ton|efeito fotoel[ée]trico)\b', re.IGNORECASE),
    
    'Quimica': re.compile(r'\b(qu[íi]mic[ao]|rea[çc][ãa]o qu[íi]mica|reagente|produto|estequiometr|massa molar|mol\b|mols\b|concentra[çc][ãa]o|solu[çc][ãa]o aquosa|soluto|solvente|molaridade|solubilidade|dilui[çc][ãa]o|precipita|ph\b|poh|acidez|alcalin|b[áa]sic[ao]|[áa]cido|hidr[óo]xido|[íi]on|[íi]ons|oxirredu[çc][ãa]o|oxida[çc][ãa]o|redu[çc][ãa]o|pilha|eletrodo|[âa]nodo|c[áa]todo|eletr[óo]lise|corros[ãa]o|entalpia|termoqu[íi]mic|exot[ée]rmic|endot[ée]rmic|calor de combust[ãa]o|lei de hess|le chatelier|equil[íi]brio qu[íi]mico|tabela peri[óo]dica|liga[çc][ãa]o covalente|liga[çc][ãa]o i[ôo]nica|liga[çc][ãa]o met[áa]lica|for[çc]as intermoleculares|liga[çc][ãa]o de hidrog[êe]nio|dipolo|hidrocarboneto|[áa]lcool|alde[íi]do|cetona|[ée]ster|[ée]ter|amina|amida|[áa]cido carbox[íi]lico|isomeria|pol[íi]mero|biodiesel|saponifica[çc]|esterifica[çc]|destila[çc][ãa]o|tratamento de [áa]gua|flocula[çc][ãa]o|decanta[çc][ãa]o|chuva [áa]cida)\b', re.IGNORECASE),
    
    'Biologia': re.compile(r'\b(biol[óo]gic[ao]|c[ée]lula|citoplasma|membrana plasm[áa]tica|mitoc[ôo]ndria|cloroplasto|fotoss[íi]ntese|respira[çc][ãa]o celular|fermenta[çc][ãa]o|atp|dna|rna|gene\b|genes\b|gen[ée]tic|heredogram|cromossomo|alelo|muta[çc][ãa]o|transcri[çc][ãa]o|tradu[çc][ãa]o|s[íi]ntese proteica|enzima|ecossistema|ecol[óo]gic|cadeia alimentar|teia alimentar|n[íi]vel tr[óo]fico|produtor|consumidor|decompositor|bioma|cerrado|caatinga|mata atl[âa]ntica|amaz[ôo]nia|desmatamento|eutrofiza[çc][ãa]o|biodiversidade|esp[ée]cie|popula[çc][ãa]o|fisiologia|sangue|imun|vacina|soro|anticorpo|v[íi]rus|bact[ée]ria|protozo[áa]rio|fungo|doen[çc]a|dengue|chagas|mal[áa]ria|parasit|horm[ôo]nio|end[óo]crino|digest|circulat[óo]rio|respirat[óo]rio|excret|nervo|neur[ôo]nio|evolu[çc][ãa]o|sele[çc][ãa]o natural|darwin|lamarck|planta|vegetal|bot[âa]nic|xilema|floema|transg[êe]nic|biotecnologia)\b', re.IGNORECASE)
}

# Granular Topic taxonomy patterns
TOPIC_PATTERNS = {
    'Matematica': [
        ('Grandezas Proporcionais, Razao e Escala', re.compile(r'\b(proporcional|escala|raz[ãa]o|regra de tr[êe]s|porcentagem|divis[ãa]o proporcional|vaz[ãa]o|densidade demogr[áa]fica)\b', re.IGNORECASE), 'H1, H2, H3'),
        ('Geometria Espacial', re.compile(r'\b(prisma|cilindro|cone|esfera|pir[âa]mide|tronco|volume|capacidade|planifica[çc][ãa]o|proje[çc][ãa]o ortogonal|cubo|paralelep[íi]pedo)\b', re.IGNORECASE), 'H7, H8, H9'),
        ('Geometria Plana', re.compile(r'\b([áa]rea|per[íi]metro|tri[âa]ngulo|quadrado|ret[âa]ngulo|c[íi]rculo|circunfer[êe]ncia|semelhan[çc]a|pit[áa]goras|trap[ée]zio|pol[íi]gono)\b', re.IGNORECASE), 'H6, H7, H8'),
        ('Estatistica e Analise de Graficos', re.compile(r'\b(m[ée]dia|mediana|moda|desvio padr[ãa]o|vari[âa]ncia|gr[áa]fico|tabela|frequ[êe]ncia|distribui[çc][ãa]o|amostra)\b', re.IGNORECASE), 'H27, H28, H29'),
        ('Probabilidade', re.compile(r'\b(probabilidade|chance|aleat[óo]rio|espa[çc]o amostral|evento|sorteio|urna|dado|moeda)\b', re.IGNORECASE), 'H28, H30'),
        ('Analise Combinatoria', re.compile(r'\b(combina[çc][ãa]o|arranjo|permuta[çc][ãa]o|fatorial|possibilidades|agrupamento|princ[íi]pio fundamental da contagem)\b', re.IGNORECASE), 'H2, H3, H4'),
        ('Funcoes (Afim, Quadratica, Exponencial, Log)', re.compile(r'\b(fun[çc][ãa]o|afim|quadr[áa]tica|par[áa]bola|v[ée]rtice|m[áa]ximo|m[íi]nimo|exponencial|logaritmo|decaimento)\b', re.IGNORECASE), 'H19, H20, H21, H22'),
        ('Trigonometria', re.compile(r'\b(seno|cosseno|tangente|trigonom[ée]tric|graus|radianos|[âa]ngulo)\b', re.IGNORECASE), 'H19, H20'),
        ('Matematica Financeira', re.compile(r'\b(juros|compostos|simples|montante|capital|parcela|desconto|infla[çc][ãa]o|financiamento|presta[çc][ãa]o)\b', re.IGNORECASE), 'H4, H5'),
        ('Progressoes (PA e PG)', re.compile(r'\b(progress[ãa]o aritm[ée]tica|progress[ãa]o geom[ée]trica|termo geral|soma dos termos|sequ[êe]ncia num[ée]rica)\b', re.IGNORECASE), 'H1, H2, H19')
    ],
    'Fisica': [
        ('Eletrodinamica e Circuitos', re.compile(r'\b(circuito|resistor|resist[êe]ncia|voltagem|tens[ãa]o|corrente el[ée]trica|ddp|pot[êe]ncia el[ée]trica|kwh|quilowatt|l[âa]mpada|fus[íi]vel|disjuntor|ohm)\b', re.IGNORECASE), 'H5, H6, H7, H20'),
        ('Termologia e Calorimetria', re.compile(r'\b(calor|calorimetria|calor espec[íi]fico|calor latente|temperatura|trocas de calor|condu[çc][ãa]o|convec[çc][ãa]o|irradia[çc][ãa]o|dilata[çc][ãa]o|termodin[âa]mica|m[áa]quina t[ée]rmica|rendimento)\b', re.IGNORECASE), 'H1, H2, H5, H6'),
        ('Ondulatoria e Acustica', re.compile(r'\b(onda|frequ[êe]ncia|hertz|comprimento de onda|ac[úu]stica|som|resson[âa]ncia|doppler|difra[çc][ãa]o|interfer[êe]ncia|timbre|intensidade sonora)\b', re.IGNORECASE), 'H1, H2, H17, H18'),
        ('Cinematica', re.compile(r'\b(velocidade|acelera[çc][ãa]o|movimento uniforme|movimento uniformemente variado|trajet[óo]ria|lan[çc]amento|queda livre|alcance|tempo de percurso|km/h|m/s|velocidade m[ée]dia)\b', re.IGNORECASE), 'H17, H20'),
        ('Dinamica e Energia Mecanica', re.compile(r'\b(newton|for[çc]a|energia cin[ée]tica|energia potencial|conserva[çc][ãa]o da energia|trabalho mec[âa]nico|atrito|mola|colis[ãa]o|quantidade de movimento)\b', re.IGNORECASE), 'H5, H6, H20'),
        ('Hidrostatica', re.compile(r'\b(press[ãa]o|empuxo|densidade|stevin|pascal|arquimedes|flutua|vasos comunicantes|atmosf[ée]rica)\b', re.IGNORECASE), 'H5, H6, H20'),
        ('Otica Geometrica', re.compile(r'\b(luz|espelho|lente|refra[çc][ãa]o|reflex[ãa]o|[íi]ndice de refra[çc][ãa]o|miopia|hipermetropia|foco|[óo]ptic[ao]|[óo]tic[ao])\b', re.IGNORECASE), 'H1, H2, H17'),
        ('Eletromagnetismo', re.compile(r'\b(campo magn[ée]tico|[íi]m[ãa]|indux|faraday|espiras|transformador|for[çc]a magn[ée]tica|solenoide)\b', re.IGNORECASE), 'H5, H6, H20'),
        ('Gravitacao e Fisica Moderna', re.compile(r'\b(kepler|gravita[çc][ãa]o|[óo]rbita|sat[ée]lite|f[óo]ton|efeito fotoel[ée]trico|qu[âa]ntica|relatividade)\b', re.IGNORECASE), 'H1, H2, H17')
    ],
    'Quimica': [
        ('Fisico-Quimica e Solucoes', re.compile(r'\b(solu[çc][ãa]o|concentra[çc][ãa]o|molaridade|solubilidade|dilui[çc][ãa]o|propriedades coligativas|press[ãa]o de vapor|ebuli[çc][ãa]o|mistura)\b', re.IGNORECASE), 'H17, H18, H24'),
        ('Estequiometria e Gases', re.compile(r'\b(estequiometr|massa molar|reagente limitante|excesso|rendimento|pureza|mol\b|mols\b|volume molar|g[áa]s ideal|balanceamento)\b', re.IGNORECASE), 'H17, H24, H25'),
        ('Quimica Organica (Funcoes e Propriedades)', re.compile(r'\b(hidrocarboneto|[áa]lcool|[áa]cido carbox[íi]lico|[ée]ster|[ée]ter|amina|amida|alde[íi]do|cetona|isomeria|polaridade org[âa]nica)\b', re.IGNORECASE), 'H17, H18, H24'),
        ('Reacoes Organicas e Polimeros', re.compile(r'\b(esterifica[çc][ãa]o|saponifica[çc][ãa]o|biodiesel|transesterifica[çc][ãa]o|pol[íi]mero|pl[áa]stico|oxida[çc][ãa]o org[âa]nica)\b', re.IGNORECASE), 'H24, H25, H26'),
        ('Eletroquimica (Pilhas e Eletrolise)', re.compile(r'\b(pilha|eletr[óo]lise|[âa]nodo|c[áa]todo|oxirredu[çc][ãa]o|potencial de redu[çc][ãa]o|corros[ãa]o|prote[çc][ãa]o cat[óo]dica)\b', re.IGNORECASE), 'H17, H20, H24'),
        ('Termoquimica', re.compile(r'\b(entalpia|exot[ée]rmic|endot[ée]rmic|delta h|calor de combust[ãa]o|lei de hess|energia de liga[çc][ãa]o)\b', re.IGNORECASE), 'H5, H6, H17'),
        ('Equilibrio Quimico e pH', re.compile(r'\b(equil[íi]brio qu[íi]mico|le chatelier|ph\b|poh|acidez|hidr[óo]lise|tamp[ãa]o|kc\b|kps)\b', re.IGNORECASE), 'H17, H24, H25'),
        ('Quimica Ambiental e Tratamento', re.compile(r'\b(chuva [áa]cida|efeito estufa|tratamento de [áa]gua|flocula[çc][ãa]o|decanta[çc][ãa]o|polui[çc][ãa]o|camada de oz[ôo]nio)\b', re.IGNORECASE), 'H24, H25, H26'),
        ('Ligacoes Quimicas e Forcas Intermoleculares', re.compile(r'\b(liga[çc][ãa]o i[ôo]nica|liga[çc][ãa]o covalente|liga[çc][ãa]o met[áa]lica|liga[çc][ãa]o de hidrog[êe]nio|dipolo|geometria molecular|tabela peri[óo]dica)\b', re.IGNORECASE), 'H17, H18')
    ],
    'Biologia': [
        ('Ecologia e Biomas', re.compile(r'\b(cadeia alimentar|teia alimentar|n[íi]vel tr[óo]fico|produtor|consumidor|decompositor|rela[çc][ãa]o ecol[óo]gica|mutualismo|parasitismo|bioma|cerrado|caatinga|mata atl[âa]ntica|amaz[ôo]nia)\b', re.IGNORECASE), 'H14, H15, H16, H29, H30'),
        ('Impactos Ambientais e Conservacao', re.compile(r'\b(eutrofiza[çc][ãa]o|magnifica[çc][ãa]o tr[óo]fica|bioacumula[çc][ãa]o|desmatamento|queimada|esp[ée]cie invasora|biodiversidade|polui[çc][ãa]o das [áa]guas|conserva[çc][ãa]o)\b', re.IGNORECASE), 'H14, H15, H16, H29, H30'),
        ('Genetica e Biologia Molecular', re.compile(r'\b(gene\b|genes\b|dna\b|rna\b|alelo|heredograma|mendel|muta[çc][ãa]o|c[óo]digo gen[ée]tico|tradu[çc][ãa]o|transcri[çc][ãa]o|s[íi]ntese proteica|grupo sangu[íi]neo|cromossomo)\b', re.IGNORECASE), 'H13, H14, H15'),
        ('Fisiologia Humana', re.compile(r'\b(sistema digest[óo]rio|sistema circulat[óo]rio|sangue|cora[çc][ãa]o|pulm[ãa]o|excre[çc][ãa]o|rim|horm[ôo]nio|insulina|sistema nervoso|sistema imunol[óo]gico|anticorpo|vacina|soro|homeostase)\b', re.IGNORECASE), 'H13, H14, H15, H28'),
        ('Citologia e Metabolismo Energetico', re.compile(r'\b(c[ée]lula|membrana plasm[áa]tica|mitoc[ôo]ndria|cloroplasto|fotoss[íi]ntese|respira[çc][ãa]o celular|fermenta[çc][ãa]o|atp|osmose|transporte ativo|organela|enzima)\b', re.IGNORECASE), 'H13, H14, H15'),
        ('Microbiologia, Parasitologia e Saude', re.compile(r'\b(v[íi]rus|bact[ée]ria|protozo[áa]rio|verme|doen[çc]a|dengue|chagas|mal[áa]ria|esquistossomose|vacina[çc][ãa]o|antibi[óo]tico|profilaxia|vetor)\b', re.IGNORECASE), 'H13, H14, H28'),
        ('Evolucao', re.compile(r'\b(sele[çc][ãa]o natural|darwin|lamarck|evolu[çc][ãa]o|especia[çc][ãa]o|adapta[çc][ãa]o|f[óo]ssil|homologia|analogia)\b', re.IGNORECASE), 'H13, H14, H15'),
        ('Biotecnologia', re.compile(r'\b(transg[êe]nico|clonagem|dna recombinante|c[ée]lula-tronco|terapia g[êe]nica|crispr|pcr|eletroforese|biotecnologia)\b', re.IGNORECASE), 'H13, H14, H15, H28'),
        ('Botanica e Fisiologia Vegetal', re.compile(r'\b(planta|vegetal|bri[óo]fita|pterid[óo]fita|gimnosperma|angiosperma|xilema|floema|transpira[çc][ãa]o|est[ôo]mato|auxina|raiz|folha)\b', re.IGNORECASE), 'H14, H15')
    ]
}

def classify_question(q_num, text):
    if q_num >= 136:
        discipline = 'Matematica'
    else:
        # Check bank code first
        bank_match = re.search(r'\b[A-Z0-9_]{0,10}(BIO|FIS|QUI|MAT)[A-Z0-9_]{0,15}\b', text)
        if bank_match:
            code = bank_match.group(1).upper()
            if code == 'FIS':
                discipline = 'Fisica'
            elif code == 'QUI':
                discipline = 'Quimica'
            elif code == 'BIO':
                discipline = 'Biologia'
            elif code == 'MAT':
                discipline = 'Matematica'
            else:
                discipline = None
        else:
            discipline = None

        if not discipline:
            # Score regex patterns
            scores = {
                'Fisica': len(DISC_PATTERNS['Fisica'].findall(text)),
                'Quimica': len(DISC_PATTERNS['Quimica'].findall(text)),
                'Biologia': len(DISC_PATTERNS['Biologia'].findall(text))
            }
            discipline = max(scores, key=scores.get)
            if scores[discipline] == 0:
                # Balanced heuristic across Natureza block (15 bio, 15 fis, 15 qui)
                pos = (q_num - 91) % 45 if q_num >= 91 else (q_num - 46) % 45
                if pos < 15:
                    discipline = 'Biologia'
                elif pos < 30:
                    discipline = 'Fisica'
                else:
                    discipline = 'Quimica'

    # Determine topic within discipline
    topics = TOPIC_PATTERNS[discipline]
    best_topic = None
    best_score = -1
    best_hab = ''
    
    for top_name, pat, hab in topics:
        score = len(pat.findall(text))
        if score > best_score:
            best_score = score
            best_topic = top_name
            best_hab = hab
            
    if best_score <= 0:
        best_topic = topics[0][0]
        best_hab = topics[0][2]
        
    # Interdisciplinary check
    inter = []
    if discipline != 'Matematica':
        for od in ['Fisica', 'Quimica', 'Biologia']:
            if od != discipline:
                sc = len(DISC_PATTERNS[od].findall(text))
                if sc >= 3:
                    inter.append(f"{discipline} + {od}")
    else:
        for od in ['Fisica', 'Quimica', 'Biologia']:
            sc = len(DISC_PATTERNS[od].findall(text))
            if sc >= 2:
                inter.append(f"Matemática aplicada a {od}")
                
    return {
        'discipline': discipline,
        'topic': best_topic,
        'habilidade': best_hab,
        'interdisciplinary': inter
    }

# Execute refined extraction across all 33 editions
refined_questions = []

for ed, s in sorted(edition_source_map.items()):
    rel = s['path']
    full = os.path.join(base, rel)
    reader = pypdf.PdfReader(full)
    full_text = ""
    for p in range(len(reader.pages)):
        full_text += f"\n[P{p+1}]\n" + (reader.pages[p].extract_text() or "")
        
    if ed == '2014_SIMULADO_1':
        q_start, q_end = 46, 90
    else:
        q_start, q_end = 91, 180
        
    for q in range(q_start, q_end + 1):
        next_q = q + 1
        pattern = rf'(?:QUEST[ÃA]O|Quest[ãa]o)\s+{q}\b(.*?)(?=(?:QUEST[ÃA]O|Quest[ãa]o)\s+{next_q}\b|\Z)'
        m = re.search(pattern, full_text, re.DOTALL | re.IGNORECASE)
        q_text = ""
        if m:
            q_text = m.group(1).strip()
        else:
            p_fallback = rf'(?:QUEST[ÃA]O|Quest[ãa]o)\s+{q}\b(.*)'
            m2 = re.search(p_fallback, full_text, re.DOTALL | re.IGNORECASE)
            if m2:
                q_text = m2.group(1)[:2500].strip()
                
        cls_result = classify_question(q, q_text)
        refined_questions.append({
            'edition': ed,
            'source_file': rel,
            'question_number': q,
            'discipline': cls_result['discipline'],
            'topic': cls_result['topic'],
            'habilidade': cls_result['habilidade'],
            'interdisciplinary': cls_result['interdisciplinary'],
            'text_snippet': q_text[:160].replace('\n', ' ')
        })

print(f"Total refined questions: {len(refined_questions)}")

with open('FINAL_gamma_questions_refined.json', 'w', encoding='utf-8') as f:
    json.dump(refined_questions, f, indent=2, ensure_ascii=False)

# Analyze stats
disc_counts = Counter(q['discipline'] for q in refined_questions)
print("\n=== DISTRIBUIÇÃO REFINADA POR DISCIPLINA ===")
for disc, count in disc_counts.most_common():
    pct = (count / len(refined_questions)) * 100
    print(f"{disc:12s}: {count:5d} ({pct:6.2f}%)")

print("\n=== TOP TÓPICOS POR DISCIPLINA ===")
for disc in ['Matematica', 'Fisica', 'Quimica', 'Biologia']:
    disc_qs = [q for q in refined_questions if q['discipline'] == disc]
    top_counts = Counter(q['topic'] for q in disc_qs)
    print(f"\n--- {disc.upper()} (Total: {len(disc_qs)}) ---")
    for top, cnt in top_counts.most_common():
        pct_disc = (cnt / len(disc_qs)) * 100
        print(f"  {top:45s}: {cnt:4d} ({pct_disc:5.2f}%)")
