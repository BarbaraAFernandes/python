from codes_complete.Alura.leilao.dominio import Usuario, Leilao

import pytest

from codes_complete.Alura.leilao.exceções import LanceInvalido


@pytest.fixture
def vini():
    return Usuario('Vini', 100)


@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_valor_da_carteira_quando_este_propoe_um_lance(vini, leilao):
    vini.propoe_lance(leilao, 50)

    assert vini.carteira == 50


def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 1.0)

    assert vini.carteira == 99.0


def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(vini, leilao):
    vini.propoe_lance(leilao, 100.0)

    assert vini.carteira == 0.00


def test_onde_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(vini, leilao):
    with pytest.raises(LanceInvalido):
        vini.propoe_lance(leilao, 150.0)

