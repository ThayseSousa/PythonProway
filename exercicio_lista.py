# tipo :01 - string
# #tipo: 02 - inteiro
# Real
# lista
# tupla
# dicionario

lista = [[],"oi","tchau",1.98,1,[1,2,3],{"agua":123},(),"fim"]

for i in lista:
    if type(i) == str:
        print("Tipo igual a string")
    elif type(i) == int:
        print("Tipo igual a inteiro")
    elif type(i) == float:
        print("Tipo igual a real(float)")
    elif type(i) == list:
        print("Tipo igual a lista")
    elif type(i) == tuple:
        print("Tipo igual a tupla")
    elif type(i) == dict:
        print("Tipo igual a dicionário")
print(len(lista))

index = len(lista)
lista.insert(index+1, "oi de novo")
print(lista)