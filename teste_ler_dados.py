import os
import xlrd 

lista_arquivos =[]

lista_arquivos = os.listdir('/Users/61096/Desktop/Teste')

# local = (f'/Users/61096/Desktop/Teste/ {lista_arquivos[0]}')

local = ('/Users/61096/Desktop/Teste')
wb = xlrd.open_workbook(local) 
sheet = wb.sheet_by_index(0) 
print(sheet.cell_value(0, 0))


