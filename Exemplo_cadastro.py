lista_alunos = []

for i in range(2):
    dict_aluno = {}
    dict_aluno['nome'] = input('Digite o seu nome: ')
    dict_aluno['sobrenome'] = input('Dgiite seu sobrenome: ')
    dict_aluno['idade'] = input('Digite sua idade: ')
    lista_alunos.append(dict_aluno)

for i in lista_alunos:
    print('Usuário cadastrado:',i['nome'],i['sobrenome'],i['idade'])