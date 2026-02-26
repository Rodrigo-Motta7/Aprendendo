def criar_carro(modelo, ano, placa, /, marca, *, motor, combustivel): #oq vier antes da / so pode ser passado por posição, depois da barra e antes do * por posição ou chave e depois do * só por chave
    print(modelo ,"\n", ano,"\n", placa,"\n", marca,"\n", motor,"\n", combustivel)

criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina") #valido
#criar_carro(modelo="Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="gasolina") #invalido