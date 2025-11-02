"""
Interface de Linha de Comando (CLI) para o Sistema de Biblioteca Digital
"""

import sys
import os
from pathlib import Path
from colorama import Fore, Style, init
from document_manager import DocumentManager

# Inicializa colorama
init(autoreset=True)


class LibraryCLI:
    """Interface de linha de comando para gerenciamento da biblioteca"""

    def __init__(self):
        """Inicializa a CLI"""
        # Define o caminho base relativo ao diretório do projeto
        base_dir = Path(__file__).parent.parent / "data"
        self.manager = DocumentManager(str(base_dir))

    def print_banner(self):
        """Exibe o banner do sistema"""
        banner = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════╗
║         {Fore.YELLOW}📚 SISTEMA DE BIBLIOTECA DIGITAL 📚{Fore.CYAN}              ║
║              {Fore.GREEN}Gestão de Documentos Acadêmicos{Fore.CYAN}                ║
╚══════════════════════════════════════════════════════════════╝{Style.RESET_ALL}
        """
        print(banner)

    def print_menu(self):
        """Exibe o menu principal"""
        menu = f"""
{Fore.CYAN}═══════════════════ MENU PRINCIPAL ═══════════════════{Style.RESET_ALL}

{Fore.GREEN}1.{Style.RESET_ALL}  📄 Adicionar novo documento
{Fore.GREEN}2.{Style.RESET_ALL}  🗑️  Remover documento
{Fore.GREEN}3.{Style.RESET_ALL}  ✏️  Renomear documento
{Fore.GREEN}4.{Style.RESET_ALL}  📋 Listar todos os documentos
{Fore.GREEN}5.{Style.RESET_ALL}  📁 Listar por tipo
{Fore.GREEN}6.{Style.RESET_ALL}  📅 Listar por ano
{Fore.GREEN}7.{Style.RESET_ALL}  🔍 Buscar documentos
{Fore.GREEN}8.{Style.RESET_ALL}  📊 Estatísticas da biblioteca
{Fore.GREEN}9.{Style.RESET_ALL}  ❓ Ajuda
{Fore.RED}0.{Style.RESET_ALL}  🚪 Sair

{Fore.CYAN}═══════════════════════════════════════════════════════{Style.RESET_ALL}
        """
        print(menu)

    def format_file_size(self, size_bytes: int) -> str:
        """Formata o tamanho do arquivo para exibição"""
        for unit in ['B', 'KB', 'MB', 'GB']:
            if size_bytes < 1024.0:
                return f"{size_bytes:.2f} {unit}"
            size_bytes /= 1024.0
        return f"{size_bytes:.2f} TB"

    def display_documents(self, documents: list, title: str = "Documentos"):
        """Exibe uma lista de documentos formatada"""
        if not documents:
            print(f"\n{Fore.YELLOW}Nenhum documento encontrado.{Style.RESET_ALL}")
            return

        print(f"\n{Fore.CYAN}{'=' * 80}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}{title} ({len(documents)} documento(s)){Style.RESET_ALL}")
        print(f"{Fore.CYAN}{'=' * 80}{Style.RESET_ALL}")

        for i, doc in enumerate(documents, 1):
            year_str = f"{doc['year']}" if doc['year'] else "N/A"
            size_str = self.format_file_size(doc['size'])

            print(f"\n{Fore.GREEN}{i}.{Style.RESET_ALL} {Fore.WHITE}{doc['title']}{Style.RESET_ALL}")
            print(f"   📄 Arquivo: {doc['filename']}")
            print(f"   📁 Tipo: {doc['type']}")
            print(f"   👤 Autor: {doc['author']}")
            print(f"   📅 Ano: {year_str}")
            print(f"   💾 Tamanho: {size_str}")

        print(f"\n{Fore.CYAN}{'=' * 80}{Style.RESET_ALL}")

    def add_document_interactive(self):
        """Interface interativa para adicionar documento"""
        print(f"\n{Fore.YELLOW}═══ ADICIONAR NOVO DOCUMENTO ═══{Style.RESET_ALL}\n")

        # Tipo do documento
        print(f"{Fore.CYAN}Tipos disponíveis:{Style.RESET_ALL}")
        print(f"  1. Artigos")
        print(f"  2. Teses")
        print(f"  3. Livros")

        type_choice = input(f"\n{Fore.GREEN}Escolha o tipo (1-3): {Style.RESET_ALL}").strip()

        type_map = {'1': 'artigos', '2': 'teses', '3': 'livros'}
        if type_choice not in type_map:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
            return

        doc_type = type_map[type_choice]

        # Caminho do arquivo
        file_path = input(f"{Fore.GREEN}Caminho completo do arquivo: {Style.RESET_ALL}").strip()

        if not file_path:
            print(f"{Fore.RED}Caminho não pode ser vazio!{Style.RESET_ALL}")
            return

        # Metadados opcionais
        title = input(f"{Fore.GREEN}Título (Enter para usar nome do arquivo): {Style.RESET_ALL}").strip()
        author = input(f"{Fore.GREEN}Autor: {Style.RESET_ALL}").strip()
        year_str = input(f"{Fore.GREEN}Ano de publicação (Enter para extrair do nome): {Style.RESET_ALL}").strip()

        year = None
        if year_str:
            try:
                year = int(year_str)
            except ValueError:
                print(f"{Fore.YELLOW}Ano inválido, será extraído do nome do arquivo.{Style.RESET_ALL}")

        # Adiciona o documento
        try:
            self.manager.add_document(
                file_path=file_path,
                doc_type=doc_type,
                year=year,
                author=author,
                title=title
            )
            print(f"\n{Fore.GREEN}✓ Documento adicionado com sucesso!{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}✗ Erro ao adicionar documento: {e}{Style.RESET_ALL}")

    def remove_document_interactive(self):
        """Interface interativa para remover documento"""
        print(f"\n{Fore.YELLOW}═══ REMOVER DOCUMENTO ═══{Style.RESET_ALL}\n")

        # Tipo do documento
        print(f"{Fore.CYAN}Tipos disponíveis:{Style.RESET_ALL}")
        print(f"  1. Artigos")
        print(f"  2. Teses")
        print(f"  3. Livros")

        type_choice = input(f"\n{Fore.GREEN}Escolha o tipo (1-3): {Style.RESET_ALL}").strip()

        type_map = {'1': 'artigos', '2': 'teses', '3': 'livros'}
        if type_choice not in type_map:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
            return

        doc_type = type_map[type_choice]

        # Lista documentos desse tipo
        docs = self.manager.list_documents(doc_type=doc_type)
        if not docs:
            print(f"\n{Fore.YELLOW}Nenhum documento deste tipo encontrado.{Style.RESET_ALL}")
            return

        self.display_documents(docs, f"Documentos - {doc_type.capitalize()}")

        # Nome do arquivo
        filename = input(f"\n{Fore.GREEN}Nome do arquivo a remover: {Style.RESET_ALL}").strip()

        if not filename:
            print(f"{Fore.RED}Nome não pode ser vazio!{Style.RESET_ALL}")
            return

        # Confirmação
        confirm = input(f"{Fore.YELLOW}Tem certeza que deseja remover '{filename}'? (s/n): {Style.RESET_ALL}").strip().lower()

        if confirm != 's':
            print(f"{Fore.YELLOW}Operação cancelada.{Style.RESET_ALL}")
            return

        # Remove o documento
        try:
            self.manager.remove_document(filename, doc_type)
            print(f"\n{Fore.GREEN}✓ Documento removido com sucesso!{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}✗ Erro ao remover documento: {e}{Style.RESET_ALL}")

    def rename_document_interactive(self):
        """Interface interativa para renomear documento"""
        print(f"\n{Fore.YELLOW}═══ RENOMEAR DOCUMENTO ═══{Style.RESET_ALL}\n")

        # Tipo do documento
        print(f"{Fore.CYAN}Tipos disponíveis:{Style.RESET_ALL}")
        print(f"  1. Artigos")
        print(f"  2. Teses")
        print(f"  3. Livros")

        type_choice = input(f"\n{Fore.GREEN}Escolha o tipo (1-3): {Style.RESET_ALL}").strip()

        type_map = {'1': 'artigos', '2': 'teses', '3': 'livros'}
        if type_choice not in type_map:
            print(f"{Fore.RED}Opção inválida!{Style.RESET_ALL}")
            return

        doc_type = type_map[type_choice]

        # Lista documentos desse tipo
        docs = self.manager.list_documents(doc_type=doc_type)
        if not docs:
            print(f"\n{Fore.YELLOW}Nenhum documento deste tipo encontrado.{Style.RESET_ALL}")
            return

        self.display_documents(docs, f"Documentos - {doc_type.capitalize()}")

        # Nome do arquivo
        old_name = input(f"\n{Fore.GREEN}Nome atual do arquivo: {Style.RESET_ALL}").strip()
        new_name = input(f"{Fore.GREEN}Novo nome do arquivo: {Style.RESET_ALL}").strip()

        if not old_name or not new_name:
            print(f"{Fore.RED}Nomes não podem ser vazios!{Style.RESET_ALL}")
            return

        # Renomeia o documento
        try:
            self.manager.rename_document(old_name, new_name, doc_type)
            print(f"\n{Fore.GREEN}✓ Documento renomeado com sucesso!{Style.RESET_ALL}")
        except Exception as e:
            print(f"\n{Fore.RED}✗ Erro ao renomear documento: {e}{Style.RESET_ALL}")

    def list_all_documents(self):
        """Lista todos os documentos"""
        docs = self.manager.list_documents()
        self.display_documents(docs, "Todos os Documentos")

    def list_by_type(self):
        """Lista documentos organizados por tipo"""
        print(f"\n{Fore.YELLOW}═══ DOCUMENTOS POR TIPO ═══{Style.RESET_ALL}\n")

        docs_by_type = self.manager.list_by_type()

        for doc_type, docs in docs_by_type.items():
            self.display_documents(docs, f"{doc_type.capitalize()}")
            print()

    def list_by_year(self):
        """Lista documentos organizados por ano"""
        print(f"\n{Fore.YELLOW}═══ DOCUMENTOS POR ANO ═══{Style.RESET_ALL}\n")

        docs_by_year = self.manager.list_by_year()

        for year, docs in docs_by_year.items():
            year_str = str(year) if isinstance(year, int) else year
            self.display_documents(docs, f"Ano {year_str}")
            print()

    def search_documents_interactive(self):
        """Interface interativa para buscar documentos"""
        print(f"\n{Fore.YELLOW}═══ BUSCAR DOCUMENTOS ═══{Style.RESET_ALL}\n")

        query = input(f"{Fore.GREEN}Digite o termo de busca: {Style.RESET_ALL}").strip()

        if not query:
            print(f"{Fore.RED}Termo de busca não pode ser vazio!{Style.RESET_ALL}")
            return

        results = self.manager.search_documents(query)
        self.display_documents(results, f"Resultados da busca: '{query}'")

    def show_statistics(self):
        """Exibe estatísticas da biblioteca"""
        print(f"\n{Fore.YELLOW}═══ ESTATÍSTICAS DA BIBLIOTECA ═══{Style.RESET_ALL}\n")

        stats = self.manager.get_statistics()

        print(f"{Fore.CYAN}📊 Estatísticas Gerais:{Style.RESET_ALL}")
        print(f"   Total de documentos: {Fore.GREEN}{stats['total_documents']}{Style.RESET_ALL}")
        print(f"   Tamanho total: {Fore.GREEN}{stats['total_size_mb']} MB{Style.RESET_ALL}")

        if stats['oldest_year'] and stats['newest_year']:
            print(f"   Período: {Fore.GREEN}{stats['oldest_year']} - {stats['newest_year']}{Style.RESET_ALL}")

        print(f"\n{Fore.CYAN}📁 Por Tipo de Documento:{Style.RESET_ALL}")
        for doc_type, count in stats['by_type'].items():
            print(f"   {doc_type.capitalize()}: {Fore.GREEN}{count}{Style.RESET_ALL}")

        if stats['by_year']:
            print(f"\n{Fore.CYAN}📅 Por Ano:{Style.RESET_ALL}")
            # Mostra os 10 anos com mais documentos
            sorted_years = sorted(stats['by_year'].items(), key=lambda x: x[1], reverse=True)[:10]
            for year, count in sorted_years:
                print(f"   {year}: {Fore.GREEN}{count}{Style.RESET_ALL}")

        print()

    def show_help(self):
        """Exibe ajuda sobre o sistema"""
        help_text = f"""
{Fore.YELLOW}═══ AJUDA DO SISTEMA ═══{Style.RESET_ALL}

{Fore.CYAN}Formatos suportados:{Style.RESET_ALL}
  • Artigos: PDF, DOC, DOCX, TXT
  • Teses: PDF, DOC, DOCX
  • Livros: PDF, EPUB, MOBI, AZW3

{Fore.CYAN}Dicas:{Style.RESET_ALL}
  • O sistema tenta extrair automaticamente o ano do nome do arquivo
  • Use nomes descritivos para facilitar a busca
  • O sistema mantém backup automático dos metadados
  • Você pode buscar por título, autor ou nome do arquivo

{Fore.CYAN}Convenções de nomenclatura recomendadas:{Style.RESET_ALL}
  • Artigos: Autor_Título_Ano.pdf
  • Teses: Título_Ano_Universidade.pdf
  • Livros: Título_Autor_Ano.pdf

{Fore.CYAN}Para mais informações:{Style.RESET_ALL}
  • Consulte a documentação completa no repositório GitHub
  • Entre em contato com o suporte técnico da biblioteca
        """
        print(help_text)

    def run(self):
        """Executa o loop principal da CLI"""
        while True:
            self.print_banner()
            self.print_menu()

            choice = input(f"{Fore.GREEN}Digite sua opção: {Style.RESET_ALL}").strip()

            if choice == '1':
                self.add_document_interactive()
            elif choice == '2':
                self.remove_document_interactive()
            elif choice == '3':
                self.rename_document_interactive()
            elif choice == '4':
                self.list_all_documents()
            elif choice == '5':
                self.list_by_type()
            elif choice == '6':
                self.list_by_year()
            elif choice == '7':
                self.search_documents_interactive()
            elif choice == '8':
                self.show_statistics()
            elif choice == '9':
                self.show_help()
            elif choice == '0':
                print(f"\n{Fore.YELLOW}Obrigado por usar o Sistema de Biblioteca Digital!{Style.RESET_ALL}")
                print(f"{Fore.GREEN}Até logo! 👋{Style.RESET_ALL}\n")
                sys.exit(0)
            else:
                print(f"\n{Fore.RED}Opção inválida! Tente novamente.{Style.RESET_ALL}")

            input(f"\n{Fore.CYAN}Pressione Enter para continuar...{Style.RESET_ALL}")
            # Limpa a tela (funciona em Unix e Windows)
            os.system('cls' if os.name == 'nt' else 'clear')


def main():
    """Função principal"""
    try:
        cli = LibraryCLI()
        cli.run()
    except KeyboardInterrupt:
        print(f"\n\n{Fore.YELLOW}Programa interrompido pelo usuário.{Style.RESET_ALL}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Fore.RED}Erro fatal: {e}{Style.RESET_ALL}")
        sys.exit(1)


if __name__ == "__main__":
    main()
