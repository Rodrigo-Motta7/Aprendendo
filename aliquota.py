nom = input("Digite o nome do usuario: ")
rend= float(input("Digite a renda do usuario: "))
if rend<1903.98:
    print(f"O usuario {nom} com a renda de R${rend} está isento da aliquota de dedução do imposto de renda")
elif rend<2826.65:
    imp1=rend * 0.075
    print(f"O usuario {nom} com a renda de R${rend} possui uma aliquota de 7.5% e tera uma redução de R${imp1:.2f}")
elif rend<3751.05:
    imp2=rend * 0.15
    print(f"O usuario {nom} com a renda de R${rend} possui uma aliquota de 15% e tera uma redução de R${imp2:.2f}")
elif rend<4664.68:
    imp3=rend * 0.225
    print(f"O usuario {nom} com a renda de R${rend} possui uma aliquota de 22.5% e tera uma redução de R${imp3:.2f}")
else:
    imp4=rend * 0.25
    print(f"O usuario {nom} com a renda de R${rend} possui uma aliquota de 25% e tera uma redução de R${imp4:.2f}")