# Dia 20/06/2020
# Des. Py

# Criar um programa que receba uma nota e 
# verifique se o aluno passou ou reprovou
# A nota de corte é 7.00
# Entre 5.50 a 7.00 Recuperação
# A baixo de 5.5 Reprovado

nota = float(input("Digite a sua nota: "))

if nota >= 7:
    print("Aprovado")
elif nota < 5.5:
    print ("reprovado")
else:
    print("Recuperação")
