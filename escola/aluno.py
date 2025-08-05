def calcular_media(numeros:list[float]) -> float:

    #   Verificando se é uma lista
    if not isinstance(numeros, list[float]):

        raise ValueError("the data provided is not a list")

    #   Verificando se a lista esta vazia
    if not numeros:

        raise ValueError("it is not allowed to send an empty list")
    
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade

    return round(media, 1)
