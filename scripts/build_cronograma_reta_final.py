#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Geração do Cronograma Tático de Reta Final do ENEM Dia 2 (11/11 a 14/11).
Estruturado estritamente para o MindNote Engine a partir de FINAL/MAPA_MENTAL_ESTUDO_ENEM.json.
"""

import os
import json
import copy

def clean_node(node, is_leaf=False):
    """
    Garante que o nó possui estritamente as 4 chaves exigidas pela especificação MindNote:
    'titulo', 'anotacao', 'cor', 'filhos'.
    Folhas recebem anotacao pauta com 3 linhas manuais.
    Nós intermediários recebem anotacao null.
    """
    titulo = node.get("titulo", "").strip()
    cor = node.get("cor", None)
    
    if is_leaf or len(node.get("filhos", [])) == 0:
        return {
            "titulo": titulo,
            "cor": cor,
            "anotacao": {
                "tipo": "pauta",
                "linhas_manuais": 3
            },
            "filhos": []
        }
    else:
        filhos = [clean_node(f) for f in node.get("filhos", [])]
        return {
            "titulo": titulo,
            "cor": cor,
            "anotacao": None,
            "filhos": filhos
        }

def build_cronograma():
    caminho_mapa = os.path.join("FINAL", "MAPA_MENTAL_ESTUDO_ENEM.json")
    with open(caminho_mapa, "r", encoding="utf-8") as f:
        mapa_original = json.load(f)

    # Indexar ramos originais
    ramos = {}
    for parte in mapa_original:
        for ramo in parte.get("filhos", []):
            ramos[ramo["titulo"]] = ramo

    # ─────────────────────────────────────────────────────────────────────────
    # DIA 1: 11/11 (Quarta): Pilares (Matemática Básica, Estatística, Ecologia)
    # ─────────────────────────────────────────────────────────────────────────
    mat_basica = copy.deepcopy(ramos["Matemática Básica, Aritmética e Proporcionalidade"])
    mat_basica["cor"] = "#DC2626"

    estatistica = copy.deepcopy(ramos["Estatística Básica e Descritiva"])
    estatistica["cor"] = "#DC2626"

    ecologia = copy.deepcopy(ramos["Ciências da Natureza Integradas"])
    ecologia["titulo"] = "Ciências da Natureza Integradas (Ecologia e Meio Ambiente)"
    ecologia["cor"] = "#DC2626"

    dia_1_filhos = [
        clean_node(mat_basica),
        clean_node(estatistica),
        clean_node(ecologia)
    ]

    raiz_dia_1 = {
        "titulo": "11/11 (Quarta): Pilares (Matemática Básica, Estatística, Ecologia)",
        "cor": "#DC2626",
        "anotacao": None,
        "filhos": dia_1_filhos
    }

    # ─────────────────────────────────────────────────────────────────────────
    # DIA 2: 12/11 (Quinta): Pilares (Eletrodinâmica, Termologia, Fís-Química)
    # ─────────────────────────────────────────────────────────────────────────
    eletrodinamica = copy.deepcopy(ramos["Eletrodinâmica e Circuitos Elétricos"])
    eletrodinamica["cor"] = "#DC2626"

    termologia = copy.deepcopy(ramos["Termologia, Calorimetria e Termodinâmica"])
    termologia["cor"] = "#DC2626"

    fis_quimica = copy.deepcopy(ramos["Físico-Química: Soluções e Concentrações"])
    fis_quimica["cor"] = "#D97706"

    dia_2_filhos = [
        clean_node(eletrodinamica),
        clean_node(termologia),
        clean_node(fis_quimica)
    ]

    raiz_dia_2 = {
        "titulo": "12/11 (Quinta): Pilares (Eletrodinâmica, Termologia, Fís-Química)",
        "cor": "#DC2626",
        "anotacao": None,
        "filhos": dia_2_filhos
    }

    # ─────────────────────────────────────────────────────────────────────────
    # DIA 3: 13/11 (Sexta): Consolidadores (Geometria, Funções, Genética, Ondulatória)
    # ─────────────────────────────────────────────────────────────────────────
    geo_plana = copy.deepcopy(ramos["Geometria Plana"])
    geo_plana["cor"] = "#D97706"

    geo_espacial = copy.deepcopy(ramos["Geometria Espacial"])
    geo_espacial["cor"] = "#D97706"

    # Filtrar Nível 3 de Funções (retirar Modelos Exponenciais e Logarítmicos)
    funcoes = copy.deepcopy(ramos["Funções, Álgebra e Equações"])
    funcoes["cor"] = "#D97706"
    funcoes["filhos"] = [sb for sb in funcoes.get("filhos", []) if "Logarítmicos" not in sb.get("titulo", "")]

    genetica = copy.deepcopy(ramos["Genética e Biologia Molecular"])
    genetica["cor"] = "#D97706"

    ondulatoria = copy.deepcopy(ramos["Ondulatória e Acústica"])
    ondulatoria["cor"] = "#DC2626"

    dia_3_filhos = [
        clean_node(geo_plana),
        clean_node(geo_espacial),
        clean_node(funcoes),
        clean_node(genetica),
        clean_node(ondulatoria)
    ]

    raiz_dia_3 = {
        "titulo": "13/11 (Sexta): Consolidadores (Geometria, Funções, Genética, Ondulatória)",
        "cor": "#D97706",
        "anotacao": None,
        "filhos": dia_3_filhos
    }

    # ─────────────────────────────────────────────────────────────────────────
    # DIA 4: 14/11 (Sábado): Véspera (Revisão visual e leitura de padrões)
    # ─────────────────────────────────────────────────────────────────────────
    def leaf_pauta(titulo):
        return {
            "titulo": titulo,
            "cor": None,
            "anotacao": {
                "tipo": "pauta",
                "linhas_manuais": 3
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

    dia_4_filhos = [
        branch(
            "Revisão Visual de Fórmulas e Relações Críticas",
            [
                branch("Fórmulas Fundamentais de Ciências da Natureza", [
                    leaf_pauta("Eletrodinâmica: Leis de Ohm (U = R*i, R = ρL/A) e Potência Elétrica (P = U*i = R*i² = U²/R)"),
                    leaf_pauta("Termologia e Ondulatória: Calor Sensível (Q = mcΔT), Latente (Q = mL) e Onda (v = λ*f)"),
                    leaf_pauta("Fís-Química e Imunologia: Diluição (C1*V1 = C2*V2), Concentração Molar e Vacina (Ativa) vs Soro (Passivo)"),
                ]),
                branch("Fórmulas Fundamentais de Matemática", [
                    leaf_pauta("Geometria Plana: Áreas de Triângulo, Círculo (π*r²), Trapézio e Teorema de Pitágoras"),
                    leaf_pauta("Geometria Espacial: Volume do Prisma/Cilindro (Ab*h), Cone/Pirâmide (Ab*h/3) e Esfera (4/3*π*r³)"),
                    leaf_pauta("Álgebra e Estatística: Vértice da Parábola (xv = -b/2a, yv = -Δ/4a) e Médias Ponderadas"),
                ]),
            ],
            cor="#DC2626"
        ),
        branch(
            "Leitura de Padrões Gráficos e Fenomenológicos",
            [
                branch("Decodificação Rápida de Gráficos e Curvas", [
                    leaf_pauta("Gráficos Cinemáticos (v x t): Área = Deslocamento Escalar e Inclinação = Aceleração"),
                    leaf_pauta("Curvas de Aquecimento: Reconhecimento de Substância Pura vs Misturas Eutética e Azeotrópica"),
                    leaf_pauta("Diagramas Estatísticos: Leitura Direta de Histogramas, Barras e Tabelas Sem Contas Excessivas"),
                ]),
                branch("Esquemas Visuais de Biologia e Meio Ambiente", [
                    leaf_pauta("Heredogramas: Identificação de Padrões Autossômicos Dominante/Recessivo e Ligados ao X"),
                    leaf_pauta("Pirâmides Ecológicas e Teias Tróficas: Fluxo Unidirecional de Energia e Bioacumulação Trófica"),
                    leaf_pauta("Ciclos do Nitrogênio e Carbono: Bactérias Fixadoras, Nitrificantes e Balanço de Carbono"),
                ]),
            ],
            cor="#D97706"
        ),
        branch(
            "Checklist Operacional e Estratégia de Prova TRI",
            [
                branch("Gestão de Tempo e Protocolo das 3 Passadas", [
                    leaf_pauta("Passada 1 (0 a 100 min): Varredura das 40-45 questões fáceis, conceituais e leitura direta"),
                    leaf_pauta("Passada 2 (100 a 230 min): Resolução concentrada das questões de cálculo intermediário e consolidadores"),
                    leaf_pauta("Passada 3 (230 a 275 min): Ataque aos itens restantes e desapego imediato de itens de Nível 3"),
                ]),
                branch("Segurança de Prova e Preenchimento de Cartão", [
                    leaf_pauta("Gabarito Blindado: 25 minutos finais (275 a 300 min) intocáveis para transposição calma"),
                    leaf_pauta("Prevenção de Erros de Marcação: Conferência de número de questão a cada bloco de 10 preenchimentos"),
                    leaf_pauta("Postura Cognitiva: Zero apego a questões travadas; 3 minutos sem evolução = pula imediatamente"),
                ]),
            ],
            cor="#DC2626"
        ),
    ]

    raiz_dia_4 = {
        "titulo": "14/11 (Sábado): Véspera (Revisão visual e leitura de padrões)",
        "cor": "#DC2626",
        "anotacao": None,
        "filhos": dia_4_filhos
    }

    cronograma_final = [
        raiz_dia_1,
        raiz_dia_2,
        raiz_dia_3,
        raiz_dia_4
    ]

    destino = os.path.join("FINAL", "CRONOGRAMA_RETA_FINAL.json")
    with open(destino, "w", encoding="utf-8") as f:
        json.dump(cronograma_final, f, ensure_ascii=False, indent=2)

    print(f"Cronograma gerado com sucesso em: {destino}")
    print(f"Tamanho do arquivo: {os.path.getsize(destino)} bytes")

if __name__ == "__main__":
    build_cronograma()
