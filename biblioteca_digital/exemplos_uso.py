#!/usr/bin/env python3
"""
Exemplos de Uso da API do Sistema de Biblioteca Digital
Este arquivo demonstra como usar o sistema programaticamente
"""

import sys
from pathlib import Path

# Adiciona o diretório src ao path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from document_manager import DocumentManager


def exemplo_basico():
    """Exemplo básico de uso do DocumentManager"""
    print("=" * 60)
    print("EXEMPLO 1: Uso Básico do DocumentManager")
    print("=" * 60)

    # Inicializa o gerenciador
    manager = DocumentManager("data")

    # Obtém estatísticas
    stats = manager.get_statistics()
    print(f"\nTotal de documentos: {stats['total_documents']}")
    print(f"Tamanho total: {stats['total_size_mb']} MB")

    # Lista documentos por tipo
    print("\nDocumentos por tipo:")
    docs_by_type = manager.list_by_type()
    for doc_type, docs in docs_by_type.items():
        print(f"  {doc_type.capitalize()}: {len(docs)} documento(s)")


def exemplo_adicionar_documento():
    """Exemplo de como adicionar documento programaticamente"""
    print("\n" + "=" * 60)
    print("EXEMPLO 2: Adicionar Documento")
    print("=" * 60)

    manager = DocumentManager("data")

    # Cria um arquivo de teste
    test_file = Path("temp_test_doc_2023.pdf")
    test_file.write_text("Este é um documento de teste")

    try:
        # Adiciona o documento
        manager.add_document(
            file_path=str(test_file),
            doc_type='artigos',
            year=2023,
            author="João Silva",
            title="Introdução ao Python"
        )
        print("\n✓ Documento adicionado com sucesso!")

        # Lista documentos para confirmar
        docs = manager.list_documents(doc_type='artigos')
        print(f"Total de artigos: {len(docs)}")

    finally:
        # Remove arquivo temporário
        if test_file.exists():
            test_file.unlink()


def exemplo_busca():
    """Exemplo de busca de documentos"""
    print("\n" + "=" * 60)
    print("EXEMPLO 3: Buscar Documentos")
    print("=" * 60)

    manager = DocumentManager("data")

    # Busca por termo
    termo = "Python"
    resultados = manager.search_documents(termo)

    print(f"\nBuscando por: '{termo}'")
    print(f"Encontrados: {len(resultados)} documento(s)")

    for doc in resultados:
        print(f"\n  Título: {doc['title']}")
        print(f"  Autor: {doc['author']}")
        print(f"  Arquivo: {doc['filename']}")


def exemplo_organizacao_por_ano():
    """Exemplo de organização por ano"""
    print("\n" + "=" * 60)
    print("EXEMPLO 4: Organização por Ano")
    print("=" * 60)

    manager = DocumentManager("data")

    docs_by_year = manager.list_by_year()

    print("\nDocumentos organizados por ano:")
    for year, docs in list(docs_by_year.items())[:5]:  # Mostra apenas 5
        year_str = str(year) if isinstance(year, int) else year
        print(f"\n  {year_str}: {len(docs)} documento(s)")
        for doc in docs[:3]:  # Mostra até 3 documentos por ano
            print(f"    - {doc['title']}")


def exemplo_estatisticas_detalhadas():
    """Exemplo de estatísticas detalhadas"""
    print("\n" + "=" * 60)
    print("EXEMPLO 5: Estatísticas Detalhadas")
    print("=" * 60)

    manager = DocumentManager("data")
    stats = manager.get_statistics()

    print("\n📊 Estatísticas da Biblioteca:")
    print(f"\nTotal de documentos: {stats['total_documents']}")
    print(f"Tamanho total: {stats['total_size_mb']} MB")

    if stats['oldest_year'] and stats['newest_year']:
        print(f"Período: {stats['oldest_year']} - {stats['newest_year']}")

    print("\nDistribuição por tipo:")
    for doc_type, count in stats['by_type'].items():
        print(f"  {doc_type.capitalize()}: {count}")

    if stats['by_year']:
        print("\nTop 5 anos com mais documentos:")
        sorted_years = sorted(stats['by_year'].items(),
                            key=lambda x: x[1], reverse=True)[:5]
        for year, count in sorted_years:
            print(f"  {year}: {count} documento(s)")


def main():
    """Função principal que executa todos os exemplos"""
    print("\n🎓 EXEMPLOS DE USO - SISTEMA DE BIBLIOTECA DIGITAL\n")

    try:
        exemplo_basico()
        exemplo_busca()
        exemplo_organizacao_por_ano()
        exemplo_estatisticas_detalhadas()

        # exemplo_adicionar_documento()  # Descomente para testar adição

        print("\n" + "=" * 60)
        print("✓ Todos os exemplos executados com sucesso!")
        print("=" * 60 + "\n")

    except Exception as e:
        print(f"\n❌ Erro ao executar exemplos: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
