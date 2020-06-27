import matplotlib.pyplot as plt

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

r1 = ["Feminino", "Masculino"]

plt.bar(r1,maior_idade, color ="#6A5ACD", label = "Maior Idade")
plt.bar(r1,menor_idade,color = "#E44FC7", label = "Menor Idade")

plt.xlabel = ("Sexo")
plt.xticks(["Feminino", "Masculino"])
plt.ylabel("Quantidade")

plt.legend()
plt.show()