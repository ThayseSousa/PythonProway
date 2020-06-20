#O usuário vai digitiar uma nota
#se for maior que sete deve aparecer aprovado e se for menor que 7 deve aparecer reprovado

#Exemplo com 4 notas
# nota = 0
contador = 0

# for i in range(4):
#     nota_aluno = float(input ('Digite a nota do aluno: '))
#     nota = nota_aluno + nota
#     contador = contador + 1

# media = nota/4

# print(media)

# # nota_aluno = float(input ('Digite a nota do aluno: '))
# if media >= 7:
#     print('Aprovado')
# elif media < 7 and nota_aluno >= 5.5:
#     print('Em recuperação')
# else:
#     print('Reprovado')

#Exemplo com 30 notas
lista = []

num = int(input('Digite o numero de notas que irá cadastrar: '))

for i in range (num):
    nota_aluno = float(input (f'Digite a nota {i+1} do aluno: '))
    lista.append(nota_aluno)

media = sum(lista)/len(lista)
print(media)

if media >= 7:
    print('Aprovado')
elif media < 7 and nota_aluno >= 5.5:
    print('Em recuperação')
else:
    print('Reprovado')