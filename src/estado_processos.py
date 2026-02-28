"""
Registro em memória de processos SPED.
Compartilhado por sped_upload (enfileirar) e sped_consulta (buscar).
DN5: Rastreabilidade – processo auditável ponta a ponta.
"""

from typing import Any, Dict, Optional

# Registro em memória: processo_id -> dados do processo
_registro: Dict[str, Dict[str, Any]] = {}


def registrar(processo_id: str, arquivo: str, status: str = "pendente") -> None:
    """Registra um processo no repositório em memória."""
    _registro[processo_id] = {
        "processoId": processo_id,
        "arquivo": arquivo,
        "status": status,
    }


def buscar(processo_id: str) -> Optional[Dict[str, Any]]:
    """Retorna os dados do processo ou None se não existir."""
    return _registro.get(processo_id)


def limpar() -> None:
    """Remove todos os processos. Útil para testes."""
    _registro.clear()
