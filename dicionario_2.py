contatos = { 
    "rodrigo@gmail.com": {"nome": "Rodrigo", "idade": 20, "telefone": "3241_6578"},
    "ricardo@gmail.com": {"nome": "Ricardo", "idade": 23, "telefone": "1432-5876"},
    "barbara@gmail.com": {"nome": "Barbara", "idade": 20, "telefone": "1324-7568"}
} #cria um dicionario aninhado

print(contatos)
print(contatos.clear()) #limpa o dicionario

#----------------------------------------------------#
contatos = { 
    "rodrigo@gmail.com": {"nome": "Rodrigo", "idade": 20, "telefone": "3241_6578"},
    "ricardo@gmail.com": {"nome": "Ricardo", "idade": 23, "telefone": "1432-5876"},
    "barbara@gmail.com": {"nome": "Barbara", "idade": 20, "telefone": "1324-7568"}
} #cria um dicionario aninhado

dados = {"rodrigo@gmail.com": {"nome": "Rodrigo", "idade": 20, "telefone": "3241_6578"}}

copia = dados.copy() #copia o dicionario dados
print(copia)

date = dict.fromkeys(["nome", "telefone"]) #cria as chaves do dicionario sem valor
print(date)
date = dict.fromkeys(["nome", "telefone",], "vazio") #cria ou modifica as chaves do dicionario sem valor e denominando os valores com vazio
print(date)

resultado = contatos.get("rodrigo@gmail.com", {}) #retorna o valor da chave indicada
print(resultado)

chaves = contatos.keys() #retorna as chaves do dicionario
print(chaves)

remover = contatos.pop("ricardo@gmail.com") #remove a chave selecionada
print(remover)
remover = contatos.pop("ricardo@gmail.com", "não encontrou") #remove a chave selecionada e retorna o valor "nao encontrou caso a chave não exista"
print(remover)

contatos.popitem() #remove os itens na sequencia

#----------------------------------------------------#

dados = {"rodrigo@gmail.com": {"nome": "Rodrigo", "idade": 20, "telefone": "3241_6578"}}

dados.setdefault("país", "Brasil") #adiciona uma chave com um valor, se a chave ja exister com outro valor ela não é alterada e retorna ele
print(dados)

dados.update({"rodrigo@gmail.com": {"nome": "Rodrigo"}}) #atualiza os dados do dicionario 
print(dados)

print(contatos.values()) #retorna as chaves e os valores do dicionario

possui = "rodrigo@gmail.com" in dados #verifica se possui o determinado item no dicionario  
print(possui)

#----------------------------------------------------#

contatos = { 
    "rodrigo@gmail.com": {"nome": "Rodrigo", "idade": 20, "telefone": "3241_6578"},
    "ricardo@gmail.com": {"nome": "Ricardo", "idade": 23, "telefone": "1432-5876"},
    "barbara@gmail.com": {"nome": "Barbara", "idade": 20, "telefone": "1324-7568"}
} #cria um dicionario aninhado

del contatos["rodrigo@gmail.com"]["telefone"] #remove o item determinado do dicionario
print(contatos)
del contatos["ricardo@gmail.com"]#remove o item determinado do dicionario
print(contatos)