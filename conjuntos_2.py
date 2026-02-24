conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b)) #serve para juntar os conjuntos

#----------------------------------------------------#

conjunto_1 = {1, 2, 3}
conjunto_2 = {2, 3, 4} 
print(conjunto_1.intersection(conjunto_2)) #serve para ver quais são os elementos iguais entre os conjuntos
print(conjunto_1.difference(conjunto_2)) #mostra oque tem no conjunto 1 mas não no 2
print(conjunto_2.difference(conjunto_1)) #mostra oque tem no conjunto 2 mas não no 1
print(conjunto_1.symmetric_difference(conjunto_2)) #mostra oque tem de diferente no conjunto 1 e 2(como se fosse a junção do exemplo acima)

#----------------------------------------------------#

sorteio = {1, 23}
sorteio.add(30) #adiciona um número ao conjunto
print(sorteio)
sorteio.clear() #limpa o conjunto
print(sorteio)

#----------------------------------------------------#

numeros = {1, 2, 3, 4, 5, 6, 7, 8}
print(numeros)
numeros.discard(2) #descarta o número selecionado, se você passa um valor que não existe o código não da erro
print(numeros)
numeros.pop() #vai tirando os valores do conjunto e imprime o valor que tirou 
print(numeros)
numeros.remove(4) #descarta o número selecionado, diferente o "discard" se você passa um valor que não existe o código da erro
print(numeros)
print(7 in numeros) #vai retornar "True" porque ele está
print(len(numeros)) #mostra quantos elementos tem no conjunto