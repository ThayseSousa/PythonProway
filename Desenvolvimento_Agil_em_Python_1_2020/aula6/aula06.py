import datetime

# data = datetime.datetime(ano,mês,dia,hora,minuto,segundo)
dt = datetime.datetime(2020,7,20,13,12,56)
print(dt)
data = dt.date()
hora = dt.time()
print(data," ",hora)

dias = dt - dt.today()
print(dias)

import time
a=time.time()
print(time.asctime())
print(f"Levou {time.time()-a} segundos para executar")

segundos = 3
print(f"Isso vai levar {segundos}...")
time.sleep(segundos)
print("para acabar")

# mensagem = "Apagando banco de dados"
# while True:
# 	try:
# 		print(mensagem)
# 	except:
		