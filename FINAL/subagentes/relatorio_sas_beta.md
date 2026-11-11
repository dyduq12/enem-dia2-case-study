# Relatório Analítico de Mineração Semântica — SAS (ENEM Dia 2 - Parte 2)
**Subagente**: Worker SAS Beta  
**Data de Execução**: 10/11/2026  
**Diretório Alvo**: `SAS` (Segunda Metade do Acervo — Índices 261 a 522 de 523 arquivos)  
**Escopo**: Exclusivo 2º Dia do ENEM (Matemática e suas Tecnologias; Ciências da Natureza e suas Tecnologias: Física, Química e Biologia)

---

## 1. Metadados de Execução e Auditoria de Arquivos

### 1.1 Delimitação da Carga de Trabalho
O acervo do diretório `SAS` totaliza 523 arquivos. Conforme a diretriz de divisão equitativa de carga:
- **Subagente Alpha (1ª Metade)**: Arquivos de índice 0 a 260 (261 arquivos, concentrando o acervo de pastas anuais `SAS/ENEM` de 2011 a 2026 e o bloco inicial de olimpíadas).
- **Subagente Beta (2ª Metade)**: Arquivos de índice 261 a 522 (262 arquivos, abrangendo as pastas `SAS/OLIMPÍADAS` [segunda parte], `SAS/PROGRAMÁTICA`, `SAS/SAS ENEM COLEGIO`, `SAS/UERJ`, `SAS/UFRS`, `SAS/UNICAMP` e subpastas vazias como `SAS/UECE`).

### 1.2 Resumo Geral de Inventário na 2ª Metade (262 Arquivos)
| Categoria | Quantidade de Arquivos | Descrição / Destino |
|:---|:---:|:---|
| **Arquivos Processados (Provas Dia 2)** | **52** | 42 Provas em PDF (`SAS ENEM COLEGIO`) + 10 Provas em DOCX (`SAS/PROGRAMÁTICA`) com mineração integral de enunciados |
| **Arquivos Correlacionados (Gabaritos / Resoluções)** | **48** | 36 Resoluções Comentadas em PDF (`SAS ENEM COLEGIO`) + 12 Gabaritos Oficiais em DOCX (`SAS/PROGRAMÁTICA`) |
| **Arquivos Descartados (Não-ENEM / Vestibulares)** | **129** | 89 arquivos de Olimpíadas SAS + 30 arquivos de UNICAMP + 8 arquivos de UFRS/UFRGS + 2 arquivos de UERJ |
| **Arquivos Descartados (Dia 1 ENEM / Duplicatas / Raster)** | **33** | 28 arquivos de Linguagens/Humanas/Redação em `PROGRAMÁTICA` + 4 duplicatas idênticas (`_2.pdf`) + 1 PDF rasterizado |
| **Total de Arquivos Auditados** | **262** | Cobertura de 100% da carga atribuída |

---

### 1.3 Arquivos Descartados e Justificativa de Filtragem Sumária

Em cumprimento estrito às regras de integridade e às diretrizes do projeto (descarte de vestibulares não-ENEM e de materiais do 1º Dia):

1. **Olimpíadas Científicas Internas (`SAS/OLIMPÍADAS` — 89 arquivos)**:
   - *Justificativa*: Simulados preparatórios para olimpíadas científicas (OBF, OBQ, OBB, OBM) de 9º ano e ensino médio (ex: `2021OLIMPIADAS1aSERIEBIOprova.pdf`, `2021OLIMPIADAS1aSERIEFISgabarito.pdf`). Não seguem a Matriz de Referência do ENEM nem o formato contextualizado de competências e habilidades.
2. **Vestibulares Regionais e Estaduais (40 arquivos)**:
   - `SAS/UERJ` (2 arquivos: `1 SAS UERJ 2026.pdf`, `2 SIMULADO UERJ 2027 CHA DE HUMANAS.pdf`): Vestibular estadual do Rio de Janeiro e caderno de Ciências Humanas (Dia 1).
   - `SAS/UFRS` (8 arquivos: `2018_SIMULADO_SAS_UFRGS_1oDia.pdf` a `4oDia.pdf` e resoluções): Vestibular tradicional da UFRGS em modelo regional de 4 dias.
   - `SAS/UNICAMP` (30 arquivos: provas e gabaritos de 1ª Fase e 2ª Fase dissertativa de 2016 a 2025): Modelo próprio do vestibular da Universidade Estadual de Campinas.
   - `SAS/UECE` (pastas `Simulados Ari 2025.2` e `2026.1`): Pastas vazias (0 arquivos).
3. **Materiais do 1º Dia do ENEM (`SAS/PROGRAMÁTICA` — 28 arquivos)**:
   - *Justificativa*: Provas e gabaritos contendo exclusivamente Linguagens, Códigos e suas Tecnologias (`LGCH`, `LCCH`), Ciências Humanas (`CH`) e Propostas de Redação (ex: `1746460210628_2020PROGRAMATICAS32aSERIERedacaoprova.docx`, `1748344913298_2025PROGRAMATICAS2_ETAPA1_SERIEREDACAO.docx`, `1748347163206_2025PROGRAMATICAS2_ETAPA2_SERIELGCHPROVA.docx`).
4. **Duplicatas Binárias e Arquivos sem Camada de Texto (`SAS ENEM COLEGIO` — 5 arquivos)**:
   - 4 duplicatas exatas com hash MD5 idêntico aos originais (`1139-21...WILL_2.pdf`, `1452-21...WILL_2.pdf`, `1925-21...ETAPA_2.pdf`, `2125-21...ETAPA_2.pdf`).
   - 1 arquivo rasterizado sem camada de texto (`9183a9_ce9c73fee68d4d13b7d48d7bf776b583.pdf`).
5. **Cadernos de Ciências Humanas pré-2017 (`SAS ENEM COLEGIO` — 945 questões)**:
   - Nas 21 provas do modelo pré-2017 (`CHST-CNST`), as questões 1 a 45 (Ciências Humanas e suas Tecnologias: História, Geografia, Filosofia e Sociologia) foram sumariamente descartadas, retendo-se estritamente as questões 46 a 90 (Ciências da Natureza).

---

### 1.4 Arquivos Processados com Extração Analítica
- **10 Provas Programáticas SAS (.docx)**: `1746460211238_2020PROGRAMATICAS32aSERIECNMATprova`, `1748344913564_2025PROGRAMATICAS2_ETAPA1_SERIEMTCNPROVA`, `1749832546041_2025PROGRAMATICAS1_ETAPA2_SERIEMTCNPROVA`, `1749832546367_2025PROGRAMATICAS2_ETAPA2_SERIEMTCNPROVA`, `1755279226423_2025PROGRAMATICAS3_ETAPA1_SERIEMTCNPROVA`, `1755279302269_2025PROGRAMATICAS3_ETAPA2_SERIEMTCNPROVA`, `1759774118897_2025PROGRAMATICAS4_ETAPA1_SERIEMTCNPROVA`, `1759774497217_2025PROGRAMATICAS4_ETAPA2_SERIEMTCNPROVA`, `1773056619665_PROVA_2026Programaticas1_Etapa1SerieMatematica_e_Ciencias_da_Natureza`, `1773057060163_PROVA_2026Programaticas1_Etapa2SerieMatematica_e_Ciencias_da_Natureza`.
- **21 Provas CNST-MST SAS Colégio (.pdf — 90 Qs Dia 2 cada)**: `1139-21`, `1241-19`, `1373-20`, `1736-18`, `1889-19`, `1925-21`, `2096-20`, `2348-21`, `3221-21`, `3344-18`, `4009-19`, `4096-20`, `4397_18`, `5023-19`, `5314_18`, `6377_18`, `6919-19`, `8623-18`, entre outras.
- **21 Provas CHST-CNST SAS Colégio (.pdf — 45 Qs CN Dia 2 cada)**: `0528_14`, `0910-AP1`, `1 simulado 0733-15`, `1054-15`, `1152-14`, `1314-15`, `1318-15`, `1435-14`, `1511-17`, `1738-16`, `2930-16`, `3999-16`, `4437-14`, `4487-16`, `4815-14`, `4simulado`, `5623-16`, `5simulado`, `6simulado`, `provavp1`, `vp3_2a-etapa_5o-simulado`.
- **48 Arquivos de Resolução Comentada e Gabaritos Oficiais Correlacionados**: Validação conceitual cruzada de resoluções completas (como `1242-19`, `1378-20`, `1452-21`, `1737-18`, `2097-20`, `2125-21`, `2220-19`, `2349-21`, `2617-14`, `3222-21`, `3552-18`, `4097-20`, `4398_18`, `4669-14`, `5315_18`, `6378_18`, `8624-18`, etc.).

---

## 2. Total de Questões Válidas do Dia 2 Analisadas

- **Total Geral de Questões Válidas do 2º Dia do ENEM**: **3.696 questões**
- **Composição por Origem**:
  - `SAS ENEM COLEGIO` (Provas CNST-MST completas): 1.890 questões
  - `SAS ENEM COLEGIO` (Provas CHST-CNST, fração de Natureza): 945 questões
  - `SAS/PROGRAMÁTICA` (Provas Programáticas Dia 2): 861 questões

---

## 3. Divisão Geral por Disciplina

| Disciplina | Quantidade de Questões | Percentual da Amostra |
|:---|:---:|:---:|
| **Matemática e suas Tecnologias** | **1.439** | **38,93%** |
| **Física** | **1.131** | **30,60%** |
| **Biologia** | **573** | **15,50%** |
| **Química** | **553** | **14,96%** |
| **Total Consolidado** | **3.696** | **100,00%** |

*Nota Estrutural*: As Ciências da Natureza agregadas (Física, Química e Biologia) somam **2.257 questões (61,07%)**, refletindo a presença das provas pré-2017 focadas em Natureza combinadas com as provas pós-2017 balanceadas em 50% Natureza e 50% Matemática.

---

## 4. Tabela de Incidência Semântica por Disciplina

### 4.1 Matemática e suas Tecnologias (1.439 questões)

| Tópico / Assunto Real | Qtd | % Disciplina | % Global | Descrição das Habilidades Típicas (Matriz ENEM) |
|:---|:---:|:---:|:---:|:---|
| **Aritmética e Proporcionalidade** | 677 | 47,05% | 18,32% | Razão, proporção, regra de três simples/composta, grandezas direta e inversamente proporcionais, escalas numéricas e cartográficas, operações com números racionais e decimais, conversão de unidades de medida (H1, H2, H3, H4). |
| **Geometria Plana** | 303 | 21,06% | 8,20% | Cálculo de áreas de superfícies poligonais (triângulos, quadriláteros, trapézios) e circulares, perímetro, Teorema de Pitágoras, semelhança de triângulos, pavimentações, congruência e simetrias (H6, H7, H8). |
| **Geometria Espacial** | 127 | 8,83% | 3,44% | Cálculo de volumes e capacidades de sólidos geométricos (prismas, cilindros, cones, esferas, pirâmides e troncos; modelagem de silos e reservatórios), áreas de superfície, planificação e projeções ortogonais (H7, H9). |
| **Matemática Financeira e Porcentagem** | 107 | 7,44% | 2,90% | Aplicação de porcentagens, aumentos e descontos sucessivos, margem de lucro e custo, juros simples e juros compostos aplicados à tomada de decisão cotidiana (H1, H3, H5). |
| **Probabilidade** | 80 | 5,56% | 2,16% | Cálculo de probabilidade clássica, probabilidade da união e interseção, probabilidade condicional e análise de riscos em situações práticas e amostrais (H28, H29). |
| **Funções e Álgebra** | 77 | 5,35% | 2,08% | Interpretação algébrica e geométrica de função afim (taxa de variação e coeficiente linear), função quadrática (vértice, máximos e mínimos, lançamentos parabólicos), funções exponenciais e logarítmicas, PA e PG (H19, H20, H21). |
| **Estatística e Análise de Dados** | 50 | 3,47% | 1,35% | Cálculo e interpretação de medidas de tendência central (média aritmética simples, média ponderada, mediana, moda), análise de dispersão (desvio-padrão) e leitura crítica de infográficos e histogramas (H27, H28). |
| **Trigonometria** | 10 | 0,69% | 0,27% | Resolução de triângulos retângulos (seno, cosseno, tangente), ângulos de elevação e depressão, ciclo trigonométrico e modelos periódicos (H6, H8). |
| **Análise Combinatória** | 8 | 0,56% | 0,22% | Princípio fundamental da contagem, combinações simples, permutações com repetição e agrupamentos com restrição de posições (H2, H3). |

---

### 4.2 Física (1.131 questões)

| Tópico / Assunto Real | Qtd | % Disciplina | % Global | Descrição das Habilidades Típicas (Matriz ENEM) |
|:---|:---:|:---:|:---:|:---|
| **Eletrodinâmica** | 400 | 35,37% | 10,82% | Análise de circuitos elétricos residenciais, associação de resistores em série e paralelo, cálculo de potência elétrica ($P = U \cdot i = R \cdot i^2$), consumo de energia em kWh e dimensionamento de disjuntores e fusíveis de proteção (H1, H2, H5, H6). |
| **Mecânica - Cinemática e Dinâmica** | 205 | 18,13% | 5,55% | Movimento retilíneo uniforme e variado, interpretação de gráficos espaço-tempo e velocidade-tempo, Leis de Newton, forças de atrito, tração, plano inclinado e dinâmica do movimento circular (H17, H18, H20). |
| **Termologia e Termodinâmica** | 203 | 17,95% | 5,49% | Calorimetria e balanço térmico ($Q = m \cdot c \cdot \Delta T$ e $Q = m \cdot L$), processos de transmissão de calor (condução, convecção e irradiação), 1ª e 2ª leis da termodinâmica, máquinas térmicas e rendimento de motores (H1, H2, H17). |
| **Ondulatória e Acústica** | 135 | 11,94% | 3,65% | Equação fundamental da onda ($v = \lambda \cdot f$), fenômenos ondulatórios (reflexão, refração, difração, interferência, polarização e ressonância), efeito Doppler e qualidades fisiológicas do som (intensidade, altura e timbre) (H1, H17, H19). |
| **Eletromagnetismo e Eletrostática** | 69 | 6,10% | 1,87% | Indução eletromagnética (Leis de Faraday e Lenz), princípio de funcionamento de transformadores e motores elétricos, campo magnético gerado por correntes e eletrização / Lei de Coulomb (H1, H5, H17). |
| **Óptica Geométrica** | 57 | 5,04% | 1,54% | Leis da reflexão e refração, formação de imagens em espelhos esféricos e lentes delgadas, prisma e dispersão luminosa, correção de anomalias visuais (miopia, hipermetropia) (H17, H20). |
| **Hidrostática** | 40 | 3,54% | 1,08% | Pressão hidrostática, teorema de Stevin, vasos comunicantes, princípio de Pascal (prensas hidráulicas) e princípio de Arquimedes (empuxo e condições de flutuação de corpos) (H17, H18). |
| **Mecânica - Trabalho, Energia e Potência** | 22 | 1,95% | 0,60% | Teorema da energia mecânica, transformações e conservação de energias cinética, potencial gravitacional e elástica, rendimento mecânico e dissipação de energia (H1, H2, H17). |

---

### 4.3 Química (553 questões)

| Tópico / Assunto Real | Qtd | % Disciplina | % Global | Descrição das Habilidades Típicas (Matriz ENEM) |
|:---|:---:|:---:|:---:|:---|
| **Química Geral: Tabela Periódica, Átomo e Funções** | 154 | 27,85% | 4,17% | Modelos atômicos, propriedades periódicas dos elementos (eletronegatividade, raio atômico, energia de ionização), identificação e comportamento de funções inorgânicas (ácidos, bases, sais e óxidos ácidos/básicos) (H17, H18). |
| **Físico-Química: Soluções e Estequiometria** | 120 | 21,70% | 3,25% | Cálculo estequiométrico em reações com pureza e rendimento, identificação de reagente limitante, expressões de concentração (molaridade mol/L, título, ppm), diluição e titulação ácido-base (H17, H19, H21). |
| **Química Orgânica: Funções e Nomenclatura** | 100 | 18,08% | 2,71% | Reconhecimento de grupos funcionais em fármacos e biomoléculas (hidrocarbonetos, álcoois, fenóis, aldeídos, cetonas, ácidos carboxílicos, ésteres, aminas e amidas) e nomenclatura sistemática IUPAC (H17, H18). |
| **Físico-Química: Eletroquímica e Equilíbrio** | 67 | 12,12% | 1,81% | Funcionamento de pilhas galvânicas, determinação de potencial padrão de redução ($\Delta E^\circ$), eletrólise aquosa/ígnea, proteção contra corrosão (metal de sacrifício), princípio de Le Chatelier e escala de pH/pOH (H17, H19, H21). |
| **Química Ambiental** | 36 | 6,51% | 0,97% | Ciclo do carbono, mecanismos de formação e impacto da chuva ácida ($\text{SO}_x, \text{NO}_x$), efeito estufa, destruição da camada de ozônio por CFCs, processos de tratamento de água e efluentes industriais (H1, H3, H12). |
| **Química Orgânica: Propriedades, Reações e Polímeros** | 35 | 6,33% | 0,95% | Polaridade e forças intermoleculares em orgânicos, solubilidade e pontos de ebulição, isomeria espacial (geométrica cis-trans e óptica com carbono quiral), reações de esterificação/saponificação e síntese de polímeros (PET, polietileno) (H17, H18, H24). |
| **Físico-Química: Termoquímica e Cinética** | 21 | 3,80% | 0,57% | Variação de entalpia ($\Delta H$), processos endotérmicos e exotérmicos, aplicação da Lei de Hess, energia de ligação, fatores determinantes da velocidade das reações e ação de catalisadores na redução da energia de ativação (H17, H19). |
| **Química Geral e Inorgânica: Ligações e Geometria** | 20 | 3,62% | 0,54% | Diferenciação entre ligações iônica, covalente e metálica, predição de geometria molecular (linear, angular, trigonal plana, tetraédrica) e determinação da polaridade molecular e forças intermoleculares (H17, H18). |

---

### 4.4 Biologia (573 questões)

| Tópico / Assunto Real | Qtd | % Disciplina | % Global | Descrição das Habilidades Típicas (Matriz ENEM) |
|:---|:---:|:---:|:---:|:---|
| **Genética e Biologia Molecular** | 156 | 27,23% | 4,22% | Primeira e Segunda Leis de Mendel, heredogramas, grupos sanguíneos (sistema ABO e fator Rh), estrutura dos ácidos nucleicos (DNA/RNA), replicação, transcrição, código genético e tradução proteica, mutações e herança ligada ao sexo (H14, H15, H16). |
| **Citologia, Bioquímica e Metabolismo** | 126 | 21,99% | 3,41% | Estrutura e permeabilidade da membrana plasmática (osmose, difusão e transporte ativo), função das organelas celulares, ação de enzimas, respiração celular aeróbica, fermentação e fotossíntese (fase clara e escura) (H13, H14). |
| **Fisiologia Humana e Saúde Pública** | 87 | 15,18% | 2,35% | Integração dos sistemas corporais (digestório, cardiovascular, respiratório, excretor e endócrino), imunologia ativa vs. passiva (soros e vacinas), epidemiologia e medidas profiláticas de viroses, bacterioses e parasitoses tropicais (H13, H14, H16). |
| **Evolução Biológica** | 78 | 13,61% | 2,11% | Teorias evolutivas (Lamarckismo vs. Darwinismo vs. Teoria Sintética), ação da seleção natural, adaptações ecológicas, evidências da evolução (homologias, analogias, fósseis) e mecanismos de especiação alopátrica e simpátrica (H15, H16). |
| **Ecologia e Meio Ambiente** | 62 | 10,82% | 1,68% | Dinâmica de populações e comunidades, cadeias e teias tróficas, pirâmides ecológicas, ciclos biogeoquímicos (água, nitrogênio e carbono), impactos antrópicos (eutrofização artificial, bioacumulação) e preservação ambiental (H10, H11, H12). |
| **Botânica** | 58 | 10,12% | 1,57% | Evolução e classificação dos grandes grupos vegetais (briófitas a angiospermas), tecidos condutores de seiva (xilema e floema), fisiologia dos hormônios vegetais (auxinas, etileno), transpiração estomática e reprodução vegetal (H14, H15). |
| **Biotecnologia e Engenharia Genética** | 6 | 1,05% | 0,16% | Tecnologia do DNA recombinante, organismos geneticamente modificados (transgênicos), clonagem celular e terapia gênica, clonagem e técnicas de PCR/eletroforese (H14, H16). |

---

## 5. Padrões Interdisciplinares Observados

A análise semântica das questões do acervo SAS Dia 2 revelou um expressivo grau de intersecção entre as quatro disciplinas, confirmando que o exame avalia a integração conceitual em cenários aplicados do mundo real.

### 5.1 Matriz de Conexões Interdisciplinares Mapeadas
| Par Interdisciplinar | Ocorrências Mapeadas | Descrição dos Padrões e Cruzamentos Típicos |
|:---|:---:|:---|
| **Física x Matemática** | **171** | Resolução de problemas de cinemática e circuitos que exigem modelagem por funções afins ou quadráticas, análise de áreas sob curvas em gráficos de potência e velocidade, e trigonometria em decomposição vetorial e lentes ópticas. |
| **Química x Física** | **96** | Termoquímica e calorimetria associadas à conservação de energia e balanço térmico de reações; processos de eletroquímica (pilhas e eletrólise) integrados com conceitos de ddp, corrente elétrica, resistência interna e potência dissipada. |
| **Física x Química** | **84** | Fenômenos de absorção e emissão de radiação eletromagnética em transições eletrônicas; dilatação e comportamento de gases ideais sob leis termodinâmicas e estequiométricas (equação de Clapeyron $PV=nRT$). |
| **Biologia x Matemática** | **72** | Genética quantitativa e mendeliana com cálculo de probabilidades compostas e árvores de decisão; dinâmica populacional e curvas de crescimento exponencial/logístico em ecologia analisadas através de gráficos e razões matemáticas. |
| **Química x Matemática** | **64** | Relações de proporcionalidade estequiométrica rigorosa, cálculo de concentrações com regras de três compostas, diluições sucessivas, funções logarítmicas na determinação de pH ($-\log[\text{H}^+]$) e rendimento percentual. |
| **Biologia x Física** | **62** | Biofísica da visão humana (óptica da formação da imagem na retina e correção por lentes esféricas); biofísica do sistema circulatório (hidrodinâmica do fluxo sanguíneo e pressão arterial); termorregulação de endotérmicos e ectotérmicos baseada em trocas de calor por condução e convecção. |
| **Matemática x Física** | **60** | Questões da prova de Matemática que utilizam contextos físicos (como escalas de termômetros, cálculo de vazão e tempo de enchimento de reservatórios por hidrostática) como pretexto para proporcionalidade e funções. |
| **Matemática x Química** | **56** | Questões de Matemática contextualizadas em receitas químicas, misturas de soluções com diferentes percentuais de pureza e interpretação de tabelas nutricionais e isotópicas. |
| **Química x Biologia** | **40** | Bioquímica celular (ação enzimática e desnaturação por variação de pH e temperatura), fotossíntese e respiração celular com balanceamento químico e transferência de elétrons, e impacto toxicológico de poluentes lipossolúveis (bioacumulação). |
| **Biologia x Química** | **30** | Estrutura química de biomoléculas (aminoácidos, lipídios saturados e insaturados, pontes de hidrogênio na dupla-hélice do DNA) e reações de fermentação alcoólica e lática aplicadas à biotecnologia. |
| **Matemática x Biologia** | **30** | Questões de modelagem estatística aplicadas à incidência de doenças, taxas de eficácia vacinal, prevalência alélica na genética de populações e dimensionamento de áreas de preservação florestal. |
| **Física x Biologia** | **29** | Mecânica da locomoção e alavancas osteomusculares no corpo humano; bioacústica (faixas de audição de mamíferos, ecolocalização em morcegos e baleias por ultrassom e efeito Doppler). |

---

## 6. Conclusões e Destaques Estatísticos

1. **Predominância Operacional de Aritmética e Proporcionalidade em Matemática**:
   - Quase metade da prova de Matemática (47,05% das questões) assenta-se sobre razão, proporção, regra de três e escalas, constituindo a base de sustentação da nota pela Teoria de Resposta ao Item (TRI).
   - Geometria Plana e Espacial somadas representam quase 30% das questões, destacando-se o cálculo de áreas, perímetros e volumes aplicados a embalagens, construções civis e capacidade de armazenagem.

2. **Hegemonia de Eletrodinâmica e Mecânica em Física**:
   - Eletrodinâmica responde por 35,37% de toda a Física minerada no acervo SAS, sendo o assunto com maior densidade de questões na disciplina, concentrando-se fortemente no consumo consciente de energia elétrica, dimensionamento de circuitos domésticos e leis de Ohm.
   - Mecânica Clássica (Cinemática, Dinâmica e Energia) e Termologia formam o segundo grande pilar, somando conjuntamente mais de 40% das questões de Física.

3. **Foco Funcional em Química Geral e Estequiometria**:
   - Em Química, há um equilíbrio notável entre Química Geral/Inorgânica (propriedades periódicas e funções, 27,85%), Cálculos Estequiométricos/Soluções (21,70%) e Química Orgânica (identificação funcional e propriedades físico-químicas, somando mais de 24%).

4. **Biologia Centrada em Biologia Celular, Genética e Saúde**:
   - A tríade Genética/Biologia Molecular (27,23%), Citologia/Metabolismo (21,99%) e Fisiologia Humana/Saúde Pública (15,18%) compõe cerca de 65% de toda a Biologia, demonstrando a ênfase em processos celulares, mecanismos de herança e políticas públicas de imunização e combate a endemias.
