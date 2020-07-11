# Aula 03 - 20/06/2020

# Crie uma função que receba uma lista 
# numérica e retorne a média
# from media import media2

def media2(lista):
    return sum(lista)/len(lista)


lista = [9,9,10,6,10,10]

md = media2(lista)

print(md)