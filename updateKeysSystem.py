from modules.getDataBase import *
from datetime import datetime
import csv

sysdate = datetime.now().strftime('%d/%m/%Y')
sysdateWSO2 = datetime.now().strftime('%m%Y')

print(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S')+': Inicio da atividade'))

db = GetDataBase()
up = UpdateDataBase()

blazon = db.blazon()
user_r12 = db.r12()
user_somar = db.somar()

list_Error_found = []


for keyR12 in user_r12:
    r12Found = False
    for blazonUser in blazon:
        if blazonUser[1] in ('R12','R12 (APLICAÇÃO)') and keyR12[0] == blazonUser[0] and keyR12[1] != blazonUser[2]:
            #print("R12 --> update FND_USER FU set FU.FAX = '"+str(blazonUser[2])+"' Where FU.USER_NAME = "+keyR12[0])
            up.r12(str(blazonUser[2]), keyR12[0])
            r12Found = True
        elif blazonUser[1] in ('R12', 'R12 (APLICAÇÃO)') and keyR12[0] == blazonUser[0] and keyR12[1] == blazonUser[2]:
            r12Found = True

    if r12Found == False:
        key = ("R12",str(keyR12[0]), str(keyR12[1]))
        list_Error_found.append(key)

for keySomar in user_somar:
    somarFound = False
    for blazonUser in blazon:
        if blazonUser[1] in ('SOMAR','SOMAR (APLICAÇÃO)') and keySomar[0] == blazonUser[0] and keySomar[1] != blazonUser[2]:
            #print("SOMAR --> update FND_USER FU set FU.FAX = '"+str(blazonUser[2])+"' Where FU.USER_NAME = "+keySomar[0])
            up.somar(str(blazonUser[2]), keySomar[0])
            somarFound = True
        elif blazonUser[1] in ('SOMAR','SOMAR (APLICAÇÃO)') and keySomar[0] == blazonUser[0] and keySomar[1] == blazonUser[2]:
            somarFound = True

    if somarFound == False:
        key = ("SOMAR",str(keySomar[0]),str(keySomar[1]))
        list_Error_found.append(key)

with open('C:/Automations/updateKeysSystem/reports/resultUpdaeKeySystem.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(["RECURSO","USUARIO","VALOR"])

    for result_list in list_Error_found:
        writer.writerow([result_list[0],result_list[1],result_list[2]])



db.closeConnection()

print(str(datetime.now().strftime('%d/%m/%Y-%H:%M:%S')+': Fim da atividade'))
