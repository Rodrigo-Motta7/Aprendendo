imaginado = 46
digitado = 0
tent = 3
print('Você entrou no jogo de adivinhação.')
print('Estou pensando em um número inteiro entre 0 e 50.')

while digitado != imaginado :
    digitado = int(input('Digite o número que você acha que estou pensando: '))
    tent = tent - 1
    if digitado > imaginado:
        print('O número digitado é maior que o número que estou pensando.')
        print(f'Você possui mais {tent} tentativas')
    if digitado < imaginado:
        print('O número digitado é menor que o número que estou pensando.')
        print(f'Você possui mais {tent} tentativas')
    if digitado == imaginado:
        print('Parabéns! Você adivinhou!')
    if tent == 0 and digitado != imaginado:
        print('Você perdeu, o número de tentativas acabou')
        break
    
print('Jogo encerrado.')
        
