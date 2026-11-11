import re

TAXONOMY = {
    'M1': ('Matemática Básica e Proporcionalidade', ['razão', 'razao', 'proporç', 'proporc', 'escala', 'regra de tr', 'porcentagem', 'aumento', 'desconto', 'conversão', 'litro', 'm³', 'km/h', 'rendimento', 'consumo']),
    'M2': ('Geometria Espacial', ['prisma', 'cilindr', 'cone', 'esfer', 'pirâmide', 'piramide', 'volume', 'paralelepípedo', 'poliedro', 'euler', 'projeção ortogonal', 'sombra', 'vista superior', 'planificaç']),
    'M3': ('Estatística Básica', ['média', 'media', 'mediana', 'moda', 'desvio padrão', 'desvio padrao', 'variância', 'gráfico de', 'tabela', 'dispersão', 'frequência']),
    'M4': ('Geometria Plana', ['triângul', 'triangul', 'círcul', 'circul', 'área', 'perímetro', 'pitágoras', 'pitagoras', 'seno', 'cosseno', 'tangente', 'semelhança', 'tales', 'trapézio']),
    'M5': ('Funções e Modelagem', ['função', 'funcao', 'afim', 'quadrática', 'quadratica', 'parábola', 'vértice', 'vertice', 'máximo', 'mínimo', 'exponencial', 'logaritm']),
    'M6': ('Probabilidade e Combinatória', ['probabilidade', 'espaço amostral', 'combinat', 'combinaç', 'arranjo', 'permutaç', 'anagrama', 'contagem', 'chance']),
    
    'B1': ('Ecologia e Meio Ambiente', ['ecolog', 'ecossistema', 'trófic', 'trofic', 'eutrofizaç', 'bioacumulaç', 'magnificaç', 'ciclo do nitrog', 'ciclo do carbon', 'aquecimento global', 'efeito estufa', 'desmatamento', 'mutualismo', 'parasitismo', 'predaç', 'bioma', 'poluiç']),
    'B2': ('Genética e Biotecnologia', ['mendel', 'alelo', 'gene', 'heredograma', 'genótipo', 'fenótipo', 'sistema abo', 'fator rh', 'dna recombinante', 'pcr', 'eletroforese', 'clonagem', 'transgênic', 'ogm', 'crispr']),
    'B3': ('Citologia e Metabolismo', ['célula', 'celula', 'organela', 'mitocôndria', 'cloroplasto', 'fotossíntese', 'respiraç', 'glicólise', 'krebs', 'fermentaç', 'osmose', 'membrana plasmática', 'transporte ativo', 'atp']),
    'B4': ('Fisiologia e Imunologia', ['vacina', 'soro', 'antígeno', 'anticorpo', 'imun', 'linfócito', 'aedes', 'dengue', 'zika', 'chikungunya', 'chagas', 'malária', 'leishmaniose', 'bactéria', 'vírus', 'hormôni']),
    
    'F1': ('Eletrodinâmica', ['circuito', 'resistor', 'resistência', 'corrente elétrica', 'ddp', 'tensão', 'voltagem', 'potência elétrica', 'kwh', 'joule', 'fusível', 'disjuntor', 'amperímetro', 'voltímetro', 'paralelo', 'ohm']),
    'F2': ('Mecânica e Hidrostática', ['cinética', 'potencial gravitacional', 'conservação da energia', 'trabalho', 'newton', 'atrito', 'plano inclinado', 'cinemática', 'aceleração', 'mru', 'pressão hidrostática', 'empuxo', 'arquimedes', 'pascal']),
    'F3': ('Ondulatória e Acústica', ['onda', 'ondulatória', 'comprimento de onda', 'frequência', 'frequencia', 'refração', 'difração', 'interferência', 'ressonância', 'doppler', 'acústica', 'timbre', 'som']),
    'F4': ('Termologia e Termodinâmica', ['calorimetria', 'calor sensível', 'calor latente', 'condução', 'convecção', 'irradiação', 'termodinâmica', 'primeira lei', 'máquina térmica', 'carnot', 'dilataç']),
    
    'Q1': ('Físico-Química', ['pilha', 'ânodo', 'cátodo', 'oxidação', 'redução', 'potencial de redução', 'eletrólise', 'corrosão', 'metal de sacrifício', 'termoquímica', 'entalpia', 'delta h', 'lei de hess', 'cinética', 'catalisador', 'equilíbrio químico', 'le chatelier', 'ph', 'solução', 'concentraç', 'molar']),
    'Q2': ('Química Geral e Estequiometria', ['estequiometria', 'mol', 'massa molar', 'pureza', 'rendimento', 'limitante', 'ligação química', 'ligações de hidrogênio', 'dipolo', 'london', 'ponto de ebulição', 'separação de misturas', 'destilaç', 'filtraç', 'decantaç']),
    'Q3': ('Química Orgânica', ['química orgânica', 'hidrocarboneto', 'álcool', 'fenol', 'aldeído', 'cetona', 'ácido carboxílico', 'éster', 'amina', 'amida', 'isomeria', 'quiral', 'esterificaç', 'biodiesel', 'polímero', 'pet', 'pvc']),
    'Q4': ('Química Ambiental', ['química ambiental', 'chuva ácida', 'efeito estufa', 'ozônio', 'cfc', 'tratamento de água', 'floculaç', 'cloraç', 'poluente'])
}

samples = [
    ('Poliedro Q91', 'N2(g) + 3 H2(g) <=> 2 NH3(g) ∆H = -92,2 kJ Considerando o equilíbrio químico estabelecido, a síntese da amônia é favorecida...'),
    ('Poliedro Q92', 'O sinal Wi-Fi é uma onda eletromagnética que está sujeita a interferências e ao enfraquecimento de sinal ao longo do caminho...'),
    ('Bernoulli Q91', 'A ovelha Dolly foi o primeiro mamífero clonado por transferência nuclear de células somáticas...'),
    ('Bernoulli Q92', 'Considere a velocidade do som como igual a 340 m/s. Qual o regime de voo de uma aeronave que viaja à velocidade de 918 km/h? A velocidade da aeronave...'),
]

for name, text in samples:
    scores = {}
    t_lower = text.lower()
    for code, (topic_name, kws) in TAXONOMY.items():
        score = sum(1 for kw in kws if kw in t_lower)
        if score > 0:
            scores[code] = (score, topic_name)
    best = sorted(scores.items(), key=lambda x: -x[1][0])
    match_code = best[0][0] if best else 'NONE'
    match_name = best[0][1][1] if best else '-'
    print(f'{name} -> Best match: {match_code} ({match_name}) | Scores: {scores}')
