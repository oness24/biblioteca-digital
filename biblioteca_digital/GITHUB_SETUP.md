# 🚀 Guia de Publicação no GitHub

## Passo a Passo para Publicar o Projeto

### Passo 1: Criar Repositório no GitHub

1. Acesse [github.com](https://github.com)
2. Faça login na sua conta
3. Clique no botão **"+"** no canto superior direito
4. Selecione **"New repository"**
5. Configure o repositório:
   - **Repository name**: `biblioteca-digital` ou `sistema-biblioteca-digital`
   - **Description**: "Sistema de Gerenciamento de Biblioteca Digital - Projeto Universitário"
   - **Visibility**:
     - ✅ **Public** (recomendado para projetos acadêmicos)
     - ou **Private** (se preferir manter privado)
   - **⚠️ NÃO marque**:
     - ❌ "Add a README file"
     - ❌ "Add .gitignore"
     - ❌ "Choose a license"
   - (Já temos esses arquivos criados!)
6. Clique em **"Create repository"**

### Passo 2: Conectar Repositório Local ao GitHub

Após criar o repositório, o GitHub mostrará instruções. Use estes comandos:

```bash
# 1. Adicione o repositório remoto
git remote add origin https://github.com/SEU-USUARIO/biblioteca-digital.git

# 2. Verifique se foi adicionado corretamente
git remote -v

# Você deve ver:
# origin  https://github.com/SEU-USUARIO/biblioteca-digital.git (fetch)
# origin  https://github.com/SEU-USUARIO/biblioteca-digital.git (push)
```

**⚠️ Importante**: Substitua `SEU-USUARIO` pelo seu nome de usuário do GitHub!

### Passo 3: Fazer Push do Código

```bash
# 1. Renomeia a branch para 'main' (se necessário)
git branch -M main

# 2. Faz o push para o GitHub
git push -u origin main
```

Se for solicitada autenticação:
- **Username**: Seu nome de usuário do GitHub
- **Password**: Use um **Personal Access Token** (não a senha da conta)

### Passo 4: Criar Personal Access Token (se necessário)

Se você não tiver um token, crie um:

1. No GitHub, vá em: **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Clique em **"Generate new token"** → **"Generate new token (classic)"**
3. Configure:
   - **Note**: "Biblioteca Digital Token"
   - **Expiration**: 90 days (ou o que preferir)
   - **Scopes**: Marque apenas:
     - ✅ `repo` (Full control of private repositories)
4. Clique em **"Generate token"**
5. **⚠️ COPIE O TOKEN AGORA** (você não poderá vê-lo novamente!)
6. Use esse token como senha quando fizer o push

### Passo 5: Verificar no GitHub

Após o push bem-sucedido:

1. Acesse `https://github.com/SEU-USUARIO/biblioteca-digital`
2. Você deve ver:
   - ✅ Todos os arquivos do projeto
   - ✅ README.md renderizado na página principal
   - ✅ 3 commits no histórico
   - ✅ Estrutura de pastas completa

---

## Comandos Completos (Resumo)

```bash
# Certifique-se de estar no diretório correto
cd /mnt/c/users/Onesmus/python_Data_science/biblioteca_digital

# Adicione o remote (substitua SEU-USUARIO)
git remote add origin https://github.com/SEU-USUARIO/biblioteca-digital.git

# Verifique
git remote -v

# Garanta que está na branch main
git branch -M main

# Faça o push
git push -u origin main

# Digite seu username e token quando solicitado
```

---

## Configurar Proteção da Branch Main (Opcional)

Para projetos colaborativos:

1. No GitHub, vá para: **Settings** → **Branches**
2. Clique em **"Add branch protection rule"**
3. Configure:
   - **Branch name pattern**: `main`
   - Marque:
     - ✅ Require a pull request before merging
     - ✅ Require approvals (1)
     - ✅ Require status checks to pass
4. Salve as regras

---

## Adicionar Colaboradores (Opcional)

1. Vá para: **Settings** → **Collaborators**
2. Clique em **"Add people"**
3. Digite o username ou email do colaborador
4. Selecione as permissões (Write, Maintain, Admin)

---

## Criar README Badge (Opcional)

Adicione badges ao README para mostrar status:

```markdown
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-active-success)
```

---

## Problemas Comuns e Soluções

### Erro: "remote origin already exists"

```bash
# Remove o remote existente
git remote remove origin

# Adicione novamente com a URL correta
git remote add origin https://github.com/SEU-USUARIO/biblioteca-digital.git
```

### Erro: "Authentication failed"

**Solução**: Use Personal Access Token em vez da senha da conta
- Crie um token seguindo as instruções acima

### Erro: "Updates were rejected"

```bash
# Force push (use com cuidado!)
git push -u origin main --force
```

### Erro: "Could not resolve host"

**Solução**: Verifique sua conexão com a internet

---

## Usando SSH (Alternativa)

Se preferir usar SSH em vez de HTTPS:

### 1. Gerar chave SSH

```bash
ssh-keygen -t ed25519 -C "seu_email@example.com"
# Pressione Enter para aceitar o local padrão
# Digite uma senha (opcional)
```

### 2. Adicionar chave ao SSH Agent

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

### 3. Copiar chave pública

```bash
cat ~/.ssh/id_ed25519.pub
# Copie toda a saída
```

### 4. Adicionar no GitHub

1. GitHub → **Settings** → **SSH and GPG keys**
2. **"New SSH key"**
3. Cole a chave pública
4. Clique em **"Add SSH key"**

### 5. Configurar remote com SSH

```bash
git remote add origin git@github.com:SEU-USUARIO/biblioteca-digital.git
git push -u origin main
```

---

## Após Publicar

### 1. Adicionar Topics no GitHub

No repositório, adicione topics para melhor descoberta:
- `python`
- `biblioteca-digital`
- `gestao-documentos`
- `projeto-universitario`
- `cli-application`

### 2. Adicionar About

Configure a descrição no topo do repositório:
- **Description**: "Sistema de Gerenciamento de Biblioteca Digital desenvolvido em Python"
- **Website**: (se tiver)
- **Topics**: (adicione as tags acima)

### 3. Criar Release (Opcional)

1. Vá para **Releases** → **"Create a new release"**
2. Configure:
   - **Tag version**: `v1.0.0`
   - **Release title**: "Versão 1.0.0 - Release Inicial"
   - **Description**: Descreva as funcionalidades
3. Clique em **"Publish release"**

---

## Clone do Projeto (Para Outros Usuários)

Outros poderão clonar seu projeto com:

```bash
git clone https://github.com/SEU-USUARIO/biblioteca-digital.git
cd biblioteca-digital
pip install -r requirements.txt
python3 main.py
```

---

## Manutenção Futura

### Fazer Novas Mudanças

```bash
# 1. Faça suas modificações no código

# 2. Adicione ao stage
git add .

# 3. Faça commit
git commit -m "tipo: descrição da mudança"

# 4. Push para GitHub
git push origin main
```

### Criar Feature Branches

```bash
# Criar e mudar para nova branch
git checkout -b feature/nova-funcionalidade

# Fazer mudanças e commit
git add .
git commit -m "feat: adiciona nova funcionalidade"

# Push da branch
git push origin feature/nova-funcionalidade

# No GitHub, crie um Pull Request
```

---

## Recursos Úteis

- **GitHub Docs**: https://docs.github.com
- **Git Cheat Sheet**: https://education.github.com/git-cheat-sheet-education.pdf
- **Markdown Guide**: https://guides.github.com/features/mastering-markdown/

---

## ✅ Checklist Final

Antes de considerar concluído, verifique:

- [ ] Repositório criado no GitHub
- [ ] Remote configurado localmente
- [ ] Push realizado com sucesso
- [ ] README renderizado corretamente
- [ ] Todos os arquivos visíveis
- [ ] Commits aparecendo no histórico
- [ ] Estrutura de pastas intacta
- [ ] .gitignore funcionando (arquivos temporários não enviados)

---

**Parabéns! Seu projeto está agora no GitHub!** 🎉

Compartilhe o link: `https://github.com/SEU-USUARIO/biblioteca-digital`
