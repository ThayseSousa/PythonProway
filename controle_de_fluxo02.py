#Pass - seguinifica que o python vai ignorar aquela função, vai 'deixar passar'


#brak - ele para o código, ou seja, vai executar tudo até aquele ponto e depois irá encerrar o código


#continue - utilizado no while ele vai executar tudo que estiver antes do wcontinue e depois retornará ao inicio
#crie um programa que que peça um número de 10 a 100
#imprmir apenas os números impares anteriores ao numero digitado
#usar if , while e continue
num = int(input("Digite um número de 10 a 100: "))

cont = 10

while cont <= num:
    cont += 1
    if (cont%2) == 0:
        continue
    print (cont)
    