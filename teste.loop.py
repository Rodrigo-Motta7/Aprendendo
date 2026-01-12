print('Programa contador de repetições')
denovo = True
contador = 0

while denovo:
    contador += 1
    op = input('Digite s para repetir ou n para encerrar e ver o número de repetições:  ')
    if op == 'n':
        denovo = False
    elif op != 's':
        print("Erro! Opção invalida! Cancelando contagem!")
        break
    else:
        print('O numero de repetições foi:', contador)
        