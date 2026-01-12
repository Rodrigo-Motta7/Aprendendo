vogais = ['a', 'e', 'i', 'o', 'u']
vogais.clear() #limpa a lista, remove todos os elementos
print(vogais) #exibe []
nums = [10, 5, 12, 7, 3, 15]
nums.reverse() #inverte a ordem, a posição, dos elementos
print(nums) #exibe [15, 3, 7, 12, 5, 10]
nums.sort() #ordena lista de forma crescente
print(nums) #exibe [3, 5, 7, 10, 12, 15] 

lista = [11, 22, 33, 44, 55] #índices 0, 1, 2, 3, 4
print(lista) #exibe [11, 22, 33, 44, 55]
print(lista[1:4]) #exibe elementos do índice 1 (incluso) até índice 4 (excluso), ou seja, [22, 33, 44]