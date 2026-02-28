"""
RF2 – Consulta de Status do Processamento
DN1: Confiabilidade fiscal
DN5: Rastreabilidade ponta a ponta
"""

from .estado_processos import buscar as _buscar_processo


def buscar_processo(processo_id: str):
    """
    Busca os dados do processo no registro compartilhado.
    DN5: Rastreabilidade – correlaciona processo com resultado.
    """
    return _buscar_processo(processo_id)


def consultar_processo(processo_id: str) -> dict:
    """
    RF2: Consultar status do processamento.
    DN5: Rastreabilidade ponta a ponta.

    Args:
        processo_id: Identificador do processo.

    Returns:
        dict com status 200 e processo, ou status 404 e error.
    """
    processo = buscar_processo(processo_id)

    if not processo:
        return {"status": 404, "error": "Processo não encontrado"}

    return {
        "status": 200,
        "processo": processo,
    }
