



def caixa(valor_funcao):
    dinheiro = [100,50,20,10,5,1,0.5,0.25,0.1,0.05,0.01]

    for pila in dinheiro:
        quantidade = int(valor_funcao // pila)
        #valor = valor -( pila * quantidade)
        valor_funcao = round(valor_funcao % pila,2)
        print(f"{quantidade:d} nota(s) valor {pila:>6.2f}"
            if pila > 1 else 
            f"{quantidade:d} moeda(s) valor {pila:>6.2f}")





# importação de modulos e funções
#################################################################################
# programa


#valor = float(input("Digite o valor desejado: "))

caixa(367.69)

print(dinheiro)