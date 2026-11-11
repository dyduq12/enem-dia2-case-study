#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Geração do Mapa Mental Oficial do ENEM Dia 2 para MindNote Engine.
Estruturado com base na meta-análise estatística de 24.419 questões em FINAL/RELATORIO_CONSOLIDADO_ENEM_DIA_2.md.
"""

import os
import json

def leaf_pauta(titulo, linhas=6, cor=None):
    return {
        "titulo": titulo,
        "cor": cor,
        "anotacao": {
            "tipo": "pauta",
            "linhas_manuais": linhas
        },
        "filhos": []
    }

def leaf_ilustracao(titulo, altura=220, cor=None):
    return {
        "titulo": titulo,
        "cor": cor,
        "anotacao": {
            "tipo": "ilustracao",
            "altura_customizada": altura
        },
        "filhos": []
    }

def branch(titulo, filhos, cor=None):
    return {
        "titulo": titulo,
        "cor": cor,
        "anotacao": None,
        "filhos": filhos
    }

def build_mapa_mental():
    # ─── PARTE 1: MATEMÁTICA E SUAS TECNOLOGIAS ──────────────────────────────
    matematica_topics = [
        # Tópico 1 (1º Geral - CRUCIAL)
        branch(
            "Matemática Básica, Aritmética e Proporcionalidade",
            [
                branch("Razão, Proporção e Regra de Três", [
                    leaf_pauta("Grandezas Direta e Inversamente Proporcionais", 6),
                    leaf_pauta("Regra de Três Simples e Composta", 6),
                    leaf_pauta("Divisão em Partes Proporcionais e Médias Ponderadas", 5),
                ]),
                branch("Porcentagem e Variações Comerciais", [
                    leaf_pauta("Fatores de Multiplicação para Aumentos e Descontos", 6),
                    leaf_pauta("Variações Percentuais Sucessivas e Inflação Acumulada", 5),
                    leaf_pauta("Relações Comerciais: Custo, Lucro, Venda e Prejuízo", 5),
                ]),
                branch("Sistema Métrico e Conversão de Unidades", [
                    leaf_pauta("Conversão no Sistema Métrico Decimal: Comprimento e Área", 6),
                    leaf_pauta("Relações de Volume e Capacidade: 1 m³ = 1000 L e 1 dm³ = 1 L", 6),
                    leaf_pauta("Conversões de Tempo (Horas, Minutos e Segundos) e Vazão", 5),
                ]),
                branch("Escalas Cartográficas e Modelagem Proporcional", [
                    leaf_pauta("Escala Linear d/D e Distâncias Reais no Mapa", 6),
                    leaf_pauta("Escala de Área (d/D)² e Escala Volumétrica (d/D)³", 6),
                    leaf_ilustracao("Diagrama de Escalas Cartográficas e Redução Proporcional", 220),
                ]),
            ],
            cor="#DC2626"
        ),

        # Tópico 2 (2º Geral - CRUCIAL)
        branch(
            "Estatística Básica e Descritiva",
            [
                branch("Leitura e Interpretação Gráfica", [
                    leaf_ilustracao("Histogramas, Gráficos de Colunas e Barras Múltiplas", 220),
                    leaf_pauta("Gráficos de Setores (Pizza) e Diagramas de Linhas Temporais", 5),
                    leaf_pauta("Tabelas de Frequência Absoluta, Relativa e Acumulada", 5),
                ]),
                branch("Medidas de Tendência Central", [
                    leaf_pauta("Média Aritmética Simples e Média Ponderada", 6),
                    leaf_pauta("Mediana: Ordenação Prévia em Rol e Casos Par/Ímpar", 6),
                    leaf_pauta("Moda: Frequência Máxima e Séries Multimodais", 4),
                ]),
                branch("Medidas de Dispersão e Variabilidade", [
                    leaf_pauta("Amplitude Total e Desvio Médio Absoluto", 5),
                    leaf_pauta("Variância e Desvio-Padrão: Medição de Regularidade e Homogeneidade", 6),
                ]),
            ],
            cor="#DC2626"
        ),

        # Tópico 3 (3º Geral - ALTO)
        branch(
            "Geometria Plana",
            [
                branch("Triângulos e Relações Métricas", [
                    leaf_pauta("Teorema de Pitágoras e Ternas Pitagóricas Clássicas (3-4-5)", 6),
                    leaf_pauta("Semelhança de Triângulos e Teorema de Tales", 6),
                    leaf_ilustracao("Cálculo de Áreas: Base*Altura/2, Triângulo Equilátero e Fórmula de Heron", 220),
                ]),
                branch("Quadriláteros e Polígonos Regulares", [
                    leaf_pauta("Áreas de Quadriláteros Notáveis: Trapézio, Paralelogramo e Losango", 5),
                    leaf_pauta("Polígonos Regulares, Soma dos Ângulos Internos e Decomposição", 5),
                ]),
                branch("Circunferência e Círculo", [
                    leaf_pauta("Comprimento da Circunferência (C = 2πr) e Número de Voltas", 5),
                    leaf_pauta("Área do Círculo, Setor Circular e Coroa Circular", 6),
                    leaf_pauta("Propriedades de Inscrição e Circunscrição de Polígonos", 5),
                ]),
            ],
            cor="#D97706"
        ),

        # Tópico 4 (5º Geral - ALTO)
        branch(
            "Funções, Álgebra e Equações",
            [
                branch("Função Afim (1º Grau)", [
                    leaf_pauta("Lei f(x) = ax + b: Taxa Instantânea de Variação e Coeficiente Linear", 6),
                    leaf_ilustracao("Interpretação Gráfica da Reta: Custo Fixo vs Custo Variável", 220),
                    leaf_pauta("Equações e Sistemas Lineares com Interpretação Geométrica", 5),
                ]),
                branch("Função Quadrática (2º Grau)", [
                    leaf_pauta("Lei f(x) = ax² + bx + c: Raízes, Discriminante e Concavidade", 6),
                    leaf_pauta("Vértice da Parábola: xv = -b/2a (Ponto Crítico) e yv = -Δ/4a (Valor Máximo/Mínimo)", 6),
                    leaf_ilustracao("Gráficos de Parábolas e Trajetórias Balísticas de Projéteis", 220),
                ]),
                branch("Modelos Exponenciais e Logarítmicos", [
                    leaf_pauta("Crescimento e Decaimento Exponencial: Modelo Populacional e Depreciação", 6),
                    leaf_pauta("Logaritmos Aplicados: Propriedades Operatórias e Mudança de Base", 6),
                    leaf_pauta("Escalas Logarítmicas do Cotidiano: Richter, Escala de pH e Decibéis", 6),
                ]),
            ],
            cor="#D97706"
        ),

        # Tópico 5 (7º Geral - ALTO)
        branch(
            "Geometria Espacial",
            [
                branch("Prismas e Poliedros", [
                    leaf_pauta("Paralelepípedo e Cubo: Diagonais, Área Total e Volume (V = a*b*c)", 6),
                    leaf_pauta("Prismas Retos Regulares: Bases Triangulares, Quadradas e Hexagonais", 5),
                ]),
                branch("Corpos Redondos", [
                    leaf_pauta("Cilindro Reto: Planificação Lateral e Volume (V = π * r² * h)", 6),
                    leaf_pauta("Cone Reto e Tronco de Cone: Geratriz, Relação Pitagórica e Volume (V = 1/3 * π * r² * h)", 6),
                    leaf_pauta("Esfera: Área Superficial (4πr²) e Volume Esférico (4/3 * π * r³)", 5),
                ]),
                branch("Percepção Espacial e Projeção Ortogonal", [
                    leaf_ilustracao("Vistas Ortogonais: Visão Frontal, Superior e Lateral Esquerda", 220),
                    leaf_ilustracao("Planificação e Montagem de Sólidos Poliédricos e Redondos", 220),
                    leaf_pauta("Projeção Ortogonal de Trajetórias e Sombras sobre Planos Horizontais", 5),
                ]),
            ],
            cor="#D97706"
        ),
    ]

    # ─── PARTE 2: FÍSICA ─────────────────────────────────────────────────────
    fisica_topics = [
        # Tópico 6 (4º Geral - ALTO)
        branch(
            "Mecânica Clássica (Cinemática, Dinâmica e Energia)",
            [
                branch("Cinemática Escalar e Vetorial", [
                    leaf_pauta("Movimento Uniforme (MU): Função Horária s = s0 + v*t", 6),
                    leaf_pauta("Movimento Uniformemente Variado (MUV): Fórmulas e Equação de Torricelli", 6),
                    leaf_ilustracao("Interpretação Gráfica: Área em v x t (Deslocamento) e Tangente (Aceleração)", 220),
                    leaf_pauta("Movimento Circular Uniforme (MCU): Frequência, Período e Velocidade Angular", 5),
                ]),
                branch("Dinâmica Newtoniana e Aplicações", [
                    leaf_ilustracao("Leis de Newton e Decomposição de Forças no Plano Inclinado", 220),
                    leaf_pauta("Força de Atrito Estático e Cinético e Lei de Hooke (Força Elástica)", 6),
                    leaf_pauta("Resultante Centrípeta em Curvas Planas, Sobreelevadas e Globos da Morte", 5),
                ]),
                branch("Trabalho, Potência e Conservação de Energia", [
                    leaf_pauta("Trabalho Mecânico: W = F * d * cos θ e Interpretação Gráfica F x d", 5),
                    leaf_pauta("Conservação da Energia Mecânica: Cinética, Gravitacional e Elástica", 6),
                    leaf_pauta("Dissipação Térmica por Forças Não Conservativas e Rendimento Mecânico", 5),
                ]),
                branch("Impulso e Quantidade de Movimento", [
                    leaf_pauta("Teorema do Impulso: I = F * Δt = ΔQ e Dispositivos de Amortecimento", 6),
                    leaf_pauta("Conservação da Quantidade de Movimento em Colisões Elásticas e Inelásticas", 5),
                ]),
            ],
            cor="#D97706"
        ),

        # Tópico 7 (6º Geral - CRUCIAL)
        branch(
            "Eletrodinâmica e Circuitos Elétricos",
            [
                branch("Grandezas Fundamentais e Resistividade", [
                    leaf_pauta("Corrente Elétrica (i = ΔQ/Δt) e Diferença de Potencial Elétrico (U)", 5),
                    leaf_pauta("1ª Lei de Ohm (U = R * i) e Curva Característica de Condutores Ôhmicos", 5),
                    leaf_pauta("2ª Lei de Ohm: Resistividade, Comprimento e Área Transversal (R = ρL/A)", 6),
                ]),
                branch("Associação de Resistores e Circuitos CC", [
                    leaf_pauta("Associação em Série: Corrente Única Constante e Soma das Quedas de Tensão", 6),
                    leaf_pauta("Associação em Paralelo: DDP Idêntica e Divisão de Correntes Inversamente às Resistências", 6),
                    leaf_ilustracao("Esquematização de Circuitos Elétricos Mistos e Detecção de Curtos-Circuitos", 220),
                ]),
                branch("Potência, Consumo Residencial e Segurança", [
                    leaf_pauta("Expressões de Potência Dissipada: P = U*i = R*i² = U²/R", 6),
                    leaf_pauta("Consumo de Energia Residencial: E = P * Δt em kWh e Cálculo da Fatura de Energia", 6),
                    leaf_pauta("Dispositivos de Proteção Elétrica: Chave Disjuntora, Fusíveis e Aterramento", 5),
                ]),
            ],
            cor="#DC2626"
        ),

        # Tópico 8 (10º Geral - CRUCIAL)
        branch(
            "Termologia, Calorimetria e Termodinâmica",
            [
                branch("Calorimetria e Transições de Fase", [
                    leaf_pauta("Calor Sensível e Capacidade Térmica: Equação Fundamental Q = m * c * ΔT", 6),
                    leaf_pauta("Calor Latente e Mudança de Estado Físico: Q = m * L", 5),
                    leaf_ilustracao("Curva de Aquecimento/Resfriamento e Patamares Térmicos de Mudança de Fase", 220),
                    leaf_pauta("Balanço Térmico em Calorímetros Isolados: Somatório dos Calores ΣQ = 0", 5),
                ]),
                branch("Processos de Transmissão de Calor", [
                    leaf_pauta("Condução Térmica: Lei de Fourier, Condutibilidade em Sólidos e Isolantes", 5),
                    leaf_pauta("Convecção Térmica em Fluidos: Correntes de Convecção, Brisas e Inversão Térmica", 6),
                    leaf_pauta("Irradiação Térmica: Ondas Eletromagnéticas no Vácuo, Efeito Estufa e Emissividade", 5),
                ]),
                branch("Termodinâmica e Máquinas Térmicas", [
                    leaf_pauta("1ª Lei da Termodinâmica: Conservação de Energia (ΔU = Q - W)", 6),
                    leaf_ilustracao("Transformações Gasosas: Diagramas P x V para Isobárica, Isocórica, Isotérmica e Adiabática", 220),
                    leaf_pauta("2ª Lei da Termodinâmica e Ciclo de Carnot: Limite Máximo de Rendimento Teórico", 6),
                ]),
            ],
            cor="#DC2626"
        ),

        # Tópico 9 (14º Geral - CRUCIAL)
        branch(
            "Ondulatória e Acústica",
            [
                branch("Fundamentos da Propagação Ondulatória", [
                    leaf_pauta("Classificação: Ondas Mecânicas vs Eletromagnéticas, Transversais vs Longitudinais", 5),
                    leaf_pauta("Equação Fundamental da Onda: v = λ * f (Velocidade Dependente do Meio)", 6),
                    leaf_ilustracao("Espectro Eletromagnético Completo: Ondas de Rádio aos Raios Gama", 220),
                ]),
                branch("Fenômenos Ondulatórios Clássicos", [
                    leaf_pauta("Reflexão e Refração de Ondas: Conservação da Frequência na Mudança de Meio", 5),
                    leaf_pauta("Difração: Capacidade de Contornar Obstáculos e Fendas Proporcionais a λ", 5),
                    leaf_pauta("Interferência Construtiva/Destrutiva e Polarização de Ondas Transversais", 6),
                ]),
                branch("Acústica e Fenômenos Sonoros", [
                    leaf_pauta("Qualidades Fisiológicas do Som: Altura (Frequência), Intensidade (Amplitude) e Timbre", 6),
                    leaf_pauta("Ressonância Sonora e Mecânica: Amplificação por Coincidência de Frequências", 5),
                    leaf_pauta("Efeito Doppler: Variação Aparente da Frequência Percebida em Fontes Sonoras Móveis", 6),
                ]),
            ],
            cor="#DC2626"
        ),
    ]

    # ─── PARTE 3: BIOLOGIA ───────────────────────────────────────────────────
    biologia_topics = [
        # Tópico 10 (9º Geral - ALTO)
        branch(
            "Genética e Biologia Molecular",
            [
                branch("Genética Mendeliana e Heredogramas", [
                    leaf_pauta("1ª Lei de Mendel: Princípio da Segregação dos Fatores e Monohibridismo", 6),
                    leaf_pauta("2ª Lei de Mendel: Segregação Independente de Dois ou Mais Pares de Genes", 6),
                    leaf_ilustracao("Simbologia de Heredogramas e Determinação de Padrões Autossômicos e Sexuais", 220),
                ]),
                branch("Grupos Sanguíneos e Herança Sexual", [
                    leaf_pauta("Sistema ABO: Alelos Múltiplos (IA, IB, i), Codominância e Doações Compatíveis", 6),
                    leaf_pauta("Sistema Rh e Eritroblastose Fetal: Mecanismo de Sensibilização Materna", 5),
                    leaf_pauta("Herança Ligada ao Cromossomo X: Daltonismo e Hemofilia em Homens e Mulheres", 5),
                ]),
                branch("Dogma Central da Biologia Molecular", [
                    leaf_ilustracao("Estrutura do DNA em Dupla-Hélice, Pontes de Hidrogênio e Replicação Semiconservativa", 220),
                    leaf_pauta("Transcrição Gênica: Maturação de RNA Mensageiro por RNA-Polimerase", 6),
                    leaf_pauta("Tradução Ribossômica: Universalidade e Redundância do Código Genético (Códons)", 6),
                ]),
            ],
            cor="#D97706"
        ),

        # Tópico 11 (11º Geral - ALTO)
        branch(
            "Biotecnologia e Engenharia Genética",
            [
                branch("Tecnologia do DNA Recombinante", [
                    leaf_pauta("Enzimas de Restrição ('Endonucleases') e Ligases na Edição Molecular", 6),
                    leaf_ilustracao("Vetor Plasmídico Bacteriano e Produção Biotecnológica de Insulina Humana", 220),
                ]),
                branch("Organismos Geneticamente Modificados (OGMs)", [
                    leaf_pauta("Transgênicos vs Cisgênicos: Incorporação Estável e Transcrição de Genes Heterólogos", 6),
                    leaf_pauta("Aplicações na Agricultura: Resistência a Herbicidas e Pragas (Linhagens Bt)", 5),
                ]),
                branch("Métodos Diagnósticos e Edição de Precisão", [
                    leaf_pauta("PCR (Reação em Cadeia da Polimerase): Desnaturação, Anelamento e Extensão Térmica", 6),
                    leaf_ilustracao("Eletroforese em Gel de Agarose e Tipagem por DNA Fingerprinting", 220),
                    leaf_pauta("Edição Genômica de Precisão por CRISPR-Cas9 e Terapias Gênicas", 6),
                    leaf_pauta("Vacinas Avançadas: Plataformas de RNA Mensageiro e Vetores Virais Não Replicantes", 6),
                ]),
            ],
            cor="#D97706"
        ),

        # Tópico 12 (15º Geral - CRUCIAL)
        branch(
            "Fisiologia Humana e Imunologia",
            [
                branch("Imunologia e Defesa do Organismo", [
                    leaf_pauta("Vacina: Imunização Ativa, Preventiva, Estímulo a Linfócitos e Memória Imune", 6),
                    leaf_pauta("Soro Heterólogo: Imunização Passiva, Curativa Emergencial e Neutralização Imediata", 6),
                    leaf_ilustracao("Curva Cinética de Resposta Imune: Comparação entre Resposta Primária e Secundária", 220),
                ]),
                branch("Sistema Cardiovascular e Trocas Gasosas", [
                    leaf_ilustracao("Circulação Cardíaca Dupla e Completa: Pequena Circulação e Grande Circulação Sistêmica", 220),
                    leaf_pauta("Hematose Alveolar e Transporte de Gases: Oxi-hemoglobina e Íon Bicarbonato Plasmático", 6),
                    leaf_pauta("Controle Fisiológico da Pressão Arterial e Sistema Renina-Angiotensina", 5),
                ]),
                branch("Sistemas Digestório, Renal e Endócrino", [
                    leaf_pauta("Digestão Química Enzimática em Diferentes Faixas de pH (Boca, Estômago e Intestino)", 6),
                    leaf_pauta("Controle Pancreático da Glicemia: Ações Antagônicas de Insulina e Glucagon", 6),
                    leaf_pauta("Filtração Renal e Osmorregulação: Ação do Hormônio Antidiurético (ADH) nos Néfrons", 5),
                ]),
            ],
            cor="#DC2626"
        ),
    ]

    # ─── PARTE 4: QUÍMICA ────────────────────────────────────────────────────
    quimica_topics = [
        # Tópico 13 (8º Geral - ALTO)
        branch(
            "Físico-Química: Soluções e Concentrações",
            [
                branch("Unidades de Concentração Química", [
                    leaf_pauta("Concentração Comum (C = m_soluto / V_solucao em g/L)", 5),
                    leaf_pauta("Concentração Molar (M = n / V em mol/L) e Relações de Conversão", 6),
                    leaf_pauta("Título em Massa (% m/m) e Partes por Milhão (ppm) em Contaminantes", 6),
                ]),
                branch("Operações Físico-Químicas com Soluções", [
                    leaf_pauta("Diluição de Soluções: Conservação da Massa de Soluto (C1 * V1 = C2 * V2)", 6),
                    leaf_pauta("Mistura de Soluções de Mesmo Soluto e Concentração Resultante", 5),
                    leaf_ilustracao("Curvas e Coeficiente de Solubilidade: Regiões Insaturada, Saturada e Supersaturada", 220),
                ]),
                branch("Análise Volumétrica e Titulometria", [
                    leaf_pauta("Titulometria Ácido-Base: Ponto de Equivalência e Proporção Estequiométrica", 6),
                    leaf_pauta("Viragem de Indicadores Ácido-Base e Determinação Experimental de Concentrações", 5),
                ]),
            ],
            cor="#D97706"
        ),

        # Tópico 14 (12º Geral - ALTO)
        branch(
            "Química Geral: Cálculos Estequiométricos",
            [
                branch("Leis Ponderais e Proporções Molares", [
                    leaf_pauta("Lei de Lavoisier (Conservação das Massas) e Lei de Proust (Proporções Fixas)", 5),
                    leaf_pauta("Grandezas Fundamentais: Mol, Massa Molar, Volume Molar nas CNTP (22,4 L) e Constante de Avogadro", 6),
                    leaf_pauta("Balanceamento Estequiométrico de Equações Químicas pelo Método das Tentativas", 5),
                ]),
                branch("Casos Especiais em Estequiometria", [
                    leaf_pauta("Identificação Analítica de Reagente Limitante e Reagente em Excesso", 6),
                    leaf_pauta("Cálculos com Grau de Pureza de Reagentes em Minérios e Processos Industriais", 6),
                    leaf_pauta("Rendimento Percentual Real versus Teórico em Sínteses Químicas", 6),
                ]),
                branch("Reações Consecutivas e Aplicações Industriais", [
                    leaf_pauta("Estequiometria de Reações Sucessivas e Montagem da Equação Global", 5),
                    leaf_pauta("Cálculo Estequiométrico com Gases fora das CNTP (Equação de Clapeyron: PV = nRT)", 6),
                ]),
            ],
            cor="#D97706"
        ),

        # Tópico 15 (13º Geral - ALTO)
        branch(
            "Ciências da Natureza Integradas",
            [
                branch("Matrizes Energéticas e Sustentabilidade", [
                    leaf_pauta("Combustíveis Fósseis vs Biocombustíveis: Etanol, Biodiesel e Biogás", 6),
                    leaf_pauta("Poder Calorífico, Eficiência de Combustão e Emissão Relativa de CO2", 6),
                    leaf_ilustracao("Balanço Energético Comparativo e Matriz Elétrica Renovável (Solar, Eólica e Hídrica)", 220),
                ]),
                branch("Ciclos Biogeoquímicos e Impactos Atmosféricos", [
                    leaf_ilustracao("Ciclo do Nitrogênio Completo: Fixação, Nitrosação, Nitratação e Desnitrificação", 220),
                    leaf_pauta("Ciclo do Carbono e Intensificação Antrópica do Efeito Estufa", 6),
                    leaf_pauta("Formação da Chuva Ácida: Química dos Óxidos de Enxofre (SOx) e Nitrogênio (NOx)", 5),
                ]),
                branch("Ecotoxicologia, Poluição e Saneamento", [
                    leaf_pauta("Biomagnificação Trófica e Bioacumulação Lipídica de Metais Pesados e DDT", 6),
                    leaf_ilustracao("Mecanismo da Eutrofização Artificial em Corpos Hídricos por Nutrientes Exógenos", 220),
                    leaf_pauta("Etapas Físico-Químicas do Tratamento em Estações de Água (ETA) e Efluentes", 6),
                ]),
            ],
            cor="#D97706"
        ),
    ]

    # ─── OS 4 NÓS RAIZ PRINCIPAIS ────────────────────────────────────────────
    root_nodes = [
        branch(
            "Parte 1: Matemática e suas Tecnologias",
            matematica_topics,
            cor="#2563EB"
        ),
        branch(
            "Parte 2: Física",
            fisica_topics,
            cor="#DC2626"
        ),
        branch(
            "Parte 3: Biologia",
            biologia_topics,
            cor="#059669"
        ),
        branch(
            "Parte 4: Química",
            quimica_topics,
            cor="#7C3AED"
        ),
    ]

    return root_nodes

def main():
    mapa = build_mapa_mental()
    destino_dir = "FINAL"
    os.makedirs(destino_dir, exist_ok=True)
    caminho_arquivo = os.path.join(destino_dir, "MAPA_MENTAL_ESTUDO_ENEM.json")

    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        json.dump(mapa, f, ensure_ascii=False, indent=2)

    print(f"Sucesso: Mapa Mental exportado com êxito para {caminho_arquivo}")

if __name__ == "__main__":
    main()
