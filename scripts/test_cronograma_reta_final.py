#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Validação exaustiva de FINAL/CRONOGRAMA_RETA_FINAL.json.
Verifica conformidade estrita com o MindNote Engine, schema de 4 chaves,
anotações de pauta com exatamente 3 linhas manuais e renderização real via Edge headless (--dump-dom).
"""

import os
import sys
import json
import subprocess

EXPECTED_ROOT_TITLES = [
    "11/11 (Quarta): Pilares (Matemática Básica, Estatística, Ecologia)",
    "12/11 (Quinta): Pilares (Eletrodinâmica, Termologia, Fís-Química)",
    "13/11 (Sexta): Consolidadores (Geometria, Funções, Genética, Ondulatória)",
    "14/11 (Sábado): Véspera (Revisão visual e leitura de padrões)"
]

VALID_CORES = {None, "#DC2626", "#D97706"}

def get_cronograma_path():
    candidates = [
        os.path.join("cases", "enem-dia-2", "FINAL", "CRONOGRAMA_RETA_FINAL.json"),
        os.path.join("FINAL", "CRONOGRAMA_RETA_FINAL.json"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return os.path.abspath(c)
    return os.path.abspath(candidates[0])

def test_json_structure():
    caminho = get_cronograma_path()
    assert os.path.exists(caminho), f"Arquivo {caminho} não existe!"

    with open(caminho, "r", encoding="utf-8") as f:
        dados = json.load(f)

    assert isinstance(dados, list), "O JSON raiz deve ser um array."
    assert len(dados) == 4, f"Esperado exatamente 4 nós raiz, obtido: {len(dados)}"

    for i, root in enumerate(dados):
        exp_title = EXPECTED_ROOT_TITLES[i]
        assert root.get("titulo") == exp_title, f"Raiz {i}: esperado título '{exp_title}', obtido '{root.get('titulo')}'"
        assert root.get("anotacao") is None, f"Raiz {i}: 'anotacao' deve ser null, obtido '{root.get('anotacao')}'"
        assert isinstance(root.get("filhos"), list) and len(root.get("filhos")) > 0, f"Raiz {i}: deve ter filhos."
        assert root.get("cor") in VALID_CORES, f"Raiz {i}: cor inválida '{root.get('cor')}'"

    total_nos = 0
    total_folhas = 0
    total_intermediarios = 0

    def validar_no(no, caminho_path, depth):
        nonlocal total_nos, total_folhas, total_intermediarios
        total_nos += 1

        assert isinstance(no, dict), f"Nó em {caminho_path} não é um objeto."
        
        # 4 campos obrigatórios e estritos
        chaves = set(no.keys())
        chaves_obrigatorias = {"titulo", "anotacao", "cor", "filhos"}
        assert chaves == chaves_obrigatorias, f"Chaves inválidas em {caminho_path}: {chaves} != {chaves_obrigatorias}"

        titulo = no["titulo"]
        assert isinstance(titulo, str) and titulo.strip(), f"Título vazio em {caminho_path}"
        assert "..." not in titulo and "placeholder" not in titulo.lower(), f"Placeholder detectado: '{titulo}'"

        # Verificar ausência de nós Nível 3 (como logaritmos)
        assert "logarítmico" not in titulo.lower(), f"Nó de nível 3 não filtrado: {titulo}"

        cor = no["cor"]
        assert cor in VALID_CORES, f"Cor inválida '{cor}' em {caminho_path}"

        filhos = no["filhos"]
        assert isinstance(filhos, list), f"Filhos não é lista em {caminho_path}"

        anotacao = no["anotacao"]
        if len(filhos) == 0:
            # Folha
            total_folhas += 1
            assert anotacao is not None, f"Folha em {caminho_path} deve ter anotação!"
            assert anotacao.get("tipo") == "pauta", f"Esperado 'pauta', obtido '{anotacao.get('tipo')}' em {caminho_path}"
            assert anotacao.get("linhas_manuais") == 3, f"Esperado exatamente 3 linhas manuais, obtido '{anotacao.get('linhas_manuais')}' em {caminho_path}"
        else:
            # Intermediário
            total_intermediarios += 1
            assert anotacao is None, f"Nó intermediário em {caminho_path} deve ter anotacao null, obtido '{anotacao}'"
            for idx, filho in enumerate(filhos):
                validar_no(filho, f"{caminho_path} > {filho.get('titulo', f'idx_{idx}')}", depth + 1)

    for i, root in enumerate(dados):
        validar_no(root, root["titulo"], 0)

    print("\n--- ESTATÍSTICAS DO CRONOGRAMA TÁTICO ---")
    print(f"Total de nós: {total_nos}")
    print(f"Total de nós intermediários/raízes: {total_intermediarios}")
    print(f"Total de folhas (linhas_manuais=3): {total_folhas}")
    print(f"Raízes diárias: {len(dados)}")
    print("✔ Validação estrutural do Python CONCLUÍDA COM 100% DE SUCESSO!")
    return total_nos, total_folhas

def test_mindnote_js_engine():
    target_path = get_cronograma_path().replace("\\", "/")
    js_test_code = """
    const fs = require('fs');

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
    console.log(`Node.js Engine: Sucesso ao processar ${processado.length} raízes diárias no MindNote Engine!`);
    """
    res = subprocess.run(["node", "-e", js_test_code], capture_output=True, text=True)
    assert res.returncode == 0, f"Erro no engine MindNote JS: {res.stderr}"
    print(res.stdout.strip())
    print("✔ Validação do motor JavaScript MindNote CONCLUÍDA COM 100% DE SUCESSO!")

def test_browser_render(exp_nos, exp_folhas):
    engine_dir = os.path.abspath(r'C:\Users\Eduardo\Documents\05_Desenvolvimento-e-Hardware\MindNote-Engine')
    json_path = get_cronograma_path()

    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = f.read()

    html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Test Render Cronograma</title>
</head>
<body>
  <div id="painel-lateral">
    <textarea id="entrada-json"></textarea>
    <input type="number" id="entrada-escala" value="26">
    <button id="botao-processar" type="button">Processar</button>
    <button id="botao-tema" type="button">Tema</button>
    <button id="botao-nova-raiz" type="button">+ Nova Raiz</button>
    <pre id="area-erro" class="erro"></pre>
  </div>
  <main id="canvas-container"></main>

  <script src="file:///{engine_dir.replace(chr(92), '/')}/js/engine.text.js"></script>
  <script src="file:///{engine_dir.replace(chr(92), '/')}/js/engine.geometry.js"></script>
  <script src="file:///{engine_dir.replace(chr(92), '/')}/js/render.svg.js"></script>
  <script src="file:///{engine_dir.replace(chr(92), '/')}/js/render.pdf.js"></script>
  <script src="file:///{engine_dir.replace(chr(92), '/')}/js/app.js"></script>

  <script>
    window.addEventListener('DOMContentLoaded', () => {{
      const report = {{}};
      try {{
        const raw = {json.dumps(json_data)};
        const txtArea = document.getElementById('entrada-json');
        txtArea.value = raw;
        document.getElementById('botao-processar').click();

        report.initialError = document.getElementById('area-erro').textContent;
        report.nodeCount = document.querySelectorAll('.mindnote-node').length;
        report.boxCount = document.querySelectorAll('.mindnote-box').length;
        report.pathCount = document.querySelectorAll('path').length;
        report.lineCount = document.querySelectorAll('line').length;

        // Testar alternância de escala
        const escalaInput = document.getElementById('entrada-escala');
        escalaInput.value = '30';
        escalaInput.dispatchEvent(new Event('change'));
        report.scaleError = document.getElementById('area-erro').textContent;

        // Testar alternância de tema
        const btnTema = document.getElementById('botao-tema');
        btnTema.click();
        report.themeError = document.getElementById('area-erro').textContent;
        report.isDark = document.body.classList.contains('tema-escuro');

        // Testar serialização
        try {{
          const reparsed = JSON.parse(txtArea.value);
          report.serializedValid = Array.isArray(reparsed) && reparsed.length === 4;
        }} catch(e) {{
          report.serializationError = e.toString();
        }}

        const resultDiv = document.createElement('div');
        resultDiv.id = 'test-results';
        resultDiv.textContent = JSON.stringify(report);
        document.body.appendChild(resultDiv);
      }} catch (e) {{
        const errDiv = document.createElement('div');
        errDiv.id = 'test-results';
        errDiv.textContent = JSON.stringify({{ fatalError: e.toString() }});
        document.body.appendChild(errDiv);
      }}
    }});
  </script>
</body>
</html>"""

    test_html_path = os.path.abspath('test_render_runner_cronograma.html')
    with open(test_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    file_url = f'file:///{test_html_path.replace(chr(92), "/")}'
    cmd = [edge_exe, '--headless', '--disable-gpu', '--dump-dom', file_url]

    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8', timeout=15)
        output = res.stdout

        if 'id="test-results"' in output:
            idx = output.find('id="test-results"')
            tag_start = output.find('>', idx) + 1
            tag_end = output.find('</div>', tag_start)
            content = output[tag_start:tag_end]
            data = json.loads(content)
            print("Browser DOM Verification Report:", json.dumps(data, indent=2))

            assert data.get('initialError') == '', f"Erro inicial no motor: {data.get('initialError')}"
            assert data.get('nodeCount') == exp_nos, f"Esperado {exp_nos} nós, obtido: {data.get('nodeCount')}"
            assert data.get('boxCount') == exp_folhas, f"Esperado {exp_folhas} caixas, obtido: {data.get('boxCount')}"
            assert data.get('scaleError') == '', f"Erro ao trocar escala: {data.get('scaleError')}"
            assert data.get('themeError') == '', f"Erro ao trocar tema: {data.get('themeError')}"
            assert data.get('isDark') is True, "Tema escuro não ativado corretamente."
            assert data.get('serializedValid') is True, "Serialização de estado para textarea falhou."
            print(f"✔ Renderização gráfica no navegador aprovada! Total de nós renderizados: {data.get('nodeCount')}, caixas de anotação: {data.get('boxCount')}")
        else:
            print("Erro: div de resultados não encontrada no DOM.")
            print(output[:1000])
            raise AssertionError("Falha na execução do navegador headless.")
    finally:
        if os.path.exists(test_html_path):
            os.remove(test_html_path)

if __name__ == "__main__":
    nos, folhas = test_json_structure()
    test_mindnote_js_engine()
    test_browser_render(nos, folhas)
    print("\n=======================================================")
    print("TODOS OS TESTES (ESTRUTURA, JS ENGINE E BROWSER) FORAM APROVADOS COM 100% DE SUCESSO!")
    print("=======================================================")
