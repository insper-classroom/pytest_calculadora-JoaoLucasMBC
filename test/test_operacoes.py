import pytest
import numpy as np
from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores

@pytest.mark.op_simples
@pytest.mark.positivos
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1, v2)


@pytest.mark.op_simples
def test_soma_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    assert -12 == soma(v1, v2)


@pytest.mark.op_simples
def test_soma_dois_valores_racionais():
    v1 = 5.63
    v2 = 7.124
    assert 12.754 == soma(v1, v2)


@pytest.mark.op_simples
@pytest.mark.positivos
def test_sub_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert -2 == sub(v1, v2)


@pytest.mark.op_simples
def test_sub_dois_valores_negativos():
    v1 = -5.0
    v2 = -7.0
    assert 2 == sub(v1, v2)


@pytest.mark.op_simples
def test_sub_dois_valores_racionais():
    v1 = 5.13
    v2 = 7
    assert -1.87 == sub(v1, v2)


@pytest.mark.positivos
def test_multiplicacao_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 35 == multiplicacao(v1, v2)


def test_multiplicacao_dois_valores_negativos():
    v1 = -5.0
    v2 = 7.0
    assert -35 == multiplicacao(v1, v2)


def test_multiplicacao_dois_valores_racionais():
    v1 = 5.123
    v2 = 7.456
    assert 38.197088 == multiplicacao(v1, v2)


@pytest.mark.positivos
def test_divisao_dois_valores_positivos():
    v1 = 21.0
    v2 = 7.0
    assert 3 == divisao(v1, v2)


def test_divisao_dois_valores_negativos():
    v1 = 21.0
    v2 = -7.0
    assert -3.0 == divisao(v1, v2)


def test_divisao_dois_valores_racionais():
    v1 = 21.12
    v2 = 3
    assert 7.04 == divisao(v1, v2)


@pytest.mark.positivos
def test_media_lista_valores_inteiros():
    v = [4, 7, 12, 9]
    assert 8 == media_lista_valores(v)


def test_media_lista_valores_negativos():
    v = [-4, 7, -12, 9]
    assert 0 == media_lista_valores(v)


# -=-=-=-=-=-=- EXERCÍCIO 1 =-=-=-=-=-=-=-=-

@pytest.mark.exercicio_1
def test_divisao_por_0():
    v1 = 5
    v2 = 0
    assert np.inf == divisao(v1, v2)


@pytest.mark.exercicio_1
def test_media_com_tipo_nao_numerico():
    v = [1, 2, 'soos', False, 3]
    assert 2 == media_lista_valores(v)


@pytest.mark.exercicio_1
def test_media_lista_vazia():
    v = []
    assert 0 == media_lista_valores(v)