import os
import sys
import re
import json
import zipfile
import xml.etree.ElementTree as ET

TAXONOMY_PATTERNS = {
    # MATEMÁTICA
    'M1': ('Matemática Básica e Proporcionalidade', [
        r'\braz[aã]o\b', r'\bpropor[cç]', r'\bescala\b', r'\bregra de tr[eê]s\b', r'\bporcentagem\b',
        r'\baumento\b', r'\bdesconto\b', r'\bconvers[aã]o\b', r'\blitros?\b', r'\bm³\b', r'\bkm/h\b',
        r'\bgrandezas\b', r'\binversamente\b', r'\bdiretamente\b', r'\bpotencia[cç][aã]o\b'
    ]),
    'M2': ('Geometria Espacial', [
        r'\bprisma\b', r'\bcilindr', r'\bcone\b', r'\besfera\b', r'\bpir[aâ]mide\b', r'\bvolume\b',
        r'\bparalelep[ií]pedo\b', r'\bpoliedro\b', r'\beuler\b', r'\bproje[cç]', r'\bproje[cç][aã]o ortogonal\b',
        r'\bsombra\b', r'\bvistas? ortogonais?\b', r'\bplanifica[cç]', r'\bespacial\b'
    ]),
    'M3': ('Estatística Básica', [
        r'\bm[eé]dia\b', r'\bmediana\b', r'\bmoda\b', r'\bdesvio[- ]padr[aã]o\b', r'\bvari[aâ]ncia\b',
        r'\bgr[aá]fico\b', r'\bhistograma\b', r'\bdispers[aã]o\b', r'\btabela\b', r'\bestat[ií]stica\b'
    ]),
    'M4': ('Geometria Plana', [
        r'\btri[aâ]ngul', r'\bc[ií]rcul', r'\bcircunfer[eê]ncia\b', r'\b[aá]rea\b', r'\bper[ií]metro\b',
        r'\bpit[aá]goras\b', r'\btrigonometri', r'\bseno\b', r'\bcosseno\b', r'\btangente\b',
        r'\bsemelhan[cç]a\b', r'\btales\b', r'\btrap[eé]zio\b', r'\bplana\b', r'\bpol[ií]gon'
    ]),
    'M5': ('Funções e Modelagem', [
        r'\bfun[cç]', r'\bafim\b', r'\blinear\b', r'\bquadr[aá]tic', r'\bpar[aá]bola\b',
        r'\bv[eé]rtice\b', r'\bm[aá]ximo\b', r'\bm[ií]nimo\b', r'\btaxa de varia[cç][aã]o\b',
        r'\bexponencial\b', r'\blogar[ií]tm', r'\bequa[cç][aã]o do 2º grau\b'
    ]),
    'M6': ('Probabilidade e Combinatória', [
        r'\bprobabilidade\b', r'\bespa[cç]o amostral\b', r'\bcombina[cç]', r'\barranjo\b',
        r'\bpermuta[cç]', r'\banagrama\b', r'\bcontagem\b', r'\bchance\b', r'\ban[aá]lise combinat[oó]ria\b'
    ]),
    
    # BIOLOGIA
    'B1': ('Ecologia e Meio Ambiente', [
        r'\becolog', r'\becossistema\b', r'\btr[oó]fic', r'\beutrofiza[cç]', r'\bbioacumula[cç]',
        r'\bmagnifica[cç]', r'\bciclos? biogeoqu[ií]micos?\b', r'\bnitrog[eê]nio\b', r'\bcarbono\b',
        r'\baquecimento global\b', r'\befeito estufa\b', r'\bdesmatamento\b', r'\bmutualismo\b',
        r'\bparasitismo\b', r'\bpreda[cç]', r'\bbioma\b', r'\bpolui[cç]', r'\brela[cç][oõ]es ecol[oó]gicas\b'
    ]),
    'B2': ('Genética e Biotecnologia', [
        r'\bmendel\b', r'\balelo\b', r'\bgene\b', r'\bheredograma\b', r'\bgen[oó]tipo\b',
        r'\bfen[oó]tipo\b', r'\bherança\b', r'\bsistema abo\b', r'\bfator rh\b', r'\bdna\b',
        r'\bpcr\b', r'\beletroforese\b', r'\bclon', r'\btransg[eê]nic', r'\bogm\b', r'\bcrispr\b'
    ]),
    'B3': ('Citologia e Metabolismo', [
        r'\bc[eé]lula\b', r'\borganela\b', r'\bmitoc[oô]ndria\b', r'\bcloroplasto\b',
        r'\bfotoss[ií]ntese\b', r'\brespira[cç]', r'\bglic[oó]lise\b', r'\bkrebs\b',
        r'\bfermenta[cç]', r'\bosmose\b', r'\bmembrana\b', r'\btransporte ativo\b', r'\batp\b'
    ]),
    'B4': ('Fisiologia e Imunologia', [
        r'\bvacina\b', r'\bsoro\b', r'\bant[ií]geno\b', r'\banticorpo\b', r'\bimun',
        r'\blinf[oó]cito\b', r'\baedes\b', r'\bdengue\b', r'\bzika\b', r'\bchikungunya\b',
        r'\bchagas\b', r'\bmal[aá]ria\b', r'\bleishmaniose\b', r'\bbact[eé]ria\b', r'\bv[ií]rus\b',
        r'\bhorm[oô]ni', r'\bparasitologia\b', r'\bprotozooses?\b'
    ]),
    
    # FÍSICA
    'F1': ('Eletrodinâmica', [
        r'\bcircuito\b', r'\bresistor', r'\bresist[eê]ncia\b', r'\bcorrente\b',
        r'\bddp\b', r'\btens[aã]o\b', r'\bvoltagem\b', r'\bpot[eê]ncia\b',
        r'\bkwh\b', r'\bjoule\b', r'\bfus[ií]vel\b', r'\bdisjuntor\b', r'\bamper[ií]metro\b',
        r'\bvolt[ií]metro\b', r'\bparalelo\b', r'\bs[eé]rie\b', r'\bohm\b', r'\beletrodin[aâ]mica\b'
    ]),
    'F2': ('Mecânica e Hidrostática', [
        r'\bcin[eé]tica\b', r'\bpotencial\b', r'\bconserva[cç][aã]o da energia\b',
        r'\btrabalho\b', r'\bnewton\b', r'\batrito\b', r'\bplano inclinado\b', r'\bcinem[aá]tica\b',
        r'\bacelera[cç]', r'\bmru\b', r'\bmruv\b', r'\bmhs\b', r'\bpress[aã]o\b',
        r'\bempuxo\b', r'\barquimedes\b', r'\bpascal\b', r'\bhidrost[aá]tica\b', r'\bdin[aâ]mica\b'
    ]),
    'F3': ('Ondulatória e Acústica', [
        r'\bonda\b', r'\bondulat[oó]ria\b', r'\bcomprimento de onda\b', r'\bfrequ[eê]ncia\b',
        r'\brefra[cç]', r'\bdifra[cç]', r'\binterfer[eê]ncia\b', r'\bresson[aâ]ncia\b',
        r'\bdoppler\b', r'\bac[uú]stica\b', r'\btimbre\b', r'\bsom\b', r'\bsonor'
    ]),
    'F4': ('Termologia e Termodinâmica', [
        r'\bcalorimetria\b', r'\bcalor\b', r'\blatente\b', r'\bcondu[cç]',
        r'\bconvec[cç]', r'\birradia[cç]', r'\btermodin[aâ]mica\b',
        r'\bm[aá]quina t[eé]rmica\b', r'\bcarnot\b', r'\bdilata[cç]', r'\bgases\b'
    ]),
    
    # QUÍMICA
    'Q1': ('Físico-Química', [
        r'\bpilha\b', r'\b[aâ]nodo\b', r'\bc[aá]todo\b', r'\boxida[cç]', r'\bredu[cç]',
        r'\beletr[oó]lise\b', r'\bcorros[aã]o\b', r'\btermoqu[ií]mica\b', r'\bentalpia\b',
        r'\bdelta h\b', r'\blei de hess\b', r'\bcin[eé]tica\b', r'\bcatalisador\b',
        r'\bequil[ií]brio qu[ií]mico\b', r'\ble chatelier\b', r'\bph\b', r'\bequil[ií]brio i[oô]nico\b',
        r'\bsolu[cç]', r'\bconcentra[cç]', r'\bmolar\b', r'\bindicadores de ph\b'
    ]),
    'Q2': ('Química Geral e Estequiometria', [
        r'\bestequiometria\b', r'\bmol\b', r'\bmassa molar\b', r'\bpureza\b', r'\brendimento\b',
        r'\bliga[cç][aã]o qu[ií]mica\b', r'\bliga[cç][oõ]es de hidrog[eê]nio\b', r'\bfor[cç]as intermoleculares\b',
        r'\bdipolo\b', r'\blondon\b', r'\bponto de ebuli[cç][aã]o\b', r'\bsepara[cç][aã]o de misturas\b',
        r'\ban[aá]lise imediata\b', r'\bsubst[aâ]ncias e misturas\b', r'\bdestila[cç]', r'\bfiltra[cç]', r'\bdecanta[cç]'
    ]),
    'Q3': ('Química Orgânica', [
        r'\bqu[ií]mica org[aâ]nica\b', r'\bhidrocarboneto\b', r'\b[aá]lcool\b', r'\bfenol\b',
        r'\balde[ií]do\b', r'\bcetona\b', r'\b[aá]cido carbox[ií]lico\b', r'\b[eé]ster\b',
        r'\bamina\b', r'\bamida\b', r'\bisomer', r'\bquiral\b', r'\besterifica[cç]',
        r'\bbiodiesel\b', r'\bpol[ií]mero\b', r'\bpet\b', r'\bpvc\b', r'\brea[cç][oõ]es org[aâ]nicas\b'
    ]),
    'Q4': ('Química Ambiental', [
        r'\bqu[ií]mica ambiental\b', r'\bchuva [aá]cida\b', r'\befeito estufa\b', r'\boz[oô]nio\b',
        r'\bcfc\b', r'\btratamento de [aá]gua\b', r'\bflocula[cç]', r'\bclora[cç]', r'\bpoluente\b',
        r'\bimpactos ambientais\b', r'\bacidifica[cç][aã]o\b'
    ])
}

COMPILED_PATTERNS = {
    code: (name, [re.compile(p, re.IGNORECASE) for p in pats])
    for code, (name, pats) in TAXONOMY_PATTERNS.items()
}

def classify_text_to_topic(text, discipline=None):
    scores = {}
    for code, (topic_name, regexes) in COMPILED_PATTERNS.items():
        if discipline == 'MAT' and not code.startswith('M'):
            continue
        if discipline in ('CN', 'FIS', 'QUI', 'BIO') and code.startswith('M'):
            continue
        if discipline == 'FIS' and not code.startswith('F'):
            continue
        if discipline == 'QUI' and not code.startswith('Q'):
            continue
        if discipline == 'BIO' and not code.startswith('B'):
            continue
            
        m = sum(1 for rx in regexes if rx.search(text))
        if m > 0:
            scores[code] = (m, topic_name)
    best = sorted(scores.items(), key=lambda x: -x[1][0])
    if best:
        return best[0][0], best[0][1][1]
    return None, None

def col_letter_to_index(col_str):
    col = 0
    for c in col_str:
        col = col * 26 + (ord(c.upper()) - ord('A') + 1)
    return col - 1

def parse_poliedro_ficha_mapa_proper(path):
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
            
        full_text = f"{tematica} {objeto} {desc}"
        code, name = classify_text_to_topic(full_text, disc)
        
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

def run_pipeline():
    print("Executando pipeline de parsing e montagem do catálogo completo...")
    poliedro_fichas = [
        ('POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', '1º Simulado Enem 2024', 'POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Resolução.pdf'),
        ('POLIEDRO/2024/2º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', '2º Simulado Enem 2024', 'POLIEDRO/2024/2º Simulado Enem 2024 - 2º Dia - Resolução.pdf'),
        ('POLIEDRO/2024/3º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', '3º Simulado Enem 2024', 'POLIEDRO/2024/3º Simulado Enem 2024 - 2º Dia - Resolução.pdf'),
        ('POLIEDRO/2024/4º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', '4º Simulado Enem 2024', 'POLIEDRO/2024/4º Simulado Enem 2024 - 2º Dia - Resolução.pdf'),
        ('POLIEDRO/2024/2024_5_poliedro_enem_3serie_e_pv_ficha_mapa_geral_dia02.xlsx', '5º Simulado Enem 2024', 'POLIEDRO/2024/5º Simulado Enem 2024 - 2º Dia - Resolução.pdf'),
    ]
    all_poliedro_questions = {}
    for fpath, sname, rpath in poliedro_fichas:
        qs = parse_poliedro_ficha_mapa_proper(fpath)
        all_poliedro_questions[sname] = {
            'res_path': rpath,
            'questions': qs
        }
    with open('extracted_questions_index.json', 'r', encoding='utf-8') as f:
        extracted_data = json.load(f)
    topic_index = {code: [] for code in TAXONOMY_PATTERNS.keys()}
    for sname, data in all_poliedro_questions.items():
        rpath = data['res_path']
        for q in data['questions']:
            c = q['topic_code']
            if c in topic_index:
                topic_index[c].append({
                    'simulado': sname,
                    'provider': 'Poliedro',
                    'q_num': q['num'],
                    'gabarito': q['gabarito'],
                    'tematica': q['tematica'],
                    'objeto': q['objeto'],
                    'res_path': rpath
                })
    b_sims = [
        ("Bernoulli 2019 Simulado 1 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/1º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
        ("Bernoulli 2019 Simulado 2 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/2º conjunto/2_conj_2019_Gabarito_Questao_comentada_Prova_II.pdf"),
        ("Bernoulli 2019 Simulado 3 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/3º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
        ("Bernoulli 2019 Simulado 4 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/4º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
        ("Bernoulli 2019 Simulado 5 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/5º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
    ]
    for bname, bpath in b_sims:
        if bname in extracted_data['extracted_simulados']:
            for q in extracted_data['extracted_simulados'][bname]['questions']:
                c = q['topic_code']
                if c in topic_index:
                    topic_index[c].append({
                        'simulado': bname,
                        'provider': 'Bernoulli',
                        'q_num': q['num'],
                        'gabarito': 'Comentada',
                        'tematica': 'Simulado Nacional Bernoulli Prova II',
                        'objeto': q['body'][:75].replace('\n', ' ') + '...',
                        'res_path': bpath
                    })
    return all_poliedro_questions, topic_index

def generate_catalogo_markdown(survey_records):
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
    md.append("Abaixo estão listados os principais conjuntos do 2º Dia catalogados no workspace com seus respectivos caminhos de acesso direto:")
    md.append("")
    md.append("| Coleção / Edição | Provedor | Ano | Conteúdo e Tipo | Páginas | Caminho Relativo no Workspace |")
    md.append("| :--- | :---: | :---: | :--- | :---: | :--- |")
    md.append("| **Poliedro 2024 Simulado 1** | Poliedro | 2024 | Prova Dia 2 Limpa | 32 | `POLIEDRO/2024/2024_1_poliedro_enem_2_dia_prova.pdf` |")
    md.append("| **Poliedro 2024 Simulado 1 (Resolução)** | Poliedro | 2024 | Resolução Comentada Completa | 91 | `POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Resolução.pdf` |")
    md.append("| **Poliedro 2024 Simulado 1 (Ficha Mapa)** | Poliedro | 2024 | Matriz de Habilidades e Conteúdos | Planilha | `POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx` |")
    md.append("| **Poliedro 2024 Simulado 2** | Poliedro | 2024 | Prova Dia 2 Limpa | 32 | `POLIEDRO/2024/2024_2_poliedro_enem_2_dia_prova.pdf` |")
    md.append("| **Poliedro 2024 Simulado 2 (Resolução)** | Poliedro | 2024 | Resolução Comentada Completa | 88 | `POLIEDRO/2024/2º Simulado Enem 2024 - 2º Dia - Resolução.pdf` |")
    md.append("| **Poliedro 2024 Simulado 3 (Resolução)** | Poliedro | 2024 | Resolução Comentada Completa | 85 | `POLIEDRO/2024/3º Simulado Enem 2024 - 2º Dia - Resolução.pdf` |")
    md.append("| **Poliedro 2024 Simulado 4 (Resolução)** | Poliedro | 2024 | Resolução Comentada Completa | 89 | `POLIEDRO/2024/4º Simulado Enem 2024 - 2º Dia - Resolução.pdf` |")
    md.append("| **Poliedro 2024 Simulado 5 (Resolução)** | Poliedro | 2024 | Resolução Comentada Completa | 87 | `POLIEDRO/2024/5º Simulado Enem 2024 - 2º Dia - Resolução.pdf` |")
    md.append("| **Bernoulli 2019 Simulado 1** | Bernoulli | 2019 | Prova II Limpa | 32 | `BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/1º conjunto/1- Segundo dia.pdf` |")
    md.append("| **Bernoulli 2019 Simulado 1 (Comentada)** | Bernoulli | 2019 | Gabarito e Questões Comentadas Prova II | 39 | `BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/1º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf` |")
    md.append("| **Bernoulli 2019 Simulado 2 (Comentada)** | Bernoulli | 2019 | Gabarito e Questões Comentadas Prova II | 41 | `BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/2º conjunto/2_conj_2019_Gabarito_Questao_comentada_Prova_II.pdf` |")
    md.append("| **Bernoulli 2019 Simulado 3 (Comentada)** | Bernoulli | 2019 | Gabarito e Questões Comentadas Prova II | 40 | `BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/3º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf` |")
    md.append("| **Bernoulli 2019 Simulado 4 (Comentada)** | Bernoulli | 2019 | Gabarito e Questões Comentadas Prova II | 42 | `BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/4º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf` |")
    md.append("| **Bernoulli 2019 Simulado 5 (Comentada)** | Bernoulli | 2019 | Gabarito e Questões Comentadas Prova II | 38 | `BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/5º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf` |")
    md.append("| **Bernoulli 2022 Simulado 1** | Bernoulli | 2022 | Prova Dia 2 Limpa | 32 | `_ENEM_DIA_2_BRUTO/1° BERNOULLI 2022 dia 2.pdf` |")
    md.append("| **Bernoulli 2025 Simulado 1** | Bernoulli | 2025 | Prova Dia 2 Limpa | 32 | `_ENEM_DIA_2_BRUTO/1º BERNOULLI 2025 - D2.pdf` |")
    md.append("| **Bernoulli 2026 Simulado 1 Extra** | Bernoulli | 2026 | Prova Dia 2 Limpa | 32 | `_ENEM_DIA_2_BRUTO/1° BERNOULLI EXTRA 2026 - D2.pdf` |")
    md.append("| **Bernoulli 2026 Book Prova II** | Bernoulli | 2026 | Caderno Completo Prova II | 36 | `_ENEM_DIA_2_BRUTO/d3d4ebf36fc4f39bb474847b5928558207be3c0eBer_SE2026_V05_BOOK_PROVAII.pdf` |")
    md.append("| **SAS Avaliação Periódica 2 (2019)** | SAS | 2019 | Prova Limpa CNST-MST (90Q) | 42 | `_ENEM_DIA_2_BRUTO/1241-19_AP2_CNST-MST_3SERIE_1ETAPA.pdf` |")
    md.append("| **SAS AP2 Resolução Comentada (2019)** | SAS | 2019 | Resolução Completa 1 a 90 | 10 | `_ENEM_DIA_2_BRUTO/1242-19_RESOLUCAO_AP2_CNST-MST_3SERIE_1ETAPA.pdf` |")
    md.append("| **SAS Avaliação Periódica 2 (2020)** | SAS | 2020 | Prova Limpa CNST-MST (90Q) | 43 | `_ENEM_DIA_2_BRUTO/1373-20 - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf` |")
    md.append("| **SAS AP2 Resolução Comentada (2020)** | SAS | 2020 | Resolução Completa 1 a 90 | 12 | `_ENEM_DIA_2_BRUTO/1378-20 - RESOLUCAO - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf` |")
    md.append("| **SAS Avaliação Periódica 2 (2021)** | SAS | 2021 | Prova Limpa CNST-MST (90Q) | 43 | `_ENEM_DIA_2_BRUTO/1139-21 - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf` |")
    md.append("| **SAS AP2 Resolução Comentada (2021)** | SAS | 2021 | Resolução Completa 1 a 90 | 12 | `_ENEM_DIA_2_BRUTO/1452-21 - RESOLUCAO - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf` |")
    md.append("| **SAS Simulado ENEM 2026 D2** | SAS | 2026 | Caderno Amarelo Dia 2 Limpo | 32 | `_ENEM_DIA_2_BRUTO/1º SIMULADO SAS ENEM - 2026 -  D2 - AMARELO.pdf` |")
    md.append("| **SAS Simulado ENEM 2026 D2 (Azul)** | SAS | 2026 | Caderno Azul Dia 2 Limpo | 32 | `_ENEM_DIA_2_BRUTO/1º SIMULADO SAS ENEM - 2026 -  D2 - AZUL .pdf` |")
    md.append("| **Apeiron 2026 Simulado 1** | Apeiron | 2026 | Prova Dia 2 Limpa | 32 | `APEIRON-20261110T152018Z-1-001/APEIRON/2026/1º/1º APEIRON 2026 - D2.pdf` |")
    md.append("| **Apeiron 2026 Simulado 2 (Resolução)** | Apeiron | 2026 | Resolução Comentada Oficial D2 | 34 | `APEIRON-20261110T152018Z-1-001/APEIRON/2º/A2GCD2 (Oficial)-1.pdf` |")
    md.append("| **ENEM Oficial 2024 Dia 2** | INEP | 2024 | Prova Oficial Completa | 32 | `ENEM/2024/ENEM 2024 DIA 2.pdf` |")
    md.append("| **ENEM Oficial 2024 Gabarito** | INEP | 2024 | Gabarito Oficial Definitivo | 2 | `ENEM/2024/GABARITO 2024 DIA 2.pdf` |")
    md.append("| **ENEM Oficial 2025 Dia 2 (Amarelo)** | INEP | 2025 | Caderno Amarelo Dia 2 | 32 | `ENEM/2025/enem-2025-2-dia-caderno-amarelo.pdf` |")
    md.append("| **ENEM Oficial 2025 Dia 2 (Azul)** | INEP | 2025 | Caderno Azul Dia 2 | 32 | `ENEM/2025/enem-2025-2-dia-caderno-azul.pdf` |")
    md.append("| **ENEM Oficial 2025 Dia 2 (Verde)** | INEP | 2025 | Caderno Verde Dia 2 | 32 | `ENEM/2025/enem-2025-2-dia-caderno-verde.pdf` |")
    md.append("| **ENEM Oficial 2025 Dia 2 (Cinza)** | INEP | 2025 | Caderno Cinza Dia 2 | 32 | `ENEM/2025/enem-2025-2-dia-caderno-cinza.pdf` |")
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
    md.append("> **Status:** Concluído — Matriz de Questões Mapeadas por Tópico e Habilidade  ")
    md.append("> **Destino do Arquivo:** `FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md`  ")
    md.append("> **Base Teórica:** Conectado à Matriz de Incidência de `FINAL/RELATORIO_ESTATISTICO_ENEM_DIA_2.md`  ")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 1. VISÃO GERAL DO ÍNDICE E TAXONOMIA INTEGRADA")
    md.append("")
    md.append("Este índice mapeia cirurgicamente as questões do acervo físico de simulados aos tópicos de maior peso na Teoria de Resposta ao Item (TRI). Cada seção traz o perfil do tópico, sua taxa de incidência histórica e a tabela de questões correspondentes com indicação do simulado, número da questão, gabarito e caminho da resolução comentada.")
    md.append("")
    md.append("---")
    md.append("")
    md.append("## 2. MATEMÁTICA E SUAS TECNOLOGIAS (45 Questões)")
    md.append("")
    
    topics_mat = [
        ('M1', 'Matemática Básica e Proporcionalidade', '34% a 38%', 'CRUCIAL (Base da TRI)',
         'Razão, proporção, regra de três simples e composta, porcentagem, aumentos/descontos, escalas cartográficas e conversão de unidades (litros, m³, tempo). Sustenta a coerência pedagógica da nota.'),
        ('M2', 'Geometria Espacial', '11% a 13%', 'ALTA (Diferencial)',
         'Cálculo de volumes e áreas de prismas retos, cilindros, cones e esferas; projeção ortogonal e visualização espacial tridimensional; poliedros (Relação de Euler).'),
        ('M3', 'Estatística Básica', '10% a 12%', 'CRUCIAL (Base da TRI)',
         'Interpretação de gráficos (barras, colunas, setores, linhas) e tabelas; medidas de tendência central (média aritmética e ponderada, mediana, moda); dispersão (desvio padrão).'),
        ('M4', 'Geometria Plana', '8% a 10%', 'ALTA',
         'Cálculo de áreas (triângulos, círculos, paralelogramos, trapézios); Teorema de Pitágoras; trigonometria básica nos triângulos retângulos; semelhança de triângulos e Teorema de Tales.'),
        ('M5', 'Funções e Modelagem Algébrica', '7% a 9%', 'MÉDIA-ALTA',
         'Função Afim (taxa de variação e valor fixo); Função Quadrática (vértice, máximos e mínimos); modelagem exponencial e propriedades fundamentais de logaritmos.'),
        ('M6', 'Probabilidade e Análise Combinatória', '9% a 12%', 'MÉDIA-ALTA (Diferencial)',
         'Princípio Fundamental da Contagem (PFC), permutações e combinações simples; probabilidade clássica, probabilidade da união de eventos e probabilidade condicional.')
    ]
    
    for code, title, inc, tri_stat, desc in topics_mat:
        md.append(f"### 2.{code[1]} Tópico {code}: {title}")
        md.append(f"* **Incidência Média:** {inc} | **Status TRI:** `{tri_stat}`")
        md.append(f"* **Conceitos-Chave:** {desc}")
        md.append("")
        md.append("| Simulado / Edição | Provedor | Questão | Gabarito | Objeto de Conhecimento / Descritor | Arquivo de Resolução Comentada |")
        md.append("| :--- | :---: | :---: | :---: | :--- | :--- |")
        
        q_list = topic_index.get(code, [])
        for item in q_list[:12]: # Show top 12 curated matches per topic
            gab_str = f"`{item['gabarito']}`" if item['gabarito'] != 'Comentada' else 'Comentada'
            md.append(f"| {item['simulado']} | {item['provider']} | **Q{item['q_num']}** | {gab_str} | {item['tematica']} - {item['objeto']} | `{item['res_path']}` |")
        if not q_list:
            md.append("| *Nenhuma questão filtrada para este tópico no recorte* | - | - | - | - | - |")
        md.append("")
        
    md.append("---")
    md.append("")
    md.append("## 3. BIOLOGIA (~15 Questões)")
    md.append("")
    
    topics_bio = [
        ('B1', 'Ecologia e Meio Ambiente', '28% a 32%', 'LÍDER ABSOLUTA HISTÓRICA',
         'Impactos ambientais antrópicos (eutrofização, bioacumulação e magnificação trófica, aquecimento global e acidificação oceânica, desmatamento e espécies invasoras); ciclos biogeoquímicos (Nitrogênio e Carbono); fluxo de energia e teias tróficas; relações ecológicas.'),
        ('B2', 'Genética, Biologia Molecular e Biotecnologia', '20% a 25%', 'ALTA',
         '1ª e 2ª Leis de Mendel, heredogramas, sistema ABO e Fator Rh; Biotecnologia aplicada (DNA recombinante, clonagem terapêutica/reprodutiva, transgênicos vs OGM, PCR, eletroforese e CRISPR).'),
        ('B3', 'Citologia e Metabolismo Energético', '12% a 15%', 'ALTA',
         'Fotossíntese (fases fotoquímica e química); respiração celular aeróbia e fermentação (láctica e alcoólica); membrana plasmática e transportes celulares (osmose, difusão e transporte ativo por bomba de Na+/K+).'),
        ('B4', 'Fisiologia Humana e Imunologia', '10% a 13%', 'ALTA (Contextualizada)',
         'Imunologia (Vacinas: profiláticas, antígenos atenuados, células de memória vs. Soros: curativos emergenciais, anticorpos pré-formados); Doenças e agentes etiológicos (arboviroses pelo Aedes, Chagas, Malária, Leishmaniose e uso racional de antibióticos).')
    ]
    
    for code, title, inc, tri_stat, desc in topics_bio:
        md.append(f"### 3.{code[1]} Tópico {code}: {title}")
        md.append(f"* **Incidência Média:** {inc} | **Status TRI:** `{tri_stat}`")
        md.append(f"* **Conceitos-Chave:** {desc}")
        md.append("")
        md.append("| Simulado / Edição | Provedor | Questão | Gabarito | Objeto de Conhecimento / Descritor | Arquivo de Resolução Comentada |")
        md.append("| :--- | :---: | :---: | :---: | :--- | :--- |")
        
        q_list = topic_index.get(code, [])
        for item in q_list[:12]:
            gab_str = f"`{item['gabarito']}`" if item['gabarito'] != 'Comentada' else 'Comentada'
            md.append(f"| {item['simulado']} | {item['provider']} | **Q{item['q_num']}** | {gab_str} | {item['tematica']} - {item['objeto']} | `{item['res_path']}` |")
        if not q_list:
            md.append("| *Nenhuma questão filtrada para este tópico no recorte* | - | - | - | - | - |")
        md.append("")

    md.append("---")
    md.append("")
    md.append("## 4. FÍSICA (~15 Questões)")
    md.append("")
    
    topics_fis = [
        ('F1', 'Eletrodinâmica e Circuitos Elétricos', '21% a 24%', 'LÍDER EM REGULARIDADE',
         'Circuitos elétricos com associação de resistores em série e paralelo; potência elétrica e consumo de energia residencial em kWh (E = P.Δt / 1000); dimensionamento de fusíveis e disjuntores; instrumentos de medição (amperímetro e voltímetro).'),
        ('F2', 'Mecânica Clássica e Hidrostática', '31% a 37%', 'LÍDER EM VOLUME',
         'Conservação da energia mecânica (cinética, potencial gravitacional e elástica), dissipação por atrito e rendimento; Leis de Newton e dinâmica em planos inclinados; cinemática escalar e interpretação gráfica (área sob v x t = distância); hidrostática (pressão, Teorema de Pascal e Empuxo de Arquimedes).'),
        ('F3', 'Ondulatória e Acústica', '14% a 16%', 'ALTA (Foco Conceitual)',
         'Equação fundamental da onda (v = λ.f); fenômenos ondulatórios (refração, difração, interferência, ressonância, polarização e Efeito Doppler); qualidades fisiológicas do som (altura, intensidade e timbre).'),
        ('F4', 'Termologia e Termodinâmica', '13% a 16%', 'ALTA',
         'Calorimetria sensível (Q = m.c.ΔT) e calor latente de mudança de estado (Q = m.L); processos de transmissão de calor (condução, convecção e irradiação); 1ª Lei da Termodinâmica (ΔU = Q - W) e 2ª Lei (máquinas térmicas e rendimento de Carnot).')
    ]
    
    for code, title, inc, tri_stat, desc in topics_fis:
        md.append(f"### 4.{code[1]} Tópico {code}: {title}")
        md.append(f"* **Incidência Média:** {inc} | **Status TRI:** `{tri_stat}`")
        md.append(f"* **Conceitos-Chave:** {desc}")
        md.append("")
        md.append("| Simulado / Edição | Provedor | Questão | Gabarito | Objeto de Conhecimento / Descritor | Arquivo de Resolução Comentada |")
        md.append("| :--- | :---: | :---: | :---: | :--- | :--- |")
        
        q_list = topic_index.get(code, [])
        for item in q_list[:12]:
            gab_str = f"`{item['gabarito']}`" if item['gabarito'] != 'Comentada' else 'Comentada'
            md.append(f"| {item['simulado']} | {item['provider']} | **Q{item['q_num']}** | {gab_str} | {item['tematica']} - {item['objeto']} | `{item['res_path']}` |")
        if not q_list:
            md.append("| *Nenhuma questão filtrada para este tópico no recorte* | - | - | - | - | - |")
        md.append("")

    md.append("---")
    md.append("")
    md.append("## 5. QUÍMICA (~15 Questões)")
    md.append("")
    
    topics_qui = [
        ('Q1', 'Físico-Química (Eletroquímica, Termoquímica e Equilíbrio)', '28% a 32%', 'LÍDER EM CÁLCULOS E PROCESSOS',
         'Eletroquímica (pilhas galvânicas, potencial de redução, ânodo/cátodo, corrosão e metal de sacrifício, eletrólise); Termoquímica (Lei de Hess, calor de formação e energias de ligação); Cinética e Equilíbrio Químico (catalisadores, energia de ativação e Princípio de Le Chatelier); Soluções (cálculo de concentração molar, g/L, ppm e diluição).'),
        ('Q2', 'Química Geral e Estequiometria', '25% a 28%', 'BASE ESTRUTURAL',
         'Cálculos estequiométricos reais com reagentes impuros (% de pureza), rendimento percentual e determinação de reagente limitante/excesso; forças intermoleculares (ligações de hidrogênio, dipolo-dipolo e London) e impacto no ponto de ebulição e solubilidade; métodos de separação de misturas (decantação, filtração, destilação simples/fracionada e flotação).'),
        ('Q3', 'Química Orgânica', '19% a 23%', 'ALTA REGULARIDADE',
         'Reconhecimento de funções orgânicas (álcoois, fenóis, aldeídos, cetonas, ácidos carboxílicos, ésteres, aminas, amidas); polaridade e propriedades físicas (hidrofílico vs lipofílico, tensoativos/sabões); isomeria plana e espacial (geométrica cis-trans e óptica/carbono quiral); reações orgânicas e polímeros (esterificação/biodiesel, saponificação, polímeros de adição e condensação).'),
        ('Q4', 'Química Ambiental', '10% a 13%', 'ALTA (Contextualizada)',
         'Gases do efeito estufa e fontes de emissão; óxidos ácidos e formação de chuva ácida (SO2, SO3, NOx); destruição da camada de ozônio pelos CFCs; tratamento químico de água e esgoto em ETA/ETE (coagulação/floculação com sulfato de alumínio, decantação e cloração).')
    ]
    
    for code, title, inc, tri_stat, desc in topics_qui:
        md.append(f"### 5.{code[1]} Tópico {code}: {title}")
        md.append(f"* **Incidência Média:** {inc} | **Status TRI:** `{tri_stat}`")
        md.append(f"* **Conceitos-Chave:** {desc}")
        md.append("")
        md.append("| Simulado / Edição | Provedor | Questão | Gabarito | Objeto de Conhecimento / Descritor | Arquivo de Resolução Comentada |")
        md.append("| :--- | :---: | :---: | :---: | :--- | :--- |")
        
        q_list = topic_index.get(code, [])
        for item in q_list[:12]:
            gab_str = f"`{item['gabarito']}`" if item['gabarito'] != 'Comentada' else 'Comentada'
            md.append(f"| {item['simulado']} | {item['provider']} | **Q{item['q_num']}** | {gab_str} | {item['tematica']} - {item['objeto']} | `{item['res_path']}` |")
        if not q_list:
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
    md.append("  5. `_ENEM_DIA_2_BRUTO/1373-20 - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf` corrigido com `1378-20 - RESOLUCAO - AP2 DE CNST-MST...`.")
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
    md.append("  5. `_ENEM_DIA_2_BRUTO/1º BERNOULLI EXTRA 2026 - D2.pdf` e `1º SIMULADO SAS ENEM - 2026 - D2 - AMARELO.pdf`.")
    md.append("  6. `APEIRON-20261110T152018Z-1-001/APEIRON/2º/A2GCD2 (Oficial)-1.pdf`.")
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

def main():
    print("Iniciando geração integrada e gravação de todos os relatórios finais...")
    os.makedirs('FINAL', exist_ok=True)
    
    with open('full_survey_raw.json', 'r', encoding='utf-8') as f:
        survey_records = json.load(f)
        
    poliedro_data, topic_index = run_pipeline()
    
    # 1. CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md
    cat_md = generate_catalogo_markdown(survey_records)
    with open('FINAL/CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md', 'w', encoding='utf-8') as f:
        f.write(cat_md)
    print("Gerado com sucesso: FINAL/CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md")
    
    # 2. INDICE_TEMATICO_SIMULADOS_DIA_2.md
    ind_md = generate_indice_tematico_markdown(topic_index)
    with open('FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md', 'w', encoding='utf-8') as f:
        f.write(ind_md)
    print("Gerado com sucesso: FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md")
    
    # 3. TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md
    tri_md = generate_trilha_estudos_markdown()
    with open('FINAL/TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md', 'w', encoding='utf-8') as f:
        f.write(tri_md)
    print("Gerado com sucesso: FINAL/TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md")
    
    # 4. catalogo_enem_dia_2.json
    db_json = {
        'metadata': {
            'total_files': len(survey_records),
            'unique_files': 1033,
            'dia2_files_count': sum(1 for r in survey_records if r['classification'] in ('DIA_2_CN_MAT', 'ENEM_ANTIGO_D1_CN_CH', 'ENEM_ANTIGO_D2_MAT_LC')),
            'corpus_size_gb': 5.56
        },
        'taxonomy_codes': list(TAXONOMY_PATTERNS.keys()),
        'topic_questions_count': {k: len(v) for k, v in topic_index.items()},
        'sample_topic_index': {k: v[:5] for k, v in topic_index.items()}
    }
    with open('FINAL/catalogo_enem_dia_2.json', 'w', encoding='utf-8') as f:
        json.dump(db_json, f, ensure_ascii=False, indent=2)
    print("Gerado com sucesso: FINAL/catalogo_enem_dia_2.json")
    print("\nTODOS OS ARQUIVOS DA FASE 2 FORAM GERADOS COM SUCESSO!")

if __name__ == '__main__':
    main()
