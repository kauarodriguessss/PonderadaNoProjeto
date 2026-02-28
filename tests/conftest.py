"""Configuração pytest: path e limpeza do registro em memória entre testes."""
import sys
from pathlib import Path

import pytest

# Garante que o pacote src seja importável a partir da raiz do projeto
raiz = Path(__file__).resolve().parent.parent
if str(raiz) not in sys.path:
    sys.path.insert(0, str(raiz))


@pytest.fixture(autouse=True)
def limpar_registro_processos():
    """Limpa o registro de processos antes de cada teste para evitar vazamento de estado."""
    from src.estado_processos import limpar
    limpar()
    yield
    limpar()
