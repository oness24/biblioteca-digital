"""
Testes unitários para o módulo DocumentManager
"""

import unittest
import tempfile
import shutil
from pathlib import Path
import sys
import os

# Adiciona o diretório src ao path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from document_manager import DocumentManager


class TestDocumentManager(unittest.TestCase):
    """Testes para a classe DocumentManager"""

    def setUp(self):
        """Configura ambiente de teste antes de cada teste"""
        # Cria diretório temporário para testes
        self.test_dir = tempfile.mkdtemp()
        self.manager = DocumentManager(self.test_dir)

        # Cria arquivos de teste
        self.test_files = {}
        for ext in ['.pdf', '.epub', '.doc']:
            test_file = Path(self.test_dir) / f"test_file_2023{ext}"
            test_file.write_text("Conteúdo de teste")
            self.test_files[ext] = str(test_file)

    def tearDown(self):
        """Limpa ambiente de teste após cada teste"""
        shutil.rmtree(self.test_dir)

    def test_initialization(self):
        """Testa inicialização do DocumentManager"""
        self.assertIsInstance(self.manager, DocumentManager)
        self.assertTrue((Path(self.test_dir) / 'artigos').exists())
        self.assertTrue((Path(self.test_dir) / 'teses').exists())
        self.assertTrue((Path(self.test_dir) / 'livros').exists())

    def test_add_document_pdf_article(self):
        """Testa adição de artigo em PDF"""
        result = self.manager.add_document(
            self.test_files['.pdf'],
            'artigos',
            year=2023,
            author="Teste Autor",
            title="Artigo de Teste"
        )

        self.assertTrue(result)
        docs = self.manager.list_documents(doc_type='artigos')
        self.assertEqual(len(docs), 1)
        self.assertEqual(docs[0]['year'], 2023)
        self.assertEqual(docs[0]['author'], "Teste Autor")

    def test_add_document_epub_book(self):
        """Testa adição de livro em EPUB"""
        result = self.manager.add_document(
            self.test_files['.epub'],
            'livros',
            year=2023,
            author="Autor Livro",
            title="Livro de Teste"
        )

        self.assertTrue(result)
        docs = self.manager.list_documents(doc_type='livros')
        self.assertEqual(len(docs), 1)

    def test_add_document_invalid_type(self):
        """Testa adição com tipo inválido"""
        with self.assertRaises(ValueError):
            self.manager.add_document(
                self.test_files['.pdf'],
                'invalido',
                year=2023
            )

    def test_add_document_nonexistent_file(self):
        """Testa adição de arquivo inexistente"""
        with self.assertRaises(FileNotFoundError):
            self.manager.add_document(
                '/caminho/inexistente.pdf',
                'artigos',
                year=2023
            )

    def test_remove_document(self):
        """Testa remoção de documento"""
        # Adiciona documento
        self.manager.add_document(
            self.test_files['.pdf'],
            'artigos',
            year=2023
        )

        # Verifica que foi adicionado
        docs = self.manager.list_documents(doc_type='artigos')
        self.assertEqual(len(docs), 1)

        # Remove documento
        filename = docs[0]['filename']
        result = self.manager.remove_document(filename, 'artigos')

        self.assertTrue(result)

        # Verifica que foi removido
        docs = self.manager.list_documents(doc_type='artigos')
        self.assertEqual(len(docs), 0)

    def test_remove_nonexistent_document(self):
        """Testa remoção de documento inexistente"""
        with self.assertRaises(FileNotFoundError):
            self.manager.remove_document('inexistente.pdf', 'artigos')

    def test_rename_document(self):
        """Testa renomeação de documento"""
        # Adiciona documento
        self.manager.add_document(
            self.test_files['.pdf'],
            'artigos',
            year=2023,
            title="Título Original"
        )

        docs = self.manager.list_documents(doc_type='artigos')
        old_name = docs[0]['filename']

        # Renomeia
        new_name = "novo_nome.pdf"
        result = self.manager.rename_document(old_name, new_name, 'artigos')

        self.assertTrue(result)

        # Verifica novo nome
        docs = self.manager.list_documents(doc_type='artigos')
        self.assertEqual(docs[0]['filename'], new_name)

    def test_rename_nonexistent_document(self):
        """Testa renomeação de documento inexistente"""
        with self.assertRaises(FileNotFoundError):
            self.manager.rename_document('old.pdf', 'new.pdf', 'artigos')

    def test_list_documents_all(self):
        """Testa listagem de todos os documentos"""
        # Adiciona documentos de diferentes tipos
        self.manager.add_document(self.test_files['.pdf'], 'artigos', year=2023)
        self.manager.add_document(self.test_files['.epub'], 'livros', year=2022)

        docs = self.manager.list_documents()
        self.assertEqual(len(docs), 2)

    def test_list_documents_by_type(self):
        """Testa listagem por tipo"""
        self.manager.add_document(self.test_files['.pdf'], 'artigos', year=2023)
        self.manager.add_document(self.test_files['.epub'], 'livros', year=2022)

        artigos = self.manager.list_documents(doc_type='artigos')
        livros = self.manager.list_documents(doc_type='livros')

        self.assertEqual(len(artigos), 1)
        self.assertEqual(len(livros), 1)

    def test_list_documents_by_year(self):
        """Testa listagem por ano"""
        self.manager.add_document(self.test_files['.pdf'], 'artigos', year=2023)

        # Cria outro arquivo para ano diferente
        test_file_2022 = Path(self.test_dir) / "test_2022.pdf"
        test_file_2022.write_text("Teste")
        self.manager.add_document(str(test_file_2022), 'artigos', year=2022)

        docs_2023 = self.manager.list_documents(year=2023)
        docs_2022 = self.manager.list_documents(year=2022)

        self.assertEqual(len(docs_2023), 1)
        self.assertEqual(len(docs_2022), 1)

    def test_list_by_type_organization(self):
        """Testa organização por tipo"""
        self.manager.add_document(self.test_files['.pdf'], 'artigos', year=2023)
        self.manager.add_document(self.test_files['.epub'], 'livros', year=2022)

        by_type = self.manager.list_by_type()

        self.assertIn('artigos', by_type)
        self.assertIn('livros', by_type)
        self.assertIn('teses', by_type)
        self.assertEqual(len(by_type['artigos']), 1)
        self.assertEqual(len(by_type['livros']), 1)

    def test_list_by_year_organization(self):
        """Testa organização por ano"""
        self.manager.add_document(self.test_files['.pdf'], 'artigos', year=2023)

        test_file_2022 = Path(self.test_dir) / "test_2022.pdf"
        test_file_2022.write_text("Teste")
        self.manager.add_document(str(test_file_2022), 'artigos', year=2022)

        by_year = self.manager.list_by_year()

        self.assertIn(2023, by_year)
        self.assertIn(2022, by_year)
        self.assertEqual(len(by_year[2023]), 1)
        self.assertEqual(len(by_year[2022]), 1)

    def test_search_documents_by_title(self):
        """Testa busca por título"""
        self.manager.add_document(
            self.test_files['.pdf'],
            'artigos',
            year=2023,
            title="Python Programming"
        )

        results = self.manager.search_documents("Python")
        self.assertEqual(len(results), 1)
        self.assertIn("Python", results[0]['title'])

    def test_search_documents_by_author(self):
        """Testa busca por autor"""
        self.manager.add_document(
            self.test_files['.pdf'],
            'artigos',
            year=2023,
            author="João Silva"
        )

        results = self.manager.search_documents("Silva")
        self.assertEqual(len(results), 1)
        self.assertIn("Silva", results[0]['author'])

    def test_search_documents_no_results(self):
        """Testa busca sem resultados"""
        self.manager.add_document(
            self.test_files['.pdf'],
            'artigos',
            year=2023
        )

        results = self.manager.search_documents("inexistente")
        self.assertEqual(len(results), 0)

    def test_get_statistics_empty(self):
        """Testa estatísticas com biblioteca vazia"""
        stats = self.manager.get_statistics()

        self.assertEqual(stats['total_documents'], 0)
        self.assertEqual(stats['total_size_bytes'], 0)
        self.assertIsNone(stats['oldest_year'])
        self.assertIsNone(stats['newest_year'])

    def test_get_statistics_with_documents(self):
        """Testa estatísticas com documentos"""
        self.manager.add_document(self.test_files['.pdf'], 'artigos', year=2023)
        self.manager.add_document(self.test_files['.epub'], 'livros', year=2022)

        stats = self.manager.get_statistics()

        self.assertEqual(stats['total_documents'], 2)
        self.assertGreater(stats['total_size_bytes'], 0)
        self.assertEqual(stats['oldest_year'], 2022)
        self.assertEqual(stats['newest_year'], 2023)
        self.assertIn('artigos', stats['by_type'])
        self.assertIn('livros', stats['by_type'])

    def test_extract_year_from_filename(self):
        """Testa extração de ano do nome do arquivo"""
        # Testa vários padrões de nome
        test_cases = [
            ("documento_2023.pdf", 2023),
            ("artigo-2022-final.pdf", 2022),
            ("tese_2021_versao2.pdf", 2021),
            ("livro2020.pdf", 2020),
            ("sem_ano.pdf", None)
        ]

        for filename, expected_year in test_cases:
            year = self.manager._extract_year_from_filename(filename)
            self.assertEqual(year, expected_year)

    def test_duplicate_filename_handling(self):
        """Testa tratamento de nomes duplicados"""
        # Adiciona primeiro documento
        self.manager.add_document(
            self.test_files['.pdf'],
            'artigos',
            year=2023
        )

        # Adiciona documento com mesmo nome
        self.manager.add_document(
            self.test_files['.pdf'],
            'artigos',
            year=2023
        )

        # Deve haver 2 documentos com nomes diferentes
        docs = self.manager.list_documents(doc_type='artigos')
        self.assertEqual(len(docs), 2)
        self.assertNotEqual(docs[0]['filename'], docs[1]['filename'])

    def test_metadata_persistence(self):
        """Testa persistência de metadados"""
        # Adiciona documento
        self.manager.add_document(
            self.test_files['.pdf'],
            'artigos',
            year=2023,
            author="Autor Teste",
            title="Título Teste"
        )

        # Cria novo manager com mesmo diretório
        new_manager = DocumentManager(self.test_dir)

        # Verifica se metadados foram carregados
        docs = new_manager.list_documents()
        self.assertEqual(len(docs), 1)
        self.assertEqual(docs[0]['author'], "Autor Teste")
        self.assertEqual(docs[0]['title'], "Título Teste")


def run_tests():
    """Executa todos os testes"""
    # Cria suite de testes
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestDocumentManager)

    # Executa testes com verbosidade
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    # Retorna True se todos os testes passaram
    return result.wasSuccessful()


if __name__ == '__main__':
    success = run_tests()
    sys.exit(0 if success else 1)
