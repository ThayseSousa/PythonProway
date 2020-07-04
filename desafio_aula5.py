import matplotlib.pyplot as plt

# 1) Crie uma lista com multiplos de 3
lista =[]
x = 0
for y in range(1, 100):
    if y % 3 == 0:
        x += y
        lista.append(y)
print(lista)


# 2) Crie uma lista de 0 a 100 com números pares
lista2 = []
num = 100
cont = 0
while cont <= num:
    cont += 1
    if (cont%2) == 0:
        lista2.append(cont)
        continue
print (lista2)

# 4) Crie 2 listas com a mesma quantidade de elementos. 
# Crie um filtro para garantir que tenha o mesmo número de elementos.
# A primeira lista é # o número de meses e a segunda é o montante
#  do empréstimo.
# Faça um gráfico com eles.
# Lembrando que a fórmula do juros composto é: 
# montante = capital * (1+ taxa)** tempo
# O valor do capital é R$100.00
# A taxa é 0.03
# Os valores devem ter 2 casas após a virgula

# def jur_composto(tempo,capital,juros):
#     taxa = taxa/100
#     montante = capital * (1+ taxa)** tempo
#     return round(montante,2)

tempo = [x for x in range(100)]
taxa = 3/100
montante = [round(100 * (1 + 0.03) ** t,2) for t in tempo]
# ou
# montante = [jur_composto(t,100,3) for t in tempo]

tam_montante = len(montante)

if len(tempo) == tam_montante:
    plt.plot(tempo,montante)
    plt.show()