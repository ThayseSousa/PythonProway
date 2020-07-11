import matplotlib.pyplot as plt

def pesquisa(lista_cadastro,num,item):
    lista = []
    for pessoa in lista_cadastro:
        if pessoa[num] == item :
            lista.append(pessoa)
    return lista

def pesquisa_idade_maior(lista_cadastro,item):
    lista = []
    for pessoa in lista_cadastro:
        if int(pessoa[2]) >= item :
            lista.append(pessoa)
    return lista

def pesquisa_idade_menor(lista_cadastro,item):
    lista = []
    for pessoa in lista_cadastro:
        if int(pessoa[2]) < item :
            lista.append(pessoa)
    return lista
    

def salvar(lista,nome,tipo):
    arquivo = open(f"aula4/exemplos/{nome}.txt",tipo)
    for pessoa in lista:
        pessoa[0],pessoa[2] = str(pessoa[0]),str(pessoa[2])
        pessoa_str = ";".join(pessoa)+"\n"
        arquivo.write(pessoa_str)
    arquivo.close()

def abrir():
    arquivo = open("aula4/exemplos/cadastro.txt",'r')
    lista_cadastro = []
    for pessoa in arquivo:
        pessoa = pessoa.strip()
        pessoa = pessoa.split(';')
        pessoa[0],pessoa[2] = int(pessoa[0]),int(pessoa[2])
        lista_cadastro.append(pessoa)
    arquivo.close()
    return lista_cadastro


# ['250', 'Edmilson', '36', 'f', 'angela_jah@hotmail.com', '023943813972']

clientes = abrir()
mulher = pesquisa(clientes,3,'f')
homem = pesquisa(clientes,3,'m')
salvar(mulher,'mulher','w')
salvar(homem,'homem','w')     

menor = pesquisa_idade_menor(clientes,18)
maior = pesquisa_idade_maior(clientes,18)
salvar(menor,'menor','w')
salvar(maior,'maior','w')

plt.bar(['F','M'],[len(mulher),len(homem)])
plt.show()

plt.bar(['MAIOR','MENOR'],[len(maior),len(menor)])
plt.show()