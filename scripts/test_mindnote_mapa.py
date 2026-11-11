#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validação exaustiva do arquivo FINAL/MAPA_MENTAL_ESTUDO_ENEM.json.
Garante 100% de conformidade com o Manual do MindNote Engine e com os requisitos do ENEM Dia 2.
"""

import os
import sys
import json
import subprocess

EXPECTED_CORES_RAMO = {None, "#2563EB", "#059669", "#D97706", "#7C3AED", "#DC2626"}

EXPECTED_ROOTS = [
    {"titulo": "Parte 1: Matemática e suas Tecnologias", "cor": "#2563EB"},
    {"titulo": "Parte 2: Física", "cor": "#DC2626"},
    {"titulo": "Parte 3: Biologia", "cor": "#059669"},
    {"titulo": "Parte 4: Química", "cor": "#7C3AED"},
]

TOP_15_EXPECTED = {
    # 1º a 3º Matemática
    "Matemática Básica, Aritmética e Proporcionalidade": {"status": "CRUCIAL", "cor": "#DC2626", "materia": "Parte 1: Matemática e suas Tecnologias"},
    "Estatística Básica e Descritiva": {"status": "CRUCIAL", "cor": "#DC2626", "materia": "Parte 1: Matemática e suas Tecnologias"},
    "Geometria Plana": {"status": "ALTO", "cor": "#D97706", "materia": "Parte 1: Matemática e suas Tecnologias"},
    # 4º Física
    "Mecânica Clássica (Cinemática, Dinâmica e Energia)": {"status": "ALTO", "cor": "#D97706", "materia": "Parte 2: Física"},
    # 5º Matemática
    "Funções, Álgebra e Equações": {"status": "ALTO", "cor": "#D97706", "materia": "Parte 1: Matemática e suas Tecnologias"},
    # 6º Física
    "Eletrodinâmica e Circuitos Elétricos": {"status": "CRUCIAL", "cor": "#DC2626", "materia": "Parte 2: Física"},
    # 7º Matemática
    "Geometria Espacial": {"status": "ALTO", "cor": "#D97706", "materia": "Parte 1: Matemática e suas Tecnologias"},
    # 8º Química
    "Físico-Química: Soluções e Concentrações": {"status": "ALTO", "cor": "#D97706", "materia": "Parte 4: Química"},
    # 9º Biologia
    "Genética e Biologia Molecular": {"status": "ALTO", "cor": "#D97706", "materia": "Parte 3: Biologia"},
    # 10º Física
    "Termologia, Calorimetria e Termodinâmica": {"status": "CRUCIAL", "cor": "#DC2626", "materia": "Parte 2: Física"},
    # 11º Biologia
    "Biotecnologia e Engenharia Genética": {"status": "ALTO", "cor": "#D97706", "materia": "Parte 3: Biologia"},
    # 12º Química
    "Química Geral: Cálculos Estequiométricos": {"status": "ALTO", "cor": "#D97706", "materia": "Parte 4: Química"},
    # 13º Natureza / Interdisciplinar
    "Ciências da Natureza Integradas": {"status": "ALTO", "cor": "#D97706", "materia": "Parte 4: Química"},
    # 14º Física
    "Ondulatória e Acústica": {"status": "CRUCIAL", "cor": "#DC2626", "materia": "Parte 2: Física"},
    # 15º Biologia
    "Fisiologia Humana e Imunologia": {"status": "CRUCIAL", "cor": "#DC2626", "materia": "Parte 3: Biologia"},
}

def get_mapa_path():
    candidates = [
        os.path.join("cases", "enem-dia-2", "FINAL", "MAPA_MENTAL_ESTUDO_ENEM.json"),
        os.path.join("FINAL", "MAPA_MENTAL_ESTUDO_ENEM.json"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return os.path.abspath(c)
    return os.path.abspath(candidates[0])

def test_json_structure():
    caminho = get_mapa_path()
    assert os.path.exists(caminho), f"Arquivo {caminho} não existe!"

    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    assert isinstance(dados, list), "O JSON raiz deve ser um array."
    assert len(dados) == 4, f"Esperado exatamente 4 nós raiz, obtido: {len(dados)}"

    # Checagem dos nós raiz
    for i, root in enumerate(dados):
        exp = EXPECTED_ROOTS[i]
        assert root.get("titulo") == exp["titulo"], f"Raiz {i}: esperado título '{exp['titulo']}', obtido '{root.get('titulo')}'"
        assert root.get("cor") == exp["cor"], f"Raiz {i}: esperada cor '{exp['cor']}', obtido '{root.get('cor')}'"
        assert root.get("anotacao") is None, f"Raiz {i}: 'anotacao' deve ser null, obtido '{root.get('anotacao')}'"
        assert isinstance(root.get("filhos"), list) and len(root.get("filhos")) > 0, f"Raiz {i}: deve ter filhos."

    # Validação recursiva de todos os nós
    total_nos = 0
    total_folhas = 0
    total_pautas = 0
    total_ilustracoes = 0
    top15_encontrados = {}

    def validar_no(no, caminho_path, depth):
        nonlocal total_nos, total_folhas, total_pautas, total_ilustracoes
        total_nos += 1

        assert isinstance(no, dict), f"Nó em {caminho_path} não é um objeto."
        
        # 4 campos obrigatórios
        chaves = set(no.keys())
        chaves_obrigatorias = {"titulo", "anotacao", "cor", "filhos"}
        assert chaves == chaves_obrigatorias, f"Chaves inválidas em {caminho_path}: {chaves} != {chaves_obrigatorias}"

        titulo = no["titulo"]
        assert isinstance(titulo, str) and titulo.strip(), f"Título vazio em {caminho_path}"
        assert "..." not in titulo and "placeholder" not in titulo.lower(), f"Placeholder detectado no título: '{titulo}'"

        cor = no["cor"]
        assert cor in EXPECTED_CORES_RAMO, f"Cor inválida '{cor}' em {caminho_path}"

        filhos = no["filhos"]
        assert isinstance(filhos, list), f"'filhos' deve ser lista em {caminho_path}"

        anotacao = no["anotacao"]

        if len(filhos) > 0:
            # Nó intermediário ou raiz
            assert anotacao is None, f"Nó intermediário em {caminho_path} com título '{titulo}' deve ter anotacao null! Obtido: {anotacao}"
            for j, filho in enumerate(filhos):
                validar_no(filho, f"{caminho_path} -> {filho.get('titulo', f'filho[{j}]')}", depth + 1)
        else:
            # Nó folha
            total_folhas += 1
            assert anotacao is not None, f"Nó folha em {caminho_path} com título '{titulo}' não pode ter anotacao null!"
            assert isinstance(anotacao, dict), f"Anotação em {caminho_path} deve ser dict."
            tipo = anotacao.get("tipo")
            assert tipo in {"pauta", "ilustracao"}, f"Tipo de anotação inválido '{tipo}' em {caminho_path}"

            if tipo == "pauta":
                total_pautas += 1
                linhas = anotacao.get("linhas_manuais")
                assert isinstance(linhas, int) and linhas >= 3, f"Linhas manuais inválidas ({linhas}) em folha {caminho_path}"
            elif tipo == "ilustracao":
                total_ilustracoes += 1
                if "altura_customizada" in anotacao:
                    alt = anotacao["altura_customizada"]
                    assert isinstance(alt, (int, float)) and alt > 0, f"Altura customizada inválida ({alt}) em folha {caminho_path}"

    for i, root in enumerate(dados):
        validar_no(root, root["titulo"], 0)
        # Mapear filhos de 1º nível (Tópicos do TOP 15)
        for t in root["filhos"]:
            top15_encontrados[t["titulo"]] = {
                "materia": root["titulo"],
                "cor": t["cor"]
            }

    print("--- ESTATÍSTICAS DA ÁRVORE ---")
    print(f"Total de nós: {total_nos}")
    print(f"Total de folhas: {total_folhas}")
    print(f"Total de anotações pauta: {total_pautas}")
    print(f"Total de anotações ilustração: {total_ilustracoes}")
    print(f"Total de tópicos TOP 15 mapeados: {len(top15_encontrados)}")

    # Validar que todos os 15 tópicos estão presentes com cores e matérias exatas
    for t_nome, exp_data in TOP_15_EXPECTED.items():
        assert t_nome in top15_encontrados, f"Tópico obrigatório '{t_nome}' ausente no JSON!"
        encontrado = top15_encontrados[t_nome]
        assert encontrado["cor"] == exp_data["cor"], f"Cor incorreta para '{t_nome}': esperado '{exp_data['cor']}', obtido '{encontrado['cor']}'"
        assert encontrado["materia"] == exp_data["materia"], f"Matéria incorreta para '{t_nome}': esperado '{exp_data['materia']}', obtido '{encontrado['materia']}'"

    print("✔ Validação estrutural do Python CONCLUÍDA COM 100% DE SUCESSO!")

def test_mindnote_js_engine():
    # Executa teste com Node.js simulando o app.js original
    target_path = get_mapa_path().replace("\\", "/")
    js_test_code = """
    const fs = require('fs');
    const path = require('path');

    const raw = fs.readFileSync('__TARGET_PATH__', 'utf8');
    const dados = JSON.parse(raw);""".replace('__TARGET_PATH__', target_path) + """

    const CORES_RAMO = [null, "#2563EB", "#059669", "#D97706", "#7C3AED", "#DC2626"];

    function normalizarAnexo(anexo) {
      if (!anexo) return null;
      const alturaValida =
        typeof anexo.altura === "number" &&
        Number.isFinite(anexo.altura) &&
        anexo.altura > 0;
      return { tipo: "ilustracao", altura: alturaValida ? anexo.altura : 220 };
    }

    function normalizarAnotacao(anotacao) {
      if (!anotacao) return null;
      const tipo = anotacao.tipo === "ilustracao" ? "ilustracao" : "pauta";
      const anexo = normalizarAnexo(anotacao.anexo);

      if (tipo === "ilustracao") {
        const alturaValida =
          typeof anotacao.altura_customizada === "number" &&
          Number.isFinite(anotacao.altura_customizada) &&
          anotacao.altura_customizada > 0;
        return {
          tipo: "ilustracao",
          alturaCustomizada: alturaValida ? anotacao.altura_customizada : 220,
          linhasManuais: null,
          palavrasEstimadas: null,
          anexo,
        };
      }

      const linhasValidas =
        typeof anotacao.linhas_manuais === "number" &&
        Number.isFinite(anotacao.linhas_manuais) &&
        anotacao.linhas_manuais > 0;
      const palavrasValidas =
        typeof anotacao.palavras_estimadas === "number" &&
        Number.isFinite(anotacao.palavras_estimadas) &&
        anotacao.palavras_estimadas >= 8;
      return {
        tipo: "pauta",
        alturaCustomizada: null,
        linhasManuais: linhasValidas ? Math.max(3, Math.floor(anotacao.linhas_manuais)) : null,
        palavrasEstimadas: linhasValidas ? null : palavrasValidas ? anotacao.palavras_estimadas : 8,
        anexo,
      };
    }

    function validarNo(no, profundidade = 0) {
      if (!no || typeof no.titulo !== "string" || no.titulo.trim() === "") {
        throw new Error(
          `Nó inválido na profundidade ${profundidade}: campo "titulo" ausente ou vazio.`
        );
      }
      const cor =
        typeof no.cor === "string" && CORES_RAMO.includes(no.cor)
          ? no.cor
          : no.cor === null || no.cor === undefined
          ? null
          : null;
      return {
        titulo: no.titulo.trim(),
        anotacao: normalizarAnotacao(no.anotacao),
        cor,
        filhos: Array.isArray(no.filhos)
          ? no.filhos.map((filho) => validarNo(filho, profundidade + 1))
          : [],
      };
    }

    const processado = dados.map(raiz => validarNo(raiz, 0));
    console.log(`Node.js Engine: Sucesso ao processar ${processado.length} raízes no MindNote Engine!`);
    """
    res = subprocess.run(["node", "-e", js_test_code], capture_output=True, text=True)
    assert res.returncode == 0, f"Erro no engine MindNote JS: {res.stderr}"
    print(res.stdout.strip())
    print("✔ Validação do motor JavaScript MindNote CONCLUÍDA COM 100% DE SUCESSO!")

def test_browser_headless_rendering():
    try:
        from test_browser_render import run_browser_render_test
    except ImportError:
        from scripts.test_browser_render import run_browser_render_test
    print("\n--- INICIANDO TESTE DE RENDERIZAÇÃO REAL NO NAVEGADOR (MS EDGE HEADLESS) ---")
    run_browser_render_test()

if __name__ == "__main__":
    test_json_structure()
    test_mindnote_js_engine()
    test_browser_headless_rendering()
    print("\n=======================================================")
    print("TODOS OS TESTES (PYTHON, NODE.JS E BROWSER) FORAM APROVADOS!")
    print("=======================================================")
