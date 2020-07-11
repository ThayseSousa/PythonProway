# 1) Crie uma lista com multiplos de 3
# 2) Crie uma lista de 0 a 100 com números pares
# 3) Crie uma lista de 0 a 1000 com números que sejam 
# multiplos de 2 e multiplos de 3

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

# 5) Abra o arquivo cadastro2.txt
# Com o list comprehension trate as string e converta para lista.
# Salve as listas em uma lista de cadastros.

# 1) Crie uma lista com multiplos de 3
lista3 = [x*3 for x in range(11)]
print(lista3)
# 2) Crie uma lista de 0 a 100 com números pares
lista_par = [x for x in range(100) if x%2 == 0]
print(lista_par)

# 4) Crie 2 listas com a mesma quantidade de elementos. 
# Crie um filtro para garantir que tenha o mesmo número de 
# elementos.
# A primeira lista é o número de meses e a segunda é o montante
#  do empréstimo.
# Faça um gráfico com eles.
# Lembrando que a fórmula do juros composto é: 
# montante = capital * (1+ taxa)** tempo
# O valor do capital é R$100.00
# A taxa é 0.03
# Os valores devem ter 2 casas após a virgula

import matplotlib.pyplot as plt

#### Opcional explico depois###
def jur_comp(tempo,capital,taxa):
    taxa = taxa / 100
    montante = capital * (1+ taxa) ** tempo
    return round(montante , 2)

tempo = [x for x in range(48)]
# montante = capital * (1+ taxa)** tempo


taxa = 3 / 100

montante1 =  [ round( 100*(1+taxa)**t,2 ) for t in tempo]
montante =  [jur_comp(t,150,3) for t in tempo]

tam_mont = len(montante)

if len(tempo) == tam_mont :
    plt.plot(tempo,montante1, color="blue")
    plt.plot(tempo,montante, color="red")
    plt.show()