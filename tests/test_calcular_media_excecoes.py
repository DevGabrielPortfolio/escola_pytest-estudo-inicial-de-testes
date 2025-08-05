#   Importações
import pytest
from escola.aluno import calcular_media

def test_calcular_media_lita_vazia():

    #   Definindo entrada
    entrada = []

    #   Executando a função e esperando erro
    with pytest.raises(ValueError, match="it is not allowed to send an empty list"):
        calcular_media(entrada)