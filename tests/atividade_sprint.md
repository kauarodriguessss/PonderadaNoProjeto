# Atividade Ponderada – Consolidação da Sprint
**Tema:** Regras de negócio em código + Verificação de qualidade
**Projeto:** API ASIS – Processamento de SPED

---

# 1. Objetivo da Atividade

Transformar direcionadores de negócio em:

- Regras de negócio documentadas em código
- Estratégia estruturada de testes
- Verificação objetiva da qualidade dos requisitos

A entrega cobre:

- ✅ Mapa de Business Drivers
- ✅ Estratégia e massa de testes
- ✅ Codificação como documentação executável

---

# 2. Mapa de Business Drivers (DN)

| Código | Direcionador de Negócio | Descrição | Métrica associada |
|--------|-------------------------|------------|-------------------|
| DN1 | Confiabilidade fiscal | Garantir processamento correto de arquivos SPED | ≥ 95% sucesso |
| DN2 | Escalabilidade operacional | Processamento assíncrono e tolerante a arquivos grandes | SLA ≤ 8s |
| DN3 | Disponibilidade do serviço | API estável sob carga | ≥ 97% uptime |
| DN5 | Rastreabilidade | Processo auditável ponta a ponta | ≥ 95% logs correlacionados |
| DN6 | Performance | Tempo de resposta aceitável | P90 ≤ 12s |

---

# 3. Direcionadores Escolhidos para Implementação

## Direcionador 1 – Confiabilidade no Upload de SPED (RF1 + RNF2)

Relacionados a:
- Validação de arquivo
- Retorno estruturado
- Segurança no tráfego

## Direcionador 2 – Rastreabilidade do Processo (RF2 + RNF3)

Relacionados a:
- Consulta consistente
- Integridade do status
- Correlação processo → resultado → auditoria

---

# 4. Regras de Negócio Documentadas em Código

## 4.1 RF1 – Upload de Arquivo SPED

```python
# RF1 – Upload SPED
# DN1, DN2, DN3

def upload_sped(file, account_key, app_key):
    """
    RF1: A API deve aceitar arquivo SPED válido
    DN1: Garantir confiabilidade fiscal
    DN2: Processamento assíncrono
    RNF2: Confidencialidade (credenciais obrigatórias)
    """

    if not account_key or not app_key:
        return {"status": 401, "error": "Credenciais inválidas"}

    if not file.endswith(".txt"):
        return {"status": 400, "error": "Formato inválido"}

    processo_id = gerar_processo_id()

    enfileirar_processamento(processo_id, file)

    return {
        "status": 202,
        "processoId": processo_id
    }
```

---

## 4.2 RF2 – Consulta de Status

```python
# RF2 – Consulta de Status
# DN1, DN5

def consultar_processo(processo_id):
    """
    RF2: Consultar status do processamento
    DN5: Rastreabilidade ponta a ponta
    """

    processo = buscar_processo(processo_id)

    if not processo:
        return {"status": 404, "error": "Processo não encontrado"}

    return {
        "status": 200,
        "processo": processo
    }
```

---

# 5. Estratégia e Massa de Testes

## 5.1 Estratégia de Teste

### Tipos de teste aplicados:

* Testes unitários
* Testes de contrato
* Testes de exceção
* Testes de borda
* Testes de carga simulada

---

## 5.2 Massa de Teste

| Caso | Arquivo                 | Credenciais | Resultado Esperado |
| ---- | ----------------------- | ----------- | ------------------ |
| T1   | SPED válido             | Válidas     | 202                |
| T2   | SPED inválido           | Válidas     | 400                |
| T3   | SPED válido             | Ausentes    | 401                |
| T4   | Processo inexistente    | —           | 404                |
| T5   | Arquivo grande (limite) | Válidas     | 202                |

---

# 6. Codificação como Documentação de Testes

## 6.1 Testes do RF1

```python
def test_upload_valido():
    response = upload_sped("arquivo_sped.txt", "acc123", "app456")
    assert response["status"] == 202


def test_upload_formato_invalido():
    response = upload_sped("arquivo.pdf", "acc123", "app456")
    assert response["status"] == 400


def test_upload_sem_credenciais():
    response = upload_sped("arquivo_sped.txt", None, None)
    assert response["status"] == 401
```

---

## 6.2 Testes do RF2

```python
def test_consulta_sucesso():
    processo_id = gerar_processo_id()
    registrar_processo_mock(processo_id)

    response = consultar_processo(processo_id)
    assert response["status"] == 200


def test_consulta_inexistente():
    response = consultar_processo("id_invalido")
    assert response["status"] == 404
```

---

# 7. Verificação de Qualidade dos Requisitos

## 7.1 Critérios Avaliados

| Critério             | RF1 | RF2 |
| -------------------- | --- | --- |
| Clareza              | ✔   | ✔   |
| Testabilidade        | ✔   | ✔   |
| Mensurabilidade      | ✔   | ✔   |
| Rastreabilidade      | ✔   | ✔   |
| Cobertura de exceção | ✔   | ✔   |

---

## 7.2 Métricas Simuladas

* 95%+ respostas válidas em SLA
* 98% autenticações corretas via HTTPS
* 100% dos processos possuem `processoId`
* Logs correlacionados com `processoId`

---

# 8. Conclusão

A atividade demonstra:

* Tradução direta de direcionadores de negócio em código executável
* Testes como documentação viva dos requisitos
* Rastreabilidade completa entre:

  * DN → RF/RNF → Código → Testes → Métricas

A estrutura garante alinhamento entre estratégia de negócio, implementação técnica e qualidade mensurável.

---

# 9. Estrutura Entregável

```
/docs
  atividade_sprint.md
/src
  sped_upload.py
  sped_consulta.py
/tests
  test_upload.py
  test_consulta.py
```

---

**Entrega Finalizada.**
