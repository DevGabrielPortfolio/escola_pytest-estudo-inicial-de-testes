# Importações
from escola.aluno import calcular_media
import pytest


@pytest.mark.parametrize("entrada, situacao_esperada",
                         [
                            ([0.0, 0.0, 0.0, 0.0], 0),                    # Cálculo com apenas notas 0
                            ([10.0, 10.0, 10.0, 10.0], 10),               # Cálculo com apenas notas 10
                            ([7.0], 7),                                   # Cálculo com apenas 1 nota
                            ([5.0, 8.8, 9.3, 5.1, 3.7, 8.0, 1.9], 6),     # Cálculo com 7 notas
                            ([5.8, 9.3], 7.6),                            # Testando o arredondamento decimal 0.55
                            ([0.8, 0.0, 0.0], 0.3),                       # Testando o arredondamento decimal maior que 0.56
                            ([5, 6, 10], 7)                               # Testando número inteiro
                         ])

def test_calcular_media_calculos_basicos_parametrizados(entrada, situacao_esperada):
    
    resultado = calcular_media(entrada)

    assert resultado == situacao_esperada