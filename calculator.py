while True:
    operacao=input('Digite a operação "adição, subtração, multiplicação e divisão" ou "saida" para encerrar o programa: ').lower()
    if operacao == "saida":
        print("Programa encerrado.")
        break
    if operacao not in ["adição", "subtração", "multiplicação", "divisão"]:
        print("Operação não encontrada, digite novamente")
        continue
    try:
        num_1 = float(input("Digite o primeiro número: "))
        num_2 = float(input("Digite o segundo número: "))

    except ValueError:
        print("Por favor, digite um número válido.")
        continue
    if operacao == "adição":
        resultado = num_1 + num_2
    elif operacao == "subtração":
        resultado = num_1 - num_2
    elif operacao == "multiplicação":
        resultado = num_1 * num_2
    elif operacao == "divisão":
        if num_2 == 0:
            print("Erro, não é possível dividir um número por 0.")
        else:
            continue
        resultado = num_1 / num_2
    
    print(f"O resultado da operação de {operacao} entre {num_1} e {num_2} é {resultado}.")


