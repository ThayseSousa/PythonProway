# Aula 03 - 20/06/2020

tupla = (98, 93, 71, 78, 4, 12, 47, 50, 21, 39, 33, 
         38, 23, 9, 28, 96, 24, 86, 26, 31, 73, 16, 
         13, 87, 44, 89, 69, 53, 94, 40, 67, 37, 55, 
         62, 91, 57, 36, 72, 79, 61, 83, 48, 56, 64, 
         17, 65, 88, 20, 27, 84)


# Crie um programa que leia um número de 1 a 100.
# Faça uma busca sequencial na tupla e mostre a posição 
# que se encontra o número

num = int(input("Digite um número de 1 a 100: "))
contador = 0

i = 1
x = 0

for i in tupla:
    if i == num:
        print('O valor', num, 'está na posição', contador)
        break
    contador += 1