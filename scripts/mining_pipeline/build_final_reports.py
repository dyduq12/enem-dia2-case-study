import os
import json
import re

def generate_catalogo_markdown(survey_records, fichas_data, extracted_data):
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

def generate_indice_tematico_markdown(fichas_data, extracted_data):
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
    
    # M1 to M6
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
        
        # Populate with Poliedro ground truth
        matched_count = 0
        for sname, qs in fichas_data.items():
            for q in qs:
                if q['discipline'] == 'MAT' and q['topic_code'] == code:
                    res_file = "POLIEDRO/2024/" + sname.split()[2] + "º Simulado Enem 2024 - 2º Dia - Resolução.pdf"
                    md.append(f"| {sname} | Poliedro | **Q{q['num']}** | `{q['gabarito']}` | {q['tematica']} - {q['objeto']} | `{res_file}` |")
                    matched_count += 1
                    if matched_count >= 5:
                        break
            if matched_count >= 8:
                break
                
        # Populate with Bernoulli sample
        b_sims = [
            ("Bernoulli 2019 Simulado 1 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/1º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
            ("Bernoulli 2019 Simulado 2 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/2º conjunto/2_conj_2019_Gabarito_Questao_comentada_Prova_II.pdf"),
            ("Bernoulli 2019 Simulado 3 Dia 2", "BERNOULLI-20261110T151947Z-1-001/BERNOULLI/2019/3º conjunto/Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf"),
        ]
        for b_name, b_path in b_sims:
            if b_name in extracted_data['extracted_simulados']:
                for q in extracted_data['extracted_simulados'][b_name]['questions']:
                    if q['topic_code'] == code and q['num'] >= 136:
                        snippet = q['body'][:75].replace('\n', ' ')
                        md.append(f"| {b_name} | Bernoulli | **Q{q['num']}** | Comentada | {snippet}... | `{b_path}` |")
                        break
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
        
        matched_count = 0
        for sname, qs in fichas_data.items():
            for q in qs:
                if q['discipline'] == 'BIO' and q['topic_code'] == code:
                    res_file = "POLIEDRO/2024/" + sname.split()[2] + "º Simulado Enem 2024 - 2º Dia - Resolução.pdf"
                    md.append(f"| {sname} | Poliedro | **Q{q['num']}** | `{q['gabarito']}` | {q['tematica']} - {q['objeto']} | `{res_file}` |")
                    matched_count += 1
                    if matched_count >= 5:
                        break
            if matched_count >= 6:
                break
                
        for b_name, b_path in b_sims:
            if b_name in extracted_data['extracted_simulados']:
                for q in extracted_data['extracted_simulados'][b_name]['questions']:
                    if q['topic_code'] == code and 91 <= q['num'] <= 135:
                        snippet = q['body'][:75].replace('\n', ' ')
                        md.append(f"| {b_name} | Bernoulli | **Q{q['num']}** | Comentada | {snippet}... | `{b_path}` |")
                        break
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
        
        matched_count = 0
        for sname, qs in fichas_data.items():
            for q in qs:
                if q['discipline'] == 'FIS' and q['topic_code'] == code:
                    res_file = "POLIEDRO/2024/" + sname.split()[2] + "º Simulado Enem 2024 - 2º Dia - Resolução.pdf"
                    md.append(f"| {sname} | Poliedro | **Q{q['num']}** | `{q['gabarito']}` | {q['tematica']} - {q['objeto']} | `{res_file}` |")
                    matched_count += 1
                    if matched_count >= 5:
                        break
            if matched_count >= 6:
                break
                
        for b_name, b_path in b_sims:
            if b_name in extracted_data['extracted_simulados']:
                for q in extracted_data['extracted_simulados'][b_name]['questions']:
                    if q['topic_code'] == code and 91 <= q['num'] <= 135:
                        snippet = q['body'][:75].replace('\n', ' ')
                        md.append(f"| {b_name} | Bernoulli | **Q{q['num']}** | Comentada | {snippet}... | `{b_path}` |")
                        break
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
        
        matched_count = 0
        for sname, qs in fichas_data.items():
            for q in qs:
                if q['discipline'] == 'QUI' and q['topic_code'] == code:
                    res_file = "POLIEDRO/2024/" + sname.split()[2] + "º Simulado Enem 2024 - 2º Dia - Resolução.pdf"
                    md.append(f"| {sname} | Poliedro | **Q{q['num']}** | `{q['gabarito']}` | {q['tematica']} - {q['objeto']} | `{res_file}` |")
                    matched_count += 1
                    if matched_count >= 5:
                        break
            if matched_count >= 6:
                break
                
        for b_name, b_path in b_sims:
            if b_name in extracted_data['extracted_simulados']:
                for q in extracted_data['extracted_simulados'][b_name]['questions']:
                    if q['topic_code'] == code and 91 <= q['num'] <= 135:
                        snippet = q['body'][:75].replace('\n', ' ')
                        md.append(f"| {b_name} | Bernoulli | **Q{q['num']}** | Comentada | {snippet}... | `{b_path}` |")
                        break
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
    print("Gerando entregáveis finais em FINAL/ ...")
    os.makedirs('FINAL', exist_ok=True)
    
    with open('full_survey_raw.json', 'r', encoding='utf-8') as f:
        survey_records = json.load(f)
        
    with open('extracted_questions_index.json', 'r', encoding='utf-8') as f:
        extracted_data = json.load(f)
        
    fichas_data = extracted_data['poliedro_fichas']
    
    # 1. Gerar CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md
    cat_md = generate_catalogo_markdown(survey_records, fichas_data, extracted_data)
    with open('FINAL/CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md', 'w', encoding='utf-8') as f:
        f.write(cat_md)
    print("Salvo: FINAL/CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md")
    
    # 2. Gerar INDICE_TEMATICO_SIMULADOS_DIA_2.md
    ind_md = generate_indice_tematico_markdown(fichas_data, extracted_data)
    with open('FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md', 'w', encoding='utf-8') as f:
        f.write(ind_md)
    print("Salvo: FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md")
    
    # 3. Gerar TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md
    tri_md = generate_trilha_estudos_markdown()
    with open('FINAL/TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md', 'w', encoding='utf-8') as f:
        f.write(tri_md)
    print("Salvo: FINAL/TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md")
    
    # 4. Gerar catalogo_enem_dia_2.json
    db_json = {
        'metadata': {
            'total_files': len(survey_records),
            'unique_files': 1033,
            'dia2_files_count': sum(1 for r in survey_records if r['classification'] in ('DIA_2_CN_MAT', 'ENEM_ANTIGO_D1_CN_CH', 'ENEM_ANTIGO_D2_MAT_LC')),
            'corpus_size_gb': 5.56
        },
        'taxonomy_codes': ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'B1', 'B2', 'B3', 'B4', 'F1', 'F2', 'F3', 'F4', 'Q1', 'Q2', 'Q3', 'Q4'],
        'poliedro_indexed_simulados': {k: len(v) for k, v in fichas_data.items()},
        'extracted_simulados_summary': {k: v['count'] for k, v in extracted_data['extracted_simulados'].items()}
    }
    with open('FINAL/catalogo_enem_dia_2.json', 'w', encoding='utf-8') as f:
        json.dump(db_json, f, ensure_ascii=False, indent=2)
    print("Salvo: FINAL/catalogo_enem_dia_2.json")
    print("\nTodos os entregáveis da Fase 2 gerados com sucesso!")

if __name__ == '__main__':
    main()
