#tuplas

#é imutável não é possível alterar as informações
#a segunda diferença com relação a listas é que os valores vem entre ()
tupla = (10,12,15,89,44,55)
print(tupla)
print(tupla[1:3])
#tentativa de alteração de uma tupla
#a tentantiva retorna um erro informando que não é possível alterar o arquivo
# tupla[2] = 22

#é possível incluir strings, numeros, listas dentro de uma tupla
#é possível também ter uma lista de tuplas dentro de uma lista
lista_notas = [10,8,6,4]
tupla_aluno = ('Thayse','Sousa',15,[10,8,6,4])
#podemos alterar a lista dentro da tupla
tupla_aluno[3][0] = 8
print(tupla_aluno)

lista_aluno = list(tupla_aluno)
print(lista_aluno)


#Dicionários

dict_alunos = {'nome':'Thayse','sobrenome':'Sousa','idade':15,'lista_notas':[10,8,6,4]}
dict_alunos2 = {'nome':'Marina','sobrenome':'Cristina','idade':22,'lista_notas':[10,8,6,4]}
lista = [dict_alunos,dict_alunos2]
print(dict_alunos)
print(dict_alunos['nome'])

#alterando um nome dentro de um dicionário
dict_alunos['nome'] = 'Thayse'
print(dict_alunos)
dict_alunos['lista_notas'][3] = 9
print(dict_alunos)
print(lista)
print('Imprimindo com for....')
for a in lista:
    print(
        a['nome'], a['sobrenome'],a['idade'],a['lista_notas']
    )