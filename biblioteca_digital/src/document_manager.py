"""
Módulo de gerenciamento de documentos digitais
Responsável por todas as operações de manipulação de arquivos
"""

import os
import shutil
import re
from pathlib import Path
from typing import List, Dict, Optional
from datetime import datetime
import json


class DocumentManager:
    """Gerencia documentos digitais da biblioteca"""

    SUPPORTED_FORMATS = {
        'artigos': ['.pdf', '.doc', '.docx', '.txt'],
        'teses': ['.pdf', '.doc', '.docx'],
        'livros': ['.pdf', '.epub', '.mobi', '.azw3']
    }

    def __init__(self, base_path: str = "data"):
        """
        Inicializa o gerenciador de documentos

        Args:
            base_path: Caminho base para armazenamento dos documentos
        """
        self.base_path = Path(base_path)
        self._ensure_directories()
        self.metadata_file = self.base_path / "metadata.json"
        self.metadata = self._load_metadata()

    def _ensure_directories(self):
        """Garante que os diretórios necessários existam"""
        for doc_type in self.SUPPORTED_FORMATS.keys():
            (self.base_path / doc_type).mkdir(parents=True, exist_ok=True)

    def _load_metadata(self) -> Dict:
        """Carrega metadados dos documentos"""
        if self.metadata_file.exists():
            try:
                with open(self.metadata_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except json.JSONDecodeError:
                return {}
        return {}

    def _save_metadata(self):
        """Salva metadados dos documentos"""
        with open(self.metadata_file, 'w', encoding='utf-8') as f:
            json.dump(self.metadata, f, indent=4, ensure_ascii=False)

    def _extract_year_from_filename(self, filename: str) -> Optional[int]:
        """
        Extrai o ano do nome do arquivo usando regex

        Args:
            filename: Nome do arquivo

        Returns:
            Ano encontrado ou None
        """
        # Procura por padrões de ano (1900-2099)
        year_patterns = [
            r'(\d{4})',  # Qualquer sequência de 4 dígitos
            r'_(\d{4})_',  # Ano entre underscores
            r'-(\d{4})-',  # Ano entre hífens
        ]

        for pattern in year_patterns:
            match = re.search(pattern, filename)
            if match:
                year = int(match.group(1))
                if 1900 <= year <= 2099:
                    return year
        return None

    def add_document(self, file_path: str, doc_type: str, year: Optional[int] = None,
                    author: str = "", title: str = "") -> bool:
        """
        Adiciona um novo documento à biblioteca

        Args:
            file_path: Caminho do arquivo a ser adicionado
            doc_type: Tipo do documento (artigos, teses, livros)
            year: Ano de publicação
            author: Autor do documento
            title: Título do documento

        Returns:
            True se adicionado com sucesso, False caso contrário
        """
        source = Path(file_path)

        # Validações
        if not source.exists():
            raise FileNotFoundError(f"Arquivo não encontrado: {file_path}")

        if doc_type not in self.SUPPORTED_FORMATS:
            raise ValueError(f"Tipo de documento inválido. Use: {list(self.SUPPORTED_FORMATS.keys())}")

        file_ext = source.suffix.lower()
        if file_ext not in self.SUPPORTED_FORMATS[doc_type]:
            raise ValueError(f"Formato {file_ext} não suportado para {doc_type}")

        # Se o ano não foi fornecido, tenta extrair do nome do arquivo
        if year is None:
            year = self._extract_year_from_filename(source.name)

        # Destino do arquivo
        dest_dir = self.base_path / doc_type
        dest_file = dest_dir / source.name

        # Verifica se já existe e renomeia se necessário
        counter = 1
        while dest_file.exists():
            name_without_ext = source.stem
            dest_file = dest_dir / f"{name_without_ext}_{counter}{file_ext}"
            counter += 1

        # Copia o arquivo
        shutil.copy2(source, dest_file)

        # Salva metadados
        self.metadata[str(dest_file.relative_to(self.base_path))] = {
            'type': doc_type,
            'year': year,
            'author': author,
            'title': title or source.stem,
            'added_date': datetime.now().isoformat(),
            'file_size': source.stat().st_size
        }
        self._save_metadata()

        return True

    def remove_document(self, filename: str, doc_type: str) -> bool:
        """
        Remove um documento da biblioteca

        Args:
            filename: Nome do arquivo
            doc_type: Tipo do documento

        Returns:
            True se removido com sucesso, False caso contrário
        """
        file_path = self.base_path / doc_type / filename

        if not file_path.exists():
            raise FileNotFoundError(f"Documento não encontrado: {filename}")

        # Remove o arquivo
        file_path.unlink()

        # Remove dos metadados
        rel_path = str(file_path.relative_to(self.base_path))
        if rel_path in self.metadata:
            del self.metadata[rel_path]
            self._save_metadata()

        return True

    def rename_document(self, old_name: str, new_name: str, doc_type: str) -> bool:
        """
        Renomeia um documento

        Args:
            old_name: Nome atual do arquivo
            new_name: Novo nome do arquivo
            doc_type: Tipo do documento

        Returns:
            True se renomeado com sucesso, False caso contrário
        """
        old_path = self.base_path / doc_type / old_name

        if not old_path.exists():
            raise FileNotFoundError(f"Documento não encontrado: {old_name}")

        # Garante que a extensão seja mantida
        if not new_name.endswith(old_path.suffix):
            new_name += old_path.suffix

        new_path = self.base_path / doc_type / new_name

        if new_path.exists():
            raise FileExistsError(f"Já existe um arquivo com o nome: {new_name}")

        # Renomeia o arquivo
        old_path.rename(new_path)

        # Atualiza metadados
        old_rel = str(old_path.relative_to(self.base_path))
        new_rel = str(new_path.relative_to(self.base_path))

        if old_rel in self.metadata:
            self.metadata[new_rel] = self.metadata.pop(old_rel)
            # Atualiza o título se necessário
            if self.metadata[new_rel]['title'] == old_path.stem:
                self.metadata[new_rel]['title'] = new_path.stem
            self._save_metadata()

        return True

    def list_documents(self, doc_type: Optional[str] = None,
                      year: Optional[int] = None) -> List[Dict]:
        """
        Lista documentos filtrados por tipo e/ou ano

        Args:
            doc_type: Tipo do documento (opcional)
            year: Ano de publicação (opcional)

        Returns:
            Lista de documentos com metadados
        """
        documents = []

        # Define quais tipos listar
        types_to_list = [doc_type] if doc_type else list(self.SUPPORTED_FORMATS.keys())

        for dtype in types_to_list:
            doc_dir = self.base_path / dtype
            if not doc_dir.exists():
                continue

            for file_path in doc_dir.iterdir():
                if file_path.is_file():
                    rel_path = str(file_path.relative_to(self.base_path))
                    metadata = self.metadata.get(rel_path, {})

                    # Filtra por ano se especificado
                    doc_year = metadata.get('year')
                    if year is not None and doc_year != year:
                        continue

                    documents.append({
                        'filename': file_path.name,
                        'type': dtype,
                        'year': doc_year,
                        'author': metadata.get('author', 'Desconhecido'),
                        'title': metadata.get('title', file_path.stem),
                        'size': file_path.stat().st_size,
                        'added_date': metadata.get('added_date', 'N/A')
                    })

        return documents

    def list_by_type(self) -> Dict[str, List[Dict]]:
        """
        Lista documentos organizados por tipo

        Returns:
            Dicionário com documentos organizados por tipo
        """
        result = {}
        for doc_type in self.SUPPORTED_FORMATS.keys():
            result[doc_type] = self.list_documents(doc_type=doc_type)
        return result

    def list_by_year(self) -> Dict[int, List[Dict]]:
        """
        Lista documentos organizados por ano

        Returns:
            Dicionário com documentos organizados por ano
        """
        all_docs = self.list_documents()
        result = {}

        for doc in all_docs:
            year = doc.get('year')
            if year:
                if year not in result:
                    result[year] = []
                result[year].append(doc)

        # Adiciona documentos sem ano
        docs_without_year = [d for d in all_docs if not d.get('year')]
        if docs_without_year:
            result['Sem ano'] = docs_without_year

        return dict(sorted(result.items(), reverse=True))

    def search_documents(self, query: str) -> List[Dict]:
        """
        Busca documentos por título, autor ou nome do arquivo

        Args:
            query: Termo de busca

        Returns:
            Lista de documentos encontrados
        """
        all_docs = self.list_documents()
        query_lower = query.lower()

        results = []
        for doc in all_docs:
            if (query_lower in doc['filename'].lower() or
                query_lower in doc['title'].lower() or
                query_lower in doc['author'].lower()):
                results.append(doc)

        return results

    def get_statistics(self) -> Dict:
        """
        Retorna estatísticas sobre a biblioteca

        Returns:
            Dicionário com estatísticas
        """
        all_docs = self.list_documents()

        stats = {
            'total_documents': len(all_docs),
            'by_type': {},
            'by_year': {},
            'total_size_bytes': 0,
            'oldest_year': None,
            'newest_year': None
        }

        years = []
        for doc in all_docs:
            # Por tipo
            doc_type = doc['type']
            stats['by_type'][doc_type] = stats['by_type'].get(doc_type, 0) + 1

            # Por ano
            year = doc.get('year')
            if year:
                years.append(year)
                stats['by_year'][year] = stats['by_year'].get(year, 0) + 1

            # Tamanho total
            stats['total_size_bytes'] += doc['size']

        if years:
            stats['oldest_year'] = min(years)
            stats['newest_year'] = max(years)

        # Converte bytes para MB
        stats['total_size_mb'] = round(stats['total_size_bytes'] / (1024 * 1024), 2)

        return stats
