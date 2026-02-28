"""
RF1 – Upload de Arquivo SPED
DN1: Confiabilidade fiscal
DN2: Processamento assíncrono
DN3: Disponibilidade do serviço
RNF2: Confidencialidade (credenciais obrigatórias)
"""

import uuid

from .estado_processos import registrar as _registrar_processo


def gerar_processo_id() -> str:
    """Gera um identificador único para o processo (rastreabilidade DN5)."""
    return str(uuid.uuid4())


def enfileirar_processamento(processo_id: str, file: str) -> None:
    """
    Registra o processo para processamento assíncrono (DN2).
    Usa registro em memória compartilhado com o módulo de consulta.
    """
    _registrar_processo(processo_id, file, status="pendente")


def upload_sped(file: str, account_key: str, app_key: str) -> dict:
    """
    RF1: A API deve aceitar arquivo SPED válido.
    DN1: Garantir confiabilidade fiscal.
    DN2: Processamento assíncrono.
    RNF2: Confidencialidade (credenciais obrigatórias).

    Args:
        file: Nome ou caminho do arquivo (deve terminar em .txt).
        account_key: Chave da conta (obrigatória).
        app_key: Chave da aplicação (obrigatória).

    Returns:
        dict com status e processoId (202) ou status e error (400/401).
    """
    if not account_key or not app_key:
        return {"status": 401, "error": "Credenciais inválidas"}

    if not file.endswith(".txt"):
        return {"status": 400, "error": "Formato inválido"}

    processo_id = gerar_processo_id()
    enfileirar_processamento(processo_id, file)

    return {
        "status": 202,
        "processoId": processo_id,
    }
