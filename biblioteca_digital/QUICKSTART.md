# 🚀 Guia Rápido de Início

## Instalação em 3 Passos

### 1. Clone e Entre no Diretório
```bash
cd biblioteca_digital
```

### 2. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 3. Execute o Sistema
```bash
python main.py
```

## Primeiro Uso

Quando o programa iniciar, você verá o menu principal:

```
╔══════════════════════════════════════════════════════════════╗
║         📚 SISTEMA DE BIBLIOTECA DIGITAL 📚              ║
║              Gestão de Documentos Acadêmicos                ║
╚══════════════════════════════════════════════════════════════╝

1.  📄 Adicionar novo documento
2.  🗑️  Remover documento
3.  ✏️  Renomear documento
4.  📋 Listar todos os documentos
5.  📁 Listar por tipo
6.  📅 Listar por ano
7.  🔍 Buscar documentos
8.  📊 Estatísticas da biblioteca
9.  ❓ Ajuda
0.  🚪 Sair
```

## Exemplo: Adicionar seu Primeiro Documento

1. Digite `1` e pressione Enter
2. Escolha o tipo:
   - `1` para Artigos
   - `2` para Teses
   - `3` para Livros
3. Informe o caminho completo do arquivo
4. Preencha os metadados (título, autor, ano)
5. Pronto! Documento adicionado

## Exemplo Completo

```
Digite sua opção: 1

═══ ADICIONAR NOVO DOCUMENTO ═══

Tipos disponíveis:
  1. Artigos
  2. Teses
  3. Livros

Escolha o tipo (1-3): 1
Caminho completo do arquivo: C:\Downloads\meu_artigo.pdf
Título (Enter para usar nome do arquivo): Introdução ao Python
Autor: João Silva
Ano de publicação (Enter para extrair do nome): 2023

✓ Documento adicionado com sucesso!
```

## Executar Testes

Para verificar que tudo está funcionando:

```bash
python tests/test_document_manager.py
```

Você deve ver:
```
Ran 22 tests in 0.145s
OK
```

## Usar Programaticamente

```python
from src.document_manager import DocumentManager

# Criar gerenciador
manager = DocumentManager("data")

# Adicionar documento
manager.add_document(
    file_path="artigo.pdf",
    doc_type="artigos",
    year=2023,
    author="João Silva",
    title="Meu Artigo"
)

# Listar documentos
docs = manager.list_documents()
for doc in docs:
    print(f"{doc['title']} - {doc['author']}")

# Buscar
resultados = manager.search_documents("Python")

# Estatísticas
stats = manager.get_statistics()
print(f"Total: {stats['total_documents']} documentos")
```

## Precisa de Ajuda?

- **Menu de Ajuda:** Digite `9` no menu principal
- **Manual Completo:** Veja `docs/MANUAL_USUARIO.md`
- **Documentação:** Veja `README.md`
- **Exemplos:** Execute `python exemplos_uso.py`

## Formatos Aceitos

- **Artigos:** PDF, DOC, DOCX, TXT
- **Teses:** PDF, DOC, DOCX
- **Livros:** PDF, EPUB, MOBI, AZW3

## Dica Importante

Use nomes de arquivo com ano para extração automática:
- ✅ `Silva_Introducao_Python_2023.pdf`
- ✅ `artigo-2023-final.pdf`
- ✅ `tese_2022_v2.pdf`

## Estrutura de Dados

Seus documentos serão organizados em:
```
data/
├── artigos/    # Seus artigos ficam aqui
├── teses/      # Suas teses ficam aqui
├── livros/     # Seus livros ficam aqui
└── metadata.json  # Metadados (faça backup!)
```

## Comandos Úteis

```bash
# Ver estrutura do projeto
ls -la biblioteca_digital/

# Executar testes
python tests/test_document_manager.py

# Ver exemplos de uso
python exemplos_uso.py

# Sair do programa
Digite 0 no menu ou pressione Ctrl+C
```

## Troubleshooting

### Erro: "colorama not found"
```bash
pip install colorama
```

### Erro: "Permission denied"
- No Windows: Execute como Administrador
- No Linux/Mac: Verifique permissões da pasta

### Documento não é adicionado
- Verifique se o caminho está correto
- Verifique se o formato é suportado
- Verifique se você tem permissão de leitura

## Próximos Passos

1. ✅ Adicione alguns documentos de teste
2. ✅ Explore as funcionalidades de busca
3. ✅ Veja as estatísticas
4. ✅ Leia o manual completo em `docs/MANUAL_USUARIO.md`

---

**Pronto para começar!** 🎉

Para documentação completa, veja `README.md`
