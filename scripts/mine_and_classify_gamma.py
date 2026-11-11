import os
import re
import json
import pypdf

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

print(f"Mapping {len(edition_source_map)} editions for deep semantic extraction.")

# Topic taxonomy dictionaries with weighted conceptual anchors
TAXONOMY = {
    'Matematica': {
        'Grandezas Proporcionais, Razao e Escala': {
            'keywords': ['proporcional', 'escala', 'razão', 'regra de três', 'porcentagem', 'divisão proporcional', 'diretamente proporcional', 'inversamente proporcional', 'densidade demográfica', 'vazão', 'taxa'],
            'habilidade': 'H1, H2, H3'
        },
        'Geometria Espacial': {
            'keywords': ['prisma', 'cilindro', 'cone', 'esfera', 'pirâmide', 'tronco', 'volume', 'capacidade', 'área superficial', 'planificação', 'projeção ortogonal', 'poliedro', 'paralelepípedo', 'cubo'],
            'habilidade': 'H7, H8, H9'
        },
        'Geometria Plana': {
            'keywords': ['área', 'perímetro', 'triângulo', 'quadilátero', 'retângulo', 'círculo', 'circunferência', 'semelhança', 'pitágoras', 'trapézio', 'polígono', 'lado', 'vértice', 'diagonal'],
            'habilidade': 'H6, H7, H8'
        },
        'Estatistica e Analise de Graficos': {
            'keywords': ['média', 'mediana', 'moda', 'desvio padrão', 'variância', 'gráfico de barras', 'gráfico de setores', 'gráfico de linhas', 'frequência', 'tabela', 'dispersão', 'distribuição'],
            'habilidade': 'H27, H28, H29'
        },
        'Probabilidade': {
            'keywords': ['probabilidade', 'chance', 'aleatório', 'espaço amostral', 'evento', 'independente', 'condicional', 'sorteio', 'dado', 'urna', 'moeda'],
            'habilidade': 'H28, H30'
        },
        'Analise Combinatoria': {
            'keywords': ['combinação', 'arranjo', 'permutação', 'fatorial', 'maneiras', 'possibilidades', 'escolha', 'agrupamento', 'comissões', 'princípio fundamental da contagem'],
            'habilidade': 'H2, H3, H4'
        },
        'Funcoes (Afim, Quadratica, Exponencial, Log)': {
            'keywords': ['função', 'afim', 'quadrática', 'parábola', 'vértice', 'máximo', 'mínimo', 'exponencial', 'logaritmo', 'crescimento', 'decaimento', 'raízes', 'gráfico da função'],
            'habilidade': 'H19, H20, H21, H22'
        },
        'Matematica Financeira': {
            'keywords': ['juros', 'compostos', 'simples', 'montante', 'capital', 'parcela', 'desconto', 'inflação', 'financiamento', 'prestação', 'investimento'],
            'habilidade': 'H4, H5'
        },
        'Trigonometria': {
            'keywords': ['seno', 'cosseno', 'tangente', 'trigonométrica', 'graus', 'radianos', 'triângulo retângulo', 'ângulo', 'ciclo trigonométrico'],
            'habilidade': 'H19, H20'
        },
        'Progressoes (PA e PG)': {
            'keywords': ['progressão aritmética', 'progressão geométrica', 'razão da pa', 'razão da pg', 'termo geral', 'soma dos termos', 'sequência'],
            'habilidade': 'H1, H2, H19'
        }
    },
    'Fisica': {
        'Eletrodinamica e Circuitos': {
            'keywords': ['circuito', 'resistor', 'resistência', 'corrente elétrica', 'tensão', 'voltagem', 'potência elétrica', 'quilowatt-hora', 'kwh', 'ohm', 'chuveiro', 'lâmpadas', 'paralelo', 'série', 'fusível', 'disjuntor'],
            'habilidade': 'H5, H6, H7, H20'
        },
        'Termologia e Calorimetria': {
            'keywords': ['calor', 'calorimetria', 'temperatura', 'capacidade térmica', 'calor específico', 'calor latente', 'troca de calor', 'condução', 'convecção', 'irradiação', 'dilatação', 'termodinâmica', 'máquina térmica', 'rendimento'],
            'habilidade': 'H1, H2, H5, H6'
        },
        'Ondulatoria e Acustica': {
            'keywords': ['onda', 'comprimento de onda', 'frequência', 'hertz', 'acústica', 'som', 'difração', 'interferência', 'polarização', 'refração', 'ressonância', 'doppler', 'timbre', 'intensidade', 'eco'],
            'habilidade': 'H1, H2, H17, H18'
        },
        'Dinamica e Energia Mecanica': {
            'keywords': ['newton', 'força', 'energia cinética', 'energia potencial', 'conservação da energia', 'trabalho mecânico', 'potência mecânica', 'atrito', 'mola', 'colisão', 'quantidade de movimento', 'impulso'],
            'habilidade': 'H5, H6, H20'
        },
        'Cinematica': {
            'keywords': ['velocidade', 'aceleração', 'movimento uniforme', 'movimento uniformemente variado', 'trajetória', 'lançamento', 'queda livre', 'alcance', 'tempo de queda', 'velocidade média'],
            'habilidade': 'H17, H20'
        },
        'Hidrostatica': {
            'keywords': ['pressão', 'empuxo', 'densidade', 'arquimedes', 'pascal', 'stevin', 'vasos comunicantes', 'mergulhado', 'flutua', 'líquido', 'atmosférica'],
            'habilidade': 'H5, H6, H20'
        },
        'Otica Geometrica': {
            'keywords': ['luz', 'espelho', 'lente', 'refração', 'reflexão', 'índice de refração', 'miopia', 'hipermetropia', 'convergente', 'divergente', 'foco', 'imagem real', 'imagem virtual'],
            'habilidade': 'H1, H2, H17'
        },
        'Eletromagnetismo': {
            'keywords': ['campo magnético', 'ímã', 'indução', 'faraday', 'espiras', 'transformador', 'força magnética', 'corrente induzida', 'solenoide'],
            'habilidade': 'H5, H6, H20'
        },
        'Gravitacao e Fisica Moderna': {
            'keywords': ['kepler', 'gravitação', 'órbita', 'satélite', 'planeta', 'fóton', 'efeito fotoelétrico', 'quântica', 'relatividade', 'decaimento nuclear'],
            'habilidade': 'H1, H2, H17'
        }
    },
    'Quimica': {
        'Fisico-Quimica e Solucoes': {
            'keywords': ['solução', 'concentração', 'molaridade', 'mol/l', 'solubilidade', 'diluição', 'mistura', 'propriedades coligativas', 'pressão de vapor', 'ebulição', 'congelamento'],
            'habilidade': 'H17, H18, H24'
        },
        'Quimica Organica (Funcoes e Propriedades)': {
            'keywords': ['hidrocarboneto', 'álcool', 'ácido carboxílico', 'éster', 'amina', 'amida', 'aldeído', 'cetona', 'polaridade', 'solubilidade orgânica', 'ponto de ebulição', 'isomeria', 'cadeia carbônica'],
            'habilidade': 'H17, H18, H24'
        },
        'Reacoes Organicas e Polimeros': {
            'keywords': ['esterificação', 'saponificação', 'biodiesel', 'transesterificação', 'polímero', 'plástico', 'oxidação', 'adição', 'substituição', 'condensação', 'monômero'],
            'habilidade': 'H24, H25, H26'
        },
        'Estequiometria e Gases': {
            'keywords': ['estequiometria', 'massa molar', 'reagente limitante', 'excesso', 'rendimento', 'pureza', 'mol', 'volume molar', 'gás ideal', 'equação química', 'balanceamento'],
            'habilidade': 'H17, H24, H25'
        },
        'Eletroquimica (Pilhas e Eletrolise)': {
            'keywords': ['pilha', 'eletrólise', 'ânodo', 'cátodo', 'oxidação', 'redução', 'potencial de redução', 'espontânea', 'corrosão', 'proteção catódica', 'galvanoplastia'],
            'habilidade': 'H17, H20, H24'
        },
        'Termoquimica': {
            'keywords': ['entalpia', 'exotérmica', 'endotérmica', 'delta h', 'calor de combustão', 'lei de hess', 'energia de ligação', 'combustível'],
            'habilidade': 'H5, H6, H17'
        },
        'Equilibrio Quimico e pH': {
            'keywords': ['equilíbrio químico', 'le chatelier', 'ph', 'poh', 'acidez', 'basicidade', 'hidrólise', 'tampão', 'constante de equilíbrio', 'kc', 'kps', 'indicador'],
            'habilidade': 'H17, H24, H25'
        },
        'Quimica Ambiental e Tratamento': {
            'keywords': ['chuva ácida', 'efeito estufa', 'tratamento de água', 'floculação', 'filtração', 'decantação', 'cloração', 'poluição', 'metais pesados', 'camada de ozônio', 'sustentabilidade'],
            'habilidade': 'H24, H25, H26'
        },
        'Ligacoes Quimicas e Forcas Intermoleculares': {
            'keywords': ['ligação iônica', 'ligação covalente', 'ligação metálica', 'ligação de hidrogênio', 'dipolo-dipolo', 'dispersão de london', 'geometria molecular', 'tabela periódica', 'eletronegatividade'],
            'habilidade': 'H17, H18'
        }
    },
    'Biologia': {
        'Ecologia e Biomas': {
            'keywords': ['cadeia alimentar', 'teia alimentar', 'nível trófico', 'produtor', 'consumidor', 'decompositor', 'relação ecológica', 'mutualismo', 'parasitismo', 'predação', 'competição', 'bioma', 'cerrado', 'caatinga', 'mata atlântica', 'sucessão ecológica'],
            'habilidade': 'H14, H15, H16, H29, H30'
        },
        'Impactos Ambientais e Conservacao': {
            'keywords': ['eutrofização', 'magnificação trófica', 'bioacumulação', 'desmatamento', 'queimada', 'espécie invasora', 'biodiversidade', 'aquecimento global', 'poluição das águas', 'conservação'],
            'habilidade': 'H14, H15, H16, H29, H30'
        },
        'Genetica e Biologia Molecular': {
            'keywords': ['gene', 'dna', 'rna', 'alelo', 'heredograma', 'mendel', 'mutação', 'código genético', 'tradução', 'transcrição', 'síntese proteica', 'grupo sanguíneo', 'cromossomo'],
            'habilidade': 'H13, H14, H15'
        },
        'Fisiologia Humana': {
            'keywords': ['sistema digestório', 'sistema circulatório', 'sangue', 'coração', 'respiração', 'pulmão', 'excreção', 'rim', 'hormônio', 'insulina', 'nervoso', 'imunológico', 'anticorpo', 'vacina', 'soro', 'homeostase'],
            'habilidade': 'H13, H14, H15, H28'
        },
        'Citologia e Metabolismo Energetico': {
            'keywords': ['célula', 'membrana plasmática', 'mitocôndria', 'cloroplasto', 'fotossíntese', 'respiração celular', 'fermentação', 'atp', 'osmose', 'transporte ativo', 'organela', 'enzima'],
            'habilidade': 'H13, H14, H15'
        },
        'Microbiologia, Parasitologia e Saude': {
            'keywords': ['vírus', 'bactéria', 'protozoário', 'verme', 'doença', 'dengue', 'chagas', 'malária', 'esquistossomose', 'vacinação', 'antibiótico', 'profilaxia', 'transmissão', 'vetor'],
            'habilidade': 'H13, H14, H28'
        },
        'Evolucao': {
            'keywords': ['seleção natural', 'darwin', 'lamarck', 'evolução', 'especiação', 'adaptação', 'fóssil', 'homologia', 'analogia', 'ancestral comum'],
            'habilidade': 'H13, H14, H15'
        },
        'Biotecnologia': {
            'keywords': ['transgênico', 'clonagem', 'dna recombinante', 'célula-tronco', 'terapia gênica', 'crispr', 'pcr', 'eletroforese', 'biotecnologia'],
            'habilidade': 'H13, H14, H15, H28'
        },
        'Botanica e Fisiologia Vegetal': {
            'keywords': ['planta', 'vegetal', 'briófita', 'pteridófita', 'gimnosperma', 'angiosperma', 'xilema', 'floema', 'transpiração', 'estômato', 'auxina', 'caule', 'raiz', 'folha'],
            'habilidade': 'H14, H15'
        }
    }
}

def classify_question_text(q_num, text):
    lower = text.lower()
    
    # 1. Determine discipline
    if q_num >= 136:
        discipline = 'Matematica'
    else:
        # q_num is 91-135 or 45-90 in 2014: Natureza
        # Score Fisica, Quimica, Biologia
        scores = {'Fisica': 0, 'Quimica': 0, 'Biologia': 0}
        for disc in ['Fisica', 'Quimica', 'Biologia']:
            for topic, data in TAXONOMY[disc].items():
                for kw in data['keywords']:
                    if kw in lower:
                        scores[disc] += 1
                        
        # Specific discipline bias based on strong unique indicators
        if any(w in lower for w in ['resistor', 'volt', 'ohm', 'circuito', 'acústica', 'calorimetria', 'lançamento', 'empuxo', 'óptica', 'ótico', 'onda eletromagnética', 'refração da luz', 'joule', 'newton']):
            scores['Fisica'] += 4
        if any(w in lower for w in ['ácido', 'reação química', 'solução', 'mol', 'massa molar', 'estequiometria', 'hidrocarboneto', 'éster', 'oxirredução', 'elétrons', 'ânodo', 'cátodo', 'tabela periódica', 'entalpia']):
            scores['Quimica'] += 4
        if any(w in lower for w in ['célula', 'dna', 'rna', 'espécie', 'organismo', 'cadeia alimentar', 'ecossistema', 'hormônio', 'vírus', 'bactéria', 'parasita', 'doença', 'enzima', 'fotossíntese', 'heredograma', 'mutação']):
            scores['Biologia'] += 4
            
        discipline = max(scores, key=scores.get)
        if scores[discipline] == 0:
            # Default to round-robin or balanced
            if q_num <= 105:
                discipline = 'Biologia'
            elif q_num <= 120:
                discipline = 'Fisica'
            else:
                discipline = 'Quimica'
                
    # 2. Determine conceptual topic
    topic_scores = {}
    disc_taxonomy = TAXONOMY[discipline]
    for topic, data in disc_taxonomy.items():
        score = 0
        for kw in data['keywords']:
            # Count occurrences or presence
            if kw in lower:
                score += lower.count(kw)
        topic_scores[topic] = score
        
    best_topic = max(topic_scores, key=topic_scores.get)
    if topic_scores[best_topic] == 0:
        best_topic = list(disc_taxonomy.keys())[0]
        
    hab = disc_taxonomy[best_topic]['habilidade']
    
    # 3. Interdisciplinary check
    inter = []
    if discipline != 'Matematica':
        other_discs = [d for d in ['Fisica', 'Quimica', 'Biologia'] if d != discipline]
        for od in other_discs:
            for t, data in TAXONOMY[od].items():
                matches = [kw for kw in data['keywords'] if kw in lower]
                if len(matches) >= 2:
                    inter.append(f"{discipline} + {od} ({t})")
                    break
    else:
        # Check if Math models a Nature problem
        nat_words = ['física', 'química', 'biologia', 'temperatura', 'velocidade', 'bactéria', 'população', 'concentração', 'decaimento', 'substância']
        if any(w in lower for w in nat_words):
            inter.append("Matemática aplicada a Ciências da Natureza")
            
    return {
        'discipline': discipline,
        'topic': best_topic,
        'habilidade': hab,
        'interdisciplinary': list(set(inter))
    }

# Execute extraction across all 33 editions
all_extracted_questions = []

for ed, s in sorted(edition_source_map.items()):
    rel = s['path']
    full = os.path.join(base, rel)
    reader = pypdf.PdfReader(full)
    full_text = ""
    for p in range(len(reader.pages)):
        full_text += f"\n[P{p+1}]\n" + (reader.pages[p].extract_text() or "")
        
    # Determine question range
    if ed == '2014_SIMULADO_1':
        q_start, q_end = 46, 90
    else:
        q_start, q_end = 91, 180
        
    count_ed = 0
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
                
        cls_result = classify_question_text(q, q_text)
        all_extracted_questions.append({
            'edition': ed,
            'source_file': rel,
            'question_number': q,
            'discipline': cls_result['discipline'],
            'topic': cls_result['topic'],
            'habilidade': cls_result['habilidade'],
            'interdisciplinary': cls_result['interdisciplinary'],
            'text_length': len(q_text),
            'text_snippet': q_text[:200].replace('\n', ' ')
        })
        count_ed += 1
        
    print(f"Extracted and classified {count_ed} questions for {ed}.")

print(f"\nTOTAL QUESTIONS PROCESSED: {len(all_extracted_questions)}")

with open('FINAL_gamma_questions.json', 'w', encoding='utf-8') as f:
    json.dump(all_extracted_questions, f, indent=2, ensure_ascii=False)

print("Saved complete questions database to FINAL_gamma_questions.json")
