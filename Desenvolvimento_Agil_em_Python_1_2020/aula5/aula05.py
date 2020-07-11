import sys
sys.path.append('/Users/mdgranemann/Documents/Github/AlunosPython/TrabalhosPython/Aula33/Aula33-4')


Transposição Com O Método Zip

a = ['a','b','c','d']
b = [0,1,2,3]
lista_empacotada = list( zip(a,b) )
des_a , des_b = zip(*lista_empacotada)
dicionario = dict(lista_empacotada)
des_a , des_b = zip(*dicionario.items())



List Comprehension
Ação, intens interados, filtro
lista = [x for x in range(100) if x%2 == 0]


Geradores e Generator Expression
def meu_range(num):
    for i in range(num):
        yield i

contador = meu_range(10)
print(next(contador))


Formatando String
(referencia https://pyformat.info/)

:< alinhar a esquerda
:> alinhar a direita
:^ alinhar ao centro

s = string
d = inteiros
f = float

:04d = adiciona 0 na frente
:+s  = adiciona + na frente, para negativo, colocar na frente da variável
print(f"{-a:9.2f}")
"{:9.2f}".format(-a)

: numero de casas .

format
print("{:.2f}".format(a))
'{1} {0}'.format('Um', 'Dois')
'{0} {0}'.format('Um', 'Dois')

f-string
a=15.656565656565
print(f"{a:.2f}")

Bonus....
assert 
