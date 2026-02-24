alimentos = set(("arroz", "ovo", "arroz", "feijão")) #set serve para criar ou modificar conjuntos para que não possuem itens duplicados, somente únicos.
print(alimentos)

letras = set("abacaxi") #aqui ele separa a palavra em letras sem as repetir.
print(letras)

#A ORDEM DO SET É ALEATÓRIA 

numeros = {1, 2, 3, 2} 
numeros = list(numeros)
print(numeros[0])