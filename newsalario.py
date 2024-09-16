nom=input("Digite o nome do funciaonario:")
salr=float(input(f"Digite o salário do funcionário {nom}:"))
temp=int(input(f"Digite o tempo de empresa do funcioanrio {nom}:"))
if temp<5:
    newsalr=salr +(salr * 0.06)
    print(f"O funcionário {nom} com {temp} anos na empresa possui um novo salário de R${newsalr:.2f}, o antigo salário era R${salr}")
elif temp<10:
    newsalr = salr +(salr * 0.10)
    print(f"O funcionário {nom} com {temp} anos na empresa possui um novo salário de R${newsalr:.2f}, o antigo salário era R${salr}")
elif temp<15:
    newsalr = salr +(salr * 0.15)
    print(f"O funcionário {nom} com {temp} anos na empresa possui um novo salário de R${newsalr:.2f}, o antigo salário era R${salr}")
else:
    newsalr = salr +(salr * 0.20)
    print(f"O funcionário {nom} com {temp} anos na empresa possui um novo salário de R${newsalr:.2f}, o antigo salário era R${salr}")
