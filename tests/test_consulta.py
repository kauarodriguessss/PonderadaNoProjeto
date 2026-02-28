"""
Testes RF2 – Consulta de Status (documentação executável).
T4 e consulta sucesso.
"""

from src.sped_consulta import consultar_processo
from src.sped_upload import upload_sped


def test_consulta_sucesso():
    """Registrar processo via upload e consultar → 200 e dados do processo."""
    # Registra um processo usando RF1
    resp_upload = upload_sped("arquivo_sped.txt", "acc123", "app456")
    assert resp_upload["status"] == 202
    processo_id = resp_upload["processoId"]

    response = consultar_processo(processo_id)
    assert response["status"] == 200
    assert "processo" in response
    processo = response["processo"]
    assert processo["processoId"] == processo_id
    assert processo.get("status") == "pendente"
    assert processo.get("arquivo") == "arquivo_sped.txt"


def test_consulta_inexistente():
    """T4: Processo inexistente → 404."""
    response = consultar_processo("id_invalido")
    assert response["status"] == 404
    assert "error" in response
    assert "não encontrado" in response["error"].lower()
