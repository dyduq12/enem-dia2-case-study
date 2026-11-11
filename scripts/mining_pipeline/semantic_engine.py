import re

def compile_patterns(topic_list):
    compiled = []
    for topic_name, patterns, skill in topic_list:
        regexes = [re.compile(r'\b' + pat + r'\b', re.IGNORECASE) for pat in patterns]
        compiled.append((topic_name, regexes, skill))
    return compiled

RAW_BIOLOGY = [
    ("Ecologia e Impactos Ambientais", [
        r"ecologia", r"cadeias? alimentares?", r"teias? alimentares?", r"tr[óo]fic[oa]s?", r"biomassa", 
        r"biomagnifica[çc][ãa]o", r"bioacumula[çc][ãa]o", r"nicho[s]? ecol[óo]gico[s]?", r"habitat[s]?", 
        r"sucess[ãa]o ecol[óo]gica", r"ciclo[s]? biogeoqu[íi]mico[s]?", r"ciclo do nitrog[êe]nio", 
        r"ciclo do carbono", r"eutrofiza[çc][ãa]o", r"desmatamento", r"esp[ée]cie[s]? invasora[s]?", 
        r"bioma[s]?", r"cerrado", r"mata atl[âa]ntica", r"caatinga", r"amaz[ôo]nia", r"poliniza[çc][ãa]o", 
        r"mutualismo", r"parasitismo", r"comensalismo", r"preda[çc][ãa]o", r"competi[çc][ãa]o interespec[íi]fica",
        r"sustentabilidade", r"reciclagem", r"pegada ecol[óo]gica", r"aquecimento global", r"biodiversidade"
    ], "H10"),
    ("Genética Molecular e Biotecnologia", [
        r"gen[ée]tica", r"dna", r"rna", r"genes?", r"alelos?", r"cromossomos?", r"muta[çc][ãa]o", r"muta[çc][õo]es", 
        r"transg[êe]nic[oa]s?", r"crispr", r"clonagem", r"c[óo]digo gen[ée]tico", r"tradu[çc][ãa]o g[êe]nica", 
        r"transcri[çc][ãa]o", r"mendel", r"mendeliana", r"gen[óo]tipo", r"fen[óo]tipo", r"recombina[çc][ãa]o", 
        r"plasm[íi]deo[s]?", r"eletroforese", r"pcr", r"epigen[ée]tica", r"hereditariedade", r"engenharia gen[ée]tica"
    ], "H14"),
    ("Citologia e Bioquímica Celular", [
        r"c[ée]lulas?", r"celulares?", r"membrana plasm[áa]tica", r"organelas?", r"mitoc[ôo]ndrias?", 
        r"ribossomos?", r"complexo de golgi", r"ret[íi]culo endoplasm[áa]tico", r"cloroplastos?", 
        r"fotoss[íi]ntese", r"respira[çc][ãa]o celular", r"fermenta[çc][ãa]o", r"glic[óo]lise", r"atp", 
        r"enzimas?", r"prote[íi]nas?", r"lip[íi]dios?", r"fosfolip[íi]dios?", r"carboidratos?", r"glicose", 
        r"meiose", r"mitose", r"osmose celular", r"desnatura[çc][ãa]o proteica"
    ], "H15"),
    ("Fisiologia Humana e Animal", [
        r"fisiologia", r"sistema circulat[óo]rio", r"cora[çc][ãa]o", r"vasos? sangu[íi]neos?", r"press[ãa]o arterial", 
        r"sistema digest[óo]rio", r"est[ôo]mago", r"intestino", r"sistema respirat[óo]rio", r"pulm[ãa]o", 
        r"alv[ée]olos?", r"sistema excretor", r"rins?", r"n[ée]frons?", r"urina", r"sistema nervoso", 
        r"neur[ôo]nios?", r"sinapses?", r"neurotransmissores?", r"sistema end[óo]crino", r"horm[ôo]nios?", 
        r"insulina", r"glucagon", r"tireoide", r"sistema imune", r"imunol[óo]gico", r"anticorpos?", 
        r"ant[íi]genos?", r"vacinas?", r"vacina[çc][ãa]o", r"soro terap[êe]utico", r"linf[óo]citos?", r"hemoglobina"
    ], "H16"),
    ("Microbiologia, Parasitologia e Saúde Pública", [
        r"v[íi]rus", r"v[íi]rion", r"bact[ée]rias?", r"protozo[áa]rios?", r"fungos?", r"helmintos?", 
        r"doen[çc]as?", r"infec[çc][ãa]o", r"dengue", r"aedes", r"mal[áa]ria", r"chagas", r"leishmaniose", 
        r"esquistossomose", r"ten[íi]ase", r"tuberculose", r"c[óo]lera", r"antibi[óo]ticos?", r"sorologia", 
        r"pandemia", r"vetores? de doen[çc]as?", r"rotav[íi]rus", r"protozoose"
    ], "H11"),
    ("Botânica e Fisiologia Vegetal", [
        r"bot[âa]nica", r"vegetais?", r"plantas?", r"xilema", r"floema", r"est[ôo]matos?", 
        r"transpira[çc][ãa]o vegetal", r"auxinas?", r"fitorm[ôo]nios?", r"angiospermas?", 
        r"gimnospermas?", r"pterid[óo]fitas?", r"bri[óo]fitas?", r"caule", r"folhas?", r"sementes?", 
        r"ra[íi]zes?", r"frutos?"
    ], "H13"),
    ("Evolução e Seleção Natural", [
        r"evolu[çc][ãa]o", r"darwin", r"sele[çc][ãa]o natural", r"adapta[çc][ãa]o evolutiva", r"ancestral comum", 
        r"especia[çc][ãa]o", r"deriva gen[ée]tica", r"isolamento reprodutivo", r"homologia", r"analogia", 
        r"cladogramas?", r"f[óo]sseis"
    ], "H12")
]

RAW_CHEMISTRY = [
    ("Estequiometria e Leis Ponderais", [
        r"estequiometria", r"estequiom[ée]tric[oa]s?", r"massa molar", r"mols?", r"rendimento da rea[çc][ãa]o", 
        r"pureza", r"reagente limitante", r"reagente em excesso", r"volume molar", r"constante de avogadro", 
        r"leis ponderais", r"propor[çc][ãa]o estequiom[ée]trica", r"g\/mol"
    ], "H17"),
    ("Físico-Química: Termoquímica", [
        r"termoqu[íi]mica", r"entalpia", r"delta h", r"\b\u0394h\b", r"endot[ée]rmic[oa]", r"exot[ée]rmic[oa]", 
        r"calor de combust[ãa]o", r"lei de hess", r"energia de liga[çc][ãa]o", r"calor de rea[çc][ãa]o", 
        r"kj\/mol", r"kcal\/mol"
    ], "H18"),
    ("Físico-Química: Cinética e Equilíbrio Químico", [
        r"cin[ée]tica qu[íi]mica", r"velocidade da rea[çc][ãa]o", r"energia de ativa[çc][ãa]o", r"catalisadores?", 
        r"equil[íi]brio qu[íi]mico", r"le chatelier", r"\bkc\b", r"\bkp\b", r"deslocamento do equil[íi]brio", 
        r"\bph\b", r"\bpoh\b", r"constante de ioniza[çc][ãa]o", r"\bka\b", r"\bkb\b", r"hidr[óo]lise salina", 
        r"solu[çc][ãa]o tamp[ãa]o"
    ], "H19"),
    ("Físico-Química: Eletroquímica (Pilhas e Eletrólise)", [
        r"eletroqu[íi]mica", r"pilhas?", r"baterias?", r"eletr[óo]lise", r"[âa]nodo", r"c[áa]todo", 
        r"potencial de redu[çc][ãa]o", r"diferen[çc]a de potencial", r"\bddp\b", r"oxida[çc][ãa]o", 
        r"redu[çc][ãa]o", r"semi-?rea[çc][ãa]o", r"n[úu]mero de oxida[çc][ãa]o", r"\bnox\b", 
        r"corros[ãa]o", r"prote[çc][ãa]o cat[óo]dica", r"galvanoplastia"
    ], "H20"),
    ("Físico-Química: Soluções e Concentrações", [
        r"solu[çc][ãa]o", r"solu[çc][õo]es", r"solutos?", r"solventes?", r"concentra[çc][ãa]o comum", 
        r"concentra[çc][ãa]o molar", r"molaridade", r"dilui[çc][ãa]o", r"titula[çc][ãa]o", 
        r"solubilidade", r"coeficiente de solubilidade", r"curva de solubilidade", r"coloide[s]?", 
        r"dispers[ãa]o", r"g\/l", r"mol\/l"
    ], "H21"),
    ("Química Orgânica: Estrutura, Funções e Isomeria", [
        r"qu[íi]mica org[âa]nica", r"hidrocarbonetos?", r"[áa]lcoois?", r"alde[íi]dos?", r"cetonas?", 
        r"[áa]cido[s]? carbox[íi]lico[s]?", r"[ée]steres?", r"[ée]teres?", r"aminas?", r"amidas?", 
        r"fen[óo]is?", r"haletos? org[âa]nicos?", r"isomeria", r"is[ôo]meros?", r"enanti[ôo]meros?", 
        r"quiral", r"quiralidade", r"cadeia carb[ôo]nica", r"polaridade org[âa]nica"
    ], "H24"),
    ("Química Orgânica: Reações Orgânicas e Polímeros", [
        r"rea[çc][ãa]o org[âa]nica", r"rea[çc][õo]es org[âa]nicas", r"esterifica[çc][ãa]o", r"saponifica[çc][ãa]o", 
        r"pol[íi]meros?", r"polimeriza[çc][ãa]o", r"pl[áa]sticos?", r"biodegrad[áa]vel", r"combust[ãa]o org[âa]nica", 
        r"substitui[çc][ãa]o eletrof[íi]lica", r"adi[çc][ãa]o", r"oxida[çc][ãa]o org[âa]nica"
    ], "H25"),
    ("Química Geral, Modelos Atômicos e Ligações", [
        r"tabela peri[óo]dica", r"liga[çc][ãa]o i[ôo]nica", r"liga[çc][ãa]o covalente", r"liga[çc][ãa]o met[áa]lica", 
        r"geometria molecular", r"for[çc]as intermoleculares", r"liga[çc][ãa]o de hidrog[êe]nio", 
        r"separa[çc][ãa]o de misturas", r"destila[çc][ãa]o", r"filtra[çc][ãa]o", r"decanta[çc][ãa]o", 
        r"fun[çc][õo]es inorg[âa]nicas", r"[óo]xidos?", r"[áa]cidos? inorg[âa]nicos?", r"bases? de arrhenius", 
        r"modelos? at[ôo]micos?", r"dalton", r"thomson", r"rutherford", r"bohr", r"decaimento radioativo", 
        r"radioatividade", r"part[íi]culas? alfa", r"part[íi]culas? beta"
    ], "H22"),
    ("Química Ambiental e Sustentabilidade", [
        r"qu[íi]mica ambiental", r"chuva [áa]cida", r"efeito estufa", r"camada de oz[ôo]nio", r"biodiesel", 
        r"biog[áa]s", r"combust[íi]veis? f[óo]sseis?", r"metais pesados", r"tratamento de [áa]gua", 
        r"tratamento de esgoto", r"polui[çc][ãa]o ambiental", r"mon[óo]xido de carbono"
    ], "H23")
]

RAW_PHYSICS = [
    ("Eletrodinâmica e Circuitos Elétricos", [
        r"circuitos? el[ée]tricos?", r"corrente el[ée]trica", r"resistores?", r"resist[êe]ncia el[ée]trica", 
        r"tens[ãa]o el[ée]trica", r"voltagem", r"pot[êe]ncia el[ée]trica", r"leis? de ohm", 
        r"associa[çc][ãa]o de resistores?", r"resistores? em s[ée]rie", r"resistores? em paralelo", 
        r"disjuntores?", r"fus[íi]veis?", r"consumo de energia", r"\bkwh\b", r"choque el[ée]trico", 
        r"aterramento", r"fio terra"
    ], "H1"),
    ("Eletrostática e Magnetismo", [
        r"eletrost[áa]tica", r"cargas? el[ée]tricas?", r"campo el[ée]trico", r"for[çc]a el[ée]trica", 
        r"lei de coulomb", r"potencial el[ée]trico", r"capacitores?", r"campo magn[ée]tico", 
        r"for[çc]a magn[ée]tica", r"indu[çc][ãa]o eletromagn[ée]tica", r"lei de faraday", 
        r"transformadores?", r"[íi]m[ãa]s?", r"fluxo magn[ée]tico"
    ], "H2"),
    ("Termologia, Calorimetria e Termodinâmica", [
        r"termologia", r"calorimetria", r"calor sens[íi]vel", r"calor latente", r"capacidade t[ée]rmica", 
        r"trocas? de calor", r"condu[çc][ãa]o t[ée]rmica", r"convec[çc][ãa]o", r"irradia[çc][ãa]o", 
        r"radia[çc][ãa]o t[ée]rmica", r"dilata[çc][ãa]o t[ée]rmica", r"leis? da termodin[âa]mica", 
        r"m[áa]quinas? t[ée]rmicas?", r"ciclo de carnot", r"rendimento t[ée]rmico", r"g[áa]s ideal", 
        r"temperatura", r"escalas? termom[ée]tricas?", r"term[ôo]metros?", r"rankine", r"kelvin", r"celsius"
    ], "H3"),
    ("Ondulatória e Acústica", [
        r"ondulat[óo]ria", r"ondas?", r"comprimento de onda", r"frequ[êe]ncia da onda", r"espectro eletromagn[ée]tico", 
        r"refra[çc][ãa]o de onda", r"difra[çc][ãa]o", r"interfer[êe]ncia", r"resson[âa]ncia", 
        r"efeito doppler", r"polariza[çc][ãa]o", r"ac[úu]stica", r"som", r"intensidade sonora", 
        r"decib[ée]is", r"altura do som", r"timbre", r"tubos? sonoros?"
    ], "H4"),
    ("Óptica Geométrica", [
        r"[óo]ptica", r"espelhos?", r"espelho plano", r"espelho c[ôo]ncavo", r"espelho convexo", 
        r"lentes?", r"lente convergente", r"lente divergente", r"refra[çc][ãa]o da luz", 
        r"lei de snell", r"[íi]ndice de refra[çc][ãa]o", r"reflex[ãa]o total", r"fibra [óo]ptica", 
        r"miopia", r"hipermetropia", r"olho humano"
    ], "H5"),
    ("Mecânica: Cinemática", [
        r"cinem[áa]tica", r"velocidade m[ée]dia", r"acelera[çc][ãa]o", r"movimento uniforme", 
        r"movimento uniformemente variado", r"\bmuv\b", r"lan[çc]amento vertical", r"queda livre", 
        r"lan[çc]amento obl[íi]quo", r"movimento circular", r"trajet[óo]ria", r"dist[âa]ncia de frenagem"
    ], "H6"),
    ("Mecânica: Dinâmica, Leis de Newton e Gravitação", [
        r"din[âa]mica", r"leis? de newton", r"in[ée]rcia", r"a[çc][ãa]o e rea[çc][ãa]o", 
        r"for[çc]a de atrito", r"atrito est[áa]tico", r"atrito cin[ée]tico", r"plano inclinado", 
        r"for[çc]a centr[íi]peta", r"gravita[çc][ãa]o universal", r"leis? de kepler"
    ], "H7"),
    ("Mecânica: Trabalho, Energia e Quantidade de Movimento", [
        r"energia mec[âa]nica", r"energia cin[ée]tica", r"energia potencial", r"conserva[çc][ãa]o da energia", 
        r"trabalho de uma for[çc]a", r"pot[êe]ncia mec[âa]nica", r"rendimento mec[âa]nico", 
        r"impulso", r"quantidade de movimento", r"colis[ãa]o"
    ], "H8"),
    ("Hidrostática e Estática", [
        r"hidrost[áa]tica", r"press[ãa]o hidrost[áa]tica", r"densidade", r"massa espec[íi]fica", 
        r"empuxo", r"princ[íi]pio de arquimedes", r"princ[íi]pio de pascal", r"vasos comunicantes", 
        r"est[áa]tica", r"torque", r"momento de uma for[çc]a", r"alavancas?"
    ], "H9")
]

RAW_MATH = [
    ("Geometria Espacial (Sólidos, Volumes e Áreas)", [
        r"geometria espacial", r"volumes?", r"cilindros?", r"cones?", r"esferas?", r"cubos?", 
        r"paralelep[íi]pedos?", r"prismas?", r"pir[âa]mides?", r"tronco de cone", r"capacidade em litros", 
        r"[áa]rea total do s[óo]lido", r"[áa]rea superficial", r"s[óo]lidos? geom[ée]tricos?", r"litros?", 
        r"cm\u00b3", r"m\u00b3", r"capacidade m[áa]xima"
    ], "H8"),
    ("Geometria Plana (Áreas, Perímetros e Trigonometria Básica)", [
        r"geometria plana", r"[áa]reas?", r"per[íi]metros?", r"tri[âa]ngulos?", r"ret[âa]ngulos?", 
        r"c[íi]rculos?", r"circunfer[êe]ncias?", r"trap[ée]zios?", r"losangos?", r"pol[íi]gonos?", 
        r"semelhan[çc]a de tri[âa]ngulos", r"teorema de pit[áa]goras", r"raio", r"di[âa]metro", 
        r"setor circular", r"cm\u00b2", r"m\u00b2", r"[âa]ngulos?", r"graus"
    ], "H7"),
    ("Estatística Descritiva (Média, Mediana, Moda e Gráficos)", [
        r"estat[íi]stica", r"m[ée]dia aritm[ée]tica", r"m[ée]dia ponderada", r"medianas?", r"modas?", 
        r"desvio padr[ãa]o", r"vari[âa]ncia", r"frequ[êe]ncia", r"tabela de frequ[êe]ncia", 
        r"gr[áa]fico de barras", r"gr[áa]fico de setores", r"histogramas?", r"amostragem", 
        r"tabela", r"valores? médios?", r"distribui[çc][ãa]o"
    ], "H27"),
    ("Probabilidade e Espaço Amostral", [
        r"probabilidade", r"chances?", r"espa[çc]o amostral", r"eventos? favor[áa]veis?", 
        r"probabilidade condicional", r"eventos? independentes?", r"evento complementar", 
        r"urnas?", r"sorteio", r"sorteada[s]?", r"aleatoriamente", r"dados? de seis faces", 
        r"probabilidade de que"
    ], "H28"),
    ("Análise Combinatória (Arranjos, Combinações e Permutações)", [
        r"an[áa]lise combinat[óo]ria", r"combinat[óo]ria", r"combina[çc][ãa]o simples", 
        r"arranjos?", r"permuta[çc][ãa]o", r"fatorial", r"princ[íi]pio fundamental da contagem", 
        r"\bpfc\b", r"possibilidades? de escolha", r"anagramas?", r"quantos modos", r"quantas maneiras", 
        r"quantas formas", r"senhas?", r"agrupamentos?"
    ], "H29"),
    ("Funções Algébricas e Análise de Gráficos (1º e 2º Graus)", [
        r"fun[çc][ãa]o afim", r"fun[çc][ãa]o do 1[ºo] grau", r"coeficiente angular", 
        r"fun[çc][ãa]o quadr[áa]tica", r"fun[çc][ãa]o do 2[ºo] grau", r"par[áa]bola", 
        r"v[ée]rtice da par[áa]bola", r"ponto m[áa]ximo", r"ponto m[íi]nimo", r"zeros da fun[çc][ãa]o", 
        r"gr[áa]fico da reta", r"f\(x\)", r"y\s*=\s*a?x", r"eixo das abscissas", r"eixo das ordenadas"
    ], "H21"),
    ("Funções Exponenciais e Logaritmos", [
        r"fun[çc][ãa]o exponencial", r"crescimento exponencial", r"decaimento exponencial", 
        r"logaritmos?", r"fun[çc][ãa]o logar[íi]tmica", r"escala logar[íi]tmica", r"escala richter", 
        r"\blog\b"
    ], "H22"),
    ("Razão, Proporção, Regra de Três e Escala", [
        r"raz[ãa]o", r"propor[çc][ãa]o", r"diretamente proporcional", r"inversamente proporcional", 
        r"regra de tr[êe]s", r"escalas? cartogr[áa]ficas?", r"mapas?", r"maquetes?", 
        r"divis[ãa]o proporcional", r"proporcionalidade", r"escala 1:"
    ], "H19"),
    ("Aritmética, Porcentagem e Matemática Financeira", [
        r"porcentagem", r"percentual", r"aumento percentual", r"desconto percentual", 
        r"lucro", r"preju[íi]zo", r"juros simples", r"juros compostos", r"montante", 
        r"matem[áa]tica financeira", r"opera[çc][õo]es b[áa]sicas", r"fra[çc][õo]es", 
        r"infla[çc][ãa]o", r"reais", r"r\$", r"pre[çc]o de venda", r"custo total"
    ], "H20"),
    ("Trigonometria e Funções Trigonométricas", [
        r"trigonometria", r"seno", r"cosseno", r"tangente", r"c[íi]rculo trigonom[ée]trico", 
        r"lei dos senos", r"lei dos cossenos", r"fun[çc][ãa]o trigonom[ée]trica"
    ], "H9"),
    ("Progressões Aritméticas e Geométricas (PA e PG)", [
        r"progress[ãa]o aritm[ée]tica", r"\bpa\b", r"progress[ãa]o geom[ée]trica", r"\bpg\b", 
        r"termo geral da pa", r"termo geral da pg", r"soma dos termos da pa", r"sequ[êe]ncia num[ée]rica"
    ], "H25")
]

BIOLOGY_COMPILED = compile_patterns(RAW_BIOLOGY)
CHEMISTRY_COMPILED = compile_patterns(RAW_CHEMISTRY)
PHYSICS_COMPILED = compile_patterns(RAW_PHYSICS)
MATH_COMPILED = compile_patterns(RAW_MATH)

def classify_question(q_num, text):
    t_clean = text.lower()
    
    # 1. Determine Discipline
    if q_num >= 136:
        discipline = "Matemática"
    else:
        # Score each compiled discipline
        bio_matches = sum(sum(1 for r in regs if r.search(t_clean)) for _, regs, _ in BIOLOGY_COMPILED)
        chem_matches = sum(sum(1 for r in regs if r.search(t_clean)) for _, regs, _ in CHEMISTRY_COMPILED)
        phys_matches = sum(sum(1 for r in regs if r.search(t_clean)) for _, regs, _ in PHYSICS_COMPILED)
        
        # Physics-specific units/terms boost
        if re.search(r'\b(volts?|amperes?|ohms?|\u03a9|joules?|watts?|newtons?|m\/s|km\/h|m\/s\u00b2|hertz|hz)\b', t_clean, re.I):
            phys_matches += 4
        # Chemistry-specific units/terms boost
        if re.search(r'\b(mol|g\/mol|mol\/l|soluto|solvente|entalpia|qu[íi]mica|rea[çc][ãa]o qu[íi]mica|[áa]cido|base|tabela peri[óo]dica)\b', t_clean, re.I):
            chem_matches += 4
        # Biology-specific terms boost
        if re.search(r'\b(c[ée]lulas?|organismo|esp[ée]cie|dna|rna|ecossistema|prote[íi]na|vacina|v[íi]rus|bact[ée]ria|planta)\b', t_clean, re.I):
            bio_matches += 4
            
        scores = [("Física", phys_matches), ("Química", chem_matches), ("Biologia", bio_matches)]
        scores.sort(key=lambda x: x[1], reverse=True)
        discipline = scores[0][0] if scores[0][1] > 0 else "Biologia"

    # 2. Determine Real Topic and Skill
    topic = "Conceitos Fundamentais"
    skill = "H1"
    
    if discipline == "Matemática":
        best_topic = None
        best_count = -1
        best_skill = "H19"
        for t_name, regs, sk in MATH_COMPILED:
            count = sum(1 for r in regs if r.search(t_clean))
            if count > best_count:
                best_count = count
                best_topic = t_name
                best_skill = sk
        topic = best_topic if (best_topic and best_count > 0) else "Aritmética, Porcentagem e Matemática Financeira"
        skill = best_skill
        
    elif discipline == "Biologia":
        best_topic = None
        best_count = -1
        best_skill = "H10"
        for t_name, regs, sk in BIOLOGY_COMPILED:
            count = sum(1 for r in regs if r.search(t_clean))
            if count > best_count:
                best_count = count
                best_topic = t_name
                best_skill = sk
        topic = best_topic if (best_topic and best_count > 0) else "Ecologia e Impactos Ambientais"
        skill = best_skill
        
    elif discipline == "Química":
        best_topic = None
        best_count = -1
        best_skill = "H17"
        for t_name, regs, sk in CHEMISTRY_COMPILED:
            count = sum(1 for r in regs if r.search(t_clean))
            if count > best_count:
                best_count = count
                best_topic = t_name
                best_skill = sk
        topic = best_topic if (best_topic and best_count > 0) else "Físico-Química: Soluções e Concentrações"
        skill = best_skill
        
    elif discipline == "Física":
        best_topic = None
        best_count = -1
        best_skill = "H1"
        for t_name, regs, sk in PHYSICS_COMPILED:
            count = sum(1 for r in regs if r.search(t_clean))
            if count > best_count:
                best_count = count
                best_topic = t_name
                best_skill = sk
        topic = best_topic if (best_topic and best_count > 0) else "Eletrodinâmica e Circuitos Elétricos"
        skill = best_skill

    # 3. Interdisciplinary Detection
    interdisc = []
    if discipline == "Biologia":
        if re.search(r'\b(rea[çc][ãa]o|composto|ph|[áa]cido|oxida[çc][ãa]o|subst[âa]ncia|solu[çc][ãa]o|enzim[áa]tic[oa])\b', t_clean, re.I):
            interdisc.append("Bioquímica / Conexão com Química")
        if re.search(r'\b(energia|temperatura|calor|radia[çc][ãa]o|luz|press[ãa]o|press[ãa]o osm[óo]tica)\b', t_clean, re.I):
            interdisc.append("Biofísica / Conexão com Física")
    elif discipline == "Química":
        if re.search(r'\b(organismo|c[ée]lulas?|meio ambiente|solo|[áa]gua|biomassa|biol[óo]gico)\b', t_clean, re.I):
            interdisc.append("Química Ambiental / Bioquímica")
        if re.search(r'\b(energia|calor|trabalho|eletricidade|corrente|potencial|volts?|temperatura)\b', t_clean, re.I):
            interdisc.append("Físico-Química / Conexão com Física")
    elif discipline == "Física":
        if re.search(r'\b(olho|corpo humano|pele|c[ée]lula|audi[çc][ãa]o|ouvido|biol[óo]gico)\b', t_clean, re.I):
            interdisc.append("Física Biológica / Fisiologia da Visão e Audição")
        if re.search(r'\b(g[áa]s|combust[ãa]o|rea[çc][ãa]o|termoqu[íi]mica|entalpia)\b', t_clean, re.I):
            interdisc.append("Físico-Química e Termodinâmica")
    elif discipline == "Matemática":
        if re.search(r'\b(popula[çc][ãa]o|v[íi]rus|bact[ée]ria|meio ambiente|ecossistema)\b', t_clean, re.I):
            interdisc.append("Modelagem Matemática em Dinâmica Populacional / Biologia")
        if re.search(r'\b(velocidade|acelera[çc][ãa]o|temperatura|tanque|combust[íi]vel|press[ãa]o|for[çc]a)\b', t_clean, re.I):
            interdisc.append("Matemática Aplicada à Física e Engenharia")

    return {
        "discipline": discipline,
        "topic": topic,
        "skill": skill,
        "interdisciplinary": interdisc
    }
