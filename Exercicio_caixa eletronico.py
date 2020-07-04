print('-'*30)
print('{:^30}'.format('Banco Python Proway'))
print('-'*30)
valor = int(input("Digite o valor a ser sacado: "))
total = valor
ced = 100
total_ced = 0
while True:
    if total >= ced:
        total -= ced
        total_ced += 1
    else:
        if total_ced > 0:
            print(f'Total de {total_ced} de R$ {ced}')
        if ced == 100:
            ced=50
        elif ced==50:
            ced = 20
        elif ced ==20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        total_ced = 0
        if total == 0:
            break
print ('-'*30)
print ('Saque realizado com sucesso!')