# primeiro nós importamos todos os arquivos 
import matplotlib.pyplot as plt
#from matplotlib import pyplot
#from matplotlib import * (não é o correto fazer vai importar tudo que está na biblioteca para o pragrama)

#Depois colocamos as funções necessárias

x = [i for i in range(1,7)]
y = [i for i in range(11,17)]

meses = ['Janeiro','Fevereiro','Março', 'Abril','Maio','Junho']
valores = [105235,107697,110256,109236,108859,109986]

#----Primeiro teste
# plt.plot(x,y, color = 'yellow') #gráfico de linha
# plt.bar(x,y, color= 'red') #gráfico de barra
# plt.bbar(x,y, color= 'red') #gráfico de barras invertido (de lado)
# plt.scatter (x,y, color = '#714FB6') #gráfico de pontos
# plt.title('Teste solvente')
# plt.xlabel('Solvente')
# plt.ylabel('Produto resultante')

#----Segundo teste
plt.plot (meses,valores, color = '#714FB6') #gráfico de pontos
plt.title('Faturamento por mês')
plt.xlabel('Meses')
plt.ylabel('Faturamento em R$')

#limitar os valores do eixo x e y
# plt.ylim(0,20)
# plt.xlim(0,7)


plt.show()