def calcular_media(numeros:list[float]) -> float:

    if not numeros:

        raise ValueError("it is not allowed to send an empty list")
    
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade

    return round(media, 1)
