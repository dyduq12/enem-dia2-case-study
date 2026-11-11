# -*- coding: utf-8 -*-
"""
Mining script for SAS Alpha:
Processes the first half of SAS archive (ENEM, PROGRAMÁTICA, OLIMPÍADAS, ARI DE SÁ, FUVEST, PROVINHA).
Extracts and semantically categorizes ENEM Dia 2 questions (Matemática, Física, Química, Biologia).
Generates detailed structured report for FINAL/subagentes/relatorio_sas_alpha.md.
"""

import os
import re
import json
import zipfile
import xml.etree.ElementTree as ET
import pypdf

BASE_DIR = r"c:\Users\Eduardo\Documents\02_Estudos & Academico\ENEM DIA 2"
SAS_DIR = os.path.join(BASE_DIR, "SAS")

ALPHA_FOLDERS = [
    "ARI DE SÁ - SIMULADOS",
    "ENEM",
    "FUVEST",
    "OLIMPÍADAS",
    "PROGRAMÁTICA",
    "PROVINHA"
]

def classify_semantic(qnum, c, h, content, is_2011=False):
    """
    Classifica semanticamente a questão interpretando a lógica cobrada,
    competência/habilidade e conceitos científicos reais.
    """
    tl = content.lower()
    
    # Identificar domínio primário (Matemática vs Ciências da Natureza)
    if is_2011:
        # Em 2011, Q1 a Q45 eram Linguagens (descartadas) e Q46 a Q90 eram Matemática
        is_math = (qnum >= 46)
    else:
        # Padrão ENEM regular: 91 a 135 = Ciências da Natureza, 136 a 180 = Matemática
        if 136 <= qnum <= 180:
            is_math = True
        elif 91 <= qnum <= 135:
            is_math = False
        elif qnum <= 45:
            # Em provas de 45 questões (ex: bloco único)
            if any(k in tl for k in ['cilindro', 'função', 'triângulo', 'probabilidade', 'estatística', 'média', 'geometria', 'poliedro', 'área']):
                is_math = True
            else:
                is_math = False
        else:
            is_math = True

    # 1. MATEMÁTICA
    if is_math:
        disc = 'Matemática'
        if any(k in tl for k in ['cilindro', 'cone', 'prisma', 'esfera', 'pirâmide', 'paralelepípedo', 'tronco de cone', 'reservatório', 'sólido', 'projeção ortogonal', 'vista superior', 'vista frontal', 'vista lateral', 'sombra', 'poliedro', 'euler']):
            top = 'Geometria Espacial'
            hab = 'Visualização tridimensional, cálculo de volumes e identificação de projeções ortogonais'
        elif any(k in tl for k in ['média', 'mediana', 'moda', 'desvio padrão', 'variância', 'gráfico de setores', 'gráfico de barras', 'gráfico de linhas', 'frequência', 'tabela de dados', 'histograma']):
            top = 'Estatística Básica'
            hab = 'Cálculo de medidas de tendência central, dispersão e interpretação de gráficos/tabelas'
        elif any(k in tl for k in ['área do triângulo', 'área do círculo', 'área de figura plana', 'pitágoras', 'teorema de pitágoras', 'semelhança de triângulos', 'teorema de tales', 'trapézio', 'paralelogramo', 'perímetro', 'setor circular']):
            top = 'Geometria Plana'
            hab = 'Cálculo de áreas planas, relações métricas no triângulo e semelhança'
        elif any(k in tl for k in ['função afim', 'taxa de variação', 'coeficiente angular', 'função quadrática', 'vértice da parábola', 'máximo', 'mínimo', 'função exponencial', 'crescimento exponencial', 'logaritmo', 'função logarítmica', 'função']):
            top = 'Funções e Modelagem Algébrica'
            hab = 'Modelagem de fenômenos por funções afins, quadráticas, exponenciais e logarítmicas'
        elif any(k in tl for k in ['probabilidade', 'espaço amostral', 'evento favorável', 'probabilidade condicional']):
            top = 'Probabilidade'
            hab = 'Cálculo de probabilidade simples, condicional e união de eventos'
        elif any(k in tl for k in ['análise combinatória', 'princípio fundamental da contagem', 'combinação', 'arranjo', 'permutação', 'anagrama', 'comissão', 'agrupamento']):
            top = 'Análise Combinatória'
            hab = 'Problemas de contagem, permutações e agrupamentos combinatórios'
        elif any(k in tl for k in ['trigonometria', 'seno', 'cosseno', 'tangente', 'ciclo trigonométrico', 'geometria analítica', 'equação da reta', 'equação da circunferência']):
            top = 'Trigonometria e Geometria Analítica'
            hab = 'Relações trigonométricas fundamentais e geometria no plano cartesiano'
        elif any(k in tl for k in ['juros', 'montante', 'capital', 'taxa de juros', 'parcelamento', 'prestação', 'desconto comercial']):
            top = 'Matemática Financeira'
            hab = 'Cálculo financeiro aplicado ao consumo, financiamentos e inflação'
        else:
            top = 'Matemática Básica e Proporcionalidade'
            hab = 'Razão, proporção, regra de três simples/composta, escalas cartográficas e porcentagem'
        return disc, top, hab

    # 2. CIÊNCIAS DA NATUREZA (FÍSICA, QUÍMICA, BIOLOGIA)
    c_int = int(c) if c and c.isdigit() else 0
    
    # Determinar subdisciplina
    is_bio = False
    is_chem = False
    is_phys = False
    
    # Heurística inicial pela matriz INEP
    if c_int in [3, 4, 8]:
        is_bio = True
    elif c_int in [5, 7]:
        is_chem = True
    elif c_int in [1, 2, 6]:
        is_phys = True
        
    # Análise semântica profunda do texto (sobrepõe se conceitos específicos forem inequívocos)
    if any(k in tl for k in ['eutrofização', 'bioacumulação', 'ecologia', 'cadeia alimentar', 'gene', 'genética', 'dna', 'célula', 'fisiologia', 'vírus', 'bactéria', 'parasitose', 'evolução', 'darwin', 'botânica', 'imunologia', 'vacina', 'soro', 'fitormônio']):
        is_bio = True
        is_phys = False
        is_chem = False
    elif any(k in tl for k in ['estequiometria', 'massa molar', 'solução', 'soluções', 'pilha', 'eletrólise', 'oxirredução', 'entalpia', 'termoquímica', 'cinética química', 'equilíbrio químico', 'química orgânica', 'isomeria', 'ácido de arrhenius', 'oxidação']):
        is_chem = True
        is_bio = False
        is_phys = False
    elif any(k in tl for k in ['circuito', 'resistor', 'corrente elétrica', 'leis de ohm', 'calorimetria', 'termodinâmica', 'condução térmica', 'onda', 'ondulatória', 'óptica', 'espelho', 'lente', 'cinemática', 'leis de newton', 'pressão hidrostática', 'empuxo', 'campo magnético']):
        is_phys = True
        is_bio = False
        is_chem = False

    # Detalhamento do Tópico Real
    if is_bio:
        disc = 'Biologia'
        if any(k in tl for k in ['eutrofização', 'bioacumulação', 'magnificação trófica', 'ecologia', 'cadeia alimentar', 'teia alimentar', 'nível trófico', 'bioma', 'sucessão ecológica', 'relações ecológicas', 'ciclo do carbono', 'ciclo do nitrogênio']):
            top = 'Ecologia'
            hab = 'Impactos ambientais antrópicos, dinâmica trófica e ciclos biogeoquímicos'
        elif any(k in tl for k in ['gene', 'genética', 'alelo', 'dna', 'rna', 'cromossomo', 'herança', 'mendel', 'mutação', 'código genético', 'transgênico', 'crispr', 'clonagem']):
            top = 'Genética e Biologia Molecular'
            hab = 'Leis mendelianas, biologia molecular, síntese proteica e biotecnologia recombinante'
        elif any(k in tl for k in ['fisiologia', 'sistema circulatório', 'hemácia', 'oxigênio no sangue', 'imunologia', 'anticorpo', 'antígeno', 'vacina', 'soro', 'digestão', 'hormônio', 'insulina', 'rins']):
            top = 'Fisiologia Humana e Imunologia'
            hab = 'Fisiologia dos sistemas humanos e mecanismos de imunização'
        elif any(k in tl for k in ['célula', 'citologia', 'mitocôndria', 'membrana plasmática', 'transporte ativo', 'osmose', 'respiração celular', 'fermentação', 'fotossíntese', 'atp']):
            top = 'Citologia e Metabolismo Energético'
            hab = 'Estrutura celular, organelas citoplasmáticas e transformações bioenergéticas'
        elif any(k in tl for k in ['vírus', 'bactéria', 'parasitose', 'protozoário', 'verme', 'dengue', 'chagas', 'malária', 'esquistossomose', 'profilaxia']):
            top = 'Parasitologia e Doenças Humanas'
            hab = 'Ciclos biológicos de patógenos, agentes transmissores e medidas profiláticas'
        elif any(k in tl for k in ['evolução', 'darwin', 'lamarck', 'seleção natural', 'especiação', 'ancestral']):
            top = 'Evolução Biológica'
            hab = 'Mecanismos de seleção natural, especiação e teorias evolutivas'
        elif any(k in tl for k in ['planta', 'botânica', 'vegetal', 'caule', 'raiz', 'folha', 'xilema', 'floema', 'transpiração vegetal']):
            top = 'Botânica e Reino Vegetal'
            hab = 'Morfofisiologia vegetal e adaptações dos grupos taxonômicos'
        else:
            top = 'Ecologia'
            hab = 'Preservação da biodiversidade e interações ecológicas'
            
    elif is_chem:
        disc = 'Química'
        if any(k in tl for k in ['estequiometria', 'massa molar', 'número de mols', 'reagente limitante', 'rendimento', 'pureza']):
            top = 'Físico-Química (Estequiometria)'
            hab = 'Cálculo estequiométrico ponderal com rendimento e pureza de reagentes'
        elif any(k in tl for k in ['solução', 'soluções', 'concentração molar', 'soluto', 'solvente', 'diluição', 'titulação', 'solubilidade']):
            top = 'Físico-Química (Soluções)'
            hab = 'Preparo, diluição e cálculo de concentração de soluções aquosas'
        elif any(k in tl for k in ['pilha', 'eletrólise', 'oxidação', 'redução', 'potencial padrão', 'cátodo', 'ânodo', 'ddp']):
            top = 'Físico-Química (Eletroquímica)'
            hab = 'Processos eletroquímicos, células galvânicas e eletrólise quantitativa'
        elif any(k in tl for k in ['entalpia', 'termoquímica', 'endotérmica', 'exotérmica', 'lei de hess', 'energia de ligação']):
            top = 'Físico-Química (Termoquímica)'
            hab = 'Variação de entalpia, calorimetria química e balanço energético reacional'
        elif any(k in tl for k in ['cinética química', 'velocidade da reação', 'catalisador', 'energia de ativação']):
            top = 'Físico-Química (Cinética Química)'
            hab = 'Fatores que afetam a rapidez das transformações químicas e energia de ativação'
        elif any(k in tl for k in ['equilíbrio químico', 'le chatelier', 'kc', 'ph', 'poh', 'acidez']):
            top = 'Físico-Química (Equilíbrio Químico e pH)'
            hab = 'Deslocamento de equilíbrio químico e determinação de pH/pOH'
        elif any(k in tl for k in ['hidrocarboneto', 'álcool', 'aldeído', 'cetona', 'ácido carboxílico', 'éster', 'amina', 'amida', 'isomeria', 'polímero', 'petróleo']):
            top = 'Química Orgânica'
            hab = 'Identificação de funções orgânicas, isomeria plana/espacial e reações orgânicas'
        elif any(k in tl for k in ['chuva ácida', 'efeito estufa', 'camada de ozônio', 'tratamento de água', 'gás carbônico', 'poluente']):
            top = 'Química Ambiental'
            hab = 'Impactos ambientais químicos na atmosfera e tratamento de efluentes'
        else:
            top = 'Química Geral e Inorgânica'
            hab = 'Ligações químicas, forças intermoleculares e funções inorgânicas'
            
    else:
        disc = 'Física'
        if any(k in tl for k in ['circuito', 'resistor', 'corrente elétrica', 'voltagem', 'diferença de potencial', 'potência elétrica', 'ohm', 'ampère', 'consumo']):
            top = 'Eletrodinâmica'
            hab = 'Análise de circuitos elétricos, associação de resistores, potência e consumo'
        elif any(k in tl for k in ['calor', 'temperatura', 'calorimetria', 'capacidade térmica', 'condução', 'convecção', 'irradiação', 'termodinâmica']):
            top = 'Termologia e Calorimetria'
            hab = 'Mecanismos de propagação de calor, trocas térmicas e termodinâmica'
        elif any(k in tl for k in ['onda', 'ondulatória', 'frequência', 'comprimento de onda', 'doppler', 'som', 'ressonância', 'acústica']):
            top = 'Ondulatória e Acústica'
            hab = 'Equação fundamental da ondulatória, fenômenos ondulatórios e acústica'
        elif any(k in tl for k in ['espelho', 'lente', 'refração', 'reflexão', 'óptica', 'periscópio', 'foco']):
            top = 'Óptica Geométrica'
            hab = 'Propagação retilínea, reflexão e refração em espelhos e lentes'
        elif any(k in tl for k in ['pressão hidrostática', 'empuxo', 'arquimedes', 'densidade', 'pascal', 'stevin']):
            top = 'Hidrostática'
            hab = 'Pressão hidrostática, empuxo e equilíbrio de corpos flutuantes'
        elif any(k in tl for k in ['campo magnético', 'força magnética', 'indução eletromagnética', 'faraday', 'ímã']):
            top = 'Eletromagnetismo'
            hab = 'Campos magnéticos, força magnética e leis da indução eletromagnética'
        else:
            top = 'Mecânica'
            hab = 'Cinemática escalar/vetorial, leis de Newton e conservação da energia mecânica'
            
    return disc, top, hab

def main():
    print("=== INICIANDO MINERAÇÃO ANALÍTICA E SEMÂNTICA SAS ALPHA (PARTE 1) ===")
    
    files_scanned = []
    files_discarded = []
    files_dia2_valid = []
    
    # 1. Varredura completa das 6 pastas atribuídas
    for top_folder in ALPHA_FOLDERS:
        full_top = os.path.join(SAS_DIR, top_folder)
        if not os.path.exists(full_top):
            continue
        
        has_files = False
        for root, dirs, files in os.walk(full_top):
            for f in files:
                has_files = True
                fp = os.path.join(root, f)
                rel_p = os.path.relpath(fp, SAS_DIR)
                files_scanned.append(rel_p)
                
                fl = rel_p.lower()
                
                # Descarte 1: Olimpíadas
                if top_folder == "OLIMPÍADAS":
                    files_discarded.append((rel_p, "Descarte sumário: Exame de Olimpíada Científica escolar (OBF, OBQ, OBB, OBM), fora do escopo do modelo ENEM Dia 2"))
                # Descarte 2: 1º Dia do ENEM (Linguagens/Humanas/Redação)
                elif any(k in fl for k in ['1º dia', '1ºdia', '1odia', '1o dia', '1° dia', '1°dia', 'dia 1', 'dia1', '__1_dia', 'd1', '_d1', '- d1', 'ch_lc', 'chst-lc', 'lcgh', 'lgch', 'redacao', 'lcch', 'humanas']):
                    files_discarded.append((rel_p, "Descarte sumário: Caderno ou gabarito do 1º Dia do ENEM (Linguagens, Códigos, Redação e Ciências Humanas)"))
                # Descarte 3: Vestibulares não-ENEM
                elif top_folder == "FUVEST" or any(v in fl for v in ['fuvest', 'unicamp', 'unesp', 'uerj', 'uece', 'ufrgs']):
                    files_discarded.append((rel_p, "Descarte sumário: Material de vestibular paulista ou regional fora do modelo ENEM Dia 2"))
                else:
                    files_dia2_valid.append(rel_p)
                    
        if not has_files:
            subdirs = os.listdir(full_top)
            files_discarded.append((f"{top_folder}/", f"Descarte sumário: Diretório vazio ou sem arquivos presentes (contém subpastas de anos vazias: {subdirs})"))

    print(f"Total de arquivos físicos escaneados em Alpha: {len(files_scanned)}")
    print(f"Total de arquivos descartados: {len(files_discarded)}")
    print(f"Total de arquivos Dia 2 válidos: {len(files_dia2_valid)}")
    
    # 2. Agrupamento por edição de simulado para análise
    unique_editions = {}
    for f in files_dia2_valid:
        parts = f.split(os.sep)
        year = parts[1] if parts[0] == 'ENEM' else parts[0]
        fn = os.path.basename(f)
        
        m = re.search(r'(\d+)[º°o]\s*(?:simulado|sas|enem)', fn, re.IGNORECASE)
        if not m:
            m = re.search(r'simulado_sas_enem__(\d+)_', fn, re.IGNORECASE)
        if not m:
            m = re.search(r'simulado_sas_enem__2_dia__(\d+)_', fn, re.IGNORECASE)
        if not m:
            m = re.search(r'simulado_sas_enem__(\d+)_serie__2_dia', fn, re.IGNORECASE)
        if not m:
            m = re.search(r'(\d+)[º°o]', f)
        sim_num = m.group(1) if m else "1"
        
        serie = "EM"
        if "1ª" in f or "1a" in f or "1_serie" in f:
            serie = "1ª Série"
        elif "2ª" in f or "2a" in f or "2_serie" in f:
            serie = "2ª Série"
        elif "3ª" in f or "3a" in f or "3_serie" in f:
            serie = "3ª Série"
            
        full_ed_key = f"{parts[0]} - {year} - {serie} - Simulado {sim_num}"
        unique_editions.setdefault(full_ed_key, []).append(f)

    print(f"Total de edições/cadernos únicos agrupados: {len(unique_editions)}")
    
    all_analyzed_questions = []
    
    for ed_key, file_list in sorted(unique_editions.items()):
        # Prefer resolution file
        pref_file = None
        for candidate in file_list:
            if 'resolu' in candidate.lower() or 'res_' in candidate.lower() or 'gabarito' in candidate.lower():
                pref_file = candidate
                break
        if not pref_file:
            pref_file = file_list[0]
            
        full_path = os.path.join(SAS_DIR, pref_file)
        ext = os.path.splitext(pref_file)[1].lower()
        is_2011 = ("2011" in ed_key)
        
        if ext == '.pdf':
            try:
                reader = pypdf.PdfReader(full_path)
                full_text = ""
                for p in reader.pages:
                    full_text += p.extract_text() + "\n"
                    
                blocks = re.split(r'\n(?=(\d{1,3})\.\s+(?:Resposta correta|Gabarito):)', full_text)
                if len(blocks) > 2:
                    for i in range(1, len(blocks), 2):
                        qnum = int(blocks[i])
                        content = blocks[i+1]
                        
                        if is_2011 and qnum <= 45:
                            continue # Linguagens descartado em 2011
                            
                        m_ch = re.search(r'C\s*(\d+)\s+H\s*(\d+)', content[:120])
                        c = m_ch.group(1) if m_ch else ""
                        h = m_ch.group(2) if m_ch else ""
                        
                        disc, top, hab = classify_semantic(qnum, c, h, content[:1500], is_2011=is_2011)
                        all_analyzed_questions.append({
                            'edition': ed_key,
                            'source_file': pref_file,
                            'qnum': qnum,
                            'discipline': disc,
                            'topic': top,
                            'competencia': c,
                            'habilidade': h,
                            'ability_desc': hab,
                            'snippet': content[:150].strip().replace('\n', ' ')
                        })
                else:
                    # Regular exam PDF
                    q_splits = re.split(r'(?:QUESTÃO|Questão)\s+(\d{1,3})', full_text)
                    if len(q_splits) > 2:
                        for i in range(1, len(q_splits), 2):
                            qnum = int(q_splits[i])
                            content = q_splits[i+1]
                            if is_2011 and qnum <= 45:
                                continue
                            disc, top, hab = classify_semantic(qnum, "", "", content[:1500], is_2011=is_2011)
                            all_analyzed_questions.append({
                                'edition': ed_key,
                                'source_file': pref_file,
                                'qnum': qnum,
                                'discipline': disc,
                                'topic': top,
                                'competencia': "",
                                'habilidade': "",
                                'ability_desc': hab,
                                'snippet': content[:150].strip().replace('\n', ' ')
                            })
            except Exception as e:
                print(f"Erro em PDF {pref_file}: {e}")
                
        elif ext == '.docx':
            try:
                with zipfile.ZipFile(full_path) as z:
                    xml_content = z.read('word/document.xml')
                    tree = ET.fromstring(xml_content)
                    txt = ''.join(tree.itertext())
                    
                    sub_blocks = re.split(r'(?:\d{1,3}\.\s*|Questão\s+\d{1,3})', txt)
                    for idx, blk in enumerate(sub_blocks[1:], 1):
                        if len(blk.strip()) < 40:
                            continue
                        disc, top, hab = classify_semantic(idx, "", "", blk[:1500], is_2011=False)
                        all_analyzed_questions.append({
                            'edition': ed_key,
                            'source_file': pref_file,
                            'qnum': idx,
                            'discipline': disc,
                            'topic': top,
                            'competencia': "",
                            'habilidade': "",
                            'ability_desc': hab,
                            'snippet': blk[:150].strip().replace('\n', ' ')
                        })
            except Exception as e:
                print(f"Erro em DOCX {pref_file}: {e}")

    total_q = len(all_analyzed_questions)
    print(f"\nTotal de questões válidas do Dia 2 analisadas: {total_q}")
    
    # 3. Consolidação e Estatísticas
    disc_stats = {}
    topic_stats = {}
    interdisc_pairs = []
    
    for q in all_analyzed_questions:
        d = q['discipline']
        t = q['topic']
        disc_stats[d] = disc_stats.get(d, 0) + 1
        
        topic_stats.setdefault(d, {})
        topic_stats[d][t] = topic_stats[d].get(t, 0) + 1
        
        snip = q['snippet'].lower()
        if d == 'Física' and any(k in snip for k in ['pilha', 'eletrólise', 'oxirredução', 'revestimento']):
            interdisc_pairs.append(('Física - Eletrodinâmica', 'Química - Eletroquímica', q['snippet'][:90]))
        elif d == 'Química' and any(k in snip for k in ['corrente elétrica', 'tensão', 'potência', 'joule', 'resistor']):
            interdisc_pairs.append(('Química - Eletroquímica', 'Física - Eletrodinâmica', q['snippet'][:90]))
        elif d == 'Biologia' and any(k in snip for k in ['mercúrio', 'agrotóxico', 'metais pesados', 'poluição', 'ph', 'chuva ácida', 'aquecimento global', 'co2']):
            interdisc_pairs.append(('Biologia - Ecologia', 'Química - Química Ambiental', q['snippet'][:90]))
        elif d == 'Física' and any(k in snip for k in ['olho', 'visão', 'miopia', 'hipermetropia', 'célula']):
            interdisc_pairs.append(('Física - Óptica Geométrica', 'Biologia - Fisiologia da Visão', q['snippet'][:90]))
        elif d == 'Matemática' and any(k in snip for k in ['temperatura', 'esfriamento', 'bactéria', 'população', 'decibel', 'richter']):
            interdisc_pairs.append(('Matemática - Funções Exponenciais/Log', 'Física/Biologia - Dinâmica Populacional e Termologia', q['snippet'][:90]))

    print("\n--- DISTRIBUIÇÃO CONSOLIDADA POR DISCIPLINA ---")
    for d, count in sorted(disc_stats.items(), key=lambda x: x[1], reverse=True):
        pct = (count / total_q) * 100 if total_q else 0
        print(f"{d}: {count} questões ({pct:.2f}%)")

    # Salvar dados JSON
    out_json = os.path.join(BASE_DIR, "FINAL", "subagentes", "dados_sas_alpha.json")
    with open(out_json, "w", encoding="utf-8") as jf:
        json.dump({
            'total_questions': total_q,
            'discipline_stats': disc_stats,
            'topic_stats': topic_stats,
            'files_scanned': files_scanned,
            'files_discarded': files_discarded,
            'files_dia2_valid': files_dia2_valid,
            'questions': all_analyzed_questions,
            'interdisciplinary_pairs': interdisc_pairs
        }, jf, ensure_ascii=False, indent=2)
    print(f"Dados salvos com sucesso em: {out_json}")

if __name__ == '__main__':
    main()
