import matplotlib.pyplot as plt
import numpy as np

arquivo = open('cadastro.txt', 'r')

lista_cadastro = []
for pessoa in arquivo:
    pessoa = pessoa.strip()
    pessoa = pessoa.split(';') 
    lista_cadastro.append(pessoa)

arquivo.close()

contador_homem_menorIdade = 0
contador_homem_maiorIdade = 0
contador_mulher_menorIdade = 0
contador_mulher_maiorIdade = 0

for pessoa in lista_cadastro:
    if pessoa[3].upper() == "F" and int(pessoa[2]) < 18:
        contador_mulher_menorIdade += 1
    elif pessoa[3].upper() == "F" and int(pessoa[2]) >= 18:
        contador_mulher_maiorIdade += 1
    elif pessoa[3].upper() == "M" and int(pessoa[2]) < 18:
        contador_homem_menorIdade += 1
    else:
        contador_homem_maiorIdade += 1

print("Homens maiores de idade:",contador_homem_maiorIdade)
print("Homens menores de idade:",contador_homem_menorIdade)
print("Mulheres maiores de idade:",contador_mulher_maiorIdade)
print("Mulheres menores de idade",contador_mulher_menorIdade)

maior_idade = [contador_mulher_maiorIdade,contador_homem_maiorIdade]
menor_idade = [contador_mulher_menorIdade,contador_homem_menorIdade]

plt.figure(figsize=(10,5))

barWidth = 0.25
r1 = np.arange(len(maior_idade))
r2 = [x + barWidth for x in r1]

plt.bar(r1,maior_idade, color ="#6A5ACD", width=barWidth,label = "Maior Idade")
plt.bar(r2,menor_idade,color = "#E44FC7", width=barWidth,label = "Menor Idade")

plt.xlabel = ("Sexo")
plt.xticks([r + barWidth for r in range(len(maior_idade))],["Feminino", "Masculino"])
plt.ylabel("Quantidade")
plt.title("Quantidade de meiores de idade e menores de idade por sexo")

plt.legend()
plt.show()