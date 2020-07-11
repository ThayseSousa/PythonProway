# 1) Com a lista abaixo, faça um for e mostre o tipo de 
# cada item desta forma:

# Tipo: 01 - String 
# Tipo: 02 - Inteiro 
# Tipo: 03 - Real
# Tipo: 04 - Lista
# Tipo: 05 - Tupla
# Tipo: 06 - Dicionário

# 2) Mostre o tamanho da lista

lista = [[],"oi", "tchau",1.98,1,[1,2,3],{"agua":123},(),"fim"]

for i in lista:
    if type(i) == str:
        print('Tipo: 01 - String')
    elif type(i) == int:
        print('Tipo: 02 - Inteiro')
    elif type(i) == float:
        print('Tipo: 03 - Real')
    elif type(i) == list:
        print('Tipo: 04 - Lista')
    elif type(i) == tuple:
        print('Tipo: 05 - Tupla')
    elif type(i) == dict:
        print('Tipo: 06 - Dicionário')

print(len(lista))

