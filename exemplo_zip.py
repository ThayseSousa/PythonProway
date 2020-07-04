arquivo = open('cadastro.txt', 'r')
lista = []
for pessoa in arquivo:
    pessoa = pessoa.strip()
    pessoa = pessoa.split(';')
    lista.append(pessoa)

arquivo.close()

chaves = ["id","nome","idade","sexo","email","telefone"]
lista_cadastro = [dict(zip(chaves,pessoa)) for pessoa in lista]

print(lista_cadastro)