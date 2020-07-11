# Aula 03 - 20/06/2020

# Faça um programa que mostre um menu interativo,
# Este menu deve ter a opção para cada uma das operações matemáticas (+, -, /, *)
# do python.
# Caso digite s ou S o programa acaba.

# Use o while e o break

menu = """ 
Opções:
1) Soma
2) Subtração
3) Multiplicação
4) Divisão
S) para sair

Digite a opção desejada: """

while True:
    opcoes = input(menu)
    if opcoes == '1':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f'A soma é: {soma}')
    if opcoes == '2':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 - num2
        print(f'A subtração é: {soma}')
    if opcoes == '3':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 + num2
        print(f'A divisão é: {soma}')
    if opcoes == '4':
        num1 = int(input("Digite o primeiro número: "))
        num2 = int(input("Digite o segundo número: "))
        soma = num1 * num2
        print(f'A multiplicação é: {soma}')
    if opcoes.upper() == 'S':
        print(f'Saindo!')
        break
