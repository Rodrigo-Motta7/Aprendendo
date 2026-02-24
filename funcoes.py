def salvar_carro(marca, modelo, ano, placa): #cria a função
    print(f"Carro inserido com sucesso! Marca:{marca}, Modelo:{modelo}, Ano:{ano}, Placa:{placa}")

salvar_carro("Fiat", "Palio", 1999, "ABC-1234") #passa os valores da função, se a ordem do def for alterada vai ficar tudo fpra de posição
salvar_carro(**{"marca": "Fiat", "modelo" : "Palio", "ano" : 1999, "placa" : "ABC-1234"}) #passa os valores da função por um dicionario (os ** indicam que vai ser um dicionario)

print("")
#----------------------------------------------------#

def exibir_poema(data_extenso, *args, **kwargs):
    # data_extenso -> argumento obrigatório (a data do poema)
    # *args -> recebe vários argumentos posicionais extras (vira uma tupla)
    # **kwargs -> recebe vários argumentos nomeados (vira um dicionário)
    texto = "\n".join(args)
    # Junta todos os textos passados em *args
    # "\n" significa quebra de linha
    # .join(args) une cada item da tupla separando por quebra de linha
    meta_dados = "\n".join([f"{chave.title()}: {valor}" for chave, valor in kwargs.items()])
    # kwargs.items() retorna pares (chave, valor) do dicionário
    # f"{chave.title()}: {valor}" cria uma string formatada
    # .title() deixa a primeira letra da chave maiúscula
    # Depois o join junta tudo separando por quebra de linha
    mensagem = f"{data_extenso}\n\n{texto}\n\n{meta_dados}"
    # Monta a mensagem final usando f-string
    # \n\n cria uma linha em branco entre as partes
    print(mensagem)

exibir_poema("Terça-feira, 24 fev 26", "Zen of Python", "Beautiful is better than ugly.", autor="Tim Peters", ano=1999)