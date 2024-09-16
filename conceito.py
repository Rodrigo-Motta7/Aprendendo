nome=input("Digite o nome do aluno\n:")
teste=float(input(f"Digite a nota do teste do aluno {nome}\n:"))
prova=float(input(f"Digite a nota da prova do aluno {nome}\n:"))
media= (teste+prova)/2
if media>=9:
    conceito ="A"
elif media>=7.5:
    conceito ="B"
elif media>=6:
    conceito ="C"
elif media>=4:
    conceito ="D"
else:
    conceito ="E"
print(f"O aluno {nome} obteve uma média de {media:.1f}, com isso ele tem conceito {conceito}")