#   Importações
import pytest
from escola.aluno import calcular_media

def test_calcular_media_lita_vazia():

    #   Definindo entrada
    entrada = []

    #   Executando a função e esperando erro
    with pytest.raises(ValueError, match="it is not allowed to send an empty list"):
        calcular_media(entrada)


def test_calcular_media_com_string_ao_invez_de_lista_numerica():
    entrada2 = "ola"

    with pytest.raises(TypeError, match="invalid note: texts are not allowed"):
        calcular_media(entrada2)


def test_calcular_media_com_string_e_numero_na_lista():
    entrada3 = ["ola", 3.0]

    with pytest.raises(TypeError, match="invalid note: texts are not allowed"):
        calcular_media(entrada3)


def test_calcular_media_com_numero_negativo_na_lista():
    entrada4 = [-10.0]

    with pytest.raises(ValueError, match="grades can be from 0 to 10"):
        calcular_media(entrada4)

def test_calcular_media_com_numero_maior_que_10_na_lista():
    entrada5 = [-10.0]

    with pytest.raises(ValueError, match="grades can be from 0 to 10"):
        calcular_media(entrada5)