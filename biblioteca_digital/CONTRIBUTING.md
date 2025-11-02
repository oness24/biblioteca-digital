# 🤝 Guia de Contribuição

Obrigado por considerar contribuir para o Sistema de Gerenciamento de Biblioteca Digital! Este documento fornece diretrizes para contribuir com o projeto.

## 📋 Índice

- [Como Começar](#como-começar)
- [Workflow de Desenvolvimento](#workflow-de-desenvolvimento)
- [Padrões de Código](#padrões-de-código)
- [Commits e Mensagens](#commits-e-mensagens)
- [Pull Requests](#pull-requests)
- [Reportando Bugs](#reportando-bugs)
- [Sugerindo Melhorias](#sugerindo-melhorias)

## 🚀 Como Começar

### 1. Fork e Clone

```bash
# Fork o repositório no GitHub
# Clone seu fork
git clone https://github.com/SEU-USUARIO/biblioteca_digital.git
cd biblioteca_digital
```

### 2. Configure o Ambiente

```bash
# Crie um ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows:
venv\Scripts\activate
# No Linux/Mac:
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Configure o Git

```bash
# Configure o repositório upstream
git remote add upstream https://github.com/ORIGINAL-OWNER/biblioteca_digital.git

# Verifique os remotes
git remote -v
```

## 🔄 Workflow de Desenvolvimento

### 1. Mantenha Sincronizado

Antes de começar qualquer trabalho, sincronize com o repositório principal:

```bash
# Busca mudanças do repositório original
git fetch upstream

# Muda para a branch main
git checkout main

# Merge das mudanças
git merge upstream/main

# Atualiza seu fork no GitHub
git push origin main
```

### 2. Crie uma Branch

Sempre crie uma branch para suas mudanças:

```bash
# Para novas funcionalidades
git checkout -b feature/nome-da-funcionalidade

# Para correções de bugs
git checkout -b fix/descricao-do-bug

# Para melhorias de documentação
git checkout -b docs/descricao-melhoria
```

### 3. Faça suas Mudanças

- Escreva código limpo e bem documentado
- Siga os padrões de código do projeto
- Adicione testes para novas funcionalidades
- Atualize a documentação quando necessário

### 4. Teste suas Mudanças

```bash
# Execute os testes unitários
python tests/test_document_manager.py

# Teste manualmente o sistema
python main.py
```

### 5. Commit suas Mudanças

```bash
# Adicione os arquivos modificados
git add .

# Faça o commit com mensagem descritiva
git commit -m "Tipo: Descrição clara da mudança"

# Exemplos:
# git commit -m "feat: Adiciona suporte para formato AZW3"
# git commit -m "fix: Corrige bug na extração de ano"
# git commit -m "docs: Atualiza README com novos exemplos"
```

### 6. Push e Pull Request

```bash
# Envie para seu fork
git push origin nome-da-sua-branch
```

Então, no GitHub:
1. Vá para seu fork do repositório
2. Clique em "Pull Request"
3. Preencha o template de PR (veja seção abaixo)
4. Aguarde revisão

## 📝 Padrões de Código

### Python Style Guide

Seguimos a [PEP 8](https://pep8.org/) com algumas adaptações:

- **Indentação**: 4 espaços (não tabs)
- **Comprimento de linha**: Máximo 100 caracteres
- **Aspas**: Use aspas duplas para strings
- **Docstrings**: Use formato Google/NumPy

### Exemplo de Código Bem Formatado

```python
def add_document(self, file_path: str, doc_type: str, year: Optional[int] = None) -> bool:
    """
    Adiciona um novo documento à biblioteca

    Args:
        file_path: Caminho do arquivo a ser adicionado
        doc_type: Tipo do documento (artigos, teses, livros)
        year: Ano de publicação (opcional)

    Returns:
        True se adicionado com sucesso, False caso contrário

    Raises:
        FileNotFoundError: Se o arquivo não existir
        ValueError: Se o tipo de documento for inválido
    """
    # Seu código aqui
    pass
```

### Nomenclatura

- **Variáveis e funções**: `snake_case`
- **Classes**: `PascalCase`
- **Constantes**: `UPPER_CASE`
- **Arquivos**: `snake_case.py`

### Comentários

```python
# Comentários de uma linha começam com # e um espaço

"""
Docstrings para módulos, classes e funções
usam três aspas duplas
"""

# TODO: Descrição do que precisa ser feito
# FIXME: Descrição do problema que precisa ser corrigido
```

## 💬 Commits e Mensagens

### Formato de Commit

Use o formato de [Conventional Commits](https://www.conventionalcommits.org/):

```
tipo(escopo): descrição curta

[corpo opcional]

[rodapé opcional]
```

### Tipos de Commit

- **feat**: Nova funcionalidade
- **fix**: Correção de bug
- **docs**: Mudanças na documentação
- **style**: Formatação, ponto e vírgula faltando, etc
- **refactor**: Refatoração de código
- **test**: Adicionando testes
- **chore**: Manutenção, atualização de dependências

### Exemplos de Boas Mensagens

```bash
feat: Adiciona suporte para busca por múltiplos termos

fix: Corrige bug na extração de ano de nomes com hífen

docs: Atualiza guia de instalação com troubleshooting

test: Adiciona testes para função de renomeação

refactor: Melhora performance da listagem de documentos

chore: Atualiza dependência colorama para versão 0.4.6
```

### Exemplos de Mensagens Ruins

❌ `fix bug`
❌ `update`
❌ `mudanças no código`
❌ `WIP`

## 🔀 Pull Requests

### Antes de Criar um PR

- [ ] Código segue os padrões do projeto
- [ ] Todos os testes passam
- [ ] Novos testes foram adicionados (se aplicável)
- [ ] Documentação foi atualizada (se aplicável)
- [ ] Commit messages seguem o padrão

### Template de Pull Request

```markdown
## Descrição

Descrição clara e concisa das mudanças.

## Tipo de Mudança

- [ ] Bug fix (correção de problema)
- [ ] Nova funcionalidade (nova feature)
- [ ] Breaking change (mudança que quebra compatibilidade)
- [ ] Documentação

## Como Testar

1. Passo a passo para testar as mudanças
2. ...

## Checklist

- [ ] Meu código segue os padrões do projeto
- [ ] Revisei meu próprio código
- [ ] Comentei código complexo
- [ ] Atualizei a documentação
- [ ] Minhas mudanças não geram novos warnings
- [ ] Adicionei testes que provam que minha correção funciona
- [ ] Testes novos e existentes passam localmente

## Screenshots (se aplicável)

Adicione screenshots se relevante.

## Contexto Adicional

Qualquer informação adicional sobre o PR.
```

### Processo de Revisão

1. **Automated checks**: CI/CD verifica testes e linting
2. **Code review**: Pelo menos um mantenedor revisa o código
3. **Discussão**: Feedback é dado através de comentários
4. **Aprovação**: PR é aprovado ou solicitadas mudanças
5. **Merge**: Após aprovação, PR é mesclado

## 🐛 Reportando Bugs

### Antes de Reportar

- Verifique se o bug já não foi reportado
- Tente reproduzir com a última versão
- Isole o problema o máximo possível

### Template de Bug Report

```markdown
## Descrição do Bug

Descrição clara e concisa do que o bug é.

## Para Reproduzir

Passos para reproduzir o comportamento:
1. Vá para '...'
2. Clique em '...'
3. Role até '...'
4. Veja o erro

## Comportamento Esperado

O que você esperava que acontecesse.

## Comportamento Atual

O que realmente aconteceu.

## Screenshots

Se aplicável, adicione screenshots.

## Ambiente

- OS: [ex: Windows 10]
- Python: [ex: 3.9.0]
- Versão do Sistema: [ex: 1.0.0]

## Contexto Adicional

Qualquer outra informação sobre o problema.
```

## 💡 Sugerindo Melhorias

### Template de Feature Request

```markdown
## Problema Relacionado

Esta feature está relacionada a algum problema? Descreva.

## Solução Desejada

Descrição clara e concisa do que você quer que aconteça.

## Alternativas Consideradas

Descreva alternativas que você considerou.

## Contexto Adicional

Qualquer outra informação ou screenshots sobre a feature.
```

## 📚 Recursos Adicionais

- [Como Escrever uma Boa Commit Message](https://chris.beams.io/posts/git-commit/)
- [Git Cheat Sheet](https://education.github.com/git-cheat-sheet-education.pdf)
- [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/)
- [Conventional Commits](https://www.conventionalcommits.org/)

## ❓ Dúvidas

Se você tem dúvidas sobre como contribuir:

1. Verifique a documentação existente
2. Procure em issues fechadas
3. Abra uma issue com sua dúvida
4. Entre em contato com os mantenedores

## 🙏 Agradecimentos

Obrigado por dedicar seu tempo para contribuir com este projeto! Cada contribuição, por menor que seja, faz diferença.

---

**Lembre-se**: O objetivo é criar um ambiente colaborativo e acolhedor. Seja respeitoso e construtivo em todas as interações.
