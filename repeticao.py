#Estrutura de repetição FOR

#print ("Aluno", 1)
# a cada vez que coolocamos uma virgula no print ele imprime com o espaço

#queremos que repita de 1 até 5, ou seja, 5 vezes
for i in range(1, 6):
    print("Aluno",i)

# ou 
for i in range(5):
    print("Aluno",i+1)

# Exemplo com repetição para cadastro de 2 usuarios

for i in range(2):
    nome = input('Digite seu nome: ')
    sobrenome = input("Digite seu sobrenome: ")
    idade = int(input("Digite sua idade: "))
    print("Usuároio cadastrado: \n",nome, sobrenome,"Idade:",idade)