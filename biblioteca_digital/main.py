#!/usr/bin/env python3
"""
Sistema de Gerenciamento de Biblioteca Digital
Ponto de entrada principal do sistema
"""

import sys
from pathlib import Path

# Adiciona o diretório src ao path
sys.path.insert(0, str(Path(__file__).parent / 'src'))

from cli import main

if __name__ == "__main__":
    main()
