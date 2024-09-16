temp=int(input("Digite a temperatura em Celsius:"))
if temp<0:
    clima="congelante"
elif temp<10:
    clima ="muito frio"
elif temp<20:
    clima ="frio"
elif temp<30:
    clima ="agradável"
elif temp<40:
    clima ="quente"
else:
    clima ="muito quente"
print(f"A tempera do local em Celsius é {temp}° e o clima está {clima} ")
