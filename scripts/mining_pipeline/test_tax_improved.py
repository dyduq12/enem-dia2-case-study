import re

TAXONOMY_PATTERNS = {
    # MATEMÁTICA
    'M1': ('Matemática Básica e Proporcionalidade', [
        r'\braz[aã]o\b', r'\bpropor[cç]', r'\bescala\b', r'\bregra de tr[eê]s\b', r'\bporcentagem\b',
        r'\baumento\b', r'\bdesconto\b', r'\bconvers[aã]o\b', r'\blitros?\b', r'\bm³\b', r'\bkm/h\b',
        r'\bg grandezas\b', r'\binversamente proporcional\b', r'\bdiretamente proporcional\b'
    ]),
    'M2': ('Geometria Espacial', [
        r'\bprisma\b', r'\bcilindr', r'\bcone\b', r'\besfera\b', r'\bpir[aâ]mide\b', r'\bvolume\b',
        r'\bparalelep[ií]pedo\b', r'\bpoliedro\b', r'\beuler\b', r'\bproje[cç][aã]o ortogonal\b',
        r'\bsombra\b', r'\bvista superior\b', r'\bplanifica[cç]'
    ]),
    'M3': ('Estatística Básica', [
        r'\bm[eé]dia\b', r'\bmediana\b', r'\bmoda\b', r'\bdesvio[- ]padr[aã]o\b', r'\bvari[aâ]ncia\b',
        r'\bgr[aá]fico de (barras?|setores?|linhas?|colunas?)\b', r'\bhistograma\b', r'\bdispers[aã]o\b'
    ]),
    'M4': ('Geometria Plana', [
        r'\btri[aâ]ngul', r'\bc[ií]rcul', r'\bcircunfer[eê]ncia\b', r'\b[aá]rea\b', r'\bper[ií]metro\b',
        r'\bpit[aá]goras\b', r'\btrigonometri', r'\bseno\b', r'\bcosseno\b', r'\btangente\b',
        r'\bsemelhan[cç]a de tri[aâ]ngulos?\b', r'\bteorema de tales\b', r'\btrap[eé]zio\b'
    ]),
    'M5': ('Funções e Modelagem', [
        r'\bfun[cç][aã]o (afim|linear|quadr[aá]tica|exponencial|logar[ií]tmica)\b', r'\bpar[aá]bola\b',
        r'\bv[eé]rtice\b', r'\bm[aá]ximo\b', r'\bm[ií]nimo\b', r'\btaxa de varia[cç][aã]o\b',
        r'\bcoeficiente angular\b', r'\blogaritmo\b'
    ]),
    'M6': ('Probabilidade e Combinatória', [
        r'\bprobabilidade\b', r'\bespa[cç]o amostral\b', r'\bcombina[cç][aã]o simples\b',
        r'\barranjo\b', r'\bpermuta[cç][aã]o\b', r'\banagrama\b', r'\bprinc[ií]pio fundamental da contagem\b',
        r'\bchance\b', r'\beventos independentes\b'
    ]),
    
    # BIOLOGIA
    'B1': ('Ecologia e Meio Ambiente', [
        r'\becolog', r'\becossistema\b', r'\btr[oó]fic', r'\beutrofiza[cç]', r'\bbioacumula[cç]',
        r'\bmagnifica[cç][aã]o tr[oó]fica\b', r'\bciclo do nitrog[eê]nio\b', r'\bciclo do carbono\b',
        r'\baquecimento global\b', r'\befeito estufa\b', r'\bdesmatamento\b', r'\bmutualismo\b',
        r'\bparasitismo\b', r'\bpreda[cç]', r'\bbioma\b', r'\bpolui[cç]'
    ]),
    'B2': ('Genética e Biotecnologia', [
        r'\bmendel\b', r'\balelo\b', r'\bgene\b', r'\bheredograma\b', r'\bgen[oó]tipo\b',
        r'\bfen[oó]tipo\b', r'\bsistema abo\b', r'\bfator rh\b', r'\bdna recombinante\b',
        r'\bpcr\b', r'\beletroforese\b', r'\bclon', r'\btransg[eê]nic', r'\bogm\b', r'\bcrispr\b'
    ]),
    'B3': ('Citologia e Metabolismo', [
        r'\bc[eé]lula\b', r'\borganela\b', r'\bmitoc[oô]ndria\b', r'\bcloroplasto\b',
        r'\bfotoss[ií]ntese\b', r'\brespira[cç][aã]o celular\b', r'\bglic[oó]lise\b', r'\bkrebs\b',
        r'\bfermenta[cç]', r'\bosmose\b', r'\bmembrana plasm[aá]tica\b', r'\btransporte ativo\b', r'\batp\b'
    ]),
    'B4': ('Fisiologia e Imunologia', [
        r'\bvacina\b', r'\bsoro\b', r'\bant[ií]geno\b', r'\banticorpo\b', r'\bimun',
        r'\blinf[oó]cito\b', r'\baedes\b', r'\bdengue\b', r'\bzika\b', r'\bchikungunya\b',
        r'\bchagas\b', r'\bmal[aá]ria\b', r'\bleishmaniose\b', r'\bbact[eé]ria\b', r'\bv[ií]rus\b', r'\bhorm[oô]ni'
    ]),
    
    # FÍSICA
    'F1': ('Eletrodinâmica', [
        r'\bcircuito\b', r'\bresistor', r'\bresist[eê]ncia\b', r'\bcorrente el[eé]trica\b',
        r'\bddp\b', r'\btens[aã]o el[eé]trica\b', r'\bvoltagem\b', r'\bpot[eê]ncia el[eé]trica\b',
        r'\bkwh\b', r'\befeito joule\b', r'\bfus[ií]vel\b', r'\bdisjuntor\b', r'\bamper[ií]metro\b',
        r'\bvolt[ií]metro\b', r'\bparalelo\b', r'\bohm\b'
    ]),
    'F2': ('Mecânica e Hidrostática', [
        r'\bcin[eé]tica\b', r'\bpotencial gravitacional\b', r'\bconserva[cç][aã]o da energia\b',
        r'\btrabalho\b', r'\bnewton\b', r'\batrito\b', r'\bplano inclinado\b', r'\bcinem[aá]tica\b',
        r'\bacelera[cç][aã]o\b', r'\bmru\b', r'\bmruv\b', r'\bpress[aã]o hidrost[aá]tica\b',
        r'\bempuxo\b', r'\barquimedes\b', r'\bpascal\b'
    ]),
    'F3': ('Ondulatória e Acústica', [
        r'\bonda\b', r'\bondulat[oó]ria\b', r'\bcomprimento de onda\b', r'\bfrequ[eê]ncia\b',
        r'\brefra[cç][aã]o\b', r'\bdifra[cç][aã]o\b', r'\binterfer[eê]ncia\b', r'\bresson[aâ]ncia\b',
        r'\bdoppler\b', r'\bac[uú]stica\b', r'\btimbre\b', r'\bsom\b', r'\bsonor'
    ]),
    'F4': ('Termologia e Termodinâmica', [
        r'\bcalorimetria\b', r'\bcalor sens[ií]vel\b', r'\bcalor latente\b', r'\bcondu[cç][aã]o\b',
        r'\bconvec[cç][aã]o\b', r'\birradia[cç][aã]o\b', r'\btermodin[aâ]mica\b',
        r'\bprimeira lei da termodin[aâ]mica\b', r'\bm[aá]quina t[eé]rmica\b', r'\bcarnot\b', r'\bdilata[cç]'
    ]),
    
    # QUÍMICA
    'Q1': ('Físico-Química', [
        r'\bpilha\b', r'\b[aâ]nodo\b', r'\bc[aá]todo\b', r'\boxida[cç]', r'\bredu[cç]',
        r'\bpotencial de redu[cç][aã]o\b', r'\beletr[oó]lise\b', r'\bcorros[aã]o\b', r'\bmetal de sacrif[ií]cio\b',
        r'\btermoqu[ií]mica\b', r'\bentalpia\b', r'\bdelta h\b', r'\blei de hess\b', r'\bcin[eé]tica\b',
        r'\bcatalisador\b', r'\bequil[ií]brio qu[ií]mico\b', r'\ble chatelier\b', r'\bph\b',
        r'\bsolu[cç][aã]o\b', r'\bconcentra[cç][aã]o\b', r'\bmolar\b'
    ]),
    'Q2': ('Química Geral e Estequiometria', [
        r'\bestequiometria\b', r'\bmol\b', r'\bmassa molar\b', r'\bpureza\b', r'\brendimento\b',
        r'\breagente limitante\b', r'\bliga[cç][aã]o qu[ií]mica\b', r'\bliga[cç][oõ]es de hidrog[eê]nio\b',
        r'\bdipolo\b', r'\blondon\b', r'\bponto de ebuli[cç][aã]o\b', r'\bsepara[cç][aã]o de misturas\b',
        r'\bdestila[cç]', r'\bfiltra[cç]', r'\bdecanta[cç]'
    ]),
    'Q3': ('Química Orgânica', [
        r'\bqu[ií]mica org[aâ]nica\b', r'\bhidrocarboneto\b', r'\b[aá]lcool\b', r'\bfenol\b',
        r'\balde[ií]do\b', r'\bcetona\b', r'\b[aá]cido carbox[ií]lico\b', r'\b[eé]ster\b',
        r'\bamina\b', r'\bamida\b', r'\bisomer', r'\bquiral\b', r'\besterifica[cç]',
        r'\bbiodiesel\b', r'\bpol[ií]mero\b', r'\bpet\b', r'\bpvc\b'
    ]),
    'Q4': ('Química Ambiental', [
        r'\bqu[ií]mica ambiental\b', r'\bchuva [aá]cida\b', r'\befeito estufa\b', r'\boz[oô]nio\b',
        r'\bcfc\b', r'\btratamento de [aá]gua\b', r'\bflocula[cç]', r'\bclora[cç]', r'\bpoluente\b'
    ])
}

COMPILED_PATTERNS = {
    code: (name, [re.compile(p, re.IGNORECASE) for p in pats])
    for code, (name, pats) in TAXONOMY_PATTERNS.items()
}

def classify_text(text, discipline_hint=None):
    scores = {}
    for code, (topic_name, regexes) in COMPILED_PATTERNS.items():
        # Discipline filter if hinted
        if discipline_hint == 'MAT' and not code.startswith('M'):
            continue
        if discipline_hint == 'CN' and code.startswith('M'):
            continue
        
        matches = sum(1 for rx in regexes if rx.search(text))
        if matches > 0:
            scores[code] = (matches, topic_name)
    best = sorted(scores.items(), key=lambda x: -x[1][0])
    return best

samples = [
    ('Poliedro Q91', 'N2(g) + 3 H2(g) <=> 2 NH3(g) ∆H = -92,2 kJ Considerando o equilíbrio químico estabelecido, a síntese da amônia é favorecida...'),
    ('Poliedro Q92', 'O sinal Wi-Fi é uma onda eletromagnética que está sujeita a interferências e ao enfraquecimento de sinal ao longo do caminho...'),
    ('Bernoulli Q91', 'A ovelha Dolly foi o primeiro mamífero clonado por transferência nuclear de células somáticas bellinda scottish blackface'),
    ('Bernoulli Q92', 'Considere a velocidade do som como igual a 340 m/s. Qual o regime de voo de uma aeronave que viaja à velocidade de 918 km/h? Número de Mach...'),
]

for name, text in samples:
    res = classify_text(text)
    best_code = res[0][0] if res else 'NONE'
    best_name = res[0][1][1] if res else '-'
    print(f'{name} -> Best: {best_code} ({best_name}) | Top: {res[:2]}')
