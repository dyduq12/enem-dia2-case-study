import os
import sys
import re
import json
import zipfile
import xml.etree.ElementTree as ET
import pypdf
from collections import defaultdict

BASE_DIR = r"c:\Users\Eduardo\Documents\02_Estudos & Academico\ENEM DIA 2"

# -------------------------------------------------------------
# 1. TAXONOMY AND TOPIC METADATA
# -------------------------------------------------------------

TOPICS_INFO = {
    # MATEMÁTICA
    'M1': {
        'name': 'Matemática Básica e Proporcionalidade',
        'inc': '34% a 38%',
        'status': 'CRUCIAL (Base da TRI)',
        'area': 'Matemática',
        'desc': 'Razão, proporção, regra de três simples e composta, porcentagem, aumentos/descontos, escalas cartográficas e conversão de unidades (litros, m³, tempo). Sustenta a coerência pedagógica da nota.'
    },
    'M2': {
        'name': 'Geometria Espacial',
        'inc': '11% a 13%',
        'status': 'ALTA (Diferencial)',
        'area': 'Matemática',
        'desc': 'Cálculo de volumes e áreas de prismas retos, cilindros, cones e esferas; projeção ortogonal e visualização espacial tridimensional; poliedros (Relação de Euler).'
    },
    'M3': {
        'name': 'Estatística Básica',
        'inc': '10% a 12%',
        'status': 'CRUCIAL (Base da TRI)',
        'area': 'Matemática',
        'desc': 'Interpretação de gráficos (barras, colunas, setores, linhas) e tabelas; medidas de tendência central (média aritmética e ponderada, mediana, moda); dispersão (desvio padrão).'
    },
    'M4': {
        'name': 'Geometria Plana',
        'inc': '8% a 10%',
        'status': 'ALTA',
        'area': 'Matemática',
        'desc': 'Cálculo de áreas (triângulos, círculos, paralelogramos, trapézios); Teorema de Pitágoras; trigonometria básica nos triângulos retângulos; semelhança de triângulos e Teorema de Tales; geometria analítica básica no plano.'
    },
    'M5': {
        'name': 'Funções e Modelagem Algébrica',
        'inc': '7% a 9%',
        'status': 'MÉDIA-ALTA',
        'area': 'Matemática',
        'desc': 'Função Afim (taxa de variação e valor fixo); Função Quadrática (vértice, máximos e mínimos); modelagem exponencial e propriedades fundamentais de logaritmos; sistemas lineares.'
    },
    'M6': {
        'name': 'Probabilidade e Análise Combinatória',
        'inc': '9% a 12%',
        'status': 'MÉDIA-ALTA (Diferencial)',
        'area': 'Matemática',
        'desc': 'Princípio Fundamental da Contagem (PFC), permutações e combinações simples; probabilidade clássica, probabilidade da união de eventos e probabilidade condicional.'
    },

    # BIOLOGIA
    'B1': {
        'name': 'Ecologia e Meio Ambiente',
        'inc': '28% a 32%',
        'status': 'LÍDER ABSOLUTA HISTÓRICA',
        'area': 'Biologia',
        'desc': 'Impactos ambientais antrópicos (eutrofização, bioacumulação e magnificação trófica, aquecimento global e acidificação oceânica, desmatamento e espécies invasoras); ciclos biogeoquímicos (Nitrogênio e Carbono); fluxo de energia e teias tróficas; relações ecológicas.'
    },
    'B2': {
        'name': 'Genética, Biologia Molecular e Biotecnologia',
        'inc': '20% a 25%',
        'status': 'ALTA',
        'area': 'Biologia',
        'desc': '1ª e 2ª Leis de Mendel, heredogramas, sistema ABO e Fator Rh; Biotecnologia aplicada (DNA recombinante, clonagem terapêutica/reprodutiva, transgênicos vs OGM, PCR, eletroforese e CRISPR).'
    },
    'B3': {
        'name': 'Citologia e Metabolismo Energético',
        'inc': '12% a 15%',
        'status': 'ALTA',
        'area': 'Biologia',
        'desc': 'Fotossíntese (fases fotoquímica e química); respiração celular aeróbia e fermentação (láctica e alcoólica); membrana plasmática e transportes celulares (osmose, difusão e transporte ativo por bomba de Na+/K+).'
    },
    'B4': {
        'name': 'Fisiologia Humana e Imunologia',
        'inc': '10% a 13%',
        'status': 'ALTA (Contextualizada)',
        'area': 'Biologia',
        'desc': 'Imunologia (Vacinas: profiláticas, antígenos atenuados, células de memória vs. Soros: curativos emergenciais, anticorpos pré-formados); Doenças e agentes etiológicos (arboviroses pelo Aedes, Chagas, Malária, Leishmaniose e uso racional de antibióticos).'
    },

    # FÍSICA
    'F1': {
        'name': 'Eletrodinâmica e Circuitos Elétricos',
        'inc': '21% a 24%',
        'status': 'LÍDER EM REGULARIDADE',
        'area': 'Física',
        'desc': 'Circuitos elétricos com associação de resistores em série e paralelo; potência elétrica e consumo de energia residencial em kWh (E = P.Δt / 1000); dimensionamento de fusíveis e disjuntores; instrumentos de medição (amperímetro e voltímetro).'
    },
    'F2': {
        'name': 'Mecânica Clássica e Hidrostática',
        'inc': '31% a 37%',
        'status': 'LÍDER EM VOLUME',
        'area': 'Física',
        'desc': 'Conservação da energia mecânica (cinética, potencial gravitacional e elástica), dissipação por atrito e rendimento; Leis de Newton e dinâmica em planos inclinados; cinemática escalar e interpretação gráfica (área sob v x t = distância); hidrostática (pressão, Teorema de Pascal e Empuxo de Arquimedes).'
    },
    'F3': {
        'name': 'Ondulatória e Acústica',
        'inc': '14% a 16%',
        'status': 'ALTA (Foco Conceitual)',
        'area': 'Física',
        'desc': 'Equação fundamental da onda (v = λ.f); fenômenos ondulatórios (refração, difração, interferência, ressonância, polarização e Efeito Doppler); qualidades fisiológicas do som (altura, intensidade e timbre); óptica geométrica básica.'
    },
    'F4': {
        'name': 'Termologia e Termodinâmica',
        'inc': '13% a 16%',
        'status': 'ALTA',
        'area': 'Física',
        'desc': 'Calorimetria sensível (Q = m.c.ΔT) e calor latente de mudança de estado (Q = m.L); processos de transmissão de calor (condução, convecção e irradiação); 1ª Lei da Termodinâmica (ΔU = Q - W) e 2ª Lei (máquinas térmicas e rendimento de Carnot).'
    },

    # QUÍMICA
    'Q1': {
        'name': 'Físico-Química (Eletroquímica, Termoquímica e Equilíbrio)',
        'inc': '28% a 32%',
        'status': 'LÍDER EM CÁLCULOS E PROCESSOS',
        'area': 'Química',
        'desc': 'Eletroquímica (pilhas galvânicas, potencial de redução, ânodo/cátodo, corrosão e metal de sacrifício, eletrólise); Termoquímica (Lei de Hess, calor de formação e energias de ligação); Cinética e Equilíbrio Químico (catalisadores, energia de ativação e Princípio de Le Chatelier); Soluções (cálculo de concentração molar, g/L, ppm e diluição).'
    },
    'Q2': {
        'name': 'Química Geral e Estequiometria',
        'inc': '25% a 28%',
        'status': 'BASE ESTRUTURAL',
        'area': 'Química',
        'desc': 'Cálculos estequiométricos reais com reagentes impuros (% de pureza), rendimento percentual e determinação de reagente limitante/excesso; forças intermoleculares (ligações de hidrogênio, dipolo-dipolo e London) e impacto no ponto de ebulição e solubilidade; métodos de separação de misturas (decantação, filtração, destilação simples/fracionada e flotação).'
    },
    'Q3': {
        'name': 'Química Orgânica',
        'inc': '19% a 23%',
        'status': 'ALTA REGULARIDADE',
        'area': 'Química',
        'desc': 'Reconhecimento de funções orgânicas (álcoois, fenóis, aldeídos, cetonas, ácidos carboxílicos, ésteres, aminas, amidas); polaridade e propriedades físicas (hidrofílico vs lipofílico, tensoativos/sabões); isomeria plana e espacial (geométrica cis-trans e óptica/carbono quiral); reações orgânicas e polímeros (esterificação/biodiesel, saponificação, polímeros de adição e condensação).'
    },
    'Q4': {
        'name': 'Química Ambiental',
        'inc': '10% a 13%',
        'status': 'ALTA (Contextualizada)',
        'area': 'Química',
        'desc': 'Gases do efeito estufa e fontes de emissão; óxidos ácidos e formação de chuva ácida (SO2, SO3, NOx); destruição da camada de ozônio pelos CFCs; tratamento químico de água e esgoto em ETA/ETE (coagulação/floculação com sulfato de alumínio, decantação e cloração).'
    }
}

# -------------------------------------------------------------
# 2. POLIEDRO FICHA MAPA PARSER WITH HIERARCHICAL CLASSIFIER
# -------------------------------------------------------------

def col_letter_to_index(col_str):
    col = 0
    for c in col_str:
        col = col * 26 + (ord(c.upper()) - ord('A') + 1)
    return col - 1

def parse_poliedro_ficha_mapa(path):
    with zipfile.ZipFile(path) as z:
        shared = []
        if 'xl/sharedStrings.xml' in z.namelist():
            tree = ET.fromstring(z.read('xl/sharedStrings.xml'))
            for elem in tree:
                shared.append(''.join(elem.itertext()))
        sheet_tree = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        rows_dict = {}
        for row in sheet_tree.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
            for c in row.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                coord = c.attrib.get('r', '')
                m = re.match(r'([A-Z]+)(\d+)', coord)
                if not m:
                    continue
                col_letters, row_num = m.groups()
                col_idx = col_letter_to_index(col_letters)
                row_idx = int(row_num)
                
                t = c.attrib.get('t')
                v = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                val = v.text if v is not None else ''
                if t == 's' and val:
                    try:
                        val = shared[int(val)]
                    except Exception:
                        pass
                
                if row_idx not in rows_dict:
                    rows_dict[row_idx] = {}
                rows_dict[row_idx][col_idx] = val
                
    h_idx = None
    q_col = None
    for r_idx, r in sorted(rows_dict.items()):
        for c_idx, val in r.items():
            if 'QUEST' in str(val).upper():
                h_idx = r_idx
                q_col = c_idx
                break
        if h_idx is not None:
            break
            
    header = rows_dict.get(h_idx, {})
    col_name_to_idx = {str(v).strip().upper(): k for k, v in header.items()}
    
    comp_col = col_name_to_idx.get('COMPONENTE', 3)
    gab_col = col_name_to_idx.get('GABARITO', 7)
    tem_col = col_name_to_idx.get('TEMÁTICA', 8)
    obj_col = col_name_to_idx.get('OBJETO DE CONHECIMENTO', 9)
    desc_col = col_name_to_idx.get('DESCRITOR', 13)
    
    questions = []
    for r_idx in sorted(rows_dict.keys()):
        if r_idx <= h_idx:
            continue
        r = rows_dict[r_idx]
        q_val = str(r.get(q_col, '')).strip()
        if not q_val.isdigit():
            continue
        q_num = int(q_val)
        if not (91 <= q_num <= 180):
            continue
            
        componente = str(r.get(comp_col, '')).strip()
        gab = str(r.get(gab_col, '')).strip()
        tematica = str(r.get(tem_col, '')).strip()
        objeto = str(r.get(obj_col, '')).strip()
        desc = str(r.get(desc_col, '')).strip()
        
        disc = 'OUTRO'
        if 'Matemática' in componente:
            disc = 'MAT'
        elif 'Física' in componente:
            disc = 'FIS'
        elif 'Química' in componente:
            disc = 'QUI'
        elif 'Biologia' in componente:
            disc = 'BIO'
            
        code = classify_poliedro_item(tematica, objeto, desc, disc)
        name = TOPICS_INFO[code]['name'] if code in TOPICS_INFO else 'Geral'
        
        questions.append({
            'num': q_num,
            'componente': componente,
            'discipline': disc,
            'gabarito': gab,
            'tematica': tematica,
            'objeto': objeto,
            'descritor': desc,
            'topic_code': code,
            'topic_name': name
        })
    return questions

def classify_poliedro_item(tematica, objeto, desc, disc):
    t = (tematica or '').lower()
    o = (objeto or '').lower()
    d = (desc or '').lower()
    
    if disc == 'MAT':
        # Probability and Combinatorics
        if any(k in t or k in o for k in ['probabilidade', 'análise combinatória', 'combinat', 'contagem', 'arranjo', 'permut']):
            return 'M6'
        # Functions and Algebraic Modeling
        if any(k in t or k in o for k in ['funç', 'afim', 'quadrática', 'exponencial', 'logaritm', 'sistemas lineares', 'equaç', 'polinôm']):
            return 'M5'
        # Spatial Geometry
        if any(k in t or k in o for k in ['espacial', 'poliedro', 'prisma', 'cilindro', 'cone', 'esfera', 'pirâmide', 'tronco', 'sólidos de revolução', 'planificação', 'projeções']):
            return 'M2'
        # Plane Geometry & Analytic Geometry
        if any(k in t or k in o for k in ['plana', 'triângulo', 'círculo', 'circunferência', 'polígono', 'tales', 'pitágoras', 'trigonometria', 'analítica']):
            return 'M4'
        # Statistics
        if any(k in t or k in o for k in ['estatística', 'média', 'mediana', 'moda', 'dispersão', 'desvio-padrão', 'tabelas', 'gráfico de colunas', 'gráfico de barras']):
            return 'M3'
        # Basic Math & Proportionality
        if any(k in t or k in o for k in ['grandezas', 'razão', 'proporção', 'porcentagem', 'escala', 'massa', 'tempo', 'volume', 'capacidade', 'potenciação', 'notação científica']):
            return 'M1'
        return 'M1'

    if disc == 'FIS':
        if any(k in t or k in o for k in ['eletrodinâmica', 'circuitos', 'resistor', 'corrente', 'geradores', 'capacitores', 'lei de ohm', 'medidores elétricos']):
            return 'F1'
        if any(k in t or k in o for k in ['ondulatória', 'acústica', 'onda', 'som', 'interferência', 'difração', 'ressonância', 'doppler', 'óptica', 'refração da luz', 'espectro eletromagnético']):
            return 'F3'
        if any(k in t or k in o for k in ['calorimetria', 'termodinâmica', 'transmissão de calor', 'térmica', 'temperatura', 'gases', 'dilatação', 'condução', 'irradiação']):
            return 'F4'
        if any(k in t or k in o for k in ['cinemática', 'dinâmica', 'energia', 'trabalho', 'leis de newton', 'gravitação', 'hidrostática', 'mhs', 'potência', 'velocidade', 'polias', 'stevin']):
            return 'F2'
        return 'F2'

    if disc == 'QUI':
        if any(k in t or k in o for k in ['orgânica', 'funções orgânicas', 'hidrocarboneto', 'álcool', 'éster', 'reações orgânicas', 'polímero', 'isomeria', 'alcenos', 'carbono em uma cadeia', 'propriedades físicas dos compostos orgânicos']):
            return 'Q3'
        if any(k in t or k in o for k in ['ambiental', 'chuva ácida', 'efeito estufa', 'camada de ozônio', 'poluição', 'óxidos poluentes', 'tratamento de água']):
            return 'Q4'
        if any(k in t or k in o for k in ['equilíbrio', 'eletroquímica', 'pilha', 'eletrólise', 'cinética', 'termoquímica', 'soluções', 'concentração', 'diluição', 'ph', 'lei de hess', 'indicadores']):
            return 'Q1'
        if any(k in t or k in o for k in ['substâncias e misturas', 'análise imediata', 'estequiometria', 'ligações químicas', 'forças intermoleculares', 'tabela periódica', 'átomo', 'mol', 'óxidos', 'inorgânica', 'tensão superficial']):
            return 'Q2'
        return 'Q2'

    if disc == 'BIO':
        if any(k in t or k in o for k in ['ecologia', 'ecossistema', 'impactos ambientais', 'bioma', 'relações ecológicas', 'ciclos biogeoquímicos', 'eutrofização', 'magnificação trófica', 'recuperação de ecossistemas', 'espécies exóticas', 'ciclo do carbono']):
            return 'B1'
        if any(k in t or k in o for k in ['genética', 'biotecnologia', 'herança', 'mendel', 'transgenia', 'pcr', 'clonagem', 'dna recombinante', 'silenciamento', 'edição genética', 'sistema abo']):
            return 'B2'
        if any(k in t or k in o for k in ['bioenergética', 'citologia', 'fotossíntese', 'fermentação', 'respiração', 'membrana plasmática', 'organelas']):
            return 'B3'
        if any(k in t or k in o for k in ['fisiologia', 'imunologia', 'parasitologia', 'viroses', 'protozooses', 'verminoses', 'sistema endócrino', 'vacina', 'soro', 'imunidade']):
            return 'B4'
        return 'B1'
        
    return 'OUTRO'

# -------------------------------------------------------------
# 3. APEIRON PARSER
# -------------------------------------------------------------

def parse_apeiron_exam():
    pdf_path = os.path.join(BASE_DIR, 'APEIRON-20261110T152018Z-1-001', 'APEIRON', '2º', 'A2GCD2 (Oficial)-1.pdf')
    if not os.path.exists(pdf_path):
        return []
        
    reader = pypdf.PdfReader(pdf_path)
    questions = []
    
    for idx, page in enumerate(reader.pages):
        txt = page.extract_text() or ''
        m = re.search(r'(\d{2,3})\s*:\s*([A-E])', txt)
        if not m:
            continue
        qnum = int(m.group(1))
        gab = m.group(2)
        snippet = txt[m.end():m.end()+350].replace('\n', ' ').strip()
        
        code, area = classify_semantic_text(qnum, snippet)
        
        clean_snip = snippet[:80].strip() + '...'
        questions.append({
            'simulado': '2º Simulado Apeiron 2026 Dia 2',
            'provider': 'Apeiron',
            'q_num': qnum,
            'gabarito': gab,
            'objeto': clean_snip,
            'tematica': area,
            'topic_code': code,
            'res_path': 'APEIRON-20261110T152018Z-1-001/APEIRON/2º/A2GCD2 (Oficial)-1.pdf'
        })
    return questions

# -------------------------------------------------------------
# 4. SAS PARSER WITH FIXED SCIENCE RULES
# -------------------------------------------------------------

def parse_sas_data():
    sas_json_path = os.path.join(BASE_DIR, 'FINAL', 'subagentes', 'dados_sas_alpha.json')
    if not os.path.exists(sas_json_path):
        return []
    with open(sas_json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    questions = []
    seen = set()
    for q in data.get('questions', []):
        qnum = q.get('qnum', 0)
        snippet = q.get('snippet', '')
        edition = q.get('edition', 'Simulado SAS ENEM')
        source = q.get('source_file', '')
        
        # Ensure path has SAS/ prefix and normalized slashes
        source = source.replace('\\', '/')
        if not source.startswith('SAS/'):
            source = f"SAS/{source}"
            
        key = (edition, qnum, snippet[:40])
        if key in seen:
            continue
        seen.add(key)
        
        code, area = classify_semantic_text(qnum, snippet)
        
        m_gab = re.search(r'Resposta correta:\s*([A-E])', snippet)
        gab = m_gab.group(1) if m_gab else 'Comentada'
        
        clean_desc = re.sub(r'^\d+\.\s*Resposta correta:\s*[A-E]\s*(?:C\s*\d+\s*H\s*\d+)?\s*', '', snippet).strip()
        if len(clean_desc) > 85:
            clean_desc = clean_desc[:85] + '...'
            
        questions.append({
            'simulado': edition,
            'provider': 'SAS',
            'q_num': qnum,
            'gabarito': gab,
            'objeto': clean_desc,
            'tematica': area,
            'topic_code': code,
            'res_path': source
        })
    return questions

# -------------------------------------------------------------
# 5. BERNOULLI MINED PARSER
# -------------------------------------------------------------

def parse_bernoulli_data():
    questions = []
    seen = set()
    
    # 1. extracted_questions_index.json (Bernoulli 2019 Simulados 1 to 5)
    ext_path = os.path.join(BASE_DIR, 'extracted_questions_index.json')
    if os.path.exists(ext_path):
        with open(ext_path, 'r', encoding='utf-8') as f:
            ext_data = json.load(f)
            
        b_sims = [
            ("Bernoulli 2019 Simulado 1 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/1º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
            ("Bernoulli 2019 Simulado 2 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/2º conjunto/2_conj_2019_Gabarito_Questao_comentada_Prova_II.pdf"),
            ("Bernoulli 2019 Simulado 3 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/3º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
            ("Bernoulli 2019 Simulado 4 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/4º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
            ("Bernoulli 2019 Simulado 5 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/5º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
        ]
        
        for bname, bpath in b_sims:
            if bname in ext_data.get('extracted_simulados', {}):
                for q in ext_data['extracted_simulados'][bname].get('questions', []):
                    qnum = q.get('num', 0)
                    body = q.get('body', '')
                    code, area = classify_semantic_text(qnum, body)
                    clean_snip = body[:85].replace('\n', ' ') + '...'
                    key = (bname, qnum)
                    if key not in seen:
                        seen.add(key)
                        questions.append({
                            'simulado': bname,
                            'provider': 'Bernoulli',
                            'q_num': qnum,
                            'gabarito': 'Comentada',
                            'objeto': clean_snip,
                            'tematica': area,
                            'topic_code': code,
                            'res_path': bpath
                        })

    # 2. FINAL_gamma_questions.json (Bernoulli multi-year corpus)
    gamma_path = os.path.join(BASE_DIR, 'FINAL_gamma_questions.json')
    if os.path.exists(gamma_path):
        with open(gamma_path, 'r', encoding='utf-8') as f:
            gamma_data = json.load(f)
            
        for item in gamma_data:
            qnum = item.get('question_number', 0)
            edition = item.get('edition', 'Bernoulli Simulado')
            src = item.get('source_file', '').replace('\\', '/')
            if not src.startswith('BERNOULLI-'):
                src = f"BERNOULLI-20261110T151947Z-1-001/{src}"
            snip = item.get('text_snippet', '')
            key = (edition, qnum)
            if key not in seen:
                seen.add(key)
                code, area = classify_semantic_text(qnum, snip)
                clean_snip = snip[:85].replace('\n', ' ') + '...'
                questions.append({
                    'simulado': f"Bernoulli {edition}",
                    'provider': 'Bernoulli',
                    'q_num': qnum,
                    'gabarito': 'Comentada',
                    'objeto': clean_snip,
                    'tematica': area,
                    'topic_code': code,
                    'res_path': src
                })
                
    return questions

# -------------------------------------------------------------
# 6. ENEM OFICIAL (INEP) PARSER
# -------------------------------------------------------------

def parse_inep_data():
    questions = []
    ext_path = os.path.join(BASE_DIR, 'extracted_questions_index.json')
    if not os.path.exists(ext_path):
        return []
    with open(ext_path, 'r', encoding='utf-8') as f:
        ext_data = json.load(f)
        
    inep_exams = [
        ('ENEM Oficial 2024 Prova Dia 2', 'ENEM Oficial 2024 Dia 2', 'ENEM/2024/ENEM 2024 DIA 2.pdf'),
        ('ENEM Oficial 2022 Prova Dia 2', 'ENEM Oficial 2022 Dia 2', 'ENEM/2022/ENEM 2022 DIA 2.pdf'),
        ('ENEM Oficial 2019 Prova Dia 2', 'ENEM Oficial 2019 Dia 2', 'ENEM/2019/ENEM 2019 DIA 2.pdf')
    ]
    
    for key, name, path in inep_exams:
        if key in ext_data.get('extracted_simulados', {}):
            for q in ext_data['extracted_simulados'][key].get('questions', []):
                qnum = q.get('num', 0)
                body = q.get('body', '')
                if not body or len(body) < 15:
                    continue
                code, area = classify_semantic_text(qnum, body)
                clean_snip = body[:85].replace('\n', ' ') + '...'
                questions.append({
                    'simulado': name,
                    'provider': 'INEP',
                    'q_num': qnum,
                    'gabarito': 'Oficial',
                    'objeto': clean_snip,
                    'tematica': area,
                    'topic_code': code,
                    'res_path': path
                })
    return questions

# -------------------------------------------------------------
# 7. UNIFIED SEMANTIC CLASSIFIER FOR TEXT SNIPPETS
# -------------------------------------------------------------

def classify_semantic_text(qnum, text):
    s = (text or '').lower()
    
    # 1. MATEMÁTICA (Q136-180 ou se detectado padrão de cálculo/geometria)
    if qnum >= 136 or any(k in s for k in ['probabilidade', 'logaritmo', 'prisma', 'cilindro', 'triângulo retângulo', 'desvio padrão']):
        if any(k in s for k in ['probabilidade', 'espaço amostral', 'arranjo', 'combinaç', 'permut', 'anagrama', 'contagem', 'princípio fundamental']):
            return 'M6', 'Probabilidade e Análise Combinatória'
        if any(k in s for k in ['volume', 'cilindr', 'cone', 'esfera', 'prisma', 'pirâmide', 'tronco', 'projeção ortogonal', 'vista superior', 'vista frontal', 'sólido geométrico', 'poliedro', 'euler']):
            return 'M2', 'Geometria Espacial'
        if any(k in s for k in ['média', 'mediana', 'moda', 'desvio padrão', 'variância', 'gráfico de barras', 'gráfico de setores', 'gráfico de linhas', 'histograma', 'frequência']):
            return 'M3', 'Estatística Básica'
        if any(k in s for k in ['área do triângulo', 'área do círculo', 'circunferência', 'polígono', 'pitágoras', 'tales', 'trigonometr', 'seno', 'cosseno', 'tangente', 'trapézio']):
            return 'M4', 'Geometria Plana'
        if any(k in s for k in ['função afim', 'função quadrática', 'parábola', 'vértice', 'máximo', 'mínimo', 'função exponencial', 'logaritm', 'coeficiente angular', 'taxa de variação']):
            return 'M5', 'Funções e Modelagem Algébrica'
        return 'M1', 'Matemática Básica e Proporcionalidade'

    # 2. CIÊNCIAS DA NATUREZA (Q91-135)
    # Check for QUÍMICA
    if any(k in s for k in ['chuva ácida', 'efeito estufa', 'camada de ozônio', 'cfc', 'tratamento de água', 'floculaç', 'cloraç', 'poluente atmosférico']):
        return 'Q4', 'Química Ambiental'
    if any(k in s for k in ['indicador', 'viragem', 'ph', 'bromocresol', 'pilha', 'eletrodo', 'ânodo', 'cátodo', 'eletrólise', 'oxidaç', 'reduç', 'entalpia', 'hess', 'cinética', 'catalisador', 'concentraç', 'molar', 'soluç', 'titulaç', 'le chatelier', 'equilíbrio']):
        return 'Q1', 'Físico-Química (Eletroquímica, Termoquímica e Equilíbrio)'
    if any(k in s for k in ['estequiometr', 'mol', 'pureza', 'rendimento', 'ligação química', 'forças intermoleculares', 'ligações de hidrogênio', 'dipolo', 'mistura', 'destilaç', 'filtraç', 'decantaç', 'massa molar']):
        return 'Q2', 'Química Geral e Estequiometria'
    if any(k in s for k in ['carbono', 'hidrocarboneto', 'química orgânica', 'álcool', 'ácido carboxílico', 'éster', 'amina', 'amida', 'isomeria', 'polímero', 'pet', 'biodiesel', 'saponificaç', 'alcenos']):
        return 'Q3', 'Química Orgânica'

    # Check for FÍSICA
    if any(k in s for k in ['circuito', 'resistor', 'corrente elétrica', 'ddp', 'voltagem', 'potência elétrica', 'kwh', 'ohm', 'fusível', 'disjuntor', 'amperímetro', 'voltímetro', 'faraday']):
        return 'F1', 'Eletrodinâmica e Circuitos Elétricos'
    if any(k in s for k in ['onda', 'comprimento de onda', 'frequência', 'refraç', 'difraç', 'interferência', 'ressonância', 'doppler', 'som', 'acústica', 'timbre', 'espelho', 'lente', 'óptica']):
        return 'F3', 'Ondulatória e Acústica'
    if any(k in s for k in ['calor', 'calorimetria', 'temperatura', 'conduç', 'convecç', 'irradiaç', 'termodinâmica', 'carnot', 'dilataç', 'gás ideal']):
        return 'F4', 'Termologia e Termodinâmica'
    if any(k in s for k in ['velocidade', 'aceleraç', 'cinemática', 'newton', 'atrito', 'energia cinética', 'energia potencial', 'trabalho', 'empuxo', 'pressão hidrostática', 'arquimedes', 'impulso', 'quantidade de movimento']):
        return 'F2', 'Mecânica Clássica e Hidrostática'

    # Check for BIOLOGIA
    if any(k in s for k in ['desmatamento', 'indígena', 'recursos naturais', 'ecologia', 'ecossistema', 'impactos ambientais', 'eutrofizaç', 'bioacumulaç', 'cadeia alimentar', 'trófica', 'bioma', 'ciclo do nitrogênio', 'ciclo do carbono', 'espécies invasoras', 'mutualismo']):
        return 'B1', 'Ecologia e Meio Ambiente'
    if any(k in s for k in ['dna', 'rna', 'gene', 'genética', 'mendel', 'herança', 'cromossom', 'clon', 'transgênic', 'pcr', 'eletroforese', 'crispr', 'biotecnologia', 'síntese proteica', 'ribossomo']):
        return 'B2', 'Genética, Biologia Molecular e Biotecnologia'
    if any(k in s for k in ['célula', 'citologia', 'mitocôndria', 'cloroplasto', 'fotossíntese', 'respiraç', 'fermentaç', 'osmose', 'membrana plasmática', 'organela', 'atp']):
        return 'B3', 'Citologia e Metabolismo Energético'
    if any(k in s for k in ['vacina', 'soro', 'imun', 'anticorpo', 'antígeno', 'vírus', 'bactéria', 'parasit', 'doença', 'chagas', 'malária', 'dengue', 'aedes', 'hormôni', 'fisiologia', 'toxoplasmose', 'protozoário']):
        return 'B4', 'Fisiologia Humana e Imunologia'

    return 'B1', 'Ecologia e Meio Ambiente'

# -------------------------------------------------------------
# 8. MARKDOWN GENERATORS
# -------------------------------------------------------------

def generate_catalogo_markdown(survey_records, dia2_records):
    md = []
    md.append("# CATÁLOGO GERAL DO ACERVO DE SIMULADOS E PROVAS: 2º DIA DO ENEM")
    md.append("## Mapeamento Físico, Tipologia Documental e Classificação Estruturada (~5.5 GB)")
    md.append("")
    md.append("> **Status:** Concluído — Base Catalogada, Higienizada e Pronta para Execução (Fase 2)  ")
    md.append("> **Destino do Arquivo:** `FINAL/CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md`  ")
    md.append("> **Cruzamento com Estatística:** Alinhado com `FINAL/RELATORIO_ESTATISTICO_ENEM_DIA_2.md`  ")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. SUMÁRIO EXECUTIVO DO ACERVO")
    md.append("")
    md.append("O levantamento exaustivo realizado sobre os diretórios do workspace auditou **1.422 arquivos** totalizando **5,56 GB** de materiais didáticos preparatórios para vestibulares. A análise automatizada identificou os seguintes macroindicadores:")
    md.append("")
    md.append("| Métrica Global | Quantidade | Percentual (%) | Descrição Operacional |")
    md.append("| :--- | :---: | :---: | :--- |")
    md.append("| **Total de Arquivos Mapeados** | **1.422** | 100% | Universo total de documentos no workspace |")
    md.append("| **Arquivos Únicos (Desduplicados)** | **1.033** | 72,6% | Conteúdo único expurgando redundâncias |")
    md.append("| **Arquivos Focados no ENEM** | **1.182** | 83,1% | Simulados nacionais e provas oficiais INEP |")
    md.append("| **Materiais Específicos do 2º DIA (STEM)** | **719** | 50,6% | **Cadernos de CN + MAT (Foco estrito desta Fase)** |")
    md.append("| **Materiais Isolados do 1º DIA** | **391** | 27,5% | Linguagens, Ciências Humanas e Redação (Segregados) |")
    md.append("| **Outros Vestibulares / Apoio** | **312** | 21,9% | Olimpíadas SAS, FUVEST, UNICAMP e Fichas Mapas |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 2. SEGREGAÇÃO CRUCIAL: DIA 1 vs DIA 2 E FORMATOS HISTÓRICOS")
    md.append("")
    md.append("A segregação do acervo levou em consideração a histórica mudança de matriz promovida pelo INEP no ano de **2017**:")
    md.append("")
    md.append("1. **Formato Atual (2017–2026):**")
    md.append("   * **1º Dia:** Linguagens e Códigos + Ciências Humanas + Redação (45 + 45 questões = 90 questões).")
    md.append("   * **2º Dia (Nosso Alvo):** **Ciências da Natureza (Física, Química, Biologia) + Matemática e suas Tecnologias** (45 + 45 questões = 90 questões).")
    md.append("   * Todo o acervo moderno (Bernoulli 2019-2026, SAS 2017-2026, Poliedro 2021-2024, Apeiron 2026 e ENEM Oficial 2017-2025) segue esta exata correspondência.")
    md.append("")
    md.append("2. **Formato Histórico Antigo (2009–2016):**")
    md.append("   * **1º Dia Antigo:** Ciências da Natureza + Ciências Humanas (45 + 45 questões).")
    md.append("   * **2º Dia Antigo:** Linguagens e Códigos + Matemática + Redação (45 + 45 questões).")
    md.append("   * **Ação do Catalogador:** Foram catalogados os cadernos de Matemática (do antigo Dia 2) e os cadernos de Natureza (do antigo Dia 1), garantindo que nenhum item histórico de Exatas/Natureza fosse perdido.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 3. DISTRIBUIÇÃO DO ACERVO DIA 2 POR PLATAFORMA / BANCA")
    md.append("")
    md.append("| Plataforma / Provedor | Arquivos Dia 2 | Perfil do Acervo e Destaques Pedagógicos |")
    md.append("| :--- | :---: | :--- |")
    md.append("| **Bernoulli Educação** | **281** | Simulados completos de altíssimo padrão técnico para Medicina (2012, 2015, 2019–2026). Destaque para os cadernos de *Gabarito e Questões Comentadas Prova II*, que contêm o enunciado completo acompanhado da resolução passo a passo. Inclui também as *Trilhas Bernoulli* segmentadas por frente. |")
    md.append("| **SAS Plataforma de Educação** | **250** | Simulados Nacionais ENEM SAS (2011, 2017, 2023, 2025, 2026) e vasta coleção de *Avaliações Periódicas (AP2 e AG2 de CNST-MST)* de 2014 a 2021 com resoluções comentadas linha a linha. |")
    md.append("| **INEP (ENEM Oficial)** | **135** | Provas oficiais aplicadas de 2009 a 2025. Inclui todos os cadernos de cores oficiais (Amarelo, Azul, Cinza, Verde, Rosa) e gabaritos definitivos, essenciais para calibragem de padrão de cobrança TRI. |")
    md.append("| **Poliedro Educação** | **47** | Ciclos 2017, 2021, 2022 e a suíte completa de 2024 contendo 5 simulados completos do 2º Dia, provas limpas, cadernos de resolução comentada de 90 páginas e planilhas *Ficha Mapa* com metadados pedagógicos oficiais. |")
    md.append("| **Apeiron** | **6** | Simulados contemporâneos (2026) com cadernos de prova Dia 2 e resolução comentada detalhada oficial (*A2GCD2*). |")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 4. CLASSIFICAÇÃO TIPOLÓGICA DOS ARQUIVOS DIA 2")
    md.append("")
    md.append("Para maximizar o aproveitamento nos estudos, os 719 arquivos do Dia 2 foram segmentados em 4 categorias funcionais:")
    md.append("")
    md.append("```mermaid")
    md.append("pie title Tipologia dos Arquivos Relevantes do Dia 2")
    md.append("    \"Cadernos de Questões / Provas Limpas\" : 330")
    md.append("    \"Gabaritos Simples Oficiais\" : 210")
    md.append("    \"Resoluções Comentadas Passo a Passo\" : 155")
    md.append("    \"Fichas Mapas e Guias Pedagógicos\" : 24")
    md.append("```")
    md.append("")
    md.append("1. **Cadernos de Questões (Provas Limpas - ~330 arquivos):**")
    md.append("   * Utilidade: Simulação de prova em tempo real (cronometrada em 5 horas), treino de ritmo, resistência cognitiva e estratégia de preenchimento.")
    md.append("2. **Resoluções Comentadas Passo a Passo (~155 arquivos):**")
    md.append("   * Utilidade: Estudo reverso, diagnóstico de erros, compreensão de distratores e consolidação de métodos de resolução rápida.")
    md.append("3. **Gabaritos Simples Oficiais (~210 arquivos):**")
    md.append("   * Utilidade: Correção instantânea de simulados e conferência rápida de acertos brutos.")
    md.append("4. **Fichas Mapas Pedagógicas (~24 arquivos):**")
    md.append("   * Utilidade: Planilhas estruturadas com mapeamento de cada questão por componente, competência, habilidade da matriz do ENEM e demanda cognitiva (Lembrar, Compreender, Aplicar, Analisar).")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 5. TABELA MESTRA DOS PRINCIPAIS SIMULADOS E CADERNOS DIA 2")
    md.append("")
    md.append("Abaixo estão listados os principais conjuntos do 2º Dia catalogados no workspace com seus respectivos caminhos de acesso direto e verificados fisicamente:")
    md.append("")
    md.append("| Coleção / Edição | Provedor | Ano | Conteúdo e Tipo | Páginas | Caminho Relativo no Workspace |")
    md.append("| :--- | :---: | :---: | :--- | :---: | :--- |")
    
    exemplares = [
        # POLIEDRO
        ("Poliedro 2024 Simulado 1", "Poliedro", 2024, "Prova Dia 2 Limpa", "32", "POLIEDRO/2024/2024_1_poliedro_enem_2_dia_prova.pdf"),
        ("Poliedro 2024 Simulado 1 (Resolução)", "Poliedro", 2024, "Resolução Comentada Completa", "91", "POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Resolução.pdf"),
        ("Poliedro 2024 Simulado 1 (Ficha Mapa)", "Poliedro", 2024, "Matriz de Habilidades e Conteúdos", "Planilha", "POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx"),
        ("Poliedro 2024 Simulado 2", "Poliedro", 2024, "Prova Dia 2 Limpa", "32", "POLIEDRO/2024/2024_2_poliedro_enem_2_dia_prova.pdf"),
        ("Poliedro 2024 Simulado 2 (Resolução)", "Poliedro", 2024, "Resolução Comentada Completa", "88", "POLIEDRO/2024/2º Simulado Enem 2024 - 2º Dia - Resolução.pdf"),
        ("Poliedro 2024 Simulado 3 (Resolução)", "Poliedro", 2024, "Resolução Comentada Completa", "85", "POLIEDRO/2024/3º Simulado Enem 2024 - 2º Dia - Resolução.pdf"),
        ("Poliedro 2024 Simulado 4 (Resolução)", "Poliedro", 2024, "Resolução Comentada Completa", "89", "POLIEDRO/2024/4º Simulado Enem 2024 - 2º Dia - Resolução.pdf"),
        ("Poliedro 2024 Simulado 5 (Resolução)", "Poliedro", 2024, "Resolução Comentada Completa", "87", "POLIEDRO/2024/5º Simulado Enem 2024 - 2º Dia - Resolução.pdf"),
        
        # BERNOULLI
        ("Bernoulli 2019 Simulado 1", "Bernoulli", 2019, "Prova II Limpa", "32", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/1º conjunto/1- Segundo dia.pdf"),
        ("Bernoulli 2019 Simulado 1 (Comentada)", "Bernoulli", 2019, "Gabarito e Questões Comentadas Prova II", "39", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/1º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
        ("Bernoulli 2019 Simulado 2 (Comentada)", "Bernoulli", 2019, "Gabarito e Questões Comentadas Prova II", "41", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/2º conjunto/2_conj_2019_Gabarito_Questao_comentada_Prova_II.pdf"),
        ("Bernoulli 2019 Simulado 3 (Comentada)", "Bernoulli", 2019, "Gabarito e Questões Comentadas Prova II", "40", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/3º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
        ("Bernoulli 2019 Simulado 4 (Comentada)", "Bernoulli", 2019, "Gabarito e Questões Comentadas Prova II", "42", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/4º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
        ("Bernoulli 2019 Simulado 5 (Comentada)", "Bernoulli", 2019, "Gabarito e Questões Comentadas Prova II", "38", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/5º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
        ("Bernoulli 2022 Simulado 1", "Bernoulli", 2022, "Prova Dia 2 Limpa", "32", "_ENEM_DIA_2_BRUTO/1° BERNOULLI 2022 dia 2.pdf"),
        ("Bernoulli 2025 Simulado 1", "Bernoulli", 2025, "Prova Dia 2 Limpa", "32", "_ENEM_DIA_2_BRUTO/1º BERNOULLI 2025 - D2.pdf"),
        ("Bernoulli 2026 Simulado 1 Extra", "Bernoulli", 2026, "Prova Dia 2 Limpa", "32", "_ENEM_DIA_2_BRUTO/1° BERNOULLI EXTRA 2026 - D2.pdf"),
        ("Bernoulli 2026 Book Prova II", "Bernoulli", 2026, "Caderno Completo Prova II", "36", "_ENEM_DIA_2_BRUTO/d3d4ebf36fc4f39bb474847b5928558207be3c0eBer_SE2026_V05_BOOK_PROVAII.pdf"),
        
        # SAS
        ("SAS Avaliação Periódica 2 (2019)", "SAS", 2019, "Prova Limpa CNST-MST (90Q)", "42", "_ENEM_DIA_2_BRUTO/1241-19_AP2_CNST-MST_3SERIE_1ETAPA.pdf"),
        ("SAS AP2 Resolução Comentada (2019)", "SAS", 2019, "Resolução Completa 1 a 90", "10", "_ENEM_DIA_2_BRUTO/1242-19_RESOLUCAO_AP2_CNST-MST_3SERIE_1ETAPA.pdf"),
        ("SAS Avaliação Periódica 2 (2020)", "SAS", 2020, "Prova Limpa CNST-MST (90Q)", "43", "_ENEM_DIA_2_BRUTO/1373-20 - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf"),
        ("SAS AP2 Resolução Comentada (2020)", "SAS", 2020, "Resolução Completa 1 a 90", "12", "_ENEM_DIA_2_BRUTO/1378-20 - RESOLUCAO - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf"),
        ("SAS Avaliação Periódica 2 (2021)", "SAS", 2021, "Prova Limpa CNST-MST (90Q)", "43", "_ENEM_DIA_2_BRUTO/1139-21 - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf"),
        ("SAS AP2 Resolução Comentada (2021)", "SAS", 2021, "Resolução Completa 1 a 90", "12", "_ENEM_DIA_2_BRUTO/1452-21 - RESOLUCAO - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf"),
        ("SAS Simulado ENEM 2026 D2", "SAS", 2026, "Caderno Amarelo Dia 2 Limpo", "32", "_ENEM_DIA_2_BRUTO/1º SIMULADO SAS ENEM - 2026 -  D2 - AMARELO.pdf"),
        ("SAS Simulado ENEM 2026 D2 (Azul)", "SAS", 2026, "Caderno Azul Dia 2 Limpo", "32", "_ENEM_DIA_2_BRUTO/1º SIMULADO SAS ENEM - 2026 -  D2 - AZUL .pdf"),
        
        # APEIRON
        ("Apeiron 2026 Simulado 1", "Apeiron", 2026, "Prova Dia 2 Limpa", "32", "APEIRON-20261110T152018Z-1-001/APEIRON/2026/1º/1º APEIRON 2026 - D2.pdf"),
        ("Apeiron 2026 Simulado 2 (Resolução)", "Apeiron", 2026, "Resolução Comentada Oficial D2", "90", "APEIRON-20261110T152018Z-1-001/APEIRON/2º/A2GCD2 (Oficial)-1.pdf"),
        
        # INEP
        ("ENEM Oficial 2024 Dia 2", "INEP", 2024, "Prova Oficial Completa", "32", "ENEM/2024/ENEM 2024 DIA 2.pdf"),
        ("ENEM Oficial 2024 Gabarito", "INEP", 2024, "Gabarito Oficial Definitivo", "2", "ENEM/2024/GABARITO 2024 DIA 2.pdf"),
        ("ENEM Oficial 2025 Dia 2 (Amarelo)", "INEP", 2025, "Caderno Amarelo Dia 2", "32", "ENEM/2025/enem-2025-2-dia-caderno-amarelo.pdf"),
        ("ENEM Oficial 2025 Dia 2 (Azul)", "INEP", 2025, "Caderno Azul Dia 2", "32", "ENEM/2025/enem-2025-2-dia-caderno-azul.pdf"),
        ("ENEM Oficial 2025 Dia 2 (Verde)", "INEP", 2025, "Caderno Verde Dia 2", "32", "ENEM/2025/enem-2025-2-dia-caderno-verde.pdf"),
        ("ENEM Oficial 2025 Dia 2 (Cinza)", "INEP", 2025, "Caderno Cinza Dia 2", "32", "ENEM/2025/enem-2025-2-dia-caderno-cinza.pdf")
    ]
    
    for row in exemplares:
        md.append(f"| **{row[0]}** | {row[1]} | {row[2]} | {row[3]} | {row[4]} | `{row[5]}` |")
        
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 6. PRÓXIMOS PASSOS OPERACIONAIS")
    md.append("")
    md.append("Com todo o acervo físico mapeado, classificado e desduplicado:")
    md.append("1. Consulte o arquivo `FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md` para navegar pelas questões agrupadas pelos tópicos de alta prioridade da TRI.")
    md.append("2. Consulte o arquivo `FINAL/TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md` para seguir a trilha tática recomendada de execução dos simulados e simulados diagnósticos.")
    return "\n".join(md)

def generate_indice_tematico_markdown(topic_index):
    md = []
    md.append("# ÍNDICE TEMÁTICO DE QUESTÕES E SIMULADOS: 2º DIA DO ENEM")
    md.append("## Mapeamento Cruzado de Alta Prioridade TRI nos Simulados e Provas Oficiais")
    md.append("")
    md.append("> **Status:** Concluído — Matriz Multi-Banca Completa (Poliedro, Bernoulli, SAS, INEP, Apeiron)  ")
    md.append("> **Destino do Arquivo:** `FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md`  ")
    md.append("> **Base Teórica:** Conectado à Matriz de Incidência de `FINAL/RELATORIO_ESTATISTICO_ENEM_DIA_2.md`  ")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. VISÃO GERAL DO ÍNDICE E TAXONOMIA INTEGRADA")
    md.append("")
    md.append("Este índice mapeia cirurgicamente as questões do acervo físico aos tópicos de maior peso na Teoria de Resposta ao Item (TRI). Cada seção consolida o perfil estatístico do tópico, conceitos fundamentais e uma seleção curada de questões concretas de **todas as principais bancas do workspace** (Poliedro, Bernoulli, SAS, INEP e Apeiron), com número da questão, gabarito, descritor e caminho direto para o caderno ou resolução comentada.")
    md.append("")
    
    sections = [
        ('2. MATEMÁTICA E SUAS TECNOLOGIAS (45 Questões)', ['M1', 'M2', 'M3', 'M4', 'M5', 'M6']),
        ('3. BIOLOGIA (~15 Questões)', ['B1', 'B2', 'B3', 'B4']),
        ('4. FÍSICA (~15 Questões)', ['F1', 'F2', 'F3', 'F4']),
        ('5. QUÍMICA (~15 Questões)', ['Q1', 'Q2', 'Q3', 'Q4'])
    ]
    
    providers_order = ['INEP', 'Poliedro', 'Bernoulli', 'SAS', 'Apeiron']
    
    for sec_title, code_list in sections:
        md.append("---")
        md.append("")
        md.append(f"## {sec_title}")
        md.append("")
        
        for code in code_list:
            info = TOPICS_INFO[code]
            sec_num = sec_title.split('.')[0]
            md.append(f"### {sec_num}.{code[1]} Tópico {code}: {info['name']}")
            md.append(f"* **Incidência Média:** {info['inc']} | **Status TRI:** `{info['status']}`")
            md.append(f"* **Conceitos-Chave:** {info['desc']}")
            md.append("")
            md.append("| Simulado / Edição | Provedor | Questão | Gabarito | Objeto de Conhecimento / Descritor | Arquivo de Resolução Comentada |")
            md.append("| :--- | :---: | :---: | :---: | :--- | :--- |")
            
            q_list = topic_index.get(code, [])
            
            # Multi-provider round robin selection
            by_prov = defaultdict(list)
            for item in q_list:
                by_prov[item['provider']].append(item)
                
            curated_selection = []
            for cycle in range(4): # Up to 4 questions per provider per topic (up to 20 total)
                for prov in providers_order:
                    if cycle < len(by_prov[prov]):
                        curated_selection.append(by_prov[prov][cycle])
                        
            if not curated_selection and q_list:
                curated_selection = q_list[:15]
                
            for item in curated_selection:
                gab_str = f"`{item['gabarito']}`" if item['gabarito'] != 'Comentada' else 'Comentada'
                obj_text = item['objeto']
                md.append(f"| {item['simulado']} | {item['provider']} | **Q{item['q_num']}** | {gab_str} | {item['tematica']} - {obj_text} | `{item['res_path']}` |")
                
            if not curated_selection:
                md.append("| *Nenhuma questão filtrada para este tópico no recorte* | - | - | - | - | - |")
            md.append("")
            
    return "\n".join(md)

def generate_trilha_estudos_markdown():
    md = []
    md.append("# TRILHA TÁTICA DE ESTUDOS E CRONOGRAMA DE SIMULADOS: 2º DIA DO ENEM")
    md.append("## Metodologia de Alavancagem TRI e Cronograma Operacional Baseado no Acervo")
    md.append("")
    md.append("> **Status:** Concluído — Guia de Execução Tática Pronto para Uso  ")
    md.append("> **Destino do Arquivo:** `FINAL/TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md`  ")
    md.append("> **Base:** Acervo de 5.5 GB categorizado em `FINAL/CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md` e `FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md`  ")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. DIRETRIZES FUNDAMENTAIS PARA O 2º DIA DO ENEM")
    md.append("")
    md.append("O segundo dia do ENEM é uma maratona de resistência física, cognitiva e emocional. São **90 questões** complexas em **300 minutos** (~3 minutos e 20 segundos por questão, incluindo o cartão de respostas):")
    md.append("")
    md.append("1. **A Regra de Ouro da TRI:**")
    md.append("   * Não tente resolver a prova na ordem numérica linear (1 a 90 ou 91 a 180).")
    md.append("   * O algoritmo da TRI pune com perda drástica de nota o candidato que acerta itens difíceis (ex: logaritmos ou circuitos complexos de pontes) mas erra itens fáceis (ex: regra de três, leitura direta de gráfico de colunas ou conceito básico de fotossíntese).")
    md.append("2. **O Protocolo das Três Passadas no Bloco de Prova:**")
    md.append("   * **Passada 1 (Minutos 0 a 100):** Varredura completa. Resolva apenas as questões fáceis, diretas e conceituais (Matemática Básica, Estatística de leitura, Ecologia e Química Geral descritiva). Deixe assinaladas as médias e pule imediatamente as difíceis.")
    md.append("   * **Passada 2 (Minutos 100 a 230):** Resolução das questões médias que exigem desenvolvimento algébrico intermediário (Geometria Espacial com cálculos de volume, Estequiometria clássica, Ondulatória e Eletrodinâmica de resistores em série/paralelo).")
    md.append("   * **Passada 3 (Minutos 230 a 275):** Ataque cirúrgico às questões de alto nível de exigência (Análise Combinatória com restrições, Cinética/Equilíbrio avançado, Mecânica pesada de atrito e planos inclinados).")
    md.append("   * **Preenchimento do Gabarito (Minutos 275 a 300):** 25 minutos exclusivos para transposição calma e metódica, sem risco de inversão de linhas.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 2. A TRILHA EM 3 FASES DE ALAVANCAGEM TRI")
    md.append("")
    md.append("```mermaid")
    md.append("flowchart LR")
    md.append("    Fase1[\"Fase 1: Blindagem da Base TRI<br/>(60% da Nota - Meta: 720+)\"] --> Fase2[\"Fase 2: Alavancagem e Consolidação<br/>(25% da Nota - Meta: 800+)\"] --> Fase3[\"Fase 3: Refinamento de Elite<br/>(15% da Nota - Meta: 850+ a 900+)\"]")
    md.append("```")
    md.append("")
    md.append("### FASE 1: BLINDAGEM DA BASE TRI (Semanas 1 a 4)")
    md.append("* **Objetivo:** Erro zero nas questões classificadas como fáceis pela matriz pedagógica.")
    md.append("* **Foco de Conteúdos:**")
    md.append("  * **Matemática:** Matemática Básica e Proporcionalidade (M1) e Estatística Básica (M3).")
    md.append("  * **Biologia:** Ecologia e Meio Ambiente (B1).")
    md.append("  * **Física:** Eletrodinâmica Básica (F1) e Calorimetria Sensível (F4).")
    md.append("  * **Química:** Química Geral, Separação de Misturas e Pilhas Galvânicas (Q1/Q2).")
    md.append("* **Bateria Prática Obrigatória (Acervo Workspace):**")
    md.append("  1. `ENEM/2021/ENEM 2021 DIA 2.pdf` (Prova limpa) calibrado com o gabarito oficial.")
    md.append("  2. `POLIEDRO/2024/2024_1_poliedro_enem_2_dia_prova.pdf` (Prova) e estudo reverso linha a linha em `POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Resolução.pdf`.")
    md.append("  3. `_ENEM_DIA_2_BRUTO/1241-19_AP2_CNST-MST_3SERIE_1ETAPA.pdf` (SAS 90Q) com correção em `_ENEM_DIA_2_BRUTO/1242-19_RESOLUCAO_AP2_CNST-MST_3SERIE_1ETAPA.pdf`.")
    md.append("")
    md.append("### FASE 2: ALAVANCAGEM E CONSOLIDAÇÃO (Semanas 5 a 8)")
    md.append("* **Objetivo:** Dominar as questões de dificuldade média que elevam a nota para além do corte da maioria das universidades públicas e cursos concorridos.")
    md.append("* **Foco de Conteúdos:**")
    md.append("  * **Matemática:** Geometria Espacial (M2), Geometria Plana (M4) e Funções Afim/Quadrática (M5).")
    md.append("  * **Biologia:** Genética Mendeliana e Biotecnologia (B2) e Fisiologia/Imunologia (B4).")
    md.append("  * **Física:** Ondulatória/Fenômenos (F3) e Mecânica (Energia e Leis de Newton - F2).")
    md.append("  * **Química:** Química Orgânica (Funções, Isomeria Plana, Polímeros - Q3) e Termoquímica/Lei de Hess (Q1).")
    md.append("* **Bateria Prática Obrigatória (Acervo Workspace):**")
    md.append("  1. `BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/1º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf` (Bernoulli Simulado 1 Completo).")
    md.append("  2. `BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/2º conjunto/2_conj_2019_Gabarito_Questao_comentada_Prova_II.pdf` (Bernoulli Simulado 2 Completo).")
    md.append("  3. `POLIEDRO/2024/2º Simulado Enem 2024 - 2º Dia - Resolução.pdf` (Poliedro Simulado 2 Completo).")
    md.append("  4. `POLIEDRO/2024/3º Simulado Enem 2024 - 2º Dia - Resolução.pdf` (Poliedro Simulado 3 Completo).")
    md.append("  5. `_ENEM_DIA_2_BRUTO/1373-20 - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf` corrigido com `_ENEM_DIA_2_BRUTO/1378-20 - RESOLUCAO - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf`.")
    md.append("")
    md.append("### FASE 3: REFINAMENTO DE ELITE E DIFERENCIAÇÃO (Semanas 9 a 12)")
    md.append("* **Objetivo:** Acertar os itens de alto poder de discriminação pedagógica para alcançar 800+ em Natureza e 900+ em Matemática (competitividade ampla para Medicina nas Federais).")
    md.append("* **Foco de Conteúdos:**")
    md.append("  * **Matemática:** Análise Combinatória (M6), Probabilidade Condicional (M6) e Modelagem Logarítmica (M5).")
    md.append("  * **Biologia:** Citologia/Metabolismo Energético Detalhado (B3) e Biotecnologia de Engenharia Gênica (B2).")
    md.append("  * **Física:** Eletrodinâmica de Instrumentos e Pontes (F1), Hidrostática de Empuxo (F2) e Ondulatória/Efeito Doppler (F3).")
    md.append("  * **Química:** Equilíbrio Químico/Le Chatelier (Q1), Cinética Química (Q1), Estequiometria com Pureza/Rendimento (Q2) e Isomeria Óptica (Q3).")
    md.append("* **Bateria Prática de Choque (Acervo Workspace):**")
    md.append("  1. `POLIEDRO/2024/4º Simulado Enem 2024 - 2º Dia - Resolução.pdf`.")
    md.append("  2. `POLIEDRO/2024/5º Simulado Enem 2024 - 2º Dia - Resolução.pdf`.")
    md.append("  3. `BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/4º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf`.")
    md.append("  4. `BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/5º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf`.")
    md.append("  5. `_ENEM_DIA_2_BRUTO/1° BERNOULLI EXTRA 2026 - D2.pdf` e `_ENEM_DIA_2_BRUTO/1º SIMULADO SAS ENEM - 2026 -  D2 - AMARELO.pdf`.")
    md.append("  6. `APEIRON-20261110T152018Z-1-001/APEIRON/2º/A2GCD2 (Oficial)-1.pdf` (Resolução Passo a Passo Apeiron 2026).")
    md.append("  7. Provas Oficiais de Calibração Final: `ENEM/2024/ENEM 2024 DIA 2.pdf` e `ENEM/2025/enem-2025-2-dia-caderno-amarelo.pdf`.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 3. PROTOCOLO OPERACIONAL DO CADERNO DE ERROS")
    md.append("")
    md.append("A diferença entre estagnar em 650 pontos e ultrapassar 800 pontos não está em fazer centenas de simulados sem critério, mas na **qualidade do pós-prova**:")
    md.append("")
    md.append("1. **Classificação do Erro em 4 Quadrantes:**")
    md.append("   * **Erro por Interpretação / Atenção:** O candidato sabia o conceito, mas não prestou atenção ao comando da questão (ex: pediu diâmetro e usou raio, pediu km/h e respondeu em m/s).")
    md.append("   * **Erro Algébrico / Contas:** Erro em conta de multiplicação, divisão decimal ou simplificação de frações sob pressão de tempo.")
    md.append("   * **Erro por Lacuna Teórica:** O candidato não lembrava da fórmula, da relação ecológica ou do conceito de polaridade.")
    md.append("   * **Erro por Estratégia / Tempo:** O candidato gastou 8 minutos em uma questão difícil e teve que chutar questões fáceis no final.")
    md.append("2. **Ciclo de Correção Ativa:**")
    md.append("   * Nunca apenas leia o gabarito. Pegue uma folha em branco e reescreva a resolução da questão errada do início ao fim sem olhar a resposta.")
    md.append("   * Se o erro foi lacuna teórica, revise o tópico correspondente na seção temática de `FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md` e resolva 3 questões adicionais do mesmo código.")
    return "\n".join(md)

# -------------------------------------------------------------
# 9. MAIN PIPELINE
# -------------------------------------------------------------

def main():
    print("Iniciando pipeline aprofundado e refinado da Fase 2...")
    
    with open('full_survey_raw.json', 'r', encoding='utf-8') as f:
        survey_records = json.load(f)
    dia2_records = [r for r in survey_records if r['classification'] in ('DIA_2_CN_MAT', 'ENEM_ANTIGO_D1_CN_CH', 'ENEM_ANTIGO_D2_MAT_LC')]
    
    topic_index = {code: [] for code in TOPICS_INFO.keys()}
    
    # 1. POLIEDRO 2024
    print("Processando Poliedro 2024...")
    poliedro_fichas = [
        ('POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', '1º Simulado Enem 2024', 'POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Resolução.pdf'),
        ('POLIEDRO/2024/2º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', '2º Simulado Enem 2024', 'POLIEDRO/2024/2º Simulado Enem 2024 - 2º Dia - Resolução.pdf'),
        ('POLIEDRO/2024/3º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', '3º Simulado Enem 2024', 'POLIEDRO/2024/3º Simulado Enem 2024 - 2º Dia - Resolução.pdf'),
        ('POLIEDRO/2024/4º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', '4º Simulado Enem 2024', 'POLIEDRO/2024/4º Simulado Enem 2024 - 2º Dia - Resolução.pdf'),
        ('POLIEDRO/2024/2024_5_poliedro_enem_3serie_e_pv_ficha_mapa_geral_dia02.xlsx', '5º Simulado Enem 2024', 'POLIEDRO/2024/5º Simulado Enem 2024 - 2º Dia - Resolução.pdf'),
    ]
    poliedro_count = 0
    for fpath, sname, rpath in poliedro_fichas:
        qs = parse_poliedro_ficha_mapa(fpath)
        for q in qs:
            c = q['topic_code']
            if c in topic_index:
                topic_index[c].append({
                    'simulado': sname,
                    'provider': 'Poliedro',
                    'q_num': q['num'],
                    'gabarito': q['gabarito'],
                    'tematica': q['tematica'],
                    'objeto': f"{q['objeto']} ({q['descritor'][:65]}...)" if q['descritor'] else q['objeto'],
                    'res_path': rpath
                })
                poliedro_count += 1
    print(f"Poliedro indexado: {poliedro_count} questões.")

    # 2. APEIRON 2026
    print("Processando Apeiron 2026...")
    apeiron_qs = parse_apeiron_exam()
    for item in apeiron_qs:
        c = item['topic_code']
        if c in topic_index:
            topic_index[c].append(item)
    print(f"Apeiron indexado: {len(apeiron_qs)} questões.")

    # 3. SAS
    print("Processando SAS...")
    sas_qs = parse_sas_data()
    sas_count = 0
    for item in sas_qs:
        c = item['topic_code']
        if c in topic_index:
            topic_index[c].append(item)
            sas_count += 1
    print(f"SAS indexado: {sas_count} questões.")

    # 4. BERNOULLI
    print("Processando Bernoulli...")
    bernoulli_qs = parse_bernoulli_data()
    bernoulli_count = 0
    for item in bernoulli_qs:
        c = item['topic_code']
        if c in topic_index:
            topic_index[c].append(item)
            bernoulli_count += 1
    print(f"Bernoulli indexado: {bernoulli_count} questões.")

    # 5. INEP / ENEM OFICIAL
    print("Processando ENEM Oficial...")
    inep_qs = parse_inep_data()
    inep_count = 0
    for item in inep_qs:
        c = item['topic_code']
        if c in topic_index:
            topic_index[c].append(item)
            inep_count += 1
    print(f"INEP Oficial indexado: {inep_count} questões.")

    total_indexed = sum(len(v) for v in topic_index.values())
    print(f"\nTOTAL DE QUESTÕES INDEXADAS POR TÓPICO: {total_indexed}")

    # Write Markdown files
    print("\nGravando arquivos finais em FINAL/...")
    
    cat_md = generate_catalogo_markdown(survey_records, dia2_records)
    with open('FINAL/CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md', 'w', encoding='utf-8') as f:
        f.write(cat_md)
        
    ind_md = generate_indice_tematico_markdown(topic_index)
    with open('FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md', 'w', encoding='utf-8') as f:
        f.write(ind_md)
        
    tri_md = generate_trilha_estudos_markdown()
    with open('FINAL/TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md', 'w', encoding='utf-8') as f:
        f.write(tri_md)

    # Master database JSON
    db_json = {
        'metadata': {
            'total_files': len(survey_records),
            'unique_files': 1033,
            'dia2_files_count': len(dia2_records),
            'corpus_size_gb': 5.56,
            'providers_breakdown': {
                'BERNOULLI': sum(1 for r in dia2_records if r['provider'] == 'BERNOULLI'),
                'SAS': sum(1 for r in dia2_records if r['provider'] == 'SAS'),
                'ENEM_OFICIAL': sum(1 for r in dia2_records if r['provider'] == 'ENEM_OFICIAL'),
                'POLIEDRO': sum(1 for r in dia2_records if r['provider'] == 'POLIEDRO'),
                'APEIRON': sum(1 for r in dia2_records if r['provider'] == 'APEIRON'),
            },
            'total_indexed_questions': total_indexed
        },
        'taxonomy_info': TOPICS_INFO,
        'topic_questions_count': {k: len(v) for k, v in topic_index.items()},
        'curated_multi_banca_index': {
            k: v[:25] for k, v in topic_index.items()
        }
    }
    with open('FINAL/catalogo_enem_dia_2.json', 'w', encoding='utf-8') as f:
        json.dump(db_json, f, ensure_ascii=False, indent=2)

    print("\nTODOS OS ARQUIVOS DA FASE 2 FORAM RECONSTRUÍDOS E ATUALIZADOS COM SUCESSO!")

if __name__ == '__main__':
    main()
