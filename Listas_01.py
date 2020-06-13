#Estrutura de repetição com armazenamento

idade = 151
lista_idades = [18,19,50,19]
print(lista_idades)
print(lista_idades[1])

# Removendo um item da lista
# porém remove somente a primeira ocorrência que aparece, se tiverem duas ou três a mais elas não serão retiradas
lista_idades.remove(19)
print(lista_idades)
#removendo todos os dados da lista
#lista_idades.clear()

# removendo dados da lista como a função pop
# no pop nós indicamos a posição do dado que queremos remover
# o pop retorna um resultado que é a mesma variável que foi retirada
retorno_pop = lista_idades.pop(1)
print(lista_idades)
print(retorno_pop)

#adicionar dados na lista utlizando a função append
lista_idades.append(idade)
lista_idades.append(18)
lista_idades.append(356
)
print(lista_idades)

#para identificar a quantidade de vezes que aquele valor existe na lista
print(lista_idades.count(18))

#mostrando o numero total de itens em uma lista
print(len(lista_idades))

# fatiamento da lista
    #apresentando os 3 primeiros itens da lista
print(lista_idades[:3])

    #apresentando os 3 ultimos itens da lista
index_penultimo_item = len(lista_idades) - 3
print(lista_idades[index_penultimo_item : ])

    #apresentando valores do meio da lista
print(lista_idades[2:4])

#alterar a ordem da lista
print(lista_idades)
lista_idades.reverse()
print(lista_idades)

#inserindo um dado em uma posição especifica da lista
lista_idades.insert(2,152)
print(lista_idades)

#inserindo o número 153 apó o 152

index = lista_idades.index(152)
lista_idades.insert(index+1,153)
print(lista_idades)
