import os
import re
import sys
import json
import zipfile
import xml.etree.ElementTree as ET
import pypdf

# Define scope paths
WORKSPACE = r"c:\Users\Eduardo\Documents\02_Estudos & Academico\ENEM DIA 2"
SAS_DIR = os.path.join(WORKSPACE, "SAS")
PROG_DIR = os.path.join(SAS_DIR, "PROGRAMÁTICA")
COLEGIO_DIR = os.path.join(SAS_DIR, "SAS ENEM COLEGIO")

# Semantic Topic Taxonomy Definitions
TOPIC_PATTERNS = {
    'Matemática': {
        'Geometria Espacial': [
            'volume', 'cilindro', 'cone', 'esfera', 'prisma', 'pirâmide', 'tronco', 'capacidade',
            'litros', 'metro cúbico', 'm³', 'cm³', 'silo', 'reservatório', 'caixa d\'água',
            'área total', 'área lateral', 'área da base', 'planificação', 'vistas ortogonais',
            'projeção ortogonal', 'sólido geométrico', 'poliedro', 'vértice', 'aresta', 'face'
        ],
        'Geometria Plana': [
            'área', 'perímetro', 'triângulo', 'quadrado', 'retângulo', 'trapézio', 'losango',
            'polígono', 'circunferência', 'círculo', 'raio', 'diâmetro', 'corda', 'setor circular',
            'teorema de pitágoras', 'semelhança de triângulos', 'ladrilhamento', 'pavimentação',
            'ângulos', 'simetria', 'eixo de simetria', 'congruência'
        ],
        'Aritmética e Proporcionalidade': [
            'razão', 'proporção', 'regra de três', 'diretamente proporcional', 'inversamente proporcional',
            'escala', 'escala cartográfica', 'fração', 'número decimal', 'divisão proporcional',
            'dízima', 'mdc', 'mmc', 'operações fundamentais', 'unidade de medida', 'conversão de unidades'
        ],
        'Estatística e Análise de Dados': [
            'média', 'média aritmética', 'média ponderada', 'mediana', 'moda', 'desvio padrão',
            'variância', 'gráfico de barras', 'gráfico de setores', 'gráfico de linhas', 'histograma',
            'tabela de frequências', 'distribuição de frequência', 'leitura de gráfico', 'amostra'
        ],
        'Funções e Álgebra': [
            'função', 'gráfico da função', 'função afim', 'função do 1º grau', 'função quadrática',
            'função do 2º grau', 'parábola', 'vértice da parábola', 'valor máximo', 'valor mínimo',
            'função exponencial', 'crescimento exponencial', 'função logarítmica', 'logaritmo',
            'progressão aritmética', 'progressão geométrica', 'sistema linear', 'equação'
        ],
        'Probabilidade': [
            'probabilidade', 'chance', 'espaço amostral', 'evento', 'probabilidade condicional',
            'sorteio', 'urna', 'dado', 'moeda', 'lançamento', 'jogos de azar'
        ],
        'Análise Combinatória': [
            'combinação', 'arranjo', 'permutação', 'princípio fundamental da contagem', 'fatorial',
            'agrupamento', 'anagrama', 'escolha de pessoas', 'comissão'
        ],
        'Matemática Financeira e Porcentagem': [
            'porcentagem', 'por cento', '%', 'lucro', 'prejuízo', 'desconto', 'acréscimo',
            'juros simples', 'juros compostos', 'capital', 'montante', 'taxa de juros',
            'inflação', 'depreciação', 'reajuste', 'rendimento financeiro'
        ],
        'Trigonometria': [
            'seno', 'cosseno', 'tangente', 'trigonometria', 'ciclo trigonométrico', 'triângulo retângulo',
            'lei dos senos', 'lei dos cossenos', 'ângulo reto', 'hipotenusa', 'cateto'
        ]
    },
    'Física': {
        'Eletrodinâmica': [
            'circuito', 'resistor', 'resistência', 'corrente elétrica', 'tensão', 'diferença de potencial',
            'ddp', 'volts', 'ampère', 'ohm', 'potência elétrica', 'watts', 'quilowatt-hora', 'kwh',
            'gerador', 'receptor', 'bateria', 'pilha', 'fusível', 'disjuntor', 'associação em série',
            'associação em paralelo', 'lei de ohm', 'efeito joule', 'curto-circuito', 'lâmpada'
        ],
        'Termologia e Termodinâmica': [
            'calor', 'temperatura', 'calorimetria', 'calor sensível', 'calor latente', 'capacidade térmica',
            'troca de calor', 'equilíbrio térmico', 'condução', 'convecção', 'irradiação', 'dilatação térmica',
            'gás ideal', 'termodinâmica', 'primeira lei da termodinâmica', 'segunda lei da termodinâmica',
            'ciclo de carnot', 'máquina térmica', 'rendimento térmico', 'trabalho de um gás'
        ],
        'Ondulatória e Acústica': [
            'onda', 'frequência', 'comprimento de onda', 'período', 'amplitude', 'velocidade de propagação',
            'v=λf', 'som', 'acústica', 'timbre', 'altura do som', 'intensidade sonora', 'decibéis',
            'difração', 'interferência', 'polarização', 'ressonância', 'efeito doppler', 'corda vibrante',
            'onda eletromagnética', 'espectro eletromagnético', 'eco', 'reverberação'
        ],
        'Mecânica - Cinemática e Dinâmica': [
            'velocidade', 'aceleração', 'mru', 'mruv', 'movimento retilíneo', 'queda livre', 'lançamento',
            'gráfico espaço-tempo', 'gráfico velocidade-tempo', 'força', 'leis de newton', 'inércia',
            'massa', 'peso', 'força normal', 'força de atrito', 'tração', 'plano inclinado',
            'força elástica', 'lei de hooke', 'movimento circular', 'aceleração centrípeta', 'força centrípeta'
        ],
        'Mecânica - Trabalho, Energia e Potência': [
            'trabalho', 'energia cinética', 'energia potencial gravitacional', 'energia potencial elástica',
            'energia mecânica', 'conservação da energia', 'potência mecânica', 'rendimento', 'sistema conservativo',
            'quantidade de movimento', 'momento linear', 'impulso', 'colisão', 'choque elástico'
        ],
        'Hidrostática': [
            'pressão', 'densidade', 'massa específica', 'pressão atmosférica', 'teorema de stevin',
            'vasos comunicantes', 'pressão hidrostática', 'princípio de pascal', 'prensa hidráulica',
            'empuxo', 'princípio de arquimedes', 'flutuação', 'peso aparente', 'barômetro'
        ],
        'Óptica Geométrica': [
            'luz', 'feixe luminoso', 'raio de luz', 'reflexão da luz', 'espelho plano', 'espelho esférico',
            'espelho côncavo', 'espelho convexo', 'refração da luz', 'índice de refração', 'lei de snell',
            'lente delgada', 'lente convergente', 'lente divergente', 'formação de imagens', 'olho humano',
            'miopia', 'hipermetropia', 'astigmatismo', 'prisma óptico', 'reflexão total'
        ],
        'Eletromagnetismo e Eletrostática': [
            'carga elétrica', 'elétron', 'próton', 'eletrização', 'lei de coulomb', 'campo elétrico',
            'potencial elétrico', 'campo magnético', 'imã', 'pólos magnéticos', 'força magnética',
            'indução eletromagnética', 'lei de faraday', 'lei de lenz', 'transformador', 'solenóide'
        ]
    },
    'Química': {
        'Físico-Química: Termoquímica e Cinética': [
            'entalpia', 'termoquímica', 'reação endotérmica', 'reação exotérmica', 'calor de reação',
            'lei de hess', 'energia de ligação', 'calor de combustão', 'cinética química', 'velocidade de reação',
            'energia de ativação', 'catalisador', 'complexo ativado', 'colisão efetiva', 'fatores de velocidade'
        ],
        'Físico-Química: Soluções e Estequiometria': [
            'estequiometria', 'cálculo estequiométrico', 'massa molar', 'número de mols', 'reagente limitante',
            'reagente em excesso', 'rendimento da reação', 'pureza do reagente', 'solução', 'soluto', 'solvente',
            'concentração', 'concentração comum', 'concentração molar', 'mol/l', 'título', 'ppm',
            'diluição', 'mistura de soluções', 'titulação ácido-base'
        ],
        'Físico-Química: Eletroquímica e Equilíbrio': [
            'equilíbrio químico', 'constante de equilíbrio', 'kc', 'kp', 'deslocamento de equilíbrio',
            'princípio de le chatelier', 'ph', 'poh', 'acidez', 'basicidade', 'hidrólise salina', 'solução tampão',
            'eletroquímica', 'oxirredução', 'oxidação', 'redução', 'agente oxidante', 'agente redutor',
            'pilha', 'pilha de daniell', 'cátodo', 'ânodo', 'potencial padrão', 'eletrólise', 'corrosão'
        ],
        'Química Orgânica: Funções e Nomenclatura': [
            'química orgânica', 'cadeia carbônica', 'hidrocarboneto', 'alcano', 'alceno', 'alcino',
            'aromático', 'benzeno', 'álcool', 'enois', 'fenol', 'aldeído', 'cetona', 'ácido carboxílico',
            'éster', 'éter', 'amina', 'amida', 'haleto', 'função orgânica', 'nomenclatura iupac'
        ],
        'Química Orgânica: Propriedades, Reações e Polímeros': [
            'polaridade orgânica', 'solubilidade orgânica', 'ponto de ebulição orgânico', 'forças intermoleculares em orgânicos',
            'isomeria', 'isomeria plana', 'isomeria geométrica', 'cis-trans', 'isomeria óptica', 'carbono quiral',
            'polímero', 'polímero de adição', 'polímero de condensação', 'plástico', 'pet', 'borracha',
            'reação de esterificação', 'saponificação', 'sabão', 'detergente', 'biodiesel', 'combustão orgânica'
        ],
        'Química Geral e Inorgânica: Ligações e Geometria': [
            'ligação química', 'ligação iônica', 'ligação covalente', 'ligação metálica', 'elétron de valência',
            'regra do octeto', 'geometria molecular', 'linear', 'angular', 'trigonal plana', 'piramidal', 'tetraédrica',
            'polaridade da ligação', 'polaridade da molécula', 'forças intermoleculares', 'ligação de hidrogênio',
            'dipolo-dipolo', 'dipolo induzido', 'dispersão de london'
        ],
        'Química Geral: Tabela Periódica, Átomo e Funções': [
            'átomo', 'núcleo atômico', 'elétron', 'próton', 'nêutron', 'modelos atômicos', 'dalton', 'thomson',
            'rutherford', 'bohr', 'distribuição eletrônica', 'tabela periódica', 'família', 'período',
            'eletronegatividade', 'raio atômico', 'potencial de ionização', 'função inorgânica', 'ácido',
            'base', 'sal', 'óxido', 'ácido de arrhenius'
        ],
        'Química Ambiental': [
            'química ambiental', 'poluição atmosférica', 'poluição da água', 'efeito estufa', 'aquecimento global',
            'gás carbônico', 'co2', 'metano', 'ch4', 'chuva ácida', 'óxidos de enxofre', 'óxidos de nitrogênio',
            'inversão térmica', 'camada de ozônio', 'cfc', 'tratamento de água', 'floculação', 'cloração',
            'biomassa', 'combustível fóssil', 'recursos renováveis'
        ]
    },
    'Biologia': {
        'Ecologia e Meio Ambiente': [
            'ecologia', 'ecossistema', 'comunidade', 'população', 'habitat', 'nicho ecológico',
            'cadeia alimentar', 'teia alimentar', 'produtor', 'consumidor', 'decompositor', 'nível trófico',
            'pirâmide ecológica', 'ciclo biogeoquímico', 'ciclo da água', 'ciclo do carbono', 'ciclo do nitrogênio',
            'relação ecológica', 'mutualismo', 'comensalismo', 'parasitismo', 'predatismo', 'competição',
            'sucessão ecológica', 'desmatamento', 'queimada', 'eutrofização', 'bioacumulação', 'magnificação trófica',
            'poluição', 'espécie invasora', 'conservação', 'pegada ecológica'
        ],
        'Citologia, Bioquímica e Metabolismo': [
            'célula', 'citologia', 'membrana plasmática', 'bicamada lipídica', 'transporte passivo', 'difusão',
            'osmose', 'transporte ativo', 'bomba de sódio e potássio', 'citoplasma', 'organela', 'mitocôndria',
            'cloroplasto', 'retículo endoplasmático', 'complexo de golgi', 'ribossomo', 'lisossomo', 'peroxissomo',
            'bioquímica celular', 'carboidrato', 'lipídio', 'proteína', 'aminoácido', 'enzima', 'catalisador biológico',
            'metabolismo energético', 'respiração celular', 'glicólise', 'ciclo de krebs', 'fosforilação oxidativa',
            'fotossíntese', 'fase clara', 'fase escura', 'clorofila', 'fermentação', 'fermentação lática', 'fermentação alcoólica',
            'divisão celular', 'mitose', 'meiose', 'ciclo celular'
        ],
        'Genética e Biologia Molecular': [
            'genética', 'gene', 'alelo', 'alelo dominante', 'alelo recessivo', 'homozigoto', 'heterozigoto',
            'genótipo', 'fenótipo', 'primeira lei de mendel', 'segunda lei de mendel', 'cruzamento',
            'herança monogênica', 'codominância', 'grupos sanguíneos', 'sistema abo', 'fator rh', 'aglutinação',
            'herança ligada ao sexo', 'cromossomo x', 'cromossomo y', 'dna', 'rna', 'nucleotídeo',
            'replicação do dna', 'transcrição', 'tradução', 'síntese proteica', 'código genético', 'mutação gênica'
        ],
        'Biotecnologia e Engenharia Genética': [
            'biotecnologia', 'engenharia genética', 'dna recombinante', 'transgênico', 'ogm', 'organismo geneticamente modificado',
            'clonagem', 'pcr', 'reação em cadeia da polimerase', 'eletroforese', 'enzima de restrição', 'crispr',
            'edição gênica', 'célula-tronco', 'terapia gênica', 'bioética', 'vacina de rna', 'impressão digital de dna'
        ],
        'Fisiologia Humana e Saúde Pública': [
            'fisiologia humana', 'sistema digestório', 'digestão', 'estômago', 'intestino', 'sistema respiratório',
            'pulmão', 'troca gasosa', 'alvéolo', 'sistema circulatório', 'coração', 'sangue', 'vaso sanguíneo',
            'artéria', 'veia', 'sistema excretor', 'rim', 'néfron', 'urina', 'sistema nervoso', 'neurônio', 'sinapse',
            'sistema endócrino', 'hormônio', 'insulina', 'glucagon', 'tireoide', 'hipófise', 'sistema imunitário',
            'imunologia', 'anticorpo', 'antígeno', 'vacina', 'soro', 'imunização', 'doença infecciosa', 'virose',
            'bacteriose', 'protozoose', 'verminose', 'saúde pública', 'epidemia', 'pandemia', 'vetor'
        ],
        'Evolução Biológica': [
            'evolução', 'teoria da evolução', 'darwin', 'darwinismo', 'lamarck', 'lamarckismo', 'seleção natural',
            'neodarwinismo', 'teoria sintética da evolução', 'adaptação', 'mutação e recombinação', 'especiação',
            'isolamento reprodutivo', 'homologia', 'analogia', 'órgãos homólogos', 'órgãos análogos', 'convergência evolutiva',
            'irradiação adaptativa', 'fóssil', 'deriva genética'
        ],
        'Botânica': [
            'botânica', 'reino vegetal', 'briófita', 'pteridófita', 'gimnosperma', 'angiosperma', 'vasos condutores',
            'xilema', 'floema', 'seiva bruta', 'seiva elaborada', 'raiz', 'caule', 'folha', 'flor', 'fruto',
            'semente', 'estômato', 'transpiração vegetal', 'hormônio vegetal', 'fitormônio', 'auxina', 'etileno',
            'giberelina', 'citocinina', 'fotoperiodismo', 'tropismo'
        ]
    }
}

def classify_text_semantics(text, hint_discipline=None, allowed_disciplines=None):
    t = text.lower()
    
    disc_scores = {'Matemática': 0, 'Física': 0, 'Química': 0, 'Biologia': 0}
    if hint_discipline and hint_discipline in disc_scores:
        disc_scores[hint_discipline] += 5
        
    topic_matches = {}
    
    for disc, topics in TOPIC_PATTERNS.items():
        for topic, keywords in topics.items():
            count = 0
            for kw in keywords:
                if kw in t:
                    weight = 2 if len(kw) > 6 else 1
                    count += weight
                    disc_scores[disc] += weight
            if count > 0:
                topic_matches[(disc, topic)] = count
                
    # If allowed_disciplines is specified, restrict candidate disciplines
    if allowed_disciplines:
        filtered_scores = {d: disc_scores[d] for d in allowed_disciplines}
        best_disc = max(filtered_scores, key=filtered_scores.get)
        if filtered_scores[best_disc] == 0:
            best_disc = allowed_disciplines[0]
    else:
        best_disc = max(disc_scores, key=disc_scores.get)
        if disc_scores[best_disc] == 0:
            best_disc = hint_discipline if hint_discipline else 'Matemática'
        
    disc_topics = {topic: count for (d, topic), count in topic_matches.items() if d == best_disc}
    if disc_topics:
        best_topic = max(disc_topics, key=disc_topics.get)
    else:
        defaults = {
            'Matemática': 'Aritmética e Proporcionalidade',
            'Física': 'Eletrodinâmica',
            'Química': 'Físico-Química: Soluções e Estequiometria',
            'Biologia': 'Ecologia e Meio Ambiente'
        }
        best_topic = defaults[best_disc]
        
    other_discs = [d for d, s in disc_scores.items() if d != best_disc and s >= 3]
    interdisciplinary = other_discs[0] if other_discs else None
    
    return best_disc, best_topic, interdisciplinary
