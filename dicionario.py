pessoa = {"nome": "Rodrigo", "idade": 20} #cria o dicionario
print(pessoa)

pessoa["telefone"] = "1234-5678" #adiciona uma nova chave ao dicionario
print(pessoa)

print(pessoa["nome"]) #acessa um valor especifico

pessoa["nome"] = "Ricardo"  #altera o valor de uma chave ja existente
pessoa["idade"] = 23  #altera o valor de uma chave ja existente
pessoa["telefone"] = "5678-1234"  #altera o valor de uma chave ja existente
print(pessoa)

contatos = { 
    "rodrigo@gmail.com": {"nome": "Rodrigo", "idade": 20, "telefone": "3241_6578"},
    "ricardo@gmail.com": {"nome": "Ricardo", "idade": 23, "telefone": "1432-5876"},
    "barbara@gmail.com": {"nome": "Barbara", "idade": 20, "telefone": "1324-7568"}
} #cria um dicionario aninhado

for chave, valor in contatos.items():
    print(chave, valor)

print(contatos["rodrigo@gmail.com"]["telefone"]) #faz uma consulta especifica no dicionario 