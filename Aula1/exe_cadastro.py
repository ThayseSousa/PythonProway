# Utilize os conceitos de entrada, saída e variáveis para criar um cadastro
# O cadastro deve conter:
# 1 - Um cabeçalho com nome do programa
# 2 - Um rodapé
# 3 - Solicitar o nome e salvar em uma variável
# 4 - Solicitar o sobrenome e salvar em uma variável
# 5 - Solicitar a idade e salvar em uma variável
# 6 - Imprimir os dados coletados na tela juntamente com uma mensagem
print('\n')
print('*'*10 , 'CADASTRO USUÁRIO' , '*'*10)
nome = input('Digite o nome:')
sobrenome = input('Digite o sobrenome:')
idade = input('Digite a idade:')
# impressão multiplas linhas '''
# interpolação de strings  'f'+ {}
print(f'''Os dados do usuario sao:
        Nome:{nome} 
        Sobrenome:{sobrenome}
        Idade:{idade} 
        ''')
print('*'*10 ,'FIM' , '*'*10)
print('\n')