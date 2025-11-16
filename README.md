📚 Sistema de Gerenciamento de Biblioteca Digital
Sistema completo para gestão de documentos digitais acadêmicos desenvolvido em Python.

🎯 Sobre o Projeto
Este sistema foi desenvolvido para facilitar a gestão de documentos digitais em bibliotecas universitárias, permitindo organização eficiente de artigos, teses e livros em diversos formatos digitais.

Características Principais
✅ Organização automática por tipo de documento e ano
✅ Interface de linha de comando intuitiva e colorida
✅ Suporte a múltiplos formatos (PDF, EPUB, MOBI, DOC, DOCX, TXT)
✅ Busca rápida por título, autor ou nome de arquivo
✅ Estatísticas detalhadas da biblioteca
✅ Sistema de metadados persistente
✅ Extração automática de ano do nome do arquivo
✅ Tratamento automático de nomes duplicados
📋 Requisitos
Python 3.7 ou superior
Bibliotecas Python (instaladas via requirements.txt):
colorama
🚀 Instalação
Clone o repositório:
git clone <url-do-repositorio>
cd biblioteca_digital
Instale as dependências:
pip install -r requirements.txt
Execute o sistema:
python main.py
📖 Como Usar
Menu Principal
O sistema oferece as seguintes funcionalidades:

Adicionar novo documento - Adiciona documentos com metadados
Remover documento - Remove documentos da biblioteca
Renomear documento - Renomeia arquivos mantendo metadados
Listar todos os documentos - Visualiza todos os documentos
Listar por tipo - Organiza por artigos, teses e livros
Listar por ano - Organiza cronologicamente
Buscar documentos - Busca por qualquer termo
Estatísticas da biblioteca - Visualiza métricas e estatísticas
Ajuda - Informações sobre formatos e convenções
Formatos Suportados
Artigos
PDF (.pdf)
DOC (.doc, .docx)
TXT (.txt)
Teses
PDF (.pdf)
DOC (.doc, .docx)
Livros
PDF (.pdf)
EPUB (.epub)
MOBI (.mobi)
AZW3 (.azw3)
Convenções de Nomenclatura Recomendadas
Para melhor organização, recomenda-se usar os seguintes padrões:

Artigos: Autor_Título_Ano.pdf
Teses: Título_Ano_Universidade.pdf
Livros: Título_Autor_Ano.pdf
O sistema extrai automaticamente o ano do nome do arquivo quando possível.

🏗️ Estrutura do Projeto
biblioteca_digital/
├── src/
│   ├── __init__.py
│   ├── document_manager.py    # Lógica de gerenciamento de documentos
│   └── cli.py                 # Interface de linha de comando
├── tests/
│   ├── __init__.py
│   └── test_document_manager.py  # Testes unitários
├── data/
│   ├── artigos/              # Diretório para artigos
│   ├── teses/                # Diretório para teses
│   ├── livros/               # Diretório para livros
│   └── metadata.json         # Metadados dos documentos
├── docs/
│   ├── MANUAL_USUARIO.md     # Manual do usuário
│   └── RELATORIO_TESTES.md   # Relatório de testes
├── main.py                   # Ponto de entrada do programa
├── requirements.txt          # Dependências Python
├── README.md                 # Este arquivo
└── CONTRIBUTING.md           # Guia de contribuição

🧪 Executando Testes
Para executar os testes unitários:

cd biblioteca_digital
python -m pytest tests/ -v
Ou execute diretamente:

python tests/test_document_manager.py
📊 Funcionalidades Detalhadas
1. Gerenciamento de Documentos
Adicionar: Copia documentos para a biblioteca mantendo metadados
Remover: Remove documento e seus metadados
Renomear: Atualiza nome do arquivo e metadados relacionados
2. Organização
Por Tipo: Artigos, Teses e Livros em diretórios separados
Por Ano: Visualização cronológica dos documentos
Metadados: Título, autor, ano, tamanho e data de adição
3. Busca e Estatísticas
Busca Textual: Pesquisa em título, autor e nome do arquivo
Estatísticas: Total de documentos, tamanho, distribuição por tipo e ano
🤝 Contribuindo
Por favor, leia CONTRIBUTING.md para detalhes sobre nosso código de conduta e o processo para enviar pull requests.

Workflow de Contribuição
Fork o projeto
Crie uma branch para sua feature (git checkout -b feature/NovaFuncionalidade)
Commit suas mudanças (git commit -m 'Adiciona nova funcionalidade')
Push para a branch (git push origin feature/NovaFuncionalidade)
Abra um Pull Request
📝 Licença
Este projeto é um software acadêmico desenvolvido para fins educacionais.

👥 Autores
Sistema desenvolvido como projeto universitário
🐛 Reportando Bugs
Encontrou um bug? Por favor, abra uma issue descrevendo:

O que aconteceu
O que era esperado
Passos para reproduzir
Ambiente (SO, versão do Python)
📞 Suporte
Para suporte e dúvidas:

Abra uma issue no GitHub
Entre em contato com a equipe de desenvolvimento
🔄 Versionamento
Usamos SemVer para versionamento. Versão atual: 1.0.0

📚 Documentação Adicional
Manual do Usuário
Relatório de Testes
Guia de Contribuição
✨ Agradecimentos
Biblioteca universitária pelo feedback durante o desenvolvimento
Comunidade Python pelas excelentes bibliotecas
Todos os contribuidores do projeto
