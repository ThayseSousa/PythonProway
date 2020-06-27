arquivo = open('cadastro.txt', 'r')

# for i in arquivo: ----utilizar i é padrão mas da pra mudar
lista_cadastro = []
for pessoa in arquivo:
    pessoa = pessoa.strip()
    pessoa = pessoa.split(';') #ele vai identificar que ; delimita a criação da lista. 
                                #COnverte a string em lista e usa o ; como base. Onde estiver o ; ele vai quebrar e criar uma lista
    lista_cadastro.append(pessoa)

#IMPORTANTE - como demos o comando de abrir é necessário fechar após rodar o programa. A mesma coisa para banco de dados
arquivo.close()

#for i in lista_cadastro:
# print(lista_cadastro[2][3])

# print("Nome que está naposição 300")
# for pessoa in lista_cadastro:
#     if int(pessoa[0]) == 300:
#         print(pessoa)
#         break

# print("Pessoas do sexo feminino da lista")
# for pessoa in lista_cadastro:
#     if pessoa[3].upper() == "F":
#         print(pessoa)

# print("Nomes que comecem com A e sejam do sexo f")
# for pessoa in lista_cadastro:
#     if 'A' in pessoa[1] and 'F' in pessoa[3].upper():
#         print(pessoa)


print("Pessoas do sexo feminino da lista")
mulher = []
for pessoa in lista_cadastro:
    if pessoa[3].upper() == "F":
        mulher.append(pessoa)

arquivo = open(r"C:\Users\61096\Documents\Aula 2_13.06\PythonProway\mulher.txt", "w")
for pessoa in mulher:
    pessoa_str = ";".join(pessoa) +"\n"
    arquivo.write(pessoa_str)
arquivo.close()

print("Pessoas do sexo masculino da lista")
homem = []
for pessoa in lista_cadastro:
    if pessoa[3].upper() == "M":
        homem.append(pessoa)

arquivo = open(r"C:\Users\61096\Documents\Aula 2_13.06\PythonProway\homem.txt", "w")
for pessoa in homem:
    pessoa_str = ";".join(pessoa) +"\n"
    arquivo.write(pessoa_str)
arquivo.close()