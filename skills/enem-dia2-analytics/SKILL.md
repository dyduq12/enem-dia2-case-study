---
name: enem-dia2-analytics
description: Metodologia e pipeline multiagente para mineração estatística, filtragem de não-ENEM e classificação semântica profunda de questões do ENEM Dia 2 (Matemática e Ciências da Natureza) com exportação para o MindNote.
---

# ENEM Dia 2 Analytics - Agent Skill

Esta skill formaliza a metodologia de engenharia de dados e análise cognitiva utilizada para processar grandes acervos de simulados em PDF (~5.56 GB), extrair questões autênticas do 2º Dia do ENEM, descartar ruídos e gerar cronogramas e mapas mentais acionáveis.

---

## 1. Critérios de Filtragem e Limpeza (Anti-Ruído)

Ao processar acervos mistos de simulados nacionais, cadernos de outros vestibulares frequentemente contaminam as pastas. O agente DEVE aplicar as seguintes regras de exclusão:

1. **Descarte Sumário de Vestibulares Tradicionais / Estaduais**:
   - Identificar termos no cabeçalho, rodapé ou metadados: `FUVEST`, `UNICAMP`, `UNESP`, `UERJ`, `UECE`, `UFRGS`, `UFSC`, `ITA`, `IME`, `OBF`, `OBMEP`, `OBQ`, `Prova Paulista`.
   - Se o arquivo contiver provas discursivas, número de questões incompatível ou formato disciplinar isolado não-ENEM, descartar imediatamente.

2. **Assinatura Estrutural do ENEM Dia 2**:
   - Total de 90 questões distribuídas em:
     - **Questões 91 a 135**: Ciências da Natureza e suas Tecnologias (Biologia, Física e Química intercaladas).
     - **Questões 136 a 180**: Matemática e suas Tecnologias.
   - Padrão de 5 alternativas (`A`, `B`, `C`, `D`, `E`).
   - Textos-base contextualizados com situações-problema do cotidiano.

3. **Deduplicação de Edições Canônicas**:
   - Bancas utilizam versões idênticas para turmas diferentes (ex: `Medicina`, `Extensivo`, `Nacional`).
   - Agrupar por ano, número de simulado e hash textual das primeiras 5 questões para eleger uma única edição canônica primária.

---

## 2. Taxonomia de Classificação Semântica Profunda

A classificação **NÃO** deve ser uma busca rasa de palavras-chave. Uma questão que menciona "um satélite em órbita de massa m" envolve Gravitação/Mecânica (Física), e não Astronomia descritiva. Uma questão sobre "fermentação alcoólica para produção de biocombustíveis" requer classificação em Bioquímica/Metabolismo com peso interdisciplinar em Química Orgânica.

### 2.1. Matemática e suas Tecnologias
- **M1 - Matemática Básica & Proporcionalidade**: Razão, proporção, regra de três, porcentagem, escalas, conversão de unidades, matemática financeira inicial.
- **M2 - Geometria Espacial & Plana**: Áreas de figuras planas, volumes de prismas/cilindros/cones/esferas, trigonometria básica, projeções ortogonais e vistas.
- **M3 - Estatística & Médias**: Média aritmética ponderada, moda, mediana, variância, desvio padrão e leitura crítica de gráficos/tabelas.
- **M4 - Funções & Álgebra**: Função afim, quadrática, exponencial, logarítmica e interpretação geométrica de gráficos.
- **M5 - Análise Combinatória & Probabilidade**: Princípio fundamental da contagem, permutações, arranjos, combinações e probabilidade simples/condicional.
- **M6 - Trigonometria & Tópicos Avançados**: Ciclo trigonométrico, funções periódicas, matrizes e sistemas lineares.

### 2.2. Física
- **F1 - Mecânica Clássica & Energia**: Cinemática, leis de Newton, trabalho, potência, conservação da energia mecânica, impulso e quantidade de movimento.
- **F2 - Eletrodinâmica & Circuitos**: Corrente, tensão, potência elétrica em eletrodomésticos, resistores, circuitos mistos, leis de Ohm e consumo de energia (kWh).
- **F3 - Termologia & Calorimetria**: Trocas de calor sensível/latente, calor específico, propagação térmica, termodinâmica e máquinas térmicas.
- **F4 - Ondulatória & Óptica**: Fenômenos ondulatórios (interferência, difração, refração, ressonância, efeito Doppler), espectro eletromagnético e óptica geométrica básica.

### 2.3. Química
- **Q1 - Físico-Química & Transformações**: Termoquímica (entalpia, combustão), cinética química (catalisadores, velocidade), equilíbrio químico, pH e eletroquímica (pilhas e eletrólise).
- **Q2 - Química Geral & Estequiometria**: Relações de massa, cálculo estequiométrico com rendimento e pureza, soluções (concentração em g/L, mol/L), gases e tabela periódica.
- **Q3 - Química Orgânica**: Identificação de funções orgânicas, isomeria plana e espacial, propriedades físico-químicas de compostos orgânicos e reações orgânicas principais.
- **Q4 - Química Ambiental & Soluções**: Poluição atmosférica (chuva ácida, efeito estufa), tratamento de água, separação de misturas e descarte de resíduos.

### 2.4. Biologia
- **B1 - Ecologia & Meio Ambiente**: Cadeias/teias tróficas, ciclos biogeoquímicos (carbono, nitrogênio, água), relações ecológicas, biomas e impactos antrópicos (eutrofização, biomagnificação).
- **B2 - Biotecnologia & Genética Molecular**: Engenharia genética, clonagem, transgênicos, CRISPR, PCR, teste de DNA, código genético e síntese proteica.
- **B3 - Fisiologia Humana & Saúde**: Sistemas digestório, circulatório, respiratório, excretor, nervoso e endócrino; imunologia (vacinas vs soros) e parasitoses comuns.
- **B4 - Citologia & Metabolismo Energético**: Estrutura celular, organelas e suas funções, respiração celular, fermentação e fotossíntese.

---

## 3. Protocolo de Validação Tripla (MindNote Engine)

Ao gerar mapas mentais (`.json`) para integração com o MindNote Engine, o agente deve seguir estritamente o protocolo de 3 camadas:

```mermaid
flowchart LR
    A["Python AST & Schema Check"] --> B["Node.js Engine Simulation"]
    B --> C["Headless Browser DOM Validation"]
    C --> D["Homologado para Produção"]
```

1. **Camada 1: Validação Estrutural e de Tipos (Python)**
   - Respeitar rigorosamente a tupla de 4 chaves em TODOS os nós: `titulo`, `anotacao`, `cor`, `filhos`.
   - Nós não-terminais devem conter `"anotacao": null`.
   - Nós folha devem conter `"anotacao": { "tipo": "pauta", "linhas_manuais": N }` ou `"tipo": "ilustracao"`.
   - Cores restritas aos códigos hexadecimais homologados.

2. **Camada 2: Validação no Motor de Árvores (Node.js)**
   - Simulação da lógica de cálculo de dimensões, posicionamento cartesiano de nós e layout SVG.

3. **Camada 3: Validação de Renderização Gráfica Real (Headless Edge / Chromium)**
   - Injeção do JSON no engine web real do MindNote.
   - Verificação de ausência de erros no console ou falhas de parse de layout.
   - Contagem precisa de elementos SVG (`nodeCount`, `boxCount`, `lineCount`, `pathCount`).

