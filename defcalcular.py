def calcular_media(*numeros):
    soma = sum(numeros)
    quantidade = len(numeros)
    media = soma / quantidade 
    return media

print("Média:", calcular_media(10,15,30,45))