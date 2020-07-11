from datetime import date, time, datetime, timedelta
from dateutil.relativedelta import relativedelta
from time import sleep, asctime, time

a = time()

data_hoje = date.today()
print(data_hoje.strftime('%d/%m/%Y'))
print(asctime())

data_futura=date(2020,7,30)
print(data_futura)

print(data_futura-data_hoje)

# data_desejada = date.today()+relativedelta(months=+6)
data_desejada = date.today()+relativedelta(weeks=+6)
print(data_desejada)
sleep(5) #vai parar de executar por 5 segundos
print("Cálculos feitos")
print('Os Calculos foram feitos em:',time()-a)