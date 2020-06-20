# #Funções

# #o código da função sempre deverá estar em cima o código

# def teclado():
#     num1 = float(input("Digite o primeiro número: "))
#     num2 = float(input("Digite o segundo número: "))
#     return num1,num2

# def soma(num1, num2):
#     soma = num1 + num2
#     return soma

# def subtrair(num1, num2):
#     subtrair = num1-num2
#     return subtrair

# def divisao(num1, num2):
#     divisao = num1/num2
#     return divisao

# def multiplicacao(num1, num2):
#     multiplicacao = num1 * num2
#     return multiplicacao

# menu = '''
# Opções:

# 1) Para somar
# 2) Para subtrair
# 3) Para dividir
# 4) Para multiplicar

# Digite "s" para sair

# digite a opção desejada: '''

# var = input(menu)

# while var != "s":
#     numero1, numero2 = teclado()
#     if var == "1":
#         total = soma(numero1,numero2)
#     elif var == "2":
#         total = subtrair(numero1, numero2)
#     elif var == "3":
#         total = divisao(numero1, numero2)
#     else:
#         total = multiplicacao(numero1, numero2)

#     print("O total é: ",total)

#     var = input("Digite a opçao: ")

def media(lista_fun):
    media = sum(lista_fun)/len(lista_fun)
    return print(media)

lista = [7,7,7,7]

media (lista)
