import os
import sys
import re
import json
import zipfile
import xml.etree.ElementTree as ET
import logging
import pypdf

logging.getLogger("pypdf").setLevel(logging.ERROR)

TAXONOMY_PATTERNS = {
    # MATEMÁTICA
    'M1': ('Matemática Básica e Proporcionalidade', [
        r'\braz[aã]o\b', r'\bpropor[cç]', r'\bescala\b', r'\bregra de tr[eê]s\b', r'\bporcentagem\b',
        r'\baumento\b', r'\bdesconto\b', r'\bconvers[aã]o\b', r'\blitros?\b', r'\bm³\b', r'\bkm/h\b',
        r'\bgrandezas\b', r'\binversamente proporcional\b', r'\bdiretamente proporcional\b'
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

def parse_poliedro_ficha_mapa(xlsx_path):
    with zipfile.ZipFile(xlsx_path) as z:
        shared = []
        if 'xl/sharedStrings.xml' in z.namelist():
            tree = ET.fromstring(z.read('xl/sharedStrings.xml'))
            for elem in tree:
                text = ''.join(elem.itertext())
                shared.append(text)
        
        sheet_tree = ET.fromstring(z.read('xl/worksheets/sheet1.xml'))
        rows = []
        for row in sheet_tree.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}row'):
            r_data = []
            for c in row.iter('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}c'):
                t = c.attrib.get('t')
                v = c.find('{http://schemas.openxmlformats.org/spreadsheetml/2006/main}v')
                val = v.text if v is not None else ''
                if t == 's' and val:
                    try:
                        val = shared[int(val)]
                    except Exception:
                        pass
                r_data.append(val)
            rows.append(r_data)
            
    header = rows[1] if len(rows) > 1 else []
    col_map = {name.strip().upper(): idx for idx, name in enumerate(header)}
    
    questions = []
    for r in rows[2:]:
        if len(r) < 3:
            continue
        q_num = r[col_map.get('QUESTÃO', 0)].strip()
        if not q_num.isdigit():
            continue
        componente = r[col_map.get('COMPONENTE', 2)].strip() if 'COMPONENTE' in col_map and len(r) > col_map['COMPONENTE'] else ''
        gab = r[col_map.get('GABARITO', 6)].strip() if 'GABARITO' in col_map and len(r) > col_map['GABARITO'] else ''
        tematica = r[col_map.get('TEMÁTICA', 7)].strip() if 'TEMÁTICA' in col_map and len(r) > col_map['TEMÁTICA'] else ''
        objeto = r[col_map.get('OBJETO DE CONHECIMENTO', 8)].strip() if 'OBJETO DE CONHECIMENTO' in col_map and len(r) > col_map['OBJETO DE CONHECIMENTO'] else ''
        desc = r[col_map.get('DESCRITOR', 11)].strip() if 'DESCRITOR' in col_map and len(r) > col_map['DESCRITOR'] else ''
        
        # Determine discipline
        disc = 'OUTRO'
        if 'Matemática' in componente:
            disc = 'MAT'
        elif 'Física' in componente:
            disc = 'FIS'
        elif 'Química' in componente:
            disc = 'QUI'
        elif 'Biologia' in componente:
            disc = 'BIO'
            
        full_q_text = f"{tematica} {objeto} {desc}"
        topic_code, topic_name = classify_text_to_topic(full_q_text, disc)
        
        questions.append({
            'num': int(q_num),
            'componente': componente,
            'discipline': disc,
            'gabarito': gab,
            'tematica': tematica,
            'objeto': objeto,
            'descritor': desc,
            'topic_code': topic_code,
            'topic_name': topic_name
        })
    return questions

def extract_pdf_questions(pdf_path, max_pages=80):
    """Extract individual questions from a PDF exam or resolution."""
    questions = []
    try:
        reader = pypdf.PdfReader(pdf_path)
        total_p = min(len(reader.pages), max_pages)
        full_text = ""
        for i in range(total_p):
            t = reader.pages[i].extract_text() or ""
            full_text += f"\n--- PAGE {i+1} ---\n" + t
            
        # Match questions pattern
        q_splits = re.split(r'(?i)(?:QUEST[ÃA]O|Quest[ãa]o)\s+(\d{1,3})', full_text)
        if len(q_splits) > 2:
            for k in range(1, len(q_splits), 2):
                q_num_str = q_splits[k].strip()
                q_body = q_splits[k+1][:1500].strip() if k+1 < len(q_splits) else ""
                if q_num_str.isdigit():
                    q_num = int(q_num_str)
                    if 1 <= q_num <= 180:
                        disc = 'MAT' if q_num > 135 or (46 <= q_num <= 90 and 'matem' in q_body.lower()) else 'CN'
                        topic_code, topic_name = classify_text_to_topic(q_body, disc)
                        questions.append({
                            'num': q_num,
                            'body': q_body[:400],
                            'topic_code': topic_code,
                            'topic_name': topic_name
                        })
    except Exception as e:
        pass
    return questions

def main():
    print("Iniciando processamento e catalogação completa da Fase 2...")
    with open('full_survey_raw.json', 'r', encoding='utf-8') as f:
        records = json.load(f)
        
    print(f"Total de registros na base bruta: {len(records)}")
    
    # 1. Parse all Poliedro Fichas Mapas
    poliedro_fichas = [
        ('POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', 'Poliedro 2024 Simulado 1 Dia 2'),
        ('POLIEDRO/2024/2º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', 'Poliedro 2024 Simulado 2 Dia 2'),
        ('POLIEDRO/2024/3º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', 'Poliedro 2024 Simulado 3 Dia 2'),
        ('POLIEDRO/2024/4º Simulado Enem 2024 - 2º Dia - Ficha Mapa.xlsx', 'Poliedro 2024 Simulado 4 Dia 2'),
        ('POLIEDRO/2024/2024_5_poliedro_enem_3serie_e_pv_ficha_mapa_geral_dia02.xlsx', 'Poliedro 2024 Simulado 5 Dia 2'),
    ]
    
    fichas_indexed = {}
    for fpath, name in poliedro_fichas:
        if os.path.exists(fpath):
            qs = parse_poliedro_ficha_mapa(fpath)
            fichas_indexed[name] = qs
            print(f"Indexado com sucesso {name}: {len(qs)} questões com mapeamento pedagógico.")
            
    # 2. Extract representative questions from Bernoulli, SAS, Apeiron, Enem Oficial
    sample_resolutions = [
        ('BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/1º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf', 'Bernoulli 2019 Simulado 1 Dia 2'),
        ('BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/2º conjunto/2_conj_2019_Gabarito_Questao_comentada_Prova_II.pdf', 'Bernoulli 2019 Simulado 2 Dia 2'),
        ('BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/3º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf', 'Bernoulli 2019 Simulado 3 Dia 2'),
        ('BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/4º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf', 'Bernoulli 2019 Simulado 4 Dia 2'),
        ('BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/5º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf', 'Bernoulli 2019 Simulado 5 Dia 2'),
        ('_ENEM_DIA_2_BRUTO/1242-19_RESOLUCAO_AP2_CNST-MST_3SERIE_1ETAPA.pdf', 'SAS AP2 CNST-MST Resolução 2019'),
        ('_ENEM_DIA_2_BRUTO/1378-20 - RESOLUCAO - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf', 'SAS AP2 CNST-MST Resolução 2020'),
        ('_ENEM_DIA_2_BRUTO/1452-21 - RESOLUCAO - AP2 DE CNST-MST - 3a SERIE - 1a ETAPA _ WILL.pdf', 'SAS AP2 CNST-MST Resolução 2021'),
        ('APEIRON-20261110T152018Z-1-001/APEIRON/2º/A2GCD2 (Oficial)-1.pdf', 'Apeiron 2026 Simulado 2 Resolução D2'),
        ('POLIEDRO/2024/1º Simulado Enem 2024 - 2º Dia - Resolução.pdf', 'Poliedro 2024 Simulado 1 Resolução'),
        ('POLIEDRO/2024/2º Simulado Enem 2024 - 2º Dia - Resolução.pdf', 'Poliedro 2024 Simulado 2 Resolução'),
        ('POLIEDRO/2024/3º Simulado Enem 2024 - 2º Dia - Resolução.pdf', 'Poliedro 2024 Simulado 3 Resolução'),
        ('POLIEDRO/2024/4º Simulado Enem 2024 - 2º Dia - Resolução.pdf', 'Poliedro 2024 Simulado 4 Resolução'),
        ('POLIEDRO/2024/5º Simulado Enem 2024 - 2º Dia - Resolução.pdf', 'Poliedro 2024 Simulado 5 Resolução'),
        ('ENEM/2024/ENEM 2024 DIA 2.pdf', 'ENEM Oficial 2024 Prova Dia 2'),
        ('ENEM/2022/ENEM 2022 DIA 2.pdf', 'ENEM Oficial 2022 Prova Dia 2'),
        ('ENEM/2021/ENEM 2021 DIA 2.pdf', 'ENEM Oficial 2021 Prova Dia 2'),
        ('ENEM/2019/ENEM 2019 DIA 2.pdf', 'ENEM Oficial 2019 Prova Dia 2'),
    ]
    
    extracted_simulados = {}
    for spath, sname in sample_resolutions:
        if os.path.exists(spath):
            qs = extract_pdf_questions(spath)
            if qs:
                extracted_simulados[sname] = {
                    'path': spath,
                    'count': len(qs),
                    'questions': qs
                }
                print(f"Extraídas {len(qs)} questões de {sname} ({spath})")
                
    # Save intermediate extracted data
    out_data = {
        'poliedro_fichas': fichas_indexed,
        'extracted_simulados': extracted_simulados
    }
    with open('extracted_questions_index.json', 'w', encoding='utf-8') as f:
        json.dump(out_data, f, ensure_ascii=False, indent=2)
    print("Salvo extracted_questions_index.json com sucesso.")

if __name__ == '__main__':
    main()
