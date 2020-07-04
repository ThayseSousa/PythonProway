# Abra a lista cadastro3.txt
# Crie uma List Comprehension e zip que trate e converta cada pessoa em um
#  dicionário
# Salve os dicionários em uma lista
# Encontre todos que possuam idade de 18 a 25 anos.
# Salve o resultado em um arquivo .txt

arquivo = open('cadastro3.txt', 'r')
arquivo2 = open('cadastro4.txt','w')

lista = []
for pessoa in arquivo:
    pessoa = pessoa.strip()
    pessoa = pessoa.split(';')
    lista.append(pessoa)
arquivo.close()

chaves = ["id","nome","idade","sexo","email","telefone"]
lista_cadastro = [dict(zip(chaves,pessoa)) for pessoa in lista]

pessoa2 = [x for x in lista_cadastro if int(x['idade']) >=18 and int(x['idade']) <=25]
print(pessoa2)

arquivo2.write(pessoa2)
arquivo2.close()