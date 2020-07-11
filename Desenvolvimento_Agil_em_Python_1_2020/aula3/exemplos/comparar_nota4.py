# Dia 20/06/2020
# Des. Py

# Criar um programa que receba 30 notas e faça a média e
# verifique se o aluno passou ou reprovou
# A nota de corte é 7.00
# Entre 5.50 a 7.00 Recuperação
# A baixo de 5.5 Reprovado

lista = []
num = int(input("Digite a quantidade de notas: "))

for i in range(num):
    nota = float(input(f"Digite a sua nota {i+1}: "))
    lista.append(nota)

# ac=0
# for i in lista:
#     ac = ac + i

media = sum(lista)/len(lista)


if media >= 7:
    print("Aprovado média: ", media)
elif media < 5.5:
    print ("reprovado média: ", media)
else:
    print("Recuperação média: ", media)
