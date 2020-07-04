#formas de mostrar valores arredondados sem mudar o valor realmente
# a = 10.66666661
# print('O número é:',a)
# print(f'O número é: {a:.2f}')
# print('O número é: {:.2f}'.format(a))
# print('O número é:',a)

#formatação para números inteiros
# a = 10
# print('O número é:',a)
# print(f'O número é: {a:d}')
# print('O número é: {:d}'.format(a))
# print('O número é:',a)

#formatação para string
# a = "É 20"
# print('O número é:',a)
# print(f'O número é: {a:s}')
# print('O número é: {:s}'.format(a))
# print('O número é:',a)

inteiro = 123
real = 125.666666666666668
texto = 'Olá mundo'
print(f'O preço é: R${real:.2f} pague no caixa')
print(f'O número da fila é: {inteiro:d}')
print(f'A frase do dia é: "{texto:<20s}"')