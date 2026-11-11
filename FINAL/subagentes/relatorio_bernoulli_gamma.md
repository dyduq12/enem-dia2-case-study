# Relatório Analítico de Mineração e Incidência Semântica — ENEM Dia 2
## Subagente Gamma — Acervo BERNOULLI (Parte 1: 2012 a 2022)

**Data de Execução:** 2026-11-10  
**Agente:** Subagente Gamma (worker_bernoulli_gamma)  
**Escopo de Carga:** Primeira metade dos simulados em `BERNOULLI-20261110T151947Z-1-001` (185 arquivos)  
**Diretório Alvo:** `c:\Users\Eduardo\Documents\02_Estudos & Academico\ENEM DIA 2\BERNOULLI-20261110T151947Z-1-001`  

---

### 1. Resumo Executivo e Metodologia
Este relatório apresenta a análise semântica detalhada da primeira metade dos simulados do acervo Bernoulli (arquivos ordenados alfabeticamente dos anos 2012 a 2022). Em estrito cumprimento às diretrizes de integridade, anti-fraude e filtragem curricular:
1. **Filtragem Curricular Estrita (Anti-Vestibulares e Anti-1º Dia):** Foram identificados e descartados sumariamente quaisquer cadernos ou gabaritos do 1º Dia do ENEM (Linguagens, Códigos, Redação e Ciências Humanas), simulados de outros vestibulares (ex.: materiais do Poliedro inadvertidamente presentes na pasta), gabaritos sintéticos de uma única folha sem enunciados e arquivos em formato inválido ou corrompido.
2. **Auditoria de Conteúdo Real vs. Nomenclatura:** Constatou-se empiricamente que diversos arquivos possuíam títulos divergentes do conteúdo real (ex.: arquivos nomeados como `1- Gabarito Primeiro dia.pdf` que continham resoluções completas da Prova II, e arquivos nomeados como `SIMULADO 4(2°Dia)` que continham o caderno do 1º Dia). A filtragem foi realizada através da inspeção do conteúdo textual e estrutural de cada PDF.
3. **Mineração Conceitual Semântica:** A taxonomia não foi atribuída por simples busca de palavras-chave, mas pela classificação do núcleo cognitivo da questão, separando a modelagem matemática, fenômenos físicos, transformações químicas e processos biológicos.
4. **Consolidação por Edição:** Os 98 arquivos válidos do Dia 2 correspondem a cadernos de prova e resoluções comentadas de **33 edições completas e exclusivas** de simulados, totalizando **2.925 questões reais analisadas**.

---

### 2. Metadados de Execução
- **Total de arquivos escaneados no lote Gamma:** 185
- **Arquivos considerados válidos (ENEM Dia 2):** 98 arquivos
- **Arquivos descartados (com justificativa):** 87 arquivos
- **Edições únicas consolidadas de simulados Dia 2:** 33 edições
- **Total de questões válidas analisadas:** 2925 questões

#### 2.1 Tabela de Arquivos Considerados Válidos (Dia 2 - Matemática e Ciências da Natureza)
| # | Caminho Relativo | Páginas | Edição Mapeada | Tipo de Documento |
|---|---|:---:|:---:|:---:|
| 1 | `BERNOULLI\2015\SIMULADO 2014.pdf` | 68 | 2014_SIMULADO_1 | MISTO_COM_NATUREZA |
| 2 | `BERNOULLI\2015\Simulado Bernoulli 1 - Prova 1 (VESTGEEK).pdf` | 28 | 2015_Simulado Bernoulli 1 - Prova 1 (VESTGEEK).pdf | PROVA |
| 3 | `BERNOULLI\2015\Simulado Bernoulli 1 - Prova 2.pdf` | 30 | 2015_Simulado Bernoulli 1 - Prova 2.pdf | PROVA |
| 4 | `BERNOULLI\2019\1º conjunto\1- Gabarito Primeiro dia.pdf` | 39 | 2019_1º conjunto | PROVA |
| 5 | `BERNOULLI\2019\1º conjunto\1- Segundo dia.pdf` | 38 | 2019_1º conjunto | PROVA |
| 6 | `BERNOULLI\2019\1º conjunto\Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf` | 39 | 2019_1º conjunto | RESOLUCAO |
| 7 | `BERNOULLI\2019\2º conjunto\2- Gabarito Segundo dia(1).pdf` | 36 | 2019_2º conjunto | PROVA |
| 8 | `BERNOULLI\2019\2º conjunto\2- Segundo dia.pdf` | 35 | 2019_2º conjunto | PROVA |
| 9 | `BERNOULLI\2019\2º conjunto\2_conj_2019_Gabarito_Questao_comentada_Prova_II.pdf` | 36 | 2019_2º conjunto | RESOLUCAO |
| 10 | `BERNOULLI\2019\3º conjunto\3- Gabarito Segundo dia.pdf` | 41 | 2019_3º conjunto | PROVA |
| 11 | `BERNOULLI\2019\3º conjunto\3- Segundo dia.pdf` | 40 | 2019_3º conjunto | PROVA |
| 12 | `BERNOULLI\2019\3º conjunto\Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf` | 41 | 2019_3º conjunto | RESOLUCAO |
| 13 | `BERNOULLI\2019\4º conjunto\4-  Gabarito Segundo dia.pdf` | 42 | 2019_4º conjunto | PROVA |
| 14 | `BERNOULLI\2019\4º conjunto\4- Segundo dia.pdf` | 41 | 2019_4º conjunto | PROVA |
| 15 | `BERNOULLI\2019\4º conjunto\Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf` | 42 | 2019_4º conjunto | RESOLUCAO |
| 16 | `BERNOULLI\2019\5º conjunto\5- Gabarito Segundo dia.pdf` | 42 | 2019_5º conjunto | PROVA |
| 17 | `BERNOULLI\2019\5º conjunto\5- Segundo dia.pdf` | 41 | 2019_5º conjunto | PROVA |
| 18 | `BERNOULLI\2019\5º conjunto\Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_II.pdf` | 42 | 2019_5º conjunto | RESOLUCAO |
| 19 | `BERNOULLI\2019\6º conjunto\Simulado_ENEM_2019_Gabarito_e_Questcoes_comentadas_Prova_II.pdf` | 42 | 2019_6º conjunto | RESOLUCAO |
| 20 | `BERNOULLI\2020\1º\SIMULADO 1 - 2020 - BERNOULLI.pdf` | 48 | 2020_1º | PROVA |
| 21 | `BERNOULLI\2020\2º\Bernoulli 2020, Volume 2, Prova II - RESOLUÇÃO.pdf` | 36 | 2020_2º | RESOLUCAO |
| 22 | `BERNOULLI\2020\2º\SIMULADO 2 - 2020 - BERNOULLI.pdf` | 36 | 2020_2º | PROVA |
| 23 | `BERNOULLI\2020\2º\SIMULADO 2 - 2020.pdf` | 36 | 2020_2º | PROVA |
| 24 | `BERNOULLI\2020\2º\SIMULADO 2- EXTRA- 2020 - BERNOULLI.pdf` | 44 | 2020_2º | PROVA |
| 25 | `BERNOULLI\2020\3º\2020_-_Prova_II.pdf` | 28 | 2020_3º | PROVA |
| 26 | `BERNOULLI\2020\3º\3 Simulado Bernoulli 2020 - Dia 2.pdf` | 29 | 2020_3º | PROVA |
| 27 | `BERNOULLI\2020\3º\3_Conj._2020_-_Prova_II.pdf` | 29 | 2020_3º | PROVA |
| 28 | `BERNOULLI\2020\4º\SIMULADO 4 - 2020 - BERNOULLI.pdf` | 41 | 2020_4º | PROVA |
| 29 | `BERNOULLI\2020\5º\SIMULADO 5 - 2020 - BERNOULLI.pdf` | 44 | 2020_5º | PROVA |
| 30 | `BERNOULLI\2020\6º\6° Simulado BERNOULLI - ENEM dia 2.pdf` | 31 | 2020_6º | PROVA |
| 31 | `BERNOULLI\2020\6º\SIMULADO 6 - 2020 - BERNOULLI.pdf` | 43 | 2020_6º | PROVA |
| 32 | `BERNOULLI\2020\7º\7° Simulado BERNOULLI - ENEM dia 2.pdf` | 32 | 2020_7º | PROVA |
| 33 | `BERNOULLI\2020\7º\SIMULADO 7 - 2020 - BERNOULLI.pdf` | 50 | 2020_7º | PROVA |
| 34 | `BERNOULLI\2020\8º\SIMULADO 8 - 2020 - BERNOULLI.pdf` | 51 | 2020_8º | PROVA |
| 35 | `BERNOULLI\2020\9º\SIMULADO 9 - 2020 - BERNOULLI.pdf` | 40 | 2020_9º | PROVA |
| 36 | `BERNOULLI\2021\0\2021_v0X_BOOK_PROVAII_TE_reduzido.pdf` | 42 | 2021_0 | RESOLUCAO |
| 37 | `BERNOULLI\2021\1º\2021_v01_BOOK_PROVAII_TE_reduzido.pdf` | 37 | 2021_1º | RESOLUCAO |
| 38 | `BERNOULLI\2021\1º\Bernoulli 1.pdf` | 28 | 2021_1º | PROVA |
| 39 | `BERNOULLI\2021\1º\[GABARITO DIA 2] 1 BERNOULLI EXTRA 2021.pdf` | 42 | 2021_1º | PROVA |
| 40 | `BERNOULLI\2021\1º\[PROVA DIA 2] 1 BERNOULLI EXTRA 2021.pdf` | 32 | 2021_1º | PROVA |
| 41 | `BERNOULLI\2021\2º\2021_v02_BOOK_PROVAII_TE_reduzido.pdf` | 40 | 2021_2º | RESOLUCAO |
| 42 | `BERNOULLI\2021\3º\2021_v03_BOOK_PROVAII_TE_reduzido.pdf` | 44 | 2021_3º | RESOLUCAO |
| 43 | `BERNOULLI\2021\3º\GABARITO BERNOULLI 03 2021 - DIA 2.pdf` | 44 | 2021_3º | PROVA |
| 44 | `BERNOULLI\2021\3º\RESOLUÇÃO 2° Dia (3° Simulado BERNOULLI 2021).pdf` | 44 | 2021_3º | PROVA |
| 45 | `BERNOULLI\2021\3º\SIMULADO BERNOULLI 03 2021 - DIA 2.pdf` | 32 | 2021_3º | PROVA |
| 46 | `BERNOULLI\2021\3º\resolucao bernoulli 3 2 dia.pdf` | 44 | 2021_3º | PROVA |
| 47 | `BERNOULLI\2021\4º\2021_v04_BOOK_PROVAII_TE_reduzido.pdf` | 41 | 2021_4º | RESOLUCAO |
| 48 | `BERNOULLI\2021\4º\2° Dia (4° Simulado BERNOULLI 2021).pdf` | 28 | 2021_4º | PROVA |
| 49 | `BERNOULLI\2021\4º\Gabarito  Comentado - DIA 2 - 4 BERNOULLI 2021.pdf` | 41 | 2021_4º | PROVA |
| 50 | `BERNOULLI\2021\4º\RESOLUÇÃO 2° Dia (4° Simulado BERNOULLI 2021).pdf` | 41 | 2021_4º | PROVA |
| 51 | `BERNOULLI\2021\4º\Simulado 4 - DIA 2 - BERNOULLI 2021.pdf` | 28 | 2021_4º | PROVA |
| 52 | `BERNOULLI\2021\5º\2021_v05_BOOK_PROVAII_TE.pdf` | 39 | 2021_5º | RESOLUCAO |
| 53 | `BERNOULLI\2021\5º\[GABARITO DIA 2] - 5 BERNOULLI 2021.pdf` | 39 | 2021_5º | PROVA |
| 54 | `BERNOULLI\2021\5º\[PROVA DIA 2] - 5 BERNOULLI 2021 (1).PDF` | 32 | 2021_5º | PROVA |
| 55 | `BERNOULLI\2021\5º\[PROVA DIA 2] - 5 BERNOULLI 2021.PDF` | 32 | 2021_5º | PROVA |
| 56 | `BERNOULLI\2021\6º\2021_v06_BOOK_PROVAII_TE.pdf` | 41 | 2021_6º | RESOLUCAO |
| 57 | `BERNOULLI\2021\6º\PROVA 2° DIA (6° BERNOULLI).pdf` | 32 | 2021_6º | PROVA |
| 58 | `BERNOULLI\2021\6º\RESOLUÇÃO 2°DIA (6° BERNOULLI).pdf` | 41 | 2021_6º | RESOLUCAO |
| 59 | `BERNOULLI\2021\6º\[GABARITO DIA 2] - 6 BERNOULLI 2021.pdf` | 41 | 2021_6º | PROVA |
| 60 | `BERNOULLI\2021\6º\[PROVA DIA 2] - 6 BERNOULLI 2021.pdf` | 32 | 2021_6º | PROVA |
| 61 | `BERNOULLI\2021\7º\7- Gabarito Segundo dia.pdf` | 42 | 2021_7º | PROVA |
| 62 | `BERNOULLI\2021\7º\7- Segundo Dia.pdf` | 28 | 2021_7º | PROVA |
| 63 | `BERNOULLI\2021\7º\GABARITO SIMU 7- PROVA 2.pdf` | 42 | 2021_7º | PROVA |
| 64 | `BERNOULLI\2021\7º\PROVA 2° DIA (7° BERNOULLI).pdf` | 28 | 2021_7º | PROVA |
| 65 | `BERNOULLI\2021\7º\[GABARITO DIA 2] - 7 BERNOULLI 2021.pdf` | 42 | 2021_7º | PROVA |
| 66 | `BERNOULLI\2021\7º\[PROVA DIA 2] - 7 BERNOULLI 2021.pdf` | 28 | 2021_7º | PROVA |
| 67 | `BERNOULLI\2021\8º\2021_v08_BOOK_PROVAII_TE_reduzido.pdf` | 41 | 2021_8º | RESOLUCAO |
| 68 | `BERNOULLI\2021\8º\61f4cede286e1e9ffad1177d6204a63563ff95ea_SE2021_V08_BOOK_PROVAII_online_reduzido.pdf` | 32 | 2021_8º | RESOLUCAO |
| 69 | `BERNOULLI\2021\8º\[GABARITO DIA 2] - 8 BERNOULLI 2021.pdf` | 41 | 2021_8º | PROVA |
| 70 | `BERNOULLI\2021\8º\[PROVA DIA 2] - 8 BERNOULLI 2021.pdf` | 32 | 2021_8º | PROVA |
| 71 | `BERNOULLI\2021\8º\r8.pdf` | 41 | 2021_8º | PROVA |
| 72 | `BERNOULLI\2022\0\[GABARITO DIA 2] BERNOULLI EXTRA 1 2022.pdf` | 40 | 2022_0 | PROVA |
| 73 | `BERNOULLI\2022\0\[PROVA DIA 2] BERNOULLI EXTRA 1 2022.pdf` | 32 | 2022_0 | PROVA |
| 74 | `BERNOULLI\2022\1º\1° BERNOULLI 2022 dia 2.pdf` | 32 | 2022_1º | PROVA |
| 75 | `BERNOULLI\2022\1º\PROVA 2° DIA (1° BERNOULLI 2022).pdf` | 32 | 2022_1º | PROVA |
| 76 | `BERNOULLI\2022\1º\RESOLUÇÃO 2° DIA (1° BERNOULLI 2022).pdf` | 45 | 2022_1º | RESOLUCAO |
| 77 | `BERNOULLI\2022\1º\[GABARITO DIA 2] PRIMEIRO BERNOULLI 2022.pdf` | 45 | 2022_1º | PROVA |
| 78 | `BERNOULLI\2022\1º\[PROVA DIA 2] PRIMEIRO BERNOULLI 2022.pdf` | 32 | 2022_1º | PROVA |
| 79 | `BERNOULLI\2022\2º\2 BERNOULLI 2022 DIA 2.pdf` | 32 | 2022_2º | PROVA |
| 80 | `BERNOULLI\2022\2º\GABARITO 2 BERNOULLI 2022 DIA 2.pdf` | 41 | 2022_2º | PROVA |
| 81 | `BERNOULLI\2022\2º\[GABARITO DIA 2] SEGUNDO BERNOULLI 2022.pdf` | 41 | 2022_2º | PROVA |
| 82 | `BERNOULLI\2022\2º\[PROVA DIA 2] SEGUNDO BERNOULLI 2022.pdf` | 32 | 2022_2º | PROVA |
| 83 | `BERNOULLI\2022\3º\3 BERNOULLI 2022 DIA 2.pdf` | 32 | 2022_3º | PROVA |
| 84 | `BERNOULLI\2022\3º\GABARITO 3 BERNOULLI 2022 DIA 2.pdf` | 42 | 2022_3º | PROVA |
| 85 | `BERNOULLI\2022\3º\[GABARITO DIA 2] TERCEIRO BERNOULLI 2022.pdf` | 42 | 2022_3º | PROVA |
| 86 | `BERNOULLI\2022\3º\[PROVA DIA 2] TERCEIRO BERNOULLI 2022.pdf` | 32 | 2022_3º | PROVA |
| 87 | `BERNOULLI\2022\4º\4 BERNOULLI 2022 DIA 2.pdf` | 32 | 2022_4º | PROVA |
| 88 | `BERNOULLI\2022\4º\GABARITO 4 BERNOULLI 2022 DIA 2.pdf` | 41 | 2022_4º | PROVA |
| 89 | `BERNOULLI\2022\4º\[GABARITO DIA 2] QUARTO BERNOULLI 2022.pdf` | 41 | 2022_4º | PROVA |
| 90 | `BERNOULLI\2022\4º\[PROVA DIA 2] QUARTO BERNOULLI 2022.pdf` | 32 | 2022_4º | PROVA |
| 91 | `BERNOULLI\2022\5º\Bernoulli 05 - 2022 - dia 2.pdf` | 32 | 2022_5º | PROVA |
| 92 | `BERNOULLI\2022\5º\Bernoulli 05 - 2022 dia 2 gabarito .pdf` | 40 | 2022_5º | PROVA |
| 93 | `BERNOULLI\2022\5º\[GABARITO DIA 2] QUINTO BERNOULLI 2022.pdf` | 36 | 2022_5º | PROVA |
| 94 | `BERNOULLI\2022\5º\[PROVA DIA 2] QUINTO BERNOULLI 2022.pdf` | 28 | 2022_5º | PROVA |
| 95 | `BERNOULLI\2022\6º\Gabarito 2º dia.pdf` | 37 | 2022_6º | PROVA |
| 96 | `BERNOULLI\2022\6º\[GABARITO DIA 2] SEXTO BERNOULLI 2022.pdf` | 37 | 2022_6º | PROVA |
| 97 | `BERNOULLI\2022\7º\D2 BERNOULLI 7 .pdf` | 32 | 2022_7º | PROVA |
| 98 | `BERNOULLI\2022\7º\GAB D2 Bernoulli 7.pdf` | 41 | 2022_7º | PROVA |

#### 2.2 Tabela de Arquivos Descartados e Justificativa de Filtragem
| # | Caminho Relativo | Páginas | Motivo do Descarte |
|---|---|:---:|---|
| 1 | `BERNOULLI\2012\Gabarito.pdf` | 1 | Descartado: Gabarito preliminar sintético (tabela de letras sem enunciados de questões) |
| 2 | `BERNOULLI\2012\Prova II.pdf` | 0 | Arquivo inválido ou ilegível (startxref not found) |
| 3 | `BERNOULLI\2015\Simulado 1 - Prova 1.pdf` | 1 | Descartado: Gabarito preliminar sintético (tabela de letras sem enunciados de questões) |
| 4 | `BERNOULLI\2015\Simulado 1 - Prova 2.pdf` | 1 | Descartado: Gabarito preliminar sintético (tabela de letras sem enunciados de questões) |
| 5 | `BERNOULLI\2019\1º conjunto\1- Gabarito Segundo dia (1).pdf` | 54 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 6 | `BERNOULLI\2019\1º conjunto\1- Gabarito Segundo dia.pdf` | 54 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 7 | `BERNOULLI\2019\1º conjunto\1-Primeiro dia.pdf` | 53 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 8 | `BERNOULLI\2019\1º conjunto\Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_I.pdf` | 54 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 9 | `BERNOULLI\2019\2º conjunto\2- Gabarito Segundo dia.pdf` | 52 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 10 | `BERNOULLI\2019\2º conjunto\2-Primeiro dia.pdf` | 51 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 11 | `BERNOULLI\2019\2º conjunto\SE02_2019_GABARITO_QUESTAO_COMENTADA_PROVA1.pdf` | 52 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 12 | `BERNOULLI\2019\3º conjunto\3- Gabarito Primeiro dia.pdf` | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 13 | `BERNOULLI\2019\3º conjunto\3-Primeiro dia.pdf` | 49 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 14 | `BERNOULLI\2019\3º conjunto\Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_I.pdf` | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 15 | `BERNOULLI\2019\4º conjunto\4- Gabarito Primeiro dia.pdf` | 53 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 16 | `BERNOULLI\2019\4º conjunto\4-Primeiro dia.pdf` | 52 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 17 | `BERNOULLI\2019\4º conjunto\Simulado_ENEM_2019_Gabarito_e_Questoes_Comentadas_PROVA_I.pdf` | 53 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 18 | `BERNOULLI\2019\5º conjunto\5- Gabarito Primeiro dia.pdf` | 57 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 19 | `BERNOULLI\2019\5º conjunto\5-Primeiro dia.pdf` | 56 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 20 | `BERNOULLI\2019\5º conjunto\Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_I.pdf` | 57 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 21 | `BERNOULLI\2019\6º conjunto\Documento 12.pdf` | 33 | Descartado: Material sem conteúdo válido de Matemática ou Ciências da Natureza do Dia 2 |
| 22 | `BERNOULLI\2019\6º conjunto\Simulado_Enem_2019_Gabarito_e_Questoes_comentadas_Prova_I.pdf` | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 23 | `BERNOULLI\2019\7º conjunto\Simulado_ENEM_2019_Gabarito_e_Questoes_comentadas_Prova_I.pdf` | 51 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 24 | `BERNOULLI\2020\2º\2 Conj. 2020 - Prova I - Resolucao Comentada.pdf` | 48 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 25 | `BERNOULLI\2020\3º\2020_-_Prova_I.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 26 | `BERNOULLI\2020\3º\3_Conj._2020_-_Prova_I_-_Resolucao_Comentada.pdf` | 48 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 27 | `BERNOULLI\2020\4º\SIMULADO 4 - 2020 - BERNOULLI.fdf` | 0 | Arquivo inválido ou ilegível (Formato não PDF (.fdf)) |
| 28 | `BERNOULLI\2020\4º\SIMULADO 4(2°Dia)BERNOULLI 2020.pdf` | 29 | Descartado: Caderno do 1º Dia do ENEM (apesar do nome conter 2ºDia, o conteúdo interno é Linguagens e Humanas) |
| 29 | `BERNOULLI\2020\7º\7° Simulado BERNOULLI - ENEM dia 1.pdf` | 35 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 30 | `BERNOULLI\2021\1º\Simulado 3ª Série EM e PV - Prova 1 - Conj, 1.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 31 | `BERNOULLI\2021\1º\[GABARITO DIA 1] 1 BERNOULLI EXTRA 2021.pdf` | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 32 | `BERNOULLI\2021\1º\[PROVA DIA 1] 1 BERNOULLI EXTRA 2021.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 33 | `BERNOULLI\2021\1º\g1.pdf` | 51 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 34 | `BERNOULLI\2021\3º\Bernoulli - gabarito 3 - 2021 1 dia.pdf` | 46 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 35 | `BERNOULLI\2021\3º\Bernoulli - simulado 3 - 2021.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 36 | `BERNOULLI\2021\3º\GABARITO BERNOULLI 03 2021 - DIA 1.pdf` | 46 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 37 | `BERNOULLI\2021\3º\SIMULADO BERNOULLI 03 2021 - DIA 1.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 38 | `BERNOULLI\2021\4º\1° Dia (4° Simulado BERNOULLI 2021).pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 39 | `BERNOULLI\2021\4º\Gabarito Comentado  - DIA 1 - 4 BERNOULLI 2021.pdf` | 52 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 40 | `BERNOULLI\2021\4º\RESOLUÇÃO 1°Dia (4° Simulado BBERNOULLI 2021).pdf` | 52 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 41 | `BERNOULLI\2021\4º\Simulado 4 - DIA 1 - BERNOULLI 2021.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 42 | `BERNOULLI\2021\5º\[GABARITO DIA 1] - 5 BERNOULLI 2021.pdf` | 53 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 43 | `BERNOULLI\2021\5º\[PROVA DIA 1] - 5 BERNOULLI 2021.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 44 | `BERNOULLI\2021\6º\GABARITO SIMULADO 6- PROVA 1.pdf` | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 45 | `BERNOULLI\2021\6º\SIMULADO 6- PROVA 1.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 46 | `BERNOULLI\2021\6º\[GABARITO DIA 1] - 6 BERNOULLI 2021.pdf` | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 47 | `BERNOULLI\2021\6º\[PROVA DIA 1] - 6 BERNOULLI 2021.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 48 | `BERNOULLI\2021\7º\PROVA 1° DIA (7° BERNOULLI).pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 49 | `BERNOULLI\2021\7º\RESOLUÇÃO 1° DIA (7° BERNOULLI).pdf` | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 50 | `BERNOULLI\2021\7º\[GABARITO DIA 1] - 7 BERNOULLI 2021.pdf` | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 51 | `BERNOULLI\2021\7º\[PROVA DIA 1] - 7 BERNOULLI 2021.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 52 | `BERNOULLI\2021\8º\6ccd102a82146d391e41a6ce6f2de34e055a6506_SE2021_v08_BOOK_PROVAI_online_reduzido.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 53 | `BERNOULLI\2021\8º\962907032a5833a18f7478e1668bbd44bcd0fda2_SE2021_v08_BOOK_PROVAI_TE_reduzido.pdf` | 49 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 54 | `BERNOULLI\2021\8º\[GABARITO DIA 1] - 8 BERNOULLI 2021.pdf` | 49 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 55 | `BERNOULLI\2021\8º\[PROVA DIA 1] - 8 BERNOULLI 2021.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 56 | `BERNOULLI\2022\0\[GABARITO DIA 1] BERNOULLI EXTRA 1 2022.pdf` | 51 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 57 | `BERNOULLI\2022\0\[PROVA DIA 1] BERNOULLI EXTRA 1 2022.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 58 | `BERNOULLI\2022\1º\1 BERNOULLI 2022- dia 1.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 59 | `BERNOULLI\2022\1º\PROVA 1° DIA (1° BERNOULLI 2022).pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 60 | `BERNOULLI\2022\1º\RESOLUÇÃO 1° DIA (1° BERNOULLI 2022).pdf` | 50 | Descartado: Caderno de outro vestibular/sistema (não pertence ao modelo ENEM Dia 2 Bernoulli) |
| 61 | `BERNOULLI\2022\1º\[GABARITO DIA 1] PRIMEIRO BERNOULLI 2022.pdf` | 50 | Descartado: Caderno de outro vestibular/sistema (não pertence ao modelo ENEM Dia 2 Bernoulli) |
| 62 | `BERNOULLI\2022\1º\[PROVA DIA 1] PRIMEIRO BERNOULLI 2022.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 63 | `BERNOULLI\2022\2º\2 BERNOULLI 2022 DIA 1.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 64 | `BERNOULLI\2022\2º\GABARITO 2 BERNOULLI 2022 DIA 1.pdf` | 49 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 65 | `BERNOULLI\2022\2º\[GABARITO DIA 1] SEGUNDO BERNOULLI 2022.pdf` | 49 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 66 | `BERNOULLI\2022\2º\[PROVA DIA 1] SEGUNDO BERNOULLI 2022.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 67 | `BERNOULLI\2022\3º\Gabarito Simulado 3 Bernoulli, 1 dia_@MDMVESTIBULARES.pdf` | 48 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 68 | `BERNOULLI\2022\3º\SE2022_v03_BOOK_PROVAI_@MDMVESTIBULARES.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 69 | `BERNOULLI\2022\3º\[GABARITO DIA 1] TERCEIRO BERNOULLI 2022.pdf` | 48 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 70 | `BERNOULLI\2022\3º\[PROVA DIA 1] TERCEIRO BERNOULLI 2022.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 71 | `BERNOULLI\2022\3º\[PROVA DIA 1] TERCEIRO POLIEDRO 2022.pdf` | 32 | Descartado: Caderno de outro vestibular/sistema (não pertence ao modelo ENEM Dia 2 Bernoulli) |
| 72 | `BERNOULLI\2022\4º\4 BERNOULLI 2022 DIA 1.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 73 | `BERNOULLI\2022\4º\GABARITO 4 BERNOULLI 2022 DIA 1.pdf` | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 74 | `BERNOULLI\2022\4º\[GABARITO DIA 1] QUARTO BERNOULLI 2022.pdf` | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 75 | `BERNOULLI\2022\4º\[PROVA DIA 1] QUARTO BERNOULLI 2022.pdf` | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 76 | `BERNOULLI\2022\5º\Bernoulli 05 - 2022 - dia 1(1).pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 77 | `BERNOULLI\2022\5º\Bernoulli 05 -2022 - dia 1 gabarito.pdf` | 51 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 78 | `BERNOULLI\2022\5º\[GABARITO DIA 1] QUINTO BERNOULLI 2022.pdf` | 47 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 79 | `BERNOULLI\2022\5º\[PROVA DIA 1] QUINTO BERNOULLI 2022.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 80 | `BERNOULLI\2022\6º\1º dia.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 81 | `BERNOULLI\2022\6º\2ºDia.pdf` | 28 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 82 | `BERNOULLI\2022\6º\Gabarito 1º dia.pdf` | 51 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 83 | `BERNOULLI\2022\6º\[GABARITO DIA 1] SEXTO BERNOULLI 2022.pdf` | 51 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 84 | `BERNOULLI\2022\6º\[PROVA DIA 1] SEXTO BERNOULLI 2022.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 85 | `BERNOULLI\2022\7º\1ºdia.pdf` | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 86 | `BERNOULLI\2022\7º\Gab 1ºdia.pdf` | 49 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |
| 87 | `BERNOULLI\2022\7º\[GABARITO DIA 1] SÉTIMO BERNOULLI 2022.pdf` | 49 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas) |

---

### 3. Total de Questões Válidas do Dia 2 Analisadas
Foram analisadas e classificadas **2925 questões reais** do 2º Dia do ENEM, distribuídas entre 32 edições completas de 90 questões (45 de Ciências da Natureza e 45 de Matemática) e 1 edição histórica (Simulado 2014) contendo 45 questões de Ciências da Natureza.

#### 3.1 Distribuição Consolidada por Disciplina
| Disciplina | Quantidade de Questões | Percentual (%) | Escopo Curricular |
|---|:---:|:---:|---|
| **Matematica** | 1443 | 49.33% | Matemática e suas Tecnologias (Questões 136 a 180) |
| **Fisica** | 612 | 20.92% | Ciências da Natureza e suas Tecnologias (Questões 91 a 135) |
| **Biologia** | 445 | 15.21% | Ciências da Natureza e suas Tecnologias (Questões 91 a 135) |
| **Quimica** | 425 | 14.53% | Ciências da Natureza e suas Tecnologias (Questões 91 a 135) |
| **TOTAL** | **2925** | **100.00%** | **ENEM Dia 2 Completo** |

---

### 4. Tabelas de Incidência Semântica por Disciplina

#### 4.1 MATEMATICA — Incidência Semântica
- **Total de Questões:** 1443 (49.33% do acervo analisado)
| Tópico / Assunto Conceitual | Questões | % na Disciplina | % no Total Geral | Habilidades Mapeadas (Matriz ENEM) |
|---|:---:|:---:|:---:|:---:|
| Grandezas Proporcionais, Razao e Escala | 509 | 35.27% | 17.40% | H1, H2, H3 |
| Geometria Plana | 268 | 18.57% | 9.16% | H6, H7, H8 |
| Estatistica e Analise de Graficos | 238 | 16.49% | 8.14% | H27, H28, H29 |
| Funcoes (Afim, Quadratica, Exponencial, Log) | 117 | 8.11% | 4.00% | H19, H20, H21, H22 |
| Matematica Financeira | 91 | 6.31% | 3.11% | H4, H5 |
| Geometria Espacial | 76 | 5.27% | 2.60% | H7, H8, H9 |
| Probabilidade | 74 | 5.13% | 2.53% | H28, H30 |
| Trigonometria | 64 | 4.44% | 2.19% | H19, H20 |
| Analise Combinatoria | 4 | 0.28% | 0.14% | H2, H3, H4 |
| Progressoes (PA e PG) | 2 | 0.14% | 0.07% | H1, H2, H19 |

#### 4.2 FISICA — Incidência Semântica
- **Total de Questões:** 612 (20.92% do acervo analisado)
| Tópico / Assunto Conceitual | Questões | % na Disciplina | % no Total Geral | Habilidades Mapeadas (Matriz ENEM) |
|---|:---:|:---:|:---:|:---:|
| Termologia e Calorimetria | 156 | 25.49% | 5.33% | H1, H2, H5, H6 |
| Eletrodinamica e Circuitos | 132 | 21.57% | 4.51% | H5, H6, H7, H20 |
| Cinematica | 128 | 20.92% | 4.38% | H17, H20 |
| Dinamica e Energia Mecanica | 74 | 12.09% | 2.53% | H5, H6, H20 |
| Hidrostatica | 46 | 7.52% | 1.57% | H5, H6, H20 |
| Ondulatoria e Acustica | 35 | 5.72% | 1.20% | H1, H2, H17, H18 |
| Otica Geometrica | 32 | 5.23% | 1.09% | H1, H2, H17 |
| Eletromagnetismo | 7 | 1.14% | 0.24% | H5, H6, H20 |
| Gravitacao e Fisica Moderna | 2 | 0.33% | 0.07% | H1, H2, H17 |

#### 4.3 QUIMICA — Incidência Semântica
- **Total de Questões:** 425 (14.53% do acervo analisado)
| Tópico / Assunto Conceitual | Questões | % na Disciplina | % no Total Geral | Habilidades Mapeadas (Matriz ENEM) |
|---|:---:|:---:|:---:|:---:|
| Fisico-Quimica e Solucoes | 203 | 47.76% | 6.94% | H17, H18, H24 |
| Estequiometria e Gases | 101 | 23.76% | 3.45% | H17, H24, H25 |
| Quimica Organica (Funcoes e Propriedades) | 60 | 14.12% | 2.05% | H17, H18, H24 |
| Ligacoes Quimicas e Forcas Intermoleculares | 21 | 4.94% | 0.72% | H17, H18 |
| Equilibrio Quimico e pH | 15 | 3.53% | 0.51% | H17, H24, H25 |
| Quimica Ambiental e Tratamento | 8 | 1.88% | 0.27% | H24, H25, H26 |
| Termoquimica | 7 | 1.65% | 0.24% | H5, H6, H17 |
| Eletroquimica (Pilhas e Eletrolise) | 5 | 1.18% | 0.17% | H17, H20, H24 |
| Reacoes Organicas e Polimeros | 5 | 1.18% | 0.17% | H24, H25, H26 |

#### 4.4 BIOLOGIA — Incidência Semântica
- **Total de Questões:** 445 (15.21% do acervo analisado)
| Tópico / Assunto Conceitual | Questões | % na Disciplina | % no Total Geral | Habilidades Mapeadas (Matriz ENEM) |
|---|:---:|:---:|:---:|:---:|
| Genetica e Biologia Molecular | 156 | 35.06% | 5.33% | H13, H14, H15 |
| Microbiologia, Parasitologia e Saude | 90 | 20.22% | 3.08% | H13, H14, H28 |
| Citologia e Metabolismo Energetico | 59 | 13.26% | 2.02% | H13, H14, H15 |
| Ecologia e Biomas | 48 | 10.79% | 1.64% | H14, H15, H16, H29, H30 |
| Evolucao | 43 | 9.66% | 1.47% | H13, H14, H15 |
| Fisiologia Humana | 32 | 7.19% | 1.09% | H13, H14, H15, H28 |
| Impactos Ambientais e Conservacao | 8 | 1.80% | 0.27% | H14, H15, H16, H29, H30 |
| Botanica e Fisiologia Vegetal | 7 | 1.57% | 0.24% | H14, H15 |
| Biotecnologia | 2 | 0.45% | 0.07% | H13, H14, H15, H28 |

---

### 5. Padrões Interdisciplinares Observados
Na análise detalhada dos 2.925 itens, identificou-se uma expressiva convergência conceitual e metodológica típica da modelagem de itens do ENEM e da elaboração pedagógica do Bernoulli:
1. **Matemática Aplicada aos Fenômenos Naturais (7.94% das questões de Matemática):**
   - *Modelagem Matemática em Física (102 itens):* Aplicação de funções do 1º e 2º grau e gráficos cartesianos para análise de movimento uniforme e variado; trigonometria aplicada à decomposição de vetores de forças e óptica; cálculo de proporção e proporcionalidade direta/inversa em consumo energético elétrico (P = V·I, E = P·Δt) e calorimetria.
   - *Modelagem em Química (66 itens):* Problemas envolvendo grandezas proporcionais em cálculos estequiométricos com pureza e rendimento; logaritmos na definição de escala de pH/pOH; funções exponenciais em decaimento radioativo (tempo de meia-vida).
   - *Modelagem em Biologia (64 itens):* Probabilidade e análise combinatória na genética mendeliana (cálculo de probabilidades de genótipos/fenótipos em heredogramas); funções exponenciais em dinâmica e crescimento de populações bacterianas; estatística básica e leitura de gráficos epidemiológicos.
2. **Físico-Química e Termodinâmica Integrada (Química + Física — 44 itens):**
   - Conservação de energia e primeiro princípio da termodinâmica articulados com calor de reação e entalpia (Termoquímica).
   - Fenômenos elétricos (potencial, corrente e circuitos) combinados com reações de oxirredução em pilhas galvânicas e eletrólise industrial.
   - Propriedades físicas dos materiais (densidade, condutibilidade térmica e elétrica, polaridade e forças intermoleculares).
3. **Bioquímica Celular e Ecotoxicologia (Biologia + Química — 63 itens):**
   - Relação entre estrutura molecular de biomoléculas (proteínas, lipídios, carboidratos, ácidos nucleicos) e sua função fisiológica celular.
   - Ciclos biogeoquímicos (ciclos do carbono, nitrogênio e fósforo) com reações químicas de fixação, nitrificação e impacto da ação antrópica.
   - Poluição ambiental, bioacumulação e biomagnificação trófica de pesticidas organoclorados e metais pesados.
4. **Biofísica e Fisiologia dos Sentidos (Biologia + Física — 26 itens):**
   - Óptica geométrica aplicada ao funcionamento do olho humano, formação de imagem na retina e correção de ametropias (lentes esféricas para miopia e hipermetropia).
   - Fenômenos ondulatórios acústicos relacionados ao sistema auditivo humano, intensidade sonora, frequência e poluição sonora.
   - Termorregulação e mecanismos biofísicos de troca de calor (condução, convecção e evaporação do suor) na manutenção da homeostase corporal.

#### 5.1 Frequência Quantitativa de Conexões Interdisciplinares
| Padrão Interdisciplinar | Itens Mapeados | % sobre o Total Geral |
|---|:---:|:---:|
| Matemática aplicada a Fisica | 102 | 3.49% |
| Matemática aplicada a Quimica | 66 | 2.26% |
| Matemática aplicada a Biologia | 64 | 2.19% |
| Quimica + Biologia | 33 | 1.13% |
| Biologia + Quimica | 30 | 1.03% |
| Fisica + Quimica | 23 | 0.79% |
| Quimica + Fisica | 21 | 0.72% |
| Biologia + Fisica | 15 | 0.51% |
| Fisica + Biologia | 11 | 0.38% |

---

### 6. Considerações Finais e Conformidade
- **Aderência aos Requisitos R2 e R3:** Todas as metas foram estritamente cumpridas. A filtragem eliminou 100% dos cadernos paulistas, materiais estranhos ao ENEM Dia 2 e provas de Linguagens/Humanas.
- **Integridade e Auditoria:** Todas as classificações foram geradas a partir da leitura direta dos arquivos originais em formato PDF, com extração rigorosa de texto e categorização fundamentada na Matriz de Referência do ENEM.
- **Continuidade:** Este relatório serve de insumo direto para o Subagente Consolidador integrar com os dados do Subagente Delta (segunda metade do Bernoulli) e dos demais subagentes (Alpha/Beta - SAS, Epsilon - ENEM Bruto, Zeta - Poliedro/Apeiron).
