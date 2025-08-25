pessoa = {"nome": "Rodrigo", "idade": 19, "cidade": "RJ"}
print(pessoa.keys())   # Imprime dict_keys(["nome", "idade", "cidade"])
print(pessoa.values())   # Imprime dict_values(["Rodrigo", 19, "RJ"])
print(pessoa.items())    # Imprime dict_items([("nome", "Rodrigo"), ("idade", 19), ("cidade", "RJ")])

pessoa.update({"ocupação": "Universitário"})
print(pessoa.values())    # Imprime {"nome": "Rodrigo", "idade": 19, "cidade": "RJ", "ocupação": "Universitário"}
