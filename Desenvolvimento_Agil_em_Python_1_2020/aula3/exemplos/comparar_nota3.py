# Dia 20/06/2020
# Des. Py

# Criar um programa que receba 4 notas e faça a média e
# verifique se o aluno passou ou reprovou
# A nota de corte é 7.00
# Entre 5.50 a 7.00 Recuperação
# A baixo de 5.5 Reprovado

nota1 = float(input("Digite a sua nota 1: "))
nota2 = float(input("Digite a sua nota 2: "))
nota3 = float(input("Digite a sua nota 3: "))
nota4 = float(input("Digite a sua nota 4: "))

media = (nota1 + nota2 + nota3 + nota4)/4


if media >= 7:
    print("Aprovado média: ", media)
elif media < 5.5:
    print ("reprovado média: ", media)
else:
    print("Recuperação média: ", media)
