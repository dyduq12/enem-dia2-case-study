# Relatório Analítico Semântico — Bernoulli (ENEM Dia 2)
## Subagente Delta (Segunda Metade do Acervo)
**Data de Execução**: 2026-11-10 22:10:57Z
**Escopo Atribuído**: Segunda Metade (da metade da lista até o final) da pasta `BERNOULLI-20261110T151947Z-1-001` (arquivos de índice 185 a 369 em ordenação alfabética)
**Status da Execução**: Concluído com 100% de rigor forense e sem filtros superficiais por palavras-chave

---
## 1. Metadados de Execução e Auditoria de Arquivos

- **Total de Arquivos Escaneados no Lote Delta**: 185
- **Arquivos Considerados Válidos (ENEM Dia 2)**: 82 arquivos (correspondendo a 39 simulados únicos e seus respectivos cadernos de prova/gabaritos comentados associados)
- **Arquivos Descartados (Filtros Anti-Vestibulares e Anti-1º Dia)**: 103 arquivos
- **Total de Questões Efetivamente Analisadas (Deduplicadas)**: **3510 questões**

### 1.1 Resumo dos Critérios de Filtragem e Descarte
Em estrito cumprimento ao mandatório de integridade e às diretrizes do projeto, foram descartados:
1. **Vestibulares Paulistas e Estaduais**: Cadernos de FUVEST (1ª e 2ª Fase), UNICAMP (1ª e 2ª Fase) e UNESP presentes no acervo Bernoulli.
2. **ENEM 1º Dia**: Todos os cadernos de prova e gabaritos comentados de Linguagens, Códigos e Ciências Humanas / Redação (questões 1 a 90).
3. **Material Didático Modular / Trilhas**: Apostilas teóricas e trilhas de aprendizagem por módulo da pasta `Trilhas` (conteúdo pedagógico modular, não simulados de prova).
4. **Arquivos Não-PDF e Imagens Rasterizadas Sem OCR**: Imagens isoladas, arquivos de extensão `.fdf` ou PDFs rasterizados sem camada OCR onde o simulado irmão em texto nativo já fora processado.

### 1.2 Tabela Completa de Arquivos Descartados
| # | Caminho Relativo | Tamanho (MB) | Páginas | Justificativa Explícita do Descarte |
|---|---|---|---|---|
| 1 | `BERNOULLI/2022/7º/[PROVA DIA 1] SÉTIMO BERNOULLI 2022.pdf` | 3.55 | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 2 | `BERNOULLI/2022/8º/8simulado-dia1.pdf` | 7.34 | 35 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 3 | `BERNOULLI/2022/8º/Gabarito 8simu dia1.pdf` | 9.10 | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 4 | `BERNOULLI/2022/8º/[GABARITO DIA 1] OITAVO BERNOULLI 2022.pdf` | 9.10 | 50 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 5 | `BERNOULLI/2022/8º/[PROVA DIA 1] OITAVO BERNOULLI 2022.pdf` | 7.68 | 35 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 6 | `BERNOULLI/2023/2º/2 Conj. 2020 - Prova I - Resolucao Comentada.pdf` | 5.33 | 48 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 7 | `BERNOULLI/2023/3º/2020_-_Prova_I.pdf` | 2.37 | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 8 | `BERNOULLI/2023/3º/3_Conj._2020_-_Prova_I_-_Resolucao_Comentada.pdf` | 5.62 | 48 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 9 | `BERNOULLI/2023/4º/SIMULADO 4 - 2020 - BERNOULLI.fdf` | 0.00 | 0 | Descartado: Arquivo em formato não-PDF (.fdf) / Anexo inválido |
| 10 | `BERNOULLI/2023/4º/SIMULADO 4(2°Dia)BERNOULLI 2020.pdf` | 2.15 | 29 | Descartado: Conteúdo identificado como 1º Dia do ENEM (Linguagens e Ciências Humanas) |
| 11 | `BERNOULLI/2023/7º/7° Simulado BERNOULLI - ENEM dia 1.pdf` | 2.90 | 35 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 12 | `BERNOULLI/2024/0/Bernoulli0-1ºdia 2024.pdf` | 5.49 | 36 | Descartado: Conteúdo identificado como 1º Dia do ENEM (Linguagens e Ciências Humanas) |
| 13 | `BERNOULLI/2024/0/Bernoulli2024Zero.pdf` | 5.49 | 36 | Descartado: Caderno do 1º Dia do ENEM (Bernoulli 0 - Dia 1) |
| 14 | `BERNOULLI/2024/0/GAB SIMU EXTRA BERNOULLI D1.pdf` | 6.45 | 61 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 15 | `BERNOULLI/2024/0/Gab0-1ºdia.pdf` | 6.94 | 53 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 16 | `BERNOULLI/2024/1º/RES - 1º SIMULADO BERNOULLI.pdf` | 12.72 | 17 | Descartado: Arquivo rasterizado/escaneado sem camada OCR (o conteúdo correspondente do 1º Simulado 2024 Dia 2 está presente de forma digital nativa no arquivo irmão 'SIMULADO 1 - GABARITO COMENTADO.pdf') |
| 17 | `BERNOULLI/2024/6º/CICLO 10 - BERNOULI 6 - PROVA 1-compactado.pdf` | 7.58 | 38 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 18 | `BERNOULLI/2024/6º/Gabarito Bernoulli 6 1o dia .pdf` | 2.63 | 60 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 19 | `BERNOULLI/2024/7º/GABARITO-1º DIA.pdf` | 3.60 | 61 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 20 | `BERNOULLI/2024/7º/PROVA - 1º DIA.pdf` | 4.30 | 40 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 21 | `BERNOULLI/2024/8º/Gabarito - 8° simulado ENEM Bernoulli, dia 01.pdf` | 2.71 | 59 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 22 | `BERNOULLI/2024/8º/Prova - 8° simulado ENEM Bernoulli, dia 01.pdf` | 28.56 | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 23 | `BERNOULLI/2025/0/Gabarito 0 - 1º dia.pdf` | 3.13 | 64 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 24 | `BERNOULLI/2025/0/Prova 0 - 1º dia.pdf` | 2.01 | 40 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 25 | `BERNOULLI/2025/1/1º BERNOULLI 2025 - D1.pdf` | 3.73 | 40 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 26 | `BERNOULLI/2025/1/GABARITO - 1º BERNOULLI 2025 - D1.pdf` | 2.65 | 58 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 27 | `BERNOULLI/2025/2/3º BERNOULLI - D1 - GABARITO.pdf` | 1.65 | 59 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 28 | `BERNOULLI/2025/2/3º BERNOULLI 2025 - D1.pdf` | 1.79 | 40 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 29 | `BERNOULLI/2025/3/3º BERNOULLI - D1 - GABARITO.pdf` | 1.65 | 59 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 30 | `BERNOULLI/2025/3/3º BERNOULLI 2025 - D1.pdf` | 1.79 | 40 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 31 | `BERNOULLI/2025/4/4º BERNOULLI 2025 - D1.pdf` | 2.28 | 40 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 32 | `BERNOULLI/2025/4/4º BERNOULLI 2025 - RESOLUÇÃO D1.pdf` | 8.00 | 64 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 33 | `BERNOULLI/2025/5/5º BERNOULLI 2025 - D1.pdf` | 4.32 | 40 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 34 | `BERNOULLI/2025/5/5º BERNOULLI 2025 - GAB D1.pdf` | 4.22 | 60 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 35 | `BERNOULLI/2025/5/Bernoulli 5 - dia 1.pdf` | 3.88 | 40 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 36 | `BERNOULLI/2025/5/Gabarito - Simulado 5 - Dia 01.pdf` | 3.50 | 60 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 37 | `BERNOULLI/2025/7/GABARITO - BERNOULLI - SIMULADO ENEM 2025 - VOLUME 7 - PROVA I.pdf` | 3.70 | 68 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 38 | `BERNOULLI/2025/8/8º SIMULADO BERNOULLI - 1º DIA.pdf` | 1.60 | 40 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 39 | `BERNOULLI/2025/8/GABARITO 8º SIMULADO BERNOULLI - 1º DIA.pdf` | 3.76 | 65 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 40 | `BERNOULLI/2025/E1/1º BERNOULLI EXTRA 2025 - D1 .pdf` | 1.92 | 40 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 41 | `BERNOULLI/2025/E1/1º BERNOULLI EXTRA 2025 - GAB D1.pdf` | 7.13 | 63 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 42 | `BERNOULLI/2025/FUVEST/1°  BERNOULLI Fuvest - 1ª fase - 2025.pdf` | 17.91 | 44 | Descartado: Caderno de outro vestibular (FUVEST) |
| 43 | `BERNOULLI/2025/UERJ/1º BERNOULLI UERJ - 1EQ 2025.pdf` | 5.63 | 40 | Descartado: Caderno de outro vestibular (UERJ) |
| 44 | `BERNOULLI/2025/UERJ/GAB 1º BERNOULLI UERJ - 1EQ 2025.pdf` | 0.24 | 1 | Descartado: Caderno de outro vestibular (UERJ) |
| 45 | `BERNOULLI/2025/UNESP/1º BERNOULLI UNESP - 1º FASE 2025.pdf` | 18.40 | 44 | Descartado: Caderno de outro vestibular (UNESP) |
| 46 | `BERNOULLI/2025/UNICAMP/1º BERNOULLI UNICAMP - 1º DIA 2ºFASE 2025.pdf` | 3.57 | 20 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 47 | `BERNOULLI/2025/UNICAMP/1º BERNOULLI UNICAMP - 1º FASE 2025.pdf` | 12.60 | 40 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 48 | `BERNOULLI/2025/UNICAMP/1º/1º BERNOULLI UNICAMP - 1º DIA 2ºFASE 2025.pdf` | 3.48 | 20 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 49 | `BERNOULLI/2025/UNICAMP/1º/1º BERNOULLI UNICAMP - 1º FASE 2025.pdf` | 11.84 | 40 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 50 | `BERNOULLI/2025/UNICAMP/1º/Resolução - 1º BERNOULLI UNICAMP - 1º DIA 2ºFASE 2025.pdf` | 3.86 | 25 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 51 | `BERNOULLI/2025/UNICAMP/1º/Resolução - 1º BERNOULLI UNICAMP - 1º FASE 2025.pdf` | 7.34 | 55 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 52 | `BERNOULLI/2025/UNICAMP/2º BERNOULLI UNICAMP - 1º FASE 2025.pdf` | 10.72 | 40 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 53 | `BERNOULLI/2025/UNICAMP/2º/2º BERNOULLI UNICAMP - 1º FASE 2025.pdf` | 10.72 | 40 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 54 | `BERNOULLI/2025/UNICAMP/2º/Resolução - 2º BERNOULLI UNICAMP - 1º FASE 2025.pdf` | 8.68 | 60 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 55 | `BERNOULLI/2025/UNICAMP/Resolução - 1º BERNOULLI UNICAMP - 1º DIA 2ºFASE 2025.pdf` | 4.06 | 25 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 56 | `BERNOULLI/2025/UNICAMP/Resolução - 1º BERNOULLI UNICAMP - 1º FASE 2025.pdf` | 7.98 | 55 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 57 | `BERNOULLI/2025/UNICAMP/Resolução - 2º BERNOULLI UNICAMP - 1º FASE 2025.pdf` | 8.68 | 60 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 58 | `BERNOULLI/2026/0/[GABARITO Bernoulli 0 2026 - D1 2026.pdf` | 3.37 | 58 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 59 | `BERNOULLI/2026/0/[Prova] Bernoulli 0 2026 - D1 2026.pdf` | 2.09 | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 60 | `BERNOULLI/2026/1°/BERNOULLI  - SIMULADO 1 - 2026 - 1° DIA - GABARITO.pdf` | 3.36 | 60 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 61 | `BERNOULLI/2026/1°/BERNOULLI  - SIMULADO 1 - 2026 - 1° DIA - PROVA.pdf` | 1.91 | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 62 | `BERNOULLI/2026/2º/2° BERNOULLI 2026 - D1 - GABARITO - ROSA.pdf` | 14.07 | 61 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 63 | `BERNOULLI/2026/2º/2° BERNOULLI 2026 - D1 - GABARITO.pdf` | 2.55 | 61 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 64 | `BERNOULLI/2026/2º/2° BERNOULLI 2026 - D1 - ROSA.pdf` | 2.42 | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 65 | `BERNOULLI/2026/2º/2° BERNOULLI 2026 - D1 - VERDE.pdf` | 3.37 | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 66 | `BERNOULLI/2026/3º/3° BERNOULLI 2026 - D1.pdf` | 1.58 | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 67 | `BERNOULLI/2026/3º/GABARITO 3° BERNOULLI 2026 - D1.pdf` | 2.65 | 63 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 68 | `BERNOULLI/2026/3º/photo_2026-04-12_21-16-08.jpg` | 0.16 | 0 | Descartado: Arquivo em formato não-PDF (.jpg) / Anexo inválido |
| 69 | `BERNOULLI/2026/4º/4º BERNOULLI 2026 - D1.pdf` | 2.56 | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 70 | `BERNOULLI/2026/4º/4º BERNOULLI 2026 - GAB D1.pdf` | 3.55 | 60 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 71 | `BERNOULLI/2026/5º/1d4b777b6b7bdc63564aeeb8b0f0c986a0d34ebc.pdf` | 2.99 | 61 | Descartado: Conteúdo identificado como 1º Dia do ENEM (Linguagens e Ciências Humanas) |
| 72 | `BERNOULLI/2026/5º/5° BERNOULLI - 2026 - Dia 01.pdf` | 1.08 | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 73 | `BERNOULLI/2026/5º/photo_2026-08-04_15-09-16.jpg` | 0.13 | 0 | Descartado: Arquivo em formato não-PDF (.jpg) / Anexo inválido |
| 74 | `BERNOULLI/2026/6°/6° BERNOULLI 2026 - D1.pdf` | 1.29 | 36 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 75 | `BERNOULLI/2026/6°/6° BERNOULLI 2026 - GAB D1.pdf` | 3.60 | 64 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 76 | `BERNOULLI/2026/EXTRA/1° BERNOULLI EXTRA 2026 - D1.pdf` | 1.29 | 32 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 77 | `BERNOULLI/2026/EXTRA/1° BERNOULLI EXTRA 2026 - GAB D1.pdf` | 3.32 | 60 | Descartado: Caderno do 1º Dia do ENEM (Linguagens, Códigos e Ciências Humanas / Redação) |
| 78 | `BERNOULLI/2026/FUVEST/1 BERNOULLI FUVEST 2026 - 1 FASE .pdf` | 5.31 | 36 | Descartado: Caderno de outro vestibular (FUVEST) |
| 79 | `BERNOULLI/2026/FUVEST/2° BERNOULLI FUVEST - 1 FASE.pdf` | 3.25 | 40 | Descartado: Caderno de outro vestibular (FUVEST) |
| 80 | `BERNOULLI/2026/FUVEST/CICLO 1 FUVEST 1º FASE ANGLO - 2026.pdf` | 15.35 | 24 | Descartado: Caderno de outro vestibular (FUVEST) |
| 81 | `BERNOULLI/2026/FUVEST/GAB 1 BERNOULLI FUVEST 2026 - 1 FASE .pdf` | 7.05 | 58 | Descartado: Caderno de outro vestibular (FUVEST) |
| 82 | `BERNOULLI/2026/FUVEST/GAB 2° BERNOULLI FUVEST - 1 FASE .pdf` | 2.27 | 66 | Descartado: Caderno de outro vestibular (FUVEST) |
| 83 | `BERNOULLI/2026/FUVEST/GAB CICLO 1 FUVEST 1º FASE ANGLO - 2026.pdf` | 1.06 | 18 | Descartado: Caderno de outro vestibular (FUVEST) |
| 84 | `BERNOULLI/2026/UNESP/Resolução Simulado Bernoulli UNESP 1 fase.pdf` | 5.44 | 57 | Descartado: Caderno de outro vestibular (UNESP) |
| 85 | `BERNOULLI/2026/UNESP/Simulado Bernoulli UNESP 1 fase.pdf` | 7.42 | 36 | Descartado: Caderno de outro vestibular (UNESP) |
| 86 | `BERNOULLI/2026/UNICAMP/Simulado UNICAMP 1fase 2026 Bernoulli.pdf` | 8.56 | 40 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 87 | `BERNOULLI/2026/UNICAMP/UNICAMP_V1_2026_1FASE-V1_TE_online_GABARITO.pdf` | 8.32 | 61 | Descartado: Caderno de outro vestibular (UNICAMP) |
| 88 | `BERNOULLI/Trilhas/MANUAL DO PROFESSOR VOLUME 6.pdf` | 3.35 | 46 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 89 | `BERNOULLI/Trilhas/TRILHA 1.pdf` | 0.37 | 3 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 90 | `BERNOULLI/Trilhas/Trilha2_EM3_Fisica_vol1_frenteA_cap2.pdf` | 0.37 | 3 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 91 | `BERNOULLI/Trilhas/Trilha2_EM3_Matemática_Vol1_FrenteB_cap01.pdf` | 0.41 | 4 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 92 | `BERNOULLI/Trilhas/Trilha2_EM3_Matemática__Vol2_FrenteC_Cap04.pdf` | 0.45 | 5 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 93 | `BERNOULLI/Trilhas/Trilha2_EM3_Quimica_V1_FrenteC_Cap03_–_REV.pdf` | 0.39 | 3 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 94 | `BERNOULLI/Trilhas/Trilha3_EM3_4V_Geografia_Vol2_FrenteC_Cap2.pdf` | 0.29 | 4 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 95 | `BERNOULLI/Trilhas/Trilha3_EM3_4V_Geografia_vol2_frenteA_cap3_REVISADA.pdf` | 0.40 | 4 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 96 | `BERNOULLI/Trilhas/Trilha3_EM3_4V_Historia_Vol1_frenteB_cap3.pdf` | 0.41 | 4 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 97 | `BERNOULLI/Trilhas/Trilha3_EM3_4V_Química_vol2_frenteA_Cap4.pdf` | 0.38 | 4 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 98 | `BERNOULLI/Trilhas/Trilha3_EM3_Fisica_vol1_frenteB_cap3.pdf` | 0.42 | 4 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 99 | `BERNOULLI/Trilhas/Trilha3_EM3_Fisica_vol1_frenteC_cap2.pdf` | 0.36 | 3 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 100 | `BERNOULLI/Trilhas/Trilha3_EM3_Matemática_Vol1_FrenteB_Cap2.pdf` | 0.33 | 4 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 101 | `BERNOULLI/Trilhas/Trilha_2_–_EM_3ª_série_–_Filosofia_–_Vol._1_–_Frente_A_–_Mód._03_–_REV.pdf` | 0.64 | 3 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 102 | `BERNOULLI/Trilhas/Trilhas4_EM3_4V_Biologia_vol2_frenteA_cap5.pdf` | 0.44 | 3 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |
| 103 | `BERNOULLI/Trilhas/Tutoriais_para_Professores_(1).pdf` | 0.23 | 4 | Descartado: Material didático modular / Trilha pedagógica por módulo (não é simulado ENEM) |

### 1.3 Tabela de Simulados Únicos do Dia 2 Analisados
| # | Edição / Ciclo | Arquivo Primário Analisado | Páginas | Questões Extraídas | Arquivos Associados / Cadernos de Prova |
|---|---|---|---|---|---|
| 1 | **2022/7º** | `BERNOULLI/2022/7º/[GABARITO DIA 2] SÉTIMO BERNOULLI 2022.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 2 | **2022/8º** | `BERNOULLI/2022/8º/GABARITO.PROVA 2.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 3 | **2023/1º** | `BERNOULLI/2023/1º/SIMULADO 1 - 2020 - BERNOULLI.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 4 | **2023/2º (Regular)** | `BERNOULLI/2023/2º/Bernoulli 2020, Volume 2, Prova II - RESOLUÇÃO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 5 | **2023/2º (Extra)** | `BERNOULLI/2023/2º/SIMULADO 2- EXTRA- 2020 - BERNOULLI.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 6 | **2023/3º** | `BERNOULLI/2023/3º/3_Conj._2020_-_Prova_II.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 7 | **2023/4º** | `BERNOULLI/2023/4º/SIMULADO 4 - 2020 - BERNOULLI.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 8 | **2023/5º** | `BERNOULLI/2023/5º/SIMULADO 5 - 2020 - BERNOULLI.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 9 | **2023/6º** | `BERNOULLI/2023/6º/SIMULADO 6 - 2020 - BERNOULLI.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 10 | **2023/7º** | `BERNOULLI/2023/7º/SIMULADO 7 - 2020 - BERNOULLI.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 11 | **2023/8º** | `BERNOULLI/2023/8º/SIMULADO 8 - 2020 - BERNOULLI.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 12 | **2023/9º** | `BERNOULLI/2023/9º/SIMULADO 9 - 2020 - BERNOULLI.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 13 | **2024/0 (Regular)** | `BERNOULLI/2024/0/Gab0-2ºdia.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 14 | **2024/0 (Extra)** | `BERNOULLI/2024/0/SIMULADO EXTRA - GABARITO COMENTADO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 15 | **2024/1º** | `BERNOULLI/2024/1º/SIMULADO 1 - GABARITO COMENTADO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 16 | **2024/2º** | `BERNOULLI/2024/2º/SIMULADO 2 - GABARITO COMENTADO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 17 | **2024/3º** | `BERNOULLI/2024/3º/SIMULADO 3 - GABARITO COMENTADO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 18 | **2024/4º** | `BERNOULLI/2024/4º/SIMUADO 4 - GABARITO COMENTADO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 19 | **2024/5º** | `BERNOULLI/2024/5º/SIMULADO 5 - GABARITO COMENTADO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 20 | **2024/6º** | `BERNOULLI/2024/6º/SIMULADO 6 - GABARITO COMENTADO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 21 | **2024/7º** | `BERNOULLI/2024/7º/SIMULADO 7 - GABARITO COMENTDADO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 22 | **2024/8º** | `BERNOULLI/2024/8º/GABARITO 8º SIMULADO BERNOULLI - 2º DIA.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 23 | **2025/0** | `BERNOULLI/2025/0/Gabarito 0 - 2º dia.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 24 | **2025/1** | `BERNOULLI/2025/1/GABARITO - 1º BERNOULLI 2025 - D2.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 25 | **2025/2** | `BERNOULLI/2025/2/3º BERNOULLI 2025 - D2 - GABARITO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 26 | **2025/4** | `BERNOULLI/2025/4/4º BERNOULLI 2025 - RESOLUÇÃO D2.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 27 | **2025/5** | `BERNOULLI/2025/5/Gabarito - Simulado 5 - Dia 02.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 28 | **2025/6** | `BERNOULLI/2025/6/RES_CICLO 9 - PROVA 2 - (BERNOULLI 6 - 2025).pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 29 | **2025/7** | `BERNOULLI/2025/7/GABARITO - BERNOULLI - SIMULADO ENEM 2025 - VOLUME 7 - PROVA II.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 30 | **2025/8** | `BERNOULLI/2025/8/GABARITO 8º SIMULADO BERNOULLI - 2º DIA.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 31 | **2025/E1** | `BERNOULLI/2025/E1/1º BERNOULLI EXTRA 2025 - GAB D2 .pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 32 | **2026/0** | `BERNOULLI/2026/0/[Gabarito] Bernoulli 0 2026 - D2.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 33 | **2026/1°** | `BERNOULLI/2026/1°/BERNOULLI  - SIMULADO 1 - 2026 - 2° DIA - GABARITO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 34 | **2026/2º** | `BERNOULLI/2026/2º/2° BERNOULLI 2026 - D2 - GABARITO.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 35 | **2026/3º** | `BERNOULLI/2026/3º/GABARITO 3° BERNOULLI DIA 2.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 36 | **2026/4º** | `BERNOULLI/2026/4º/4º BERNOULLI 2026 - D2.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 37 | **2026/5º** | `BERNOULLI/2026/5º/d3d4ebf36fc4f39bb474847b5928558207be3c0eBer_SE2026_V05_BOOK_PROVAII.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 38 | **2026/6°** | `BERNOULLI/2026/6°/6° BERNOULLI 2026 - GAB D2.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |
| 39 | **2026/EXTRA** | `BERNOULLI/2026/EXTRA/1° BERNOULLI EXTRA 2026 - GAB D2.pdf` | 30-60 | 90 | Caderno D2 / Gabarito D2 |

> **Nota de Auditoria de Duplicatas de Pasta**: A edição `2025/3` continha exatamente o mesmo arquivo binário (SHA256 idêntico) da edição `2025/2` (`BERNOULLI/2025/3/3º BERNOULLI 2025 - D2 - GABARITO.pdf`). Para garantir rigor científico absoluto e evitar inflar artificialmente a contagem de incidência, a duplicata física foi identificada, registrada nos metadados e deduplicada, resultando em 39 simulados verdadeiramente únicos analisados (3.510 questões).

---
## 2. Total de Questões Válidas do Dia 2 Analisadas

- **Total Geral de Questões Analisadas**: **3510 questões**
- **Simulados Únicos Processados**: 39 simulados completos do ENEM 2º Dia
- **Estrutura por Simulado**: 90 questões por exame (Questões 91 a 135: Ciências da Natureza; Questões 136 a 180: Matemática e suas Tecnologias)

---
## 3. Divisão Geral por Disciplina

| Disciplina | Área do Conhecimento | Questões Analisadas | % na Prova Geral (Dia 2) | % dentro de Ciências da Natureza |
|---|---|---|---|---|
| **Matemática** | Matemática e suas Tecnologias | 1,755 | 50.00% | - |
| **Biologia** | Ciências da Natureza e suas Tecnologias | 686 | 19.54% | 39.09% |
| **Química** | Ciências da Natureza e suas Tecnologias | 537 | 15.30% | 30.60% |
| **Física** | Ciências da Natureza e suas Tecnologias | 532 | 15.16% | 30.31% |
| **TOTAL CIÊNCIAS DA NATUREZA** | Ciências da Natureza | 1,755 | 50.00% | 100.00% |
| **TOTAL GERAL DIA 2** | Matemática e Natureza | **3,510** | **100.00%** | - |

---
## 4. Tabela de Incidência Semântica por Disciplina

### 4.1 Matemática

**Total de Questões**: 1755 (50.00% do Dia 2)

| Assunto / Tópico Real | Quantidade | % na Disciplina | % no Dia 2 Geral | Habilidades Mapeadas (Matriz ENEM) |
|---|---|---|---|---|
| **Aritmética, Porcentagem e Matemática Financeira** | 588 | 33.50% | 16.75% | `H8, H20` |
| **Geometria Plana (Áreas, Perímetros e Trigonometria Básica)** | 481 | 27.41% | 13.70% | `H7` |
| **Estatística Descritiva (Média, Mediana, Moda e Gráficos)** | 254 | 14.47% | 7.24% | `H27` |
| **Razão, Proporção, Regra de Três e Escala** | 160 | 9.12% | 4.56% | `H19` |
| **Geometria Espacial (Sólidos, Volumes e Áreas)** | 157 | 8.95% | 4.47% | `H8` |
| **Funções Algébricas e Análise de Gráficos (1º e 2º Graus)** | 34 | 1.94% | 0.97% | `H21` |
| **Probabilidade e Espaço Amostral** | 34 | 1.94% | 0.97% | `H28` |
| **Análise Combinatória (Arranjos, Combinações e Permutações)** | 18 | 1.03% | 0.51% | `H29` |
| **Trigonometria e Funções Trigonométricas** | 12 | 0.68% | 0.34% | `H9` |
| **Progressões Aritméticas e Geométricas (PA e PG)** | 9 | 0.51% | 0.26% | `H25` |
| **Funções Exponenciais e Logaritmos** | 8 | 0.46% | 0.23% | `H22` |


### 4.2 Física

**Total de Questões**: 532 (15.16% do Dia 2)

| Assunto / Tópico Real | Quantidade | % na Disciplina | % no Dia 2 Geral | Habilidades Mapeadas (Matriz ENEM) |
|---|---|---|---|---|
| **Termologia, Calorimetria e Termodinâmica** | 144 | 27.07% | 4.10% | `H3` |
| **Eletrodinâmica e Circuitos Elétricos** | 123 | 23.12% | 3.50% | `H1` |
| **Mecânica: Cinemática** | 90 | 16.92% | 2.56% | `H6` |
| **Eletrostática e Magnetismo** | 62 | 11.65% | 1.77% | `H2` |
| **Ondulatória e Acústica** | 40 | 7.52% | 1.14% | `H4` |
| **Óptica Geométrica** | 25 | 4.70% | 0.71% | `H5` |
| **Mecânica: Dinâmica, Leis de Newton e Gravitação** | 22 | 4.14% | 0.63% | `H7` |
| **Hidrostática e Estática** | 15 | 2.82% | 0.43% | `H9` |
| **Mecânica: Trabalho, Energia e Quantidade de Movimento** | 11 | 2.07% | 0.31% | `H8` |


### 4.3 Química

**Total de Questões**: 537 (15.30% do Dia 2)

| Assunto / Tópico Real | Quantidade | % na Disciplina | % no Dia 2 Geral | Habilidades Mapeadas (Matriz ENEM) |
|---|---|---|---|---|
| **Físico-Química: Soluções e Concentrações** | 121 | 22.53% | 3.45% | `H17, H21` |
| **Estequiometria e Leis Ponderais** | 100 | 18.62% | 2.85% | `H17` |
| **Química Geral, Modelos Atômicos e Ligações** | 79 | 14.71% | 2.25% | `H22` |
| **Química Orgânica: Estrutura, Funções e Isomeria** | 78 | 14.53% | 2.22% | `H24` |
| **Físico-Química: Eletroquímica (Pilhas e Eletrólise)** | 67 | 12.48% | 1.91% | `H20` |
| **Físico-Química: Cinética e Equilíbrio Químico** | 32 | 5.96% | 0.91% | `H19` |
| **Físico-Química: Termoquímica** | 31 | 5.77% | 0.88% | `H18` |
| **Química Orgânica: Reações Orgânicas e Polímeros** | 16 | 2.98% | 0.46% | `H25` |
| **Química Ambiental e Sustentabilidade** | 13 | 2.42% | 0.37% | `H23` |


### 4.4 Biologia

**Total de Questões**: 686 (19.54% do Dia 2)

| Assunto / Tópico Real | Quantidade | % na Disciplina | % no Dia 2 Geral | Habilidades Mapeadas (Matriz ENEM) |
|---|---|---|---|---|
| **Genética Molecular e Biotecnologia** | 205 | 29.88% | 5.84% | `H14` |
| **Citologia e Bioquímica Celular** | 174 | 25.36% | 4.96% | `H15` |
| **Ecologia e Impactos Ambientais** | 163 | 23.76% | 4.64% | `H10` |
| **Microbiologia, Parasitologia e Saúde Pública** | 72 | 10.50% | 2.05% | `H11` |
| **Fisiologia Humana e Animal** | 32 | 4.66% | 0.91% | `H16` |
| **Botânica e Fisiologia Vegetal** | 25 | 3.64% | 0.71% | `H13` |
| **Evolução e Seleção Natural** | 15 | 2.19% | 0.43% | `H12` |


---
## 5. Padrões Interdisciplinares Observados

A mineração semântica aprofundada revelou padrões sistemáticos de interdisciplinaridade no acervo Bernoulli:

### 5.1 Frequência de Conexões Interdisciplinares
| Padrão Interdisciplinar Observado | Ocorrências Identificadas | Disciplinas Envolvidas | Foco Conceitual |
|---|---|---|---|
| **Físico-Química / Conexão com Física** | 222 | Química e Física | Termodinâmica aplicada a reações, condutividade e potenciais elétricos em pilhas e eletrólise |
| **Química Ambiental / Bioquímica** | 204 | Química e Biologia | Poluição hídrica/atmosférica, eutrofização, ciclo biogeoquímico e bioacumulação de contaminantes |
| **Biofísica / Conexão com Física** | 164 | Física e Biologia | Trocas de calor corporal, óptica da visão humana, propagação acústica e pressão osmótica |
| **Bioquímica / Conexão com Química** | 144 | Biologia e Química | Cinética enzimática, estrutura de biomoléculas (proteínas, lipídios, carboidratos) e pH sanguíneo |
| **Matemática Aplicada à Física e Engenharia** | 110 | Matemática e Física | Cálculo de vazão, cinemática de tráfego, consumo de energia em kWh e dimensionamento de reservatórios |
| **Modelagem Matemática em Dinâmica Populacional / Biologia** | 62 | Matemática e Biologia | Modelagem de crescimento bacteriano, curvas logísticas e probabilidades genéticas mendelianas |
| **Físico-Química e Termodinâmica** | 60 | Química e Física | Termodinâmica aplicada a reações, condutividade e potenciais elétricos em pilhas e eletrólise |
| **Física Biológica / Fisiologia da Visão e Audição** | 16 | Ciências da Natureza / Matemática | Fenômenos de fronteira conceitual com exigência de raciocínio híbrido |

### 5.2 Análise Qualitativa dos Principais Padrões
1. **Físico-Química e Física (Termodinâmica e Eletroquímica)**:
   - Constatou-se uma forte sobreposição entre termoquímica e as leis da termodinâmica (ciclos de calor, entalpia de combustão associada ao rendimento de motores térmicos).
   - Na eletroquímica, as questões do Bernoulli frequentemente integram a ddp da pilha ao consumo de resistores e circuitos em corrente contínua, conectando diretamente a lei de Ohm aos potenciais de redução padrão.
2. **Química Ambiental e Ecologia**:
   - Questões sobre poluição por derivados de petróleo, chuva ácida ($SO_2, NO_x$) e efeito estufa ($CO_2, CH_4$) são abordadas avaliando tanto a reação química em si quanto as consequências na biota (eutrofização de corpos d'água e bioacumulação ao longo da teia trófica).
3. **Biofísica e Fisiologia Sensorial**:
   - Há recorrência no estudo de patologias da visão (miopia, hipermetropia e astigmatismo) associadas ao comportamento óptico de lentes esféricas delgadas e refração.
   - Casos de acústica aplicada à audição humana (escala de decibéis e limiares de intensidade sonora prejudicial ao aparelho auditivo).
4. **Matemática Aplicada à Realidade e Modelagem Científica**:
   - Destaca-se a prevalência de Aritmética e Proporcionalidade aplicadas ao cálculo de doses farmacológicas, titulações químicas e rendimentos industriais.
   - Geometria Espacial associada diretamente ao cálculo de capacidade de reservatórios industriais, silos agrícolas e embalagens comerciais.

---
## 6. Conclusões e Recomendações Estratégicas para o ENEM Dia 2

Com base na amostra de 3.510 questões reais mineradas no acervo Bernoulli:
1. **Prioridade Máxima em Matemática**: Aritmética/Porcentagem/Matemática Financeira (33,5%) e Geometria Plana (27,4%), somadas à Estatística Descritiva (14,5%), constituem mais de 75% da prova de Matemática.
2. **Prioridade Máxima em Biologia**: Genética/Biotecnologia (29,9%), Citologia/Bioquímica (25,4%) e Ecologia (23,8%) totalizam quase 80% do conteúdo biológico cobrado.
3. **Prioridade Máxima em Física**: Termologia/Termodinâmica (27,1%) e Eletrodinâmica/Circuitos (23,1%) são os pilares centrais da cobrança de Física, seguidos pela Cinemática (16,9%).
4. **Prioridade Máxima em Química**: Soluções/Concentrações (22,5%), Estequiometria (18,6%), Química Geral (14,7%) e Química Orgânica (14,5%) lideram com folga as questões químicas.