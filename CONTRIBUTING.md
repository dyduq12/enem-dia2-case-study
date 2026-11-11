# Guia de Contribuição - ENEM Dia 2 Analytics

Agradecemos o interesse em contribuir com o projeto **ENEM Dia 2 Analytics**. Este repositório reúne ferramentas de mineração de dados em PDFs de simulados, classificação semântica de questões e geração de artefatos estruturados para o MindNote.

---

## 1. Princípios de Contribuição

1. **Foco Estrito no 2º Dia do ENEM**:
   - Matemática e suas Tecnologias.
   - Ciências da Natureza e suas Tecnologias (Física, Química e Biologia).
   - O projeto descarta explicitamente vestibulares estaduais (FUVEST, UNICAMP, UNESP, etc.) ou provas de olimpíadas.

2. **Preservação de Integridade Estatística**:
   - Qualquer ajuste na taxonomia semântica de classificação deve manter retrocompatibilidade com os códigos canônicos de tópicos e passar pelos testes automatizados.

3. **Arquitetura Sem Dados Sensíveis**:
   - Os cadernos brutos de simulados e PDFs pesados (~5.56 GB) não devem ser versionados no Git (já cobertos pelo `.gitignore`).

---

## 2. Configuração do Ambiente Local

### Pré-requisitos
- Python 3.10 ou superior.
- Node.js 18+ (opcional, para validação do motor MindNote JS).
- Navegador Chromium / MS Edge (opcional, para execução de testes headless de renderização DOM).

### Instalação
```bash
# Criar e ativar ambiente virtual
python -m venv .venv
# No Windows PowerShell:
.venv\Scripts\Activate.ps1
# No Linux/macOS:
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

---

## 3. Padrão de Branches e Commits

Adotamos a convenção do **Conventional Commits**:

- `feat:` Nova funcionalidade no pipeline de mineração ou classificação.
- `fix:` Correção de bug em parser de PDF, regex de extração ou cálculo estatístico.
- `docs:` Alterações na documentação, relatórios ou guias.
- `test:` Inclusão ou aprimoramento de rotinas de validação e testes DOM.
- `chore:` Manutenção de dependências, arquivos de configuração ou scripts auxiliares.

### Nomes de Branch Sugeridos
- `feat/novo-classificador-fisica`
- `fix/extracao-regex-q94`
- `docs/atualizacao-relatorio-consolidado`

---

## 4. Como Executar os Testes Automatizados

Antes de submeter um Pull Request, execute a suíte de testes de integridade:

```bash
# Validação do Cronograma Tático (Python AST + MindNote Engine + Browser DOM)
python scripts/test_cronograma_reta_final.py

# Validação do Mapa Mental Completo (202 nós, 4 raízes)
python scripts/test_mindnote_mapa.py
```

Ambos os scripts devem finalizar com código de saída 0 e relatar 100% de aprovação.

---

## 5. Submissão de Pull Request

1. Abra uma branch a partir da `main`.
2. Faça commits atômicos com mensagens claras e objetivas.
3. Certifique-se de que nenhum arquivo `.pdf` ou dump intermediário esteja no staged do Git.
4. Descreva detalhadamente o que foi alterado e como os testes foram executados.

