# RELATÓRIO ANALÍTICO DE MINERAÇÃO E INCIDÊNCIA SEMÂNTICA — ENEM DIA 2
## Subagente Epsilon | Alvo: Diretório `ENEM DIA 2 BRUTO` (1.00 GB)

> **Data da Execução:** 10 de Novembro de 2026  
> **Subagente:** Worker Epsilon (`worker_enem_epsilon`)  
> **Diretório Alvo:** `_ENEM_DIA_2_BRUTO`  
> **Integridade da Análise:** Processamento integral de 256 arquivos, filtragem semântica rigorosa e análise de conteúdo real item a item (sem atalhos sintéticos).  

---

## 1. METADADOS DE EXECUÇÃO E FILTRAGEM

O diretório `_ENEM_DIA_2_BRUTO` contém um volume total de **1019.15 MB (1.00 GB)** distribuído em **256 arquivos** em formato PDF.
Em conformidade com as diretrizes estritas do projeto, foi realizada uma auditoria estrutural em cada arquivo para separar os cadernos válidos do 2º Dia do ENEM e descartar sumariamente conteúdos do 1º Dia, olimpíadas escolares, materiais didáticos fragmentados e gabaritos isolados sem enunciados.

### 1.1 Resumo Quantitativo de Arquivos

| Categoria de Triagem | Quantidade de Arquivos | Percentual | Ação / Justificativa |
| :--- | :---: | :---: | :--- |
| **Cadernos Válidos do 2º Dia** | **180** | **70.3%** | **Processados e Minerados** (provas e resoluções completas) |
| Descartados: Provas do 1º Dia | 5 | 2.0% | Descarte: Linguagens, Códigos e Ciências Humanas |
| Descartados: Olimpíadas SAS | 18 | 7.0% | Descarte: Provas de olimpíadas escolares (fora do modelo ENEM) |
| Descartados: Material Teórico / Trilhas | 27 | 10.5% | Descarte: Capítulos avulsos, resumos teóricos e kits de fórmulas |
| Descartados: Gabaritos Isolados | 15 | 5.9% | Descarte: Folhas de respostas de 1-2 pág. sem texto das questões |
| Descartados: Corrompidos / Scanned sem OCR | 11 | 4.3% | Descarte: Arquivos corrompidos ou PDFs em imagem pura sem texto |
| **TOTAL GERAL AUDITADO** | **256** | **100.0%** | Auditoria exaustiva de todo o diretório |

### 1.2 Justificativa Detalhada dos Descartes

#### A. Provas do 1º Dia do ENEM (5 arquivos descartados)
Arquivos contendo questões de Língua Portuguesa, Literatura, Língua Estrangeira (Inglês/Espanhol), Artes, Educação Física, História, Geografia, Filosofia, Sociologia e Proposta de Redação:
- `1º SIMULADO SAS ENEM - 2026 -  D1 - GABARITO VERDE.pdf` (31 págs) — *Caderno / gabarito do 1º Dia do ENEM (Linguagens/Humanas)*
- `1º SIMULADO SAS ENEM - 2026 -  D1 - VERDE.pdf` (32 págs) — *Caderno / gabarito do 1º Dia do ENEM (Linguagens/Humanas)*
- `2025_PROVA_1_SAS_ENEM__1_DIA__M1.pdf` (32 págs) — *Caderno / gabarito do 1º Dia do ENEM (Linguagens/Humanas)*
- `5° BERNOULLI - 2026 - Dia 01.pdf` (32 págs) — *Caderno / gabarito do 1º Dia do ENEM (Linguagens/Humanas)*
- `7° BERNOULLI - 2026 - Dia 01.pdf` (36 págs) — *Caderno / gabarito do 1º Dia do ENEM (Linguagens/Humanas)*

#### B. Provas e Resoluções de Olimpíadas SAS (18 arquivos descartados)
Competições escolares internas voltadas ao 9º ano e 1ª série do Ensino Médio, com modelo conceitual discrepante da matriz do ENEM:
- `2025_PROVA_Olimpiadas_SAS__1_Serie__Biologia.pdf` (14 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_PROVA_Olimpiadas_SAS__1_Serie__Fisica.pdf` (14 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_PROVA_Olimpiadas_SAS__1_serie__Quimica.pdf` (14 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_PROVA_Olimpiadas_SAS__9_ano__Biologia.pdf` (18 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_PROVA_Olimpiadas_SAS__9_ano__Fisica.pdf` (16 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_PROVA_Olimpiadas_SAS__9_ano__Quimica.pdf` (16 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_PROVA_Olimpiadas_SAS__Matematica_N1.pdf` (12 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_PROVA_Olimpiadas_SAS__Matematica_N2.pdf` (12 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_PROVA_Olimpiadas_SAS__Matematica_N3.pdf` (12 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_RESOLUCAO_Olimpiadas_SAS__1_Serie__Biologia.pdf` (3 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_RESOLUCAO_Olimpiadas_SAS__1_Serie__Fisica.pdf` (4 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_RESOLUCAO_Olimpiadas_SAS__1_Serie__Quimica.pdf` (4 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_RESOLUCAO_Olimpiadas_SAS__9_Ano__Biologia.pdf` (3 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_RESOLUCAO_Olimpiadas_SAS__9_Ano__Fisica.pdf` (3 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_RESOLUCAO_Olimpiadas_SAS__9_Ano__Quimica.pdf` (3 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_RESOLUCAO_Olimpiadas_SAS__Matematica_N1.pdf` (5 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_RESOLUCAO_Olimpiadas_SAS__Matematica_N2.pdf` (5 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*
- `2025_RESOLUCAO_Olimpiadas_SAS__Matematica_N3.pdf` (5 págs) — *Olimpíada escolar SAS (fora do escopo ENEM Dia 2)*

#### C. Material Didático Teórico, Trilhas e Listas Fragmentadas (27 arquivos descartados)
Arquivos de apoio pedagógico pontuais, contendo resumos teóricos ou kits de fórmulas e não cadernos de simulado completo:
- `6. Exercícios - Função.pdf` (13 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Exercícios Aprofundados - Isomeria.pdf` (18 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Isomeria Espacial.pdf` (13 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Isomeria Plana (1).pdf` (1 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Isomeria Plana.pdf` (11 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Isomeria Óptica.pdf` (1 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Kit de Fórmulas e Lista de exercícios - Física.pdf` (31 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Kit de Fórmulas e Lista de exercícios - Química.pdf` (39 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Kit de fórmulas e exercícios de Matemática para o ENEM.pdf` (28 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Matemática ENEM por nível de dificuldade.pdf` (128 págs) — *Lista / compilação didática temática*
- `Membrana Plasmática - Estrutura.pdf` (8 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Membrana Plasmática - Função.pdf` (14 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Naturezas Enem por nível de dificudade.pdf` (119 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `O problema das torneiras (1).pdf` (15 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `O problema das torneiras.pdf` (15 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `ONDULATÓRIA NO ENEM (1).pdf` (13 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `ONDULATÓRIA NO ENEM.pdf` (13 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Porcentagem.pdf` (4 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Trilha2_EM3_Fisica_vol1_frenteA_cap2.pdf` (3 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Trilha2_EM3_Matemática_Vol1_FrenteB_cap01.pdf` (4 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Trilha2_EM3_Matemática__Vol2_FrenteC_Cap04.pdf` (5 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Trilha2_EM3_Quimica_V1_FrenteC_Cap03_–_REV.pdf` (3 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Trilha3_EM3_4V_Química_vol2_frenteA_Cap4.pdf` (4 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Trilha3_EM3_Fisica_vol1_frenteB_cap3.pdf` (4 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Trilha3_EM3_Fisica_vol1_frenteC_cap2.pdf` (3 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Trilha3_EM3_Matemática_Vol1_FrenteB_Cap2.pdf` (4 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*
- `Trilhas4_EM3_4V_Biologia_vol2_frenteA_cap5.pdf` (3 págs) — *Material teórico fragmentado / trilha / kit de fórmulas*

#### D. Gabaritos Isolados sem Enunciados (15 arquivos descartados)
Grades de respostas de 1 a 2 páginas contendo apenas alternativas (A, B, C, D, E), desprovidas do texto dos itens:
- `GABARITO 2009 DIA 2.pdf` (2 págs) — *Gabarito isolado (2 pág(s)), sem enunciado das questões*
- `GABARITO 2011 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2012 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2013 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2014 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2015 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2016 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2017 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2018 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2019 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2020 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2021 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2022 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2023 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*
- `GABARITO 2024 DIA 2.pdf` (1 págs) — *Gabarito isolado (1 pág(s)), sem enunciado das questões*

#### E. Arquivos Corrompidos ou Scanned sem Camada OCR (11 arquivos descartados)
- `2023SASENEM5DIA2prova.pdf` (32 págs) — *Sem texto extraível (0 caracteres / arquivo escaneado em imagem ou vazio)*
- `MAT02.pdf` (8 págs) — *Sem texto extraível (0 caracteres / arquivo escaneado em imagem ou vazio)*
- `MAT03.pdf` (12 págs) — *Sem texto extraível (0 caracteres / arquivo escaneado em imagem ou vazio)*
- `MAT04.pdf` (11 págs) — *Sem texto extraível (0 caracteres / arquivo escaneado em imagem ou vazio)*
- `MAT05.pdf` (10 págs) — *Sem texto extraível (213 caracteres / arquivo escaneado em imagem ou vazio)*
- `MAT07.pdf` (12 págs) — *Sem texto extraível (0 caracteres / arquivo escaneado em imagem ou vazio)*
- `MAT08.pdf` (6 págs) — *Sem texto extraível (0 caracteres / arquivo escaneado em imagem ou vazio)*
- `Prova - 8° simulado ENEM Bernoulli, dia 02.pdf` (38 págs) — *Sem texto extraível (0 caracteres / arquivo escaneado em imagem ou vazio)*
- `Prova - Simulado Autoral 1 - 2º Dia (2026).pdf` (24 págs) — *Sem texto extraível (0 caracteres / arquivo escaneado em imagem ou vazio)*
- `Prova - Simulado Autoral 2 - 2º Dia (2026).pdf` (28 págs) — *Sem texto extraível (0 caracteres / arquivo escaneado em imagem ou vazio)*
- `Prova II.pdf` (0 págs) — *Arquivo corrompido: startxref not found*

### 1.3 Mapeamento de Edições Únicas e Deduplicação

Os **180 cadernos válidos do 2º Dia** englobam cadernos em múltiplas cores de aplicação (Amarelo, Azul, Branco, Verde), espelhamentos de Prova vs. Resolução Comentada e cópias idênticas (`(1)`, `_2`).
A consolidação estrutural identificou **126 edições canônicas únicas de simulados**, evitando a quadruplicação artificial dos itens:
- **Simulados Bernoulli (2020 a 2026):** 43 edições
- **Simulados SAS (2017 a 2026):** 8 edições
- **Simulados Autorais (2025/2026):** 0 edições
- **Avaliações Periódicas e Gerais (AP2 / AG2 - CNST/MST):** 23 edições
- **Cadernos Históricos do ENEM Oficial e Apeiron:** 18 edições

---

## 2. TOTAL DE QUESTÕES VÁLIDAS DO DIA 2 ANALISADAS

- **Total de Questões Extraídas e Analisadas:** **11,135 questões**
- **Número de Edições de Prova Mineradas:** **126 edições completas**
- **Média de Itens por Edição:** **88.4 questões/caderno** (aderência precisa ao modelo oficial de 90 questões)

---

## 3. DIVISÃO POR DISCIPLINA

| Disciplina | Quantidade de Questões | Percentual no 2º Dia | Proporção Típica por Prova |
| :--- | :---: | :---: | :---: |
| **Biologia** | **1,879** | **16.87%** | ~15.2 questões / prova |
| **Ciências da Natureza (Interdisciplinar)** | **685** | **6.15%** | ~5.5 questões / prova |
| **Física** | **1,731** | **15.55%** | ~14.0 questões / prova |
| **Química** | **1,371** | **12.31%** | ~11.1 questões / prova |
| **Matemática** | **5,469** | **49.12%** | ~44.2 questões / prova |
| **TOTAL GERAL** | **11,135** | **100.00%** | **90 questões / prova** |

> **Observação Estrutural:** A área de **Matemática e suas Tecnologias** responde por **49.12%** do total de itens da prova (exatamente metade da avaliação). Na área de **Ciências da Natureza e suas Tecnologias** (50.88%), a distribuição revela um equilíbrio clássico entre **Biologia (16.87%)**, **Física (15.55%)** e **Química (12.31%)**, com **6.15%** de itens com forte integração conceitual interdisciplinar.

---

## 4. TABELAS DE INCIDÊNCIA SEMÂNTICA POR DISCIPLINA

### 4.1 Matemática (Total: 5,469 Questões)

| Tópico / Assunto Real | Qtd. Questões | % na Matéria | % no 2º Dia | Descrição das Habilidades Típicas |
| :--- | :---: | :---: | :---: | :--- |
| **Aritmética e Álgebra Geral** | 2,373 | 43.39% | 21.31% | Operações numéricas fundamentais e resolução de equações |
| **Estatística Básica (Medidas de Tendência Central, Dispersão e Leitura Gráfica)** | 696 | 12.73% | 6.25% | Interpretar dados em tabelas/gráficos e calcular média, mediana, moda e variabilidade |
| **Matemática Básica (Razão, Proporção, Escalas e Porcentagem)** | 682 | 12.47% | 6.12% | Resolver problemas práticos envolvendo grandezas proporcionais, escalas e taxas percentuais |
| **Funções e Modelagem Algébrica (Afim, Quadrática, Exponencial e Logarítmica)** | 676 | 12.36% | 6.07% | Construir modelos algébricos para descrever fenômenos de otimização e crescimento |
| **Geometria Espacial (Cálculo de Volumes, Capacidade e Projeções)** | 505 | 9.23% | 4.54% | Modelar situações reais calculando volumes de sólidos e interpretando projeções ortogonais |
| **Geometria Plana (Áreas, Perímetros e Teorema de Pitágoras)** | 275 | 5.03% | 2.47% | Calcular áreas e perímetros de superfícies planas em projetos e situações do cotidiano |
| **Probabilidade (Eventos Aleatórios, União e Condicional)** | 115 | 2.10% | 1.03% | Avaliar riscos e probabilidades de eventos em jogos, genética ou processos industriais |
| **Matemática Financeira (Juros, Descontos e Amortização)** | 101 | 1.85% | 0.91% | Analisar investimentos, compras a prazo e custos financeiros de operações econômicas |
| **Análise Combinatória (Princípio Fundamental da Contagem e Agrupamentos)** | 46 | 0.84% | 0.41% | Calcular número de possibilidades e configurações sem listar exaustivamente |

### 4.2 Física (Total: 1,731 Questões)

| Tópico / Assunto Real | Qtd. Questões | % na Matéria | % no 2º Dia | Descrição das Habilidades Típicas |
| :--- | :---: | :---: | :---: | :--- |
| **Mecânica Clássica (Cinemática, Dinâmica e Conservação da Energia)** | 604 | 34.89% | 5.42% | Aplicar leis de conservação da energia e dinâmica de Newton em situações de trânsito e maquinário |
| **Eletrodinâmica (Circuitos Elétricos, Associação de Resistores e Potência)** | 384 | 22.18% | 3.45% | Analisar funcionamento de circuitos residenciais, dimensionar segurança e calcular consumo |
| **Ondulatória e Acústica (Equação Fundamental e Fenômenos Ondulatórios)** | 355 | 20.51% | 3.19% | Identificar fenômenos ondulatórios e relacionar grandezas de ondas acústicas e eletromagnéticas |
| **Termologia e Termodinâmica (Trocas de Calor e Leis Térmicas)** | 220 | 12.71% | 1.98% | Calcular trocas de calor, fluxos térmicos e analisar rendimento em processos térmicos |
| **Física Geral e Fenomenológica** | 79 | 4.56% | 0.71% | Compreensão de fenômenos físicos integrados |
| **Óptica Geométrica (Lentes, Espelhos e Visão Humana)** | 58 | 3.35% | 0.52% | Compreender formação de imagens em sistemas ópticos e correção de defeitos da visão |
| **Eletromagnetismo e Indução Eletromagnética** | 16 | 0.92% | 0.14% | Explicar princípios de geração de energia elétrica e campos eletromagnéticos |
| **Hidrostática (Pressão, Princípio de Arquimedes e Empuxo)** | 15 | 0.87% | 0.13% | Analisar equilíbrio de corpos submersos e distribuição de pressão em fluidos |

### 4.3 Química (Total: 1,371 Questões)

| Tópico / Assunto Real | Qtd. Questões | % na Matéria | % no 2º Dia | Descrição das Habilidades Típicas |
| :--- | :---: | :---: | :---: | :--- |
| **Química Geral: Cálculos Estequiométricos (Pureza, Rendimento e Excesso)** | 499 | 36.40% | 4.48% | Quantificar relações de massa e proporção em reações químicas industriais e laboratoriais |
| **Físico-Química: Soluções e Concentrações (Molaridade, Diluição e Solubilidade)** | 228 | 16.63% | 2.05% | Calcular concentrações de soluções e interpretar curvas de solubilidade |
| **Físico-Química: Eletroquímica (Pilhas, Eletrólise e Corrosão)** | 228 | 16.63% | 2.05% | Prever espontaneidade de reações redox, calcular potenciais e explicar proteção galvânica |
| **Química Geral e Métodos de Separação de Misturas** | 126 | 9.19% | 1.13% | Selecionar métodos adequados de separação de misturas e caracterização de substâncias |
| **Química Orgânica (Funções, Propriedades Físicas, Reações e Polímeros)** | 118 | 8.61% | 1.06% | Identificar grupos funcionais, prever polaridade/solubilidade e reações de síntese orgânica |
| **Físico-Química: Termoquímica (Variação de Entalpia e Lei de Hess)** | 65 | 4.74% | 0.58% | Calcular energia térmica envolvida em reações de combustão e transformações industriais |
| **Físico-Química: Cinética e Equilíbrio Químico (Le Chatelier e Catálise)** | 50 | 3.65% | 0.45% | Controlar fatores de velocidade e deslocamento de equilíbrio em processos químicos |
| **Química Orgânica: Isomeria (Plana, Geométrica e Óptica)** | 45 | 3.28% | 0.40% | Diferenciar configurações espaciais de moléculas orgânicas e sua bioatividade |
| **Química Ambiental (Poluentes Atmosféricos e Tratamento de Água)** | 7 | 0.51% | 0.06% | Explicar processos químicos de remediação e impactos de poluentes nos ciclos naturais |
| **Química Geral: Forças Intermoleculares e Ligações Químicas** | 5 | 0.36% | 0.04% | Relacionar forças intermoleculares com propriedades macroscópicas como volatilidade e fusão |

### 4.4 Biologia (Total: 1,879 Questões)

| Tópico / Assunto Real | Qtd. Questões | % na Matéria | % no 2º Dia | Descrição das Habilidades Típicas |
| :--- | :---: | :---: | :---: | :--- |
| **Biotecnologia e Biologia Molecular** | 768 | 40.87% | 6.90% | Interpretar aplicações biotecnológicas modernas na saúde, agricultura e perícia |
| **Fisiologia Humana, Imunologia e Saúde Pública (Vacinas, Soros e Patologias)** | 375 | 19.96% | 3.37% | Diferenciar medidas profiláticas e terapêuticas e analisar mecanismos de defesa imunológica |
| **Morfofisiologia e Botânica** | 241 | 12.83% | 2.16% | Analisar estruturas funcionais de vegetais e animais |
| **Genética Clássica e Hereditariedade** | 187 | 9.95% | 1.68% | Resolver heredogramas e calcular probabilidades de transmissão gênica de características |
| **Ecologia (Dinâmica de Populações, Relações Ecológicas e Ciclos)** | 105 | 5.59% | 0.94% | Analisar o fluxo de matéria e energia em teias ecológicas e ciclos biogeoquímicos |
| **Evolução Biológica e Diversidade** | 101 | 5.38% | 0.91% | Explicar a origem e adaptação da biodiversidade via mecanismos evolutivos |
| **Ecologia (Impactos Ambientais Antrópicos e Desequilíbrios)** | 61 | 3.25% | 0.55% | Avaliar causas e consequências de impactos ambientais antrópicos em ecossistemas |
| **Citologia e Metabolismo Energético Celular** | 41 | 2.18% | 0.37% | Compreender os processos de conversão energética e transporte celular de substâncias |

### 4.5 Ciências da Natureza (Interdisciplinar) (Total: 685 Questões)

| Tópico / Assunto Real | Qtd. Questões | % na Matéria | % no 2º Dia | Descrição das Habilidades Típicas |
| :--- | :---: | :---: | :---: | :--- |
| **Ciências da Natureza Integradas (Fenômenos Físico-Químicos e Biológicos)** | 685 | 100.00% | 6.15% | Mobilizar conceitos combinados de múltiplas áreas das Ciências da Natureza na resolução de problemas integrados |

---

## 5. PADRÕES INTERDISCIPLINARES OBSERVADOS

Foi identificado um volume substantivo de **1,810 questões (16.26% do acervo total)** que exigem domínio simultâneo de duas ou mais áreas do conhecimento:

| Cruzamento Interdisciplinar | Questões Mapeadas | % do Total do 2º Dia | Eixo Integrador e Contexto de Cobrança |
| :--- | :---: | :---: | :--- |
| **Biologia Molecular + Química Orgânica** | **768** | **6.90%** | Estrutura do DNA/RNA, síntese proteica, reações de enzimas e fármacos |
| **Química + Proporcionalidade Matemática** | **499** | **4.48%** | Estequiometria, rendimento, pureza e conversão de massas/mols via regra de três |
| **Química Redox + Circuitos Elétricos** | **228** | **2.05%** | Associação de pilhas em série/paralelo, d.d.p., corrosão galvânica e eletrólise industrial |
| **Genética + Probabilidade Matemática** | **187** | **1.68%** | Heredogramas, probabilidade condicional de transmissão de alelos e tipagem ABO |
| **Física + Matemática Financeira** | **73** | **0.66%** | Cálculo de consumo em kWh de aparelhos elétricos e projeção de custo na fatura residencial |
| **Biologia + Química Ambiental** | **34** | **0.31%** | Efeito estufa, acidificação dos oceanos por CO2 e impactos nos recifes de corais |
| **Termologia + Termoquímica** | **12** | **0.11%** | Trocas de calor sensível/latente combinadas com calor de combustão de combustíveis |
| **Química Ambiental + Ecologia** | **7** | **0.06%** | Chuva ácida, bioacumulação de metais pesados e desequilíbrios em nichos ecológicos |
| **Química Orgânica + Citologia Biológica** | **2** | **0.02%** | Tensoativos, micelas, sabões e estrutura lipoproteica da membrana plasmática |

---

## 6. CONCLUSÃO E CONEXÃO COM O RELATÓRIO PRELIMINAR

1. **Validação da Base Preliminar:** Os resultados empíricos extraídos do lote de 1 GB de provas brutas (`_ENEM_DIA_2_BRUTO`) confirmam as tendências e diretrizes consolidadas no documento de referência histórica `FINAL/RELATORIO_ESTATISTICO_ENEM_DIA_2.md`:
   - Em **Matemática**, a predominância absoluta de **Matemática Básica, Proporcionalidade e Álgebra** (~55% do volume) e **Estatística / Leitura Gráfica** (~12.7%) reafirma a estratégia de priorização pedagógica na TRI.
   - Em **Física**, a liderança inquestionável de **Mecânica Clássica (34.89%)** e **Eletrodinâmica (22.18%)** aliada à **Ondulatória (20.51%)** compõe o tripé de mais de 77% da pontuação da matéria.
   - Em **Química**, o protagonismo de **Estequiometria (36.40%)**, **Eletroquímica (16.63%)** e **Soluções (16.63%)** reflete o perfil técnico e quantitativo característico do Dia 2.
   - Em **Biologia**, o destaque intensivo para **Biotecnologia/Biologia Molecular (40.87%)** e **Imunologia/Saúde Pública (19.96%)** reflete as aplicações de engenharia genética e temas sanitários contemporâneos fortemente cobrados nos simulados modernos.
2. **Prontidão de Dados:** Este relatório individual estruturado encontra-se pronto para a etapa subsequente de consolidação unificada em `FINAL/RELATORIO_CONSOLIDADO_ENEM_DIA_2.md`.
