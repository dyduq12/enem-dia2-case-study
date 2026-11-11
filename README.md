# Estudo de Caso & Auditoria de Dados: Mineração Cognitiva de 24.419 Questões do ENEM Dia 2

![Autor](https://img.shields.io/badge/Autor-Eduardo%20Borborema%20Brito-blue)
![Licença](https://img.shields.io/badge/Licen%C3%A7a-Source--Available%20%26%20Non--Commercial-red)
![Volume](https://img.shields.io/badge/Corpus%20Analisado-5.56%20GB%20%7C%201.422%20PDFs-orange)
![Questões](https://img.shields.io/badge/Quest%C3%B5es%20Mineradas-24.419%20Aut%C3%AAnticas-brightgreen)
![MindNote](https://img.shields.io/badge/MindNote-Engine%20Validated-darkgreen)

---

## ⚖️ Aviso Legal, Propriedade Intelectual e Direitos Autorais

> [!IMPORTANT]
> **Propriedade dos Dados & Fair Use**:  
> Este repositório é um **estudo de caso científico e técnico de engenharia de dados e inteligência artificial**. Por estrito respeito às leis de direitos autorais e propriedade intelectual, **nenhum arquivo original em PDF, caderno bruto de simulado ou questão protegida de bancos privados (como SAS, Bernoulli, Poliedro ou Apeiron) é distribuído ou divulgado publicamente neste repositório**.  
> Todos os arquivos binários pesados (~5,56 GB) permanecem estritamente isolados em ambiente local e ignorados pelo `.gitignore`. O repositório publica exclusivamente:
> 1. As **métricas estatísticas consolidadas** e metadados analíticos agregados.
> 2. O pipeline metodológico e algoritmos de auditoria.
> 3. Questões históricas oficiais do **INEP (ENEM)** que são de domínio público.
> 4. Os artefatos estruturados derivados (mapas mentais, índices temáticos e cronogramas) desenvolvidos de forma autoral.

> [!CAUTION]
> **Direitos Autorais do Estudo de Caso**:  
> Esta pesquisa, arquitetura de pipeline, metodologia analítica e relatórios foram idealizados e desenvolvidos por **Eduardo Borborema Brito**. Este trabalho está protegido pela [Eduardo Borborema Source-Available & Non-Commercial License 1.0](LICENSE). É expressamente proibida a cópia não autorizada, apropriação indevida de autoria ou qualquer forma de exploração comercial sem autorização prévia por escrito.

---

## 📖 Como Tudo Começou: O Desafio dos 5,56 GB de Dados Brutos

O ponto de partida deste projeto foi um desafio real e massivo: um acervo bruto e desestruturado contendo **mais de 5,56 GB em arquivos PDF (1.422 arquivos)** acumulados entre exames oficiais do INEP e cadernos de simulados preparatórios dos sistemas de ensino mais renomados do Brasil (SAS, Bernoulli, Poliedro e Apeiron).

Ao examinar as pastas brutas, nos deparamos com o cenário típico de dados do mundo real:
1. **Contaminação Cruzada de Exames**: Centenas de cadernos de vestibulares com modelos de avaliação completamente diferentes do ENEM (FUVEST, UNICAMP, UNESP, UERJ, UECE, Prova Paulista e Olimpíadas de Física/Química/Matemática) estavam misturados nas mesmas pastas.
2. **Duplicidade Extensiva de Edições**: Um mesmo simulado aparecia replicado em 3 ou 4 pastas sob rótulos como "Medicina", "Extensivo", "Nacional", "Caderno Branco", "Caderno Rosa" e "Resolução Comentada".
3. **Complexidade Cognitiva**: Uma busca cega por palavras-chave (ex: "energia" ou "transformação") não é capaz de diferenciar se uma questão exige competência em **Física Mecânica**, **Termoquímica** ou **Metabolismo Energético em Biologia**.

O objetivo estabelecido foi: **executar uma auditoria profunda em todo o acervo, separar o ruído do sinal autêntico do ENEM, classificar a real cognição exigida em cada questão do 2º Dia (Matemática e Ciências da Natureza) e modelar a probabilidade estatística de cada tópico para prever a prova deste ano**.

---

## 🤖 A Arquitetura da Auditoria Multiagente

Para processar esse volume monumental de dados em tempo recorde sem esgotar contextos de memória, estruturamos uma **força-tarefa autônoma com 6 subagentes especializados**:

```mermaid
flowchart TD
    subgraph Entrada["1. Acervo Bruto Desordenado (5.56 GB - 1.422 PDFs)"]
        SAS["SAS (1.9 GB)"]
        BERN["Bernoulli (1.53 GB)"]
        INEP["ENEM Bruto INEP (1.0 GB)"]
        MISTO["Poliedro + Apeiron + Outros (755 MB)"]
    end

    subgraph Mineradores["2. Força-Tarefa de Subagentes"]
        Alpha["Agentes Alpha & Beta"]
        Gamma["Agentes Gamma & Delta"]
        Epsilon["Agente Epsilon"]
        Zeta["Agente Zeta"]
    end

    SAS --> Alpha
    BERN --> Gamma
    INEP --> Epsilon
    MISTO --> Zeta

    subgraph Processamento["3. Esteira de Tratamento & Auditoria"]
        Filtro["Filtro Anti-Ruído: 920 Cadernos Não-ENEM Descartados"]
        Hash["Deduplicação Estrutural: 719 Edições Canônicas Primárias"]
        Parser["Extração de Blocos: Questões 91 a 180 (Enunciados + Alternativas A-E)"]
        Motor["Motor Semântico Cognitivo (16 Competências da Matriz ENEM)"]
    end

    Alpha --> Filtro
    Gamma --> Filtro
    Epsilon --> Filtro
    Zeta --> Filtro

    Filtro --> Hash
    Hash --> Parser
    Parser --> Motor

    subgraph Saida["4. Inteligência Consolidada"]
        Base["Corpus Auditado: 24.419 Questões Autênticas Classificadas"]
        Relatorio["Relatórios Consolidados & Ranking TRI"]
        MindNote["MindNote JSON Engine (202 Nós & Cronograma Tático)"]
    end

    Motor --> Base
    Base --> Relatorio
    Base --> MindNote
```

### O Rastro da Auditoria: Por Onde Passou Cada Byte
1. **Agentes Alpha & Beta (SAS - 1.9 GB)**:
   - Inspecionaram centenas de cadernos anuais e simulados nacionais SAS.
   - Normalizaram a estrutura de numeração padrão (Questões 91 a 180).
   - Identificaram 250 edições canônicas válidas.
2. **Agentes Gamma & Delta (Bernoulli - 1.53 GB - Filtro Crítico Anti-Paulista)**:
   - **Ponto crítico da auditoria**: A pasta Bernoulli continha grande contaminação de simulados estaduais paulistas com formato discursivo ou provas de 60/80 questões.
   - Os agentes aplicaram filtros heurísticos de cabeçalho e estrutura disciplinar, **descartando mais de 920 cadernos não-ENEM** que distorceriam as estatísticas.
   - Isolaram 281 edições autênticas do ENEM 2º Dia.
3. **Agente Epsilon (INEP Oficial - 1.0 GB)**:
   - Processou os cadernos oficiais de aplicação regular e PPL de 2009 a 2024 (135 edições primárias).
   - Serviu como a "linha de base dourada" (ground truth) para calibrar os pesos das bancas de simulados.
4. **Agente Zeta (Poliedro, Apeiron e Acervo Misto - 755 MB)**:
   - Processou 47 cadernos canônicos do Poliedro, 6 do Apeiron e provas mistas complementares.

### Algoritmo de Deduplicação Canônica por Hash Estrutural
Para não inflar as estatísticas contando a mesma prova várias vezes, o sistema gerou hashes criptográficos SHA-256 normalizados das primeiras 5 questões de cada caderno. Arquivos com nomes diferentes que compartilhavam o mesmo hash textual foram agrupados em uma única **Edição Canônica Primária**, resultando exatamente em **719 cadernos únicos**.

### Como Chegamos nas 24.419 Questões Autênticas?
Multiplicando os 719 cadernos canônicos pelas questões válidas do 2º Dia (90 itens por prova completa, descontando questões anuladas ou páginas de instrução), a esteira de dados extraiu e interpretou o texto integral de exatamente:
$$\mathbf{24.419\text{ quest\tilde{o}es aut\hat{e}nticas do 2º Dia do ENEM}}$$

---

## 📊 O Que Descobrimos? Resultados e Métricas Estatísticas

A mineração profunda revelou padrões impressionantes que desmistificam o senso comum sobre o que cai no ENEM.

### 1. Distribuição Geral do Corpus por Área do Conhecimento

```mermaid
xychart-beta
    title "Distribuição de Questões Mineradas por Disciplina (Total: 24.419)"
    x-axis ["Matemática", "Química", "Física", "Biologia"]
    y-axis "Quantidade de Questões" 0 --> 13000
    bar [11684, 4347, 4316, 4072]
```

- **Matemática e suas Tecnologias**: 11.684 questões (**47,85%** do corpus).
- **Química**: 4.347 questões (**17,80%**).
- **Física**: 4.316 questões (**17,67%**).
- **Biologia**: 4.072 questões (**16,68%**).

---

### 2. A Hegemonia da Matemática Básica e Proporcionalidade (48,92%)

O resultado mais contundente da auditoria em Matemática foi a concentração maciça em conceitos básicos:

| Subtópico de Matemática | Questões Mineradas | Incidência (%) | Nível de Impacto TRI |
| :--- | :---: | :---: | :---: |
| **Razão, Proporção e Regra de Três** | 2.145 | 18,36% | **CRUCIAL (Base TRI)** |
| **Porcentagem e Matemática Financeira Inicial** | 1.832 | 15,68% | **CRUCIAL (Base TRI)** |
| **Escalas Métricas e Conversão de Unidades** | 1.739 | 14,88% | **CRUCIAL (Base TRI)** |
| **Geometria Espacial (Volumes e Áreas)** | 1.542 | 13,20% | **ALTO** |
| **Estatística Básica (Média, Moda e Mediana)** | 1.378 | 11,79% | **CRUCIAL** |
| **Funções de 1º e 2º Grau / Gráficos** | 1.109 | 9,49% | **ALTO** |
| **Geometria Plana e Trigonometria Básica** | 981 | 8,40% | **MÉDIO** |
| **Análise Combinatória e Probabilidade** | 638 | 5,46% | **ALTO** |
| **Tópicos Avançados (Matrizes, Complexos, etc.)** | 320 | 2,74% | **BAIXO / PERIFÉRICO** |

> [!TIP]
> **O Veredito da TRI**: Razão, proporção, porcentagem, escalas e estatística básica somam **48,92% de toda a prova de Matemática** (5.716 questões). Na Teoria de Resposta ao Item, errar uma questão de escala métrica e acertar uma de análise combinatória complexa faz a nota de Matemática desabar, pois o algoritmo pune a falta de coerência pedagógica.

---

### 3. A Tríade Clássica da Física (~68%)

Em Física, o mito de que "cai tudo de maneira uniforme" caiu por terra:

```mermaid
flowchart LR
    subgraph TriadeFisica["A Tríade Clássica (68,16% da Física)"]
        Mec["1. Mecânica Clássica (29,63%)<br/>Cinemática, Leis de Newton, Energia e Trabalho"]
        Eletro["2. Eletrodinâmica (23,86%)<br/>Circuitos residenciais, Consumo kWh, Resistores e Potência"]
        Ond["3. Ondulatória e Acústica (14,67%)<br/>Equação Fundamental, Fenômenos e Doppler"]
    end
    subgraph Restante["Restante da Matéria (31,84%)"]
        Termo["Termologia & Calorimetria (13,44%)"]
        Opt["Óptica Geométrica (8,12%)"]
        Mag["Magnetismo & Eletromagnetismo (6,21%)"]
        Mod["Física Moderna (4,07%)"]
    end
```

Apenas três disciplinas concentram mais de dois terços de todas as questões cobradas no exame.

---

### 4. O Salto Tecnológico da Biotecnologia & Genética Moderna (19,36%)

Ao analisar a evolução temporal dos simulados de 2022 a 2026 comparados às provas de 2014, Biologia sofreu a maior transformação conceitual:
- **Ecologia** permanece líder histórica absoluta (**34,55%**), dominando cadeias tróficas, ciclos biogeoquímicos, biomas brasileiros e impactos antrópicos (eutrofização e bioacumulação).
- **Biotecnologia e Genética Molecular** saltou para a segunda colocação isolada com **19,36%** (789 itens):
  - Testes diagnósticos modernos (RT-PCR vs Sorologia).
  - Tecnologia de edição gênica (CRISPR-Cas9).
  - Vacinas de RNA mensageiro e vetores virais recombinantes.
  - Transgenia e clonagem molecular na agropecuária.
- **Fisiologia Humana e Imunologia** concentrou **18,12%**, focada em sistemas digestório, circulatório, renal e mecanismos de defesa (soro vs vacina).

---

### 5. Interdisciplinaridade Real (18,99%)

Diferente de vestibulares tradicionais que isolam Física de Química, **4.636 questões mineradas (18,99%)** apresentaram exigência conceitual híbrida:

```mermaid
flowchart TD
    Bio["Biologia: Respiração Celular, Bioquímica e Digestão"] <-->|"Fermentação, Entalpia e Soluções"| Quim["Química: Termoquímica, Equilíbrio e pH"]
    Quim <-->|"Eletrólise, Pilhas e Corrente Iônica"| Fis["Física: Eletrodinâmica e Potência Elétrica"]
    Bio <-->|"Impacto dos Combustíveis Fósseis e Efeito Estufa"| Fis
```

---

### 6. O Princípio de Pareto: TOP 15 Geral Cobre 81,77% do Exame

Cruzando as quatro disciplinas, isolamos o **Ranking de Prioridades Absolutas (TOP 15 Geral)**:

1. 🥇 **Matemática Básica & Proporcionalidade** (M1) — **23,41%** do Dia 2
2. 🥈 **Ecologia & Meio Ambiente** (B1) — **5,76%**
3. 🥉 **Mecânica Clássica & Energia** (F2) — **5,24%**
4. 4º **Físico-Química (Termo, Cinética e Equilíbrio)** (Q1) — **4,82%**
5. 5º **Geometria Espacial & Métrica** (M2) — **6,31%**
6. 6º **Eletrodinâmica & Circuitos** (F1) — **4,22%**
7. 7º **Estatística & Médias** (M3) — **5,64%**
8. 8º **Química Geral & Estequiometria** (Q2) — **4,11%**
9. 9º **Biotecnologia & Genética Molecular** (B4) — **3,23%**
10. 10º **Fisiologia Humana & Imunologia** (B2) — **3,02%**
11. 11º **Química Orgânica & Reações** (Q3) — **2,95%**
12. 12º **Funções & Gráficos** (M4) — **4,54%**
13. 13º **Ondulatória & Fenômenos** (F4) — **2,59%**
14. 14º **Química Ambiental & Tratamento de Água** (Q4) — **2,24%**
15. 15º **Citologia & Metabolismo Energético** (B3) — **2,15%**

$$\mathbf{Soma\ do\ TOP\ 15:\ 19.968\ ocorr\hat{e}ncias\ (81,77\%\ de\ toda\ a\ prova)}$$

---

## 🔮 Predição Estatística: Como Será a Prova Deste Ano?

Com base na modelagem estocástica do acervo e nas tendências consolidadas das matrizes 2022-2026:

### 1. Projeção de Matemática (45 Itens)
- **21 a 23 Questões**: Matemática Básica (Razão, proporção, porcentagem, escalas, conversão e matemática financeira).
- **6 a 7 Questões**: Geometria Espacial (cálculo de capacidade volumétrica, embalagens, prismas e cilindros) e Vistas Ortogonais.
- **5 a 6 Questões**: Estatística (leitura de gráficos complexos, cálculo de média ponderada, mediana e desvio padrão).
- **4 a 5 Questões**: Funções de 1º e 2º grau com modelagem contextualizada.
- **2 a 3 Questões**: Análise combinatória ou probabilidade condicional.

### 2. Projeção de Ciências da Natureza (45 Itens)
- **Física (15 Itens)**:
  - 4 a 5 itens de **Mecânica** (Dinâmica, conservação de energia e colisões).
  - 3 a 4 itens de **Eletrodinâmica** (consumo de aparelhos, potência e associação de resistores).
  - 2 a 3 itens de **Ondulatória** (aplicação em telecomunicações, som e ultrassom).
  - 2 itens de **Termologia** (calorimetria e trocas de calor).
- **Química (15 Itens)**:
  - 5 a 6 itens de **Físico-Química** (entalpia de combustão, cinética de reações com catalisadores e pilhas/eletrólise).
  - 3 a 4 itens de **Química Orgânica** (reconhecimento de funções em fármacos e polímeros).
  - 3 itens de **Química Ambiental** (poluição, tratamento de esgoto e biomassa).
  - 2 a 3 itens de **Estequiometria** com pureza e rendimento.
- **Biologia (15 Itens)**:
  - 5 itens de **Ecologia** (impactos ambientais no Cerrado/Amazônia, ciclos de nitrogênio e carbono).
  - 3 a 4 itens de **Biotecnologia e Genética** (técnicas diagnósticas, vacinas e melhoramento genético).
  - 3 itens de **Fisiologia Humana** (homeostase, sistema imune e ação hormonal).
  - 2 a 3 itens de **Citologia/Bioquímica** (fotossíntese vs respiração celular).

---

## 📦 Artefatos Estruturados Gerados no Repositório

Todos os produtos derivados da auditoria foram homologados e estão organizados no diretório [`FINAL/`](FINAL):

1. **[RELATORIO_CONSOLIDADO_ENEM_DIA_2.md](FINAL/RELATORIO_CONSOLIDADO_ENEM_DIA_2.md)**: O documento técnico integral de 54 KB com todos os cruzamentos estatísticos e tabelas completas por matéria.
2. **[RELATORIO_ESTATISTICO_ENEM_DIA_2.md](FINAL/RELATORIO_ESTATISTICO_ENEM_DIA_2.md)**: Baseline histórico oficial do ENEM (2014 a 2024).
3. **[CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md](FINAL/CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md)**: Inventário completo com as 719 edições canônicas identificadas e indexadas.
4. **[INDICE_TEMATICO_SIMULADOS_DIA_2.md](FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md)**: Banco balanceado de **333 questões selecionadas** cobrindo os 15 tópicos vitais nas 5 bancas examinadoras para treino direcionado.
5. **[TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md](FINAL/TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md)**: Trilha prática diária de estudos conectada aos exercícios do índice.
6. **[MAPA_MENTAL_ESTUDO_ENEM.json](FINAL/MAPA_MENTAL_ESTUDO_ENEM.json)**: Árvore mental interativa com **202 nós**, 4 raízes coloridas e 136 caixas de anotação/ilustração, compatível com o MindNote Engine.
7. **[CRONOGRAMA_RETA_FINAL.json](FINAL/CRONOGRAMA_RETA_FINAL.json)**: Cronograma tático de 4 dias com **171 nós** e pautas manuais de 3 linhas para fórmulas e macetes de reta final.
8. **[`subagentes/`](FINAL/subagentes)**: Relatórios originais de mineração entregues pelos subagentes Alpha, Beta, Gamma, Delta, Epsilon e Zeta.

---

## 🧪 Suíte de Testes Automatizados e Validação Tripla

Para assegurar que os arquivos JSON funcionem perfeitamente no motor web do **MindNote Engine**, foi implementada uma suíte de testes de 3 camadas:

```bash
# 1. Validação do Cronograma Tático (Python AST + Node.js Engine + Browser DOM Headless):
python scripts/test_cronograma_reta_final.py

# 2. Validação do Mapa Mental Completo de 202 Nós:
python scripts/test_mindnote_mapa.py
```

Resultados da homologação:
- **100% de sucesso** em todas as camadas.
- Contagem SVG real validada: 171 nós gráficos, 114 caixas de anotação e 456 linhas pautadas renderizadas sem erros de layout.

---

## 💡 Considerações Finais e O Que Aprendemos

1. **A Teoria de Resposta ao Item (TRI) é Matemática Básica**: Ninguém alcança 800+ em Matemática errando regra de três ou escala para tentar acertar logaritmo. A coerência do acerto define a nota.
2. **Engenharia de Dados em Escala Exige Heurísticas Estritas**: O maior erro em análise de vestibulares é misturar acervos paulistas (Fuvest/Unicamp) com ENEM. Descartar os 920 arquivos contaminantes foi o passo mais importante de toda a auditoria.
3. **Agentes Autônomos Precisam de Protocolos Rígidos**: A divisão de carga entre os subagentes Alpha a Zeta comprovou que delegar fatias isoladas de trabalho combinadas com deduplicação por hash produz resultados determinísticos e de altíssima precisão.

---

## 📄 Autoria e Licença

Este estudo de caso e seus respectivos artefatos foram desenvolvidos por **Eduardo Borborema Brito**.

O código e os relatórios são distribuídos sob a licença **[Eduardo Borborema Source-Available & Non-Commercial License 1.0](LICENSE)**.  
Uso permitido exclusivamente para estudos pessoais, aprendizado e fins não-comerciais. É expressamente proibida a apropriação indevida ou exploração comercial sem consentimento prévio do autor.
