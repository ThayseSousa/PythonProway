# Funções 20/06/2020

def soma(num1_fun, num2_fun): # passar variáveis por parametro(s)
    soma_fun = num1_fun + num2_fun
    return soma_fun


menu = """ 
Opções:
1) Soma
2) Subtração
3) Multiplicação
4) Divisão
S) para sair

Digite a opção desejada: """

while True:
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    
    opcoes = input(menu)

    if opcoes == '1':
        soma_res = soma (num1, num2)
        print(f'A soma é: {soma_res}')
        
    if opcoes == '2':
        soma = num1 - num2
        print(f'A subtração é: {soma}')

    if opcoes == '3':
        soma = num1 + num2
        print(f'A divisão é: {soma}')

    if opcoes == '4':
        soma = num1 * num2
        print(f'A multiplicação é: {soma}')

    if opcoes.upper() == 'S':
        print(f'Saindo!')
        break



