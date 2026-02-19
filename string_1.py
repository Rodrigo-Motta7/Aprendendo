nome = "rOdrIGo"

print(nome.upper())
#imprime tudo minusculo
print(nome.lower())
#imprime tudo maiusculo
print(nome.title())
#imprime com a primeira letra maiuscula e o resto minusculo

texto = "  Olá mundo   "

print(texto + ".")
#imprime normal
print(texto.strip() + ".")
#imprime sem os espaços
print(texto.lstrip() + ".")
#imprime sem os espaços da esquerda
print(texto.rstrip() + ".")
#imprime sem os espaços da direita

menu ="Python"

print(menu.center(14))
#define que o texto ficara no centro e quantos caracteres ele tera (neste caso tera a adição de espaços)
print(menu.center(14, "#"))
#neste caso os espaços faltantes para alcançar o número determinado será preenchido com a '#'
print("-".join(menu))
#imprime a palavra com o "-" entre cada letra