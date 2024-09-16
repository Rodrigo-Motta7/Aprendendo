nom=input("Digite o nome do usuario:")
idad=int(input(f"Digite a idade do {nom}:"))
if idad<12:
    print(f"O usuario {nom} possui {idad} anos e é uma criança.")
elif idad<17:
    print(f"O usuario {nom} possui {idad} anos e é um adolescente.")
elif idad<59:
    print(f"O usuario {nom} possui {idad} anos e é um adulto.")
else:
    print(f"O usuario {nom} possui {idad} anos e é um idoso.")