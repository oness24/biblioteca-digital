# 📖 Manual do Usuário - Sistema de Biblioteca Digital

## Índice

1. [Introdução](#introdução)
2. [Instalação](#instalação)
3. [Iniciando o Sistema](#iniciando-o-sistema)
4. [Funcionalidades](#funcionalidades)
5. [Casos de Uso](#casos-de-uso)
6. [Resolução de Problemas](#resolução-de-problemas)
7. [Dicas e Boas Práticas](#dicas-e-boas-práticas)

## Introdução

O Sistema de Gerenciamento de Biblioteca Digital é uma ferramenta desenvolvida para facilitar a organização e gestão de documentos acadêmicos digitais, incluindo artigos, teses e livros em diversos formatos.

### Benefícios

- ✅ Organização automática por tipo e ano
- ✅ Busca rápida e eficiente
- ✅ Interface intuitiva
- ✅ Estatísticas em tempo real
- ✅ Sem necessidade de banco de dados

## Instalação

### Requisitos do Sistema

- **Sistema Operacional**: Windows, Linux ou macOS
- **Python**: Versão 3.7 ou superior
- **Espaço em disco**: Depende do tamanho da biblioteca
- **Memória RAM**: Mínimo 512MB

### Passo a Passo

#### 1. Instalar Python

Baixe e instale Python em [python.org](https://www.python.org/downloads/)

Verifique a instalação:
```bash
python --version
```

#### 2. Baixar o Sistema

```bash
git clone <url-do-repositorio>
cd biblioteca_digital
```

#### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

#### 4. Verificar Instalação

```bash
python main.py
```

Se aparecer o menu principal, a instalação foi bem-sucedida!

## Iniciando o Sistema

### Execução Normal

```bash
python main.py
```

### Primeira Execução

Na primeira vez que você executar o sistema:
1. Os diretórios necessários serão criados automaticamente
2. Um arquivo de metadados será inicializado
3. O menu principal será exibido

## Funcionalidades

### 1. Adicionar Novo Documento

**Como usar:**
1. Selecione opção `1` no menu
2. Escolha o tipo (Artigos, Teses ou Livros)
3. Informe o caminho completo do arquivo
4. Preencha os metadados (título, autor, ano)
5. Confirme a adição

**Exemplo:**
```
Tipo: 1 (Artigos)
Caminho: C:\Downloads\artigo_python_2023.pdf
Título: Introdução ao Python
Autor: João Silva
Ano: 2023
```

**Dicas:**
- O arquivo original não é movido, apenas copiado
- Se não informar o ano, o sistema tenta extrair do nome do arquivo
- Formatos aceitos variam por tipo de documento

### 2. Remover Documento

**Como usar:**
1. Selecione opção `2` no menu
2. Escolha o tipo do documento
3. Visualize a lista de documentos
4. Informe o nome do arquivo
5. Confirme a remoção

**Atenção:**
- ⚠️ Esta ação é irreversível!
- O arquivo será permanentemente removido
- Os metadados também serão excluídos

### 3. Renomear Documento

**Como usar:**
1. Selecione opção `3` no menu
2. Escolha o tipo do documento
3. Visualize a lista de documentos
4. Informe o nome atual
5. Informe o novo nome
6. A extensão é mantida automaticamente

**Exemplo:**
```
Nome atual: artigo_antigo.pdf
Novo nome: artigo_revisado
Resultado: artigo_revisado.pdf
```

### 4. Listar Todos os Documentos

**Como usar:**
1. Selecione opção `4` no menu
2. Visualize todos os documentos da biblioteca

**Informações exibidas:**
- Nome do arquivo
- Tipo de documento
- Título
- Autor
- Ano de publicação
- Tamanho do arquivo

### 5. Listar por Tipo

**Como usar:**
1. Selecione opção `5` no menu
2. Visualize documentos organizados por categoria:
   - Artigos
   - Teses
   - Livros

**Útil para:**
- Ver quantos documentos de cada tipo você tem
- Encontrar rapidamente um tipo específico

### 6. Listar por Ano

**Como usar:**
1. Selecione opção `6` no menu
2. Visualize documentos organizados cronologicamente

**Características:**
- Anos são ordenados do mais recente ao mais antigo
- Documentos sem ano aparecem em categoria separada
- Útil para análises temporais

### 7. Buscar Documentos

**Como usar:**
1. Selecione opção `7` no menu
2. Digite termo de busca
3. Visualize resultados

**A busca procura em:**
- Nome do arquivo
- Título do documento
- Nome do autor

**Exemplos:**
```
Busca: "Python"
Resultado: Todos documentos com "Python" em qualquer campo

Busca: "Silva"
Resultado: Documentos do autor Silva

Busca: "2023"
Resultado: Documentos com 2023 no nome ou título
```

### 8. Estatísticas da Biblioteca

**Como usar:**
1. Selecione opção `8` no menu
2. Visualize estatísticas completas

**Informações fornecidas:**
- Total de documentos
- Tamanho total em MB
- Distribuição por tipo
- Distribuição por ano
- Período da coleção (ano mais antigo e mais recente)
- Top 10 anos com mais documentos

### 9. Ajuda

**Como usar:**
1. Selecione opção `9` no menu
2. Consulte informações sobre:
   - Formatos suportados
   - Convenções de nomenclatura
   - Dicas de uso

## Casos de Uso

### Caso 1: Organizar Artigos de uma Conferência

**Cenário:** Você baixou 50 artigos de uma conferência e precisa organizá-los.

**Solução:**
1. Renomeie os arquivos seguindo padrão: `Autor_Título_2023.pdf`
2. Use a opção "Adicionar novo documento" para cada arquivo
3. Preencha os metadados conforme necessário
4. Use "Listar por ano" para verificar a organização

### Caso 2: Criar Biblioteca de Referências para TCC

**Cenário:** Organizar materiais de pesquisa para trabalho de conclusão.

**Solução:**
1. Adicione todos os documentos relevantes
2. Use títulos descritivos e autores corretos
3. Utilize a busca para encontrar rapidamente referências
4. Exporte estatísticas para conhecer sua base de dados

### Caso 3: Remover Documentos Duplicados

**Cenário:** Você tem documentos duplicados na biblioteca.

**Solução:**
1. Use "Listar todos os documentos"
2. Identifique duplicatas pelo título e tamanho
3. Use "Remover documento" para excluir duplicatas
4. Verifique as estatísticas para confirmar

### Caso 4: Migrar de Sistema Manual

**Cenário:** Você organizava documentos em pastas e quer usar o sistema.

**Solução:**
1. Mantenha seus arquivos originais
2. Adicione documentos ao sistema (serão copiados)
3. Preencha metadados aos poucos
4. Após verificar que tudo está ok, pode apagar arquivos originais

## Resolução de Problemas

### Problema: Erro ao adicionar documento

**Sintoma:** Mensagem de erro ao tentar adicionar arquivo

**Soluções:**
1. Verifique se o caminho do arquivo está correto
2. Certifique-se de que o arquivo existe
3. Verifique se o formato é suportado para aquele tipo
4. Confirme que você tem permissões de leitura no arquivo

### Problema: Documento não aparece na busca

**Sintoma:** Busca não retorna documento que você sabe que existe

**Soluções:**
1. Verifique a ortografia do termo de busca
2. Busca é case-insensitive, mas precisa ter o termo exato
3. Tente buscar parte do nome do arquivo
4. Use "Listar todos" para verificar se documento está na biblioteca

### Problema: Erro de permissão

**Sintoma:** "Permission denied" ou erro de acesso

**Soluções:**
1. Execute o programa com permissões adequadas
2. Verifique se o diretório de dados tem permissão de escrita
3. No Windows, tente executar como administrador
4. Verifique antivírus não está bloqueando

### Problema: Sistema lento

**Sintoma:** Interface demora para responder

**Soluções:**
1. Se tem muitos documentos, considere organizar em subcategorias
2. Verifique espaço em disco
3. Arquivos muito grandes podem afetar performance
4. Reinicie o programa

### Problema: Metadados perdidos

**Sintoma:** Documentos aparecem sem autor ou título

**Soluções:**
1. Verifique se arquivo metadata.json não foi corrompido
2. Re-adicione os metadados usando "Renomear" (atualiza metadados)
3. Faça backup regular do arquivo metadata.json

## Dicas e Boas Práticas

### Organização de Arquivos

1. **Use nomes descritivos**
   ```
   ✅ Silva_Introducao_Python_2023.pdf
   ❌ documento1.pdf
   ```

2. **Inclua o ano no nome do arquivo**
   - Facilita extração automática
   - Melhora organização

3. **Seja consistente com formato de nomes**
   - Escolha um padrão e siga sempre
   - Facilita manutenção futura

### Metadados

1. **Preencha todos os campos possíveis**
   - Título: Nome completo e descritivo
   - Autor: Nome completo (Sobrenome, Nome)
   - Ano: Ano de publicação

2. **Use nomenclatura padronizada para autores**
   ```
   ✅ Silva, João
   ✅ Silva, J.
   ❌ João Silva
   ❌ J. Silva
   ```

### Backup

1. **Faça backup regular**
   ```bash
   # Backup do diretório de dados
   cp -r data/ backup_data_$(date +%Y%m%d)/
   ```

2. **Especialmente importante: metadata.json**
   - Contém todas as informações dos documentos
   - Sem ele, perde-se título, autor, ano

### Performance

1. **Para bibliotecas grandes (>1000 documentos)**
   - Considere dividir em múltiplas instâncias
   - Use busca em vez de listar tudo

2. **Mantenha documentos em SSD se possível**
   - Melhora velocidade de acesso
   - Especialmente para arquivos grandes

### Segurança

1. **Não compartilhe metadata.json**
   - Pode conter informações sensíveis
   - Mantém estrutura da biblioteca

2. **Verifique permissões de diretórios**
   ```bash
   chmod 700 data/  # Somente você tem acesso
   ```

3. **Cuidado com documentos protegidos por copyright**
   - Respeite direitos autorais
   - Use apenas para fins acadêmicos permitidos

## Atalhos e Comandos Rápidos

### Navegação Rápida

- **Sair**: Digite `0` no menu principal
- **Voltar**: Pressione `Enter` após operação
- **Cancelar**: Deixe campo vazio ou pressione `Ctrl+C`

### Formatos de Entrada

**Caminhos de Arquivo:**
```bash
# Windows
C:\Users\Nome\Documents\arquivo.pdf
.\arquivo.pdf (relativo)

# Linux/Mac
/home/user/documents/arquivo.pdf
./arquivo.pdf (relativo)
```

**Anos:**
```
✅ 2023
✅ 1998
❌ 23 (use ano completo)
```

## Glossário

- **Artigo**: Documento científico ou acadêmico curto
- **Tese**: Documento acadêmico extenso (mestrado/doutorado)
- **Livro**: Obra completa em formato digital
- **Metadados**: Informações sobre o documento (autor, título, etc.)
- **CLI**: Command Line Interface (Interface de Linha de Comando)

## Suporte

### Precisa de Ajuda?

1. **Consulte este manual**
2. **Verifique CONTRIBUTING.md** para questões técnicas
3. **Abra uma issue** no GitHub
4. **Entre em contato** com suporte da biblioteca

### Recursos Adicionais

- [README.md](../README.md) - Visão geral do projeto
- [CONTRIBUTING.md](../CONTRIBUTING.md) - Guia para desenvolvedores
- [RELATORIO_TESTES.md](RELATORIO_TESTES.md) - Relatório de testes

---

**Versão do Manual:** 1.0.0
**Última Atualização:** 2024
**Desenvolvido para:** Bibliotecas Universitárias
