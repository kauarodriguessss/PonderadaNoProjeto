"""
Testes RF1 – Upload SPED (documentação executável).
T1, T2, T3, T5 da massa de teste.
"""

import pytest

from src.sped_upload import upload_sped


def test_upload_valido():
    """T1: SPED válido + credenciais válidas → 202 e processoId presente."""
    response = upload_sped("arquivo_sped.txt", "acc123", "app456")
    assert response["status"] == 202
    assert "processoId" in response
    assert len(response["processoId"]) > 0


def test_upload_formato_invalido():
    """T2: SPED inválido (não .txt) + credenciais válidas → 400."""
    response = upload_sped("arquivo.pdf", "acc123", "app456")
    assert response["status"] == 400
    assert "error" in response
    assert "Formato inválido" in response["error"]


def test_upload_sem_credenciais():
    """T3: SPED válido + credenciais ausentes → 401."""
    response = upload_sped("arquivo_sped.txt", None, None)
    assert response["status"] == 401
    assert "error" in response
    assert "Credenciais" in response["error"]


def test_upload_sem_credenciais_vazias():
    """T3 (borda): credenciais vazias → 401."""
    response = upload_sped("arquivo_sped.txt", "", "")
    assert response["status"] == 401


def test_upload_arquivo_grande_limite():
    """T5: Arquivo no limite (nome longo .txt) + credenciais válidas → 202."""
    nome_grande = "sped_" + "x" * 200 + ".txt"
    response = upload_sped(nome_grande, "acc123", "app456")
    assert response["status"] == 202
    assert "processoId" in response
