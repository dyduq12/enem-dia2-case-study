# -*- coding: utf-8 -*-
"""
Suite de Testes de Verificação e Integridade do Relatório Consolidado ENEM Dia 2.

Validações realizadas:
1. Tabela 4.1 (TOP 15 Geral):
   - Extração automática das 15 linhas do ranking TOP 15.
   - Soma das questões individuais igual a 19.236.
   - Percentual individual calculado e soma percentual igual a 78,77% (19.236 / 24.419).
   - Linha de rodapé/totais da Tabela 4.1 contendo '19.236' e '78,77%'.
   - Texto de abertura da Seção 4.2 contendo '78,77% de toda a avaliação do 2º Dia' e '(19.236 de 24.419 itens)'.
2. Somas Globais de Todas as Tabelas:
   - Tabela 1.2 (Subagentes): soma = 24.419 itens.
   - Tabela 2.0 (Síntese por Disciplina): soma = 24.419 itens (Matemática: 11.685 + Ciências da Natureza: 12.734).
   - Tabela 2.1 (Matriz de Contingência Subagente x Disciplina): soma das células = 24.419 itens.
   - Tabela 3.1 (Matemática): soma dos 10 tópicos = 11.685 itens.
   - Tabela 3.2 (Física): soma dos 8 tópicos = 4.580 itens.
   - Tabela 3.3 (Química): soma dos 10 tópicos = 3.393 itens.
   - Tabela 3.4 (Biologia): soma dos 8 tópicos = 4.076 itens.
   - Ciências da Natureza Integrada = 685 itens (11.685 + 4.580 + 3.393 + 4.076 + 685 = 24.419).
3. Higiene de Caracteres e Escapes LaTeX:
   - Ausência absoluta de bytes 0x09 (tab) no arquivo Markdown.
   - Ausência de retornos de carro espúrios (0x0D sem 0x0A).
   - Fórmulas LaTeX íntegras: '\\times', '\\rho', '\\text', '$s \\times t$', '$v \\times t$', '$R = \\rho L/A$'.
"""

import os
import re
import sys
import unittest

REPORT_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "FINAL", "RELATORIO_CONSOLIDADO_ENEM_DIA_2.md")
GEN_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "FINAL", "generate_report.py")

class TestConsolidatedReportFixes(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        if not os.path.exists(REPORT_PATH):
            raise FileNotFoundError(f"Arquivo não encontrado: {REPORT_PATH}")
        with open(REPORT_PATH, "r", encoding="utf-8") as f:
            cls.report_text = f.read()
        with open(REPORT_PATH, "rb") as f:
            cls.report_bytes = f.read()

    def test_01_top15_sum_and_percentages(self):
        """Valida que a soma dos 15 itens da Tabela 4.1 totaliza 19.236 e 78,77%."""
        # Localiza a Tabela 4.1
        match = re.search(r"### 4\.1 Tabela Consolidada do TOP 15 Geral do ENEM Dia 2\s*\n\s*\|.*?\n\|.*?\n(.*?)\n\| — \|", self.report_text, re.DOTALL)
        self.assertIsNotNone(match, "Tabela 4.1 não localizada no relatório.")
        table_body = match.group(1).strip()
        
        rows = [r.strip() for r in table_body.split("\n") if r.strip().startswith("|")]
        self.assertEqual(len(rows), 15, f"Esperadas 15 linhas de itens no ranking TOP 15, encontradas {len(rows)}.")
        
        counts = []
        for row in rows:
            cols = [c.strip() for c in row.split("|")[1:-1]]
            # A coluna de questões é a 4ª coluna (índice 3)
            # Ex: | **1º** | **Matemática** | **Matemática Básica...** | **5.716** | **23,41%** | ...
            q_str = cols[3].replace("**", "").replace(".", "").strip()
            counts.append(int(q_str))
        
        total_top15 = sum(counts)
        self.assertEqual(total_top15, 19236, f"Soma do TOP 15 ({total_top15}) deve ser exatamente 19.236.")
        
        pct_top15 = (total_top15 / 24419) * 100
        self.assertAlmostEqual(pct_top15, 78.7747, places=3)
        self.assertEqual(f"{pct_top15:.2f}".replace(".", ","), "78,77")

    def test_02_table_4_1_footer_and_section_4_2_text(self):
        """Valida a linha de totais da Tabela 4.1 e o texto de abertura da Seção 4.2."""
        footer_pattern = r"\|\s*—\s*\|\s*\*\*TOTAIS DO TOP 15\*\*\s*\|\s*\*\*15 Tópicos Mais Recorrentes do Dia 2\*\*\s*\|\s*\*\*19\.236\*\*\s*\|\s*\*\*78,77%\*\*\s*\|\s*—\s*\|\s*\*\*Concentram cerca de 79% do Exame\*\*\s*\|"
        self.assertIsNotNone(re.search(footer_pattern, self.report_text), "Rodapé da Tabela 4.1 divergente do esperado (19.236 / 78,77%).")
        
        sec_pattern = r"Os dados empíricos demonstram que os 15 tópicos líderes representam \*\*78,77% de toda a avaliação do 2º Dia\*\* \(19\.236 de 24\.419 itens\)\."
        self.assertIsNotNone(re.search(sec_pattern, self.report_text), "Texto de abertura da Seção 4.2 divergente do esperado (78,77% e 19.236 de 24.419).")

    def test_03_no_spurious_control_characters(self):
        """Valida ausência absoluta de byte 0x09 (tab) e \r espúrio no Markdown."""
        self.assertEqual(self.report_bytes.count(b"\x09"), 0, "Arquivo contém caracteres de tabulação 0x09 espúrios.")
        
        # Standalone carriage return (CR not followed by LF)
        crlf_count = self.report_bytes.count(b"\r\n")
        total_cr = self.report_bytes.count(b"\r")
        self.assertEqual(total_cr - crlf_count, 0, "Arquivo contém retornos de carro (CR) isolados.")

    def test_04_latex_math_integrity(self):
        """Valida que expressões matemáticas LaTeX foram preservadas perfeitamente."""
        self.assertIn(r"$s \times t$", self.report_text, "Expressão '$s \\times t$' ausente ou corrompida.")
        self.assertIn(r"$v \times t$", self.report_text, "Expressão '$v \\times t$' ausente ou corrompida.")
        self.assertIn(r"$R = \rho L/A$", self.report_text, "Expressão '$R = \\rho L/A$' ausente ou corrompida.")
        self.assertIn(r"22,4\text{ L/mol}", self.report_text, "Expressão '22,4\\text{ L/mol}' ausente ou corrompida.")

    def test_05_global_sums_table_1_2(self):
        """Valida fechamento da Tabela 1.2 (Subagentes) em 24.419 itens."""
        # Extrair linhas da Tabela 1.2
        match = re.search(r"### 1\.2 Volume Amostral.*?\n(\|.*?\n\|.*?\n)(.*?)\n\| \*\*TOTAIS CONSOLIDADOS\*\*", self.report_text, re.DOTALL)
        self.assertIsNotNone(match, "Tabela 1.2 não encontrada.")
        rows = [r.strip() for r in match.group(2).strip().split("\n") if r.strip().startswith("|")]
        self.assertEqual(len(rows), 6, "Esperadas 6 linhas para os subagentes Alpha a Zeta.")
        
        agent_counts = []
        for row in rows:
            cols = [c.strip() for c in row.split("|")[1:-1]]
            # Coluna de questões reais mineradas é a 6ª (índice 5)
            q_val = int(cols[5].replace("**", "").replace(".", "").strip())
            agent_counts.append(q_val)
        
        self.assertEqual(sum(agent_counts), 24419, f"Soma dos subagentes ({sum(agent_counts)}) deve ser 24.419.")

    def test_06_global_sums_table_2_0_and_2_1(self):
        """Valida fechamento da Tabela 2.0 (Disciplinas) e 2.1 (Matriz de Contingência)."""
        # Tabela 2.0
        mat_match = re.search(r"\|\s*\*\*Matemática e suas Tecnologias\*\*\s*\|\s*\*\*(\d+[\.\d]*)\*\*", self.report_text)
        cn_match = re.search(r"\|\s*\*\*SUBTOTAL: CIÊNCIAS DA NATUREZA\*\*\s*\|\s*\*\*(\d+[\.\d]*)\*\*", self.report_text)
        total_match = re.search(r"\|\s*\*\*TOTAL GERAL CONSOLIDADO\*\*\s*\|\s*\*\*(\d+[\.\d]*)\*\*", self.report_text)
        
        self.assertIsNotNone(mat_match)
        self.assertIsNotNone(cn_match)
        self.assertIsNotNone(total_match)
        
        mat_val = int(mat_match.group(1).replace(".", ""))
        cn_val = int(cn_match.group(1).replace(".", ""))
        total_val = int(total_match.group(1).replace(".", ""))
        
        self.assertEqual(mat_val, 11685)
        self.assertEqual(cn_val, 12734)
        self.assertEqual(mat_val + cn_val, 24419)
        self.assertEqual(total_val, 24419)

        # Tabela 2.1 Contingência
        match_contingency = re.search(r"### 2\.1 Matriz de Contingência.*?\n(\|.*?\n\|.*?\n)(.*?)\n\| \*\*TOTAL CONSOLIDADO\*\*", self.report_text, re.DOTALL)
        self.assertIsNotNone(match_contingency, "Tabela 2.1 não encontrada.")
        c_rows = [r.strip() for r in match_contingency.group(2).strip().split("\n") if r.strip().startswith("|")]
        self.assertEqual(len(c_rows), 6)
        
        c_totals = []
        for r in c_rows:
            cols = [c.strip() for c in r.split("|")[1:-1]]
            c_totals.append(int(cols[6].replace("**", "").replace(".", "").strip()))
        self.assertEqual(sum(c_totals), 24419)

    def test_07_subject_breakdowns(self):
        """Valida que cada tabela por disciplina soma exatamente seu total."""
        # 3.1 Matemática (10 tópicos -> 11.685)
        m_match = re.search(r"### 3\.1 Matemática e suas Tecnologias.*?\n(\|.*?\n\|.*?\n)(.*?)\n\| — \| \*\*TOTAL MATEMÁTICA\*\*", self.report_text, re.DOTALL)
        self.assertIsNotNone(m_match)
        m_rows = [r.strip() for r in m_match.group(2).strip().split("\n") if r.strip().startswith("|")]
        self.assertEqual(len(m_rows), 10)
        m_counts = [int(r.split("|")[3].replace("**", "").replace(".", "").strip()) for r in m_rows]
        self.assertEqual(sum(m_counts), 11685)

        # 3.2 Física (8 tópicos -> 4.580)
        f_match = re.search(r"### 3\.2 Física.*?\n(\|.*?\n\|.*?\n)(.*?)\n\| — \| \*\*TOTAL FÍSICA\*\*", self.report_text, re.DOTALL)
        self.assertIsNotNone(f_match)
        f_rows = [r.strip() for r in f_match.group(2).strip().split("\n") if r.strip().startswith("|")]
        self.assertEqual(len(f_rows), 8)
        f_counts = [int(r.split("|")[3].replace("**", "").replace(".", "").strip()) for r in f_rows]
        self.assertEqual(sum(f_counts), 4580)

        # 3.3 Química (10 tópicos -> 3.393)
        q_match = re.search(r"### 3\.3 Química.*?\n(\|.*?\n\|.*?\n)(.*?)\n\| — \| \*\*TOTAL QUÍMICA\*\*", self.report_text, re.DOTALL)
        self.assertIsNotNone(q_match)
        q_rows = [r.strip() for r in q_match.group(2).strip().split("\n") if r.strip().startswith("|")]
        self.assertEqual(len(q_rows), 10)
        q_counts = [int(r.split("|")[3].replace("**", "").replace(".", "").strip()) for r in q_rows]
        self.assertEqual(sum(q_counts), 3393)

        # 3.4 Biologia (8 tópicos -> 4.076)
        b_match = re.search(r"### 3\.4 Biologia.*?\n(\|.*?\n\|.*?\n)(.*?)\n\| — \| \*\*TOTAL BIOLOGIA\*\*", self.report_text, re.DOTALL)
        self.assertIsNotNone(b_match)
        b_rows = [r.strip() for r in b_match.group(2).strip().split("\n") if r.strip().startswith("|")]
        self.assertEqual(len(b_rows), 8)
        b_counts = [int(r.split("|")[3].replace("**", "").replace(".", "").strip()) for r in b_rows]
        self.assertEqual(sum(b_counts), 4076)

        # Total somado das 4 disciplinas + CN Integradas (685)
        grand_total = sum(m_counts) + sum(f_counts) + sum(q_counts) + sum(b_counts) + 685
        self.assertEqual(grand_total, 24419)

if __name__ == "__main__":
    unittest.main(verbosity=2)

