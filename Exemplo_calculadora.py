menu = '''
Opções:

1) Para somar
2) Para subtrair
3) Para dividir
4) Para multiplicar

Digite "s" para sair

digite a opção desejada: '''

var = input(menu)

while var != "s":
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))
    if var == "1":
        total = numero1 + numero2
    elif var == "2":
        total = numero1 - numero2
    elif var == "3":
        total = numero1 / numero2
    else:
        total = numero1 * numero2

    print("O total é: ",total)

    var = input("Digite a opçao: ")