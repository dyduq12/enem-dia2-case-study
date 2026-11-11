import os
import json
import subprocess

def get_mapa_path():
    candidates = [
        os.path.join("cases", "enem-dia-2", "FINAL", "MAPA_MENTAL_ESTUDO_ENEM.json"),
        os.path.join("FINAL", "MAPA_MENTAL_ESTUDO_ENEM.json"),
    ]
    for c in candidates:
        if os.path.exists(c):
            return os.path.abspath(c)
    return os.path.abspath(candidates[0])

def run_browser_render_test(custom_json_path=None):
    engine_dir = os.path.abspath(r'C:\Users\Eduardo\Documents\05_Desenvolvimento-e-Hardware\MindNote-Engine')
    json_path = os.path.abspath(custom_json_path) if custom_json_path else get_mapa_path()

    with open(json_path, 'r', encoding='utf-8') as f:
        json_data = f.read()

    html_content = f"""<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Test Render</title>
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

        // Testar mudança de entrelinha (escala)
        const escalaInput = document.getElementById('entrada-escala');
        escalaInput.value = '32';
        escalaInput.dispatchEvent(new Event('change'));
        report.scaleError = document.getElementById('area-erro').textContent;

        // Testar alternância de tema
        const btnTema = document.getElementById('botao-tema');
        btnTema.click();
        report.themeError = document.getElementById('area-erro').textContent;
        report.isDark = document.body.classList.contains('tema-escuro');

        // Testar serialização de volta para o textarea
        report.serializedValid = false;
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

    test_html_path = os.path.abspath('test_render_runner.html')
    with open(test_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)

    edge_exe = r'C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
    file_url = f'file:///{test_html_path.replace(chr(92), "/")}'
    cmd = [edge_exe, '--headless', '--disable-gpu', '--dump-dom', file_url]

    try:
        res = subprocess.run(cmd, capture_output=True, text=True, encoding='utf-8')
        output = res.stdout

        if 'id="test-results"' in output:
            idx = output.find('id="test-results"')
            tag_start = output.find('>', idx) + 1
            tag_end = output.find('</div>', tag_start)
            content = output[tag_start:tag_end]
            print('Extracted content:', repr(content))
            data = json.loads(content)
            print('Browser DOM Verification Report:', json.dumps(data, indent=2))

            assert data.get('initialError') == '', f"Erro inicial no motor: {data.get('initialError')}"
            assert data.get('nodeCount') == 202, f"Esperado 202 nós, obtido: {data.get('nodeCount')}"
            assert data.get('boxCount') == 136, f"Esperado 136 caixas, obtido: {data.get('boxCount')}"
            assert data.get('scaleError') == '', f"Erro ao trocar escala: {data.get('scaleError')}"
            assert data.get('themeError') == '', f"Erro ao trocar tema: {data.get('themeError')}"
            assert data.get('isDark') is True, "Tema escuro não ativado corretamente."
            assert data.get('serializedValid') is True, "Serialização de estado para textarea falhou."
            print("✔ Todos os ciclos do MindNote Engine no navegador real (MS Edge Headless) foram homologados com 100% de sucesso!")
        else:
            print("Erro: div de resultados não encontrada no DOM.")
            print(output[:1000])
            raise AssertionError("Falha na execução do navegador headless.")
    finally:
        if os.path.exists(test_html_path):
            os.remove(test_html_path)

if __name__ == '__main__':
    run_browser_render_test()
