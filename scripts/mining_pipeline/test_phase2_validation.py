import os
import json
import re
from collections import Counter

def test_phase2():
    print("=== TESTE DE VALIDAÇÃO COMPLETA DA FASE 2 ===")
    
    # 1. CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md
    cat_path = 'FINAL/CATALOGO_GERAL_ACERVO_ENEM_DIA_2.md'
    assert os.path.exists(cat_path), f"Arquivo não encontrado: {cat_path}"
    cat_content = open(cat_path, encoding='utf-8').read()
    assert len(cat_content) > 5000, "Catálogo geral muito curto"
    assert "1.422" in cat_content, "Total de 1.422 arquivos ausente"
    assert "719" in cat_content, "Total de 719 arquivos Dia 2 ausente"
    assert "5,56 GB" in cat_content, "Tamanho de 5,56 GB ausente"
    
    # Check paths in catalog
    cat_paths = []
    for line in cat_content.splitlines():
        line = line.strip()
        if line.startswith('|') and not line.startswith('| :') and not 'Caminho Relativo' in line and not 'Métrica Global' in line and not 'Plataforma / Provedor' in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 7:
                raw_path = parts[-2].strip('`')
                cat_paths.append(raw_path)
    assert len(cat_paths) >= 30, f"Poucos caminhos no catálogo: {len(cat_paths)}"
    missing_cat = [p for p in cat_paths if not os.path.exists(p)]
    assert len(missing_cat) == 0, f"Caminhos inexistentes no catálogo: {missing_cat}"
    print(f"[PASS] 1. Catálogo Geral validado: {len(cat_paths)} caminhos físicos verificados com 100% de existência.")

    # 2. INDICE_TEMATICO_SIMULADOS_DIA_2.md
    ind_path = 'FINAL/INDICE_TEMATICO_SIMULADOS_DIA_2.md'
    assert os.path.exists(ind_path), f"Arquivo não encontrado: {ind_path}"
    ind_content = open(ind_path, encoding='utf-8').read()
    assert len(ind_content) > 10000, "Índice temático muito curto"
    
    # Check all 18 topics present
    expected_codes = ['M1', 'M2', 'M3', 'M4', 'M5', 'M6', 'B1', 'B2', 'B3', 'B4', 'F1', 'F2', 'F3', 'F4', 'Q1', 'Q2', 'Q3', 'Q4']
    for code in expected_codes:
        assert f"Tópico {code}:" in ind_content, f"Tópico {code} ausente do índice temático"
    print(f"[PASS] 2. Todos os 18 tópicos de alta prioridade da TRI (M1-M6, B1-B4, F1-F4, Q1-Q4) estão presentes.")

    # Check providers in curated index tables
    providers = re.findall(r'\|\s*(Poliedro|Bernoulli|SAS|INEP|Apeiron)\s*\|', ind_content)
    prov_counts = Counter(providers)
    for p in ['Poliedro', 'Bernoulli', 'SAS', 'INEP', 'Apeiron']:
        assert prov_counts[p] >= 20, f"Banca {p} sub-representada no índice: {prov_counts[p]}"
    print(f"[PASS] 3. Diversidade Multi-Banca confirmada no Índice: {dict(prov_counts)}")

    # Check paths in thematic index
    ind_paths = []
    for line in ind_content.splitlines():
        line = line.strip()
        if line.startswith('|') and not line.startswith('| :') and not 'Arquivo de Resolução' in line and not '---' in line:
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 7:
                raw_path = parts[-2].strip('`')
                ind_paths.append(raw_path)
    assert len(ind_paths) >= 200, f"Poucas questões no índice: {len(ind_paths)}"
    missing_ind = [p for p in set(ind_paths) if not os.path.exists(p)]
    assert len(missing_ind) == 0, f"Caminhos inexistentes no índice temático: {missing_ind}"
    print(f"[PASS] 4. Todos os {len(set(ind_paths))} caminhos únicos do Índice Temático existem fisicamente no disco.")

    # 3. TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md
    tri_path = 'FINAL/TRILHA_ESTUDOS_CRONOGRAMA_DIA_2.md'
    assert os.path.exists(tri_path), f"Arquivo não encontrado: {tri_path}"
    tri_content = open(tri_path, encoding='utf-8').read()
    assert "FASE 1: BLINDAGEM DA BASE TRI" in tri_content
    assert "FASE 2: ALAVANCAGEM E CONSOLIDAÇÃO" in tri_content
    assert "FASE 3: REFINAMENTO DE ELITE E DIFERENCIAÇÃO" in tri_content
    assert "PROTOCOLO OPERACIONAL DO CADERNO DE ERROS" in tri_content
    
    tri_paths = re.findall(r'`([^`]+\.pdf|[^`]+\.xlsx)`', tri_content)
    missing_tri = [p for p in set(tri_paths) if not os.path.exists(p)]
    assert len(missing_tri) == 0, f"Caminhos inexistentes na trilha de estudos: {missing_tri}"
    print(f"[PASS] 5. Trilha de Estudos validada com {len(set(tri_paths))} caminhos físicos 100% verificados.")

    # 4. catalogo_enem_dia_2.json
    json_path = 'FINAL/catalogo_enem_dia_2.json'
    assert os.path.exists(json_path), f"JSON não encontrado: {json_path}"
    with open(json_path, 'r', encoding='utf-8') as f:
        db = json.load(f)
    assert db['metadata']['total_files'] == 1422
    assert db['metadata']['dia2_files_count'] == 719
    assert db['metadata']['total_indexed_questions'] > 5000
    for code in expected_codes:
        assert db['topic_questions_count'][code] > 0, f"Contagem zero para tópico {code}"
    print(f"[PASS] 6. Base de dados JSON validada: {db['metadata']['total_indexed_questions']} questões indexadas.")

    # 5. Regressão de Classificações Críticas
    import build_phase2_complete_system as b
    
    # Poliedro 1 Q160 (Geometria analítica)
    code_160 = b.classify_poliedro_item('Geometria analítica', 'Coordenadas no plano', 'Interpretar o deslocamento de uma esfera sobre o plano cartesiano...', 'MAT')
    assert code_160 == 'M4', f"Q160 esperava M4, obteve {code_160}"

    # Poliedro 2 Q173 (Funções Afins)
    code_173 = b.classify_poliedro_item('Funções', 'Afins', 'Identificar o gráfico de volume (L) por tempo...', 'MAT')
    assert code_173 == 'M5', f"Q173 esperava M5, obteve {code_173}"

    # Poliedro 1 Q171 (Probabilidade)
    code_171 = b.classify_poliedro_item('Probabilidade', 'Probabilidade da intersecção de eventos', 'Calcular o número mínimo de picolés...', 'MAT')
    assert code_171 == 'M6', f"Q171 esperava M6, obteve {code_171}"

    # Poliedro 5 Q131 (Biotecnologia)
    code_131 = b.classify_poliedro_item('Biotecnologia', 'Silenciamento da expressão gênica', 'Silenciamento gênico...', 'BIO')
    assert code_131 == 'B2', f"Q131 esperava B2, obteve {code_131}"

    # Poliedro 1 Q119 (Dinâmica Potência)
    code_119 = b.classify_poliedro_item('Dinâmica', 'Potência', 'Calcular a potência mecânica...', 'FIS')
    assert code_119 == 'F2', f"Q119 esperava F2, obteve {code_119}"

    # Poliedro 1 Q107 (Ligações químicas)
    code_107 = b.classify_poliedro_item('Ligações químicas', 'Forças intermoleculares', 'Interações moleculares...', 'QUI')
    assert code_107 == 'Q2', f"Q107 esperava Q2, obteve {code_107}"

    # SAS Q91 (Desmatamento)
    c_s91, _ = b.classify_semantic_text(91, "O aproveitamento da culinária indígena... demarcação de terras indígenas diminui o desmatamento...")
    assert c_s91 == 'B1', f"SAS Q91 esperava B1, obteve {c_s91}"

    # SAS Q93 (Verde de bromocresol pH)
    c_s93, _ = b.classify_semantic_text(93, "O verde de bromocresol é o indicador mais adequado, intervalo de viragem...")
    assert c_s93 == 'Q1', f"SAS Q93 esperava Q1, obteve {c_s93}"

    # Bernoulli Som Mach
    c_mach, _ = b.classify_semantic_text(92, "Considere a velocidade do som como igual a 340 m/s... aeronave a 918 km/h... número de Mach")
    assert c_mach == 'F3', f"Bernoulli Q92 esperava F3, obteve {c_mach}"

    # Q4 Química Ambiental contagem
    assert db['topic_questions_count']['Q4'] >= 20, f"Q4 deveria ter pelo menos 20 questões, tem {db['topic_questions_count']['Q4']}"
    print("[PASS] 7. Todos os testes de regressão de classificação semântica foram APROVADOS.")

    print("\n=======================================================")
    print("TODOS OS 7 BLOCOS DE TESTES FORAM APROVADOS COM SUCESSO!")
    print("=======================================================")

if __name__ == '__main__':
    test_phase2()
