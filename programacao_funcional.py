def soma (val, val2):
  return val+val2
print(soma(3,5))
soma_lb = lambda var,var2: var + var2
print(soma_lb(3,5))
multiplica_lb = lambda var,var2: var * var2
print(multiplica_lb(3,5))
print(soma_lb(150,65))

div = lambda valor1, valor2: valor1/valor2 if valor2 != 0 else "Não é possível dividir por zero"
print(div(18,0))

def cadastro(nome, idade, sexo):
  # def cadastro(nome,idade = 18, sexo = F) - quando as variaveis já tem valor definido é necessário que elas sejam as ultimas
  print(f'Seu nome é: {nome}, você tem {idade} anos e seu sexo é {sexo}.')

cadastro('Thayse', 22, "feminino")

lista = [0,1,2,3]
espo = lambda x, y=0:x**2+y
lista_resulado = list(map(espo,lista))
print(lista_resulado)

lista= [1,2,3,4,5,6,7,8,9,10]
espo = lambda x,y=0: x*3+y
lista_exemplo = list(map(espo,lista))
print(lista_exemplo)



#exercicios 
tempo = [1,2,3,4,5,6,7,8,9,10,11,12]
montante = (200*(1+(10/100)))
espo = lambda t,valor = 200, i= 10:round(valor*(1+(i/100))**t)
lista_exemplo2 = list(map(espo,tempo))
print(lista_exemplo2)