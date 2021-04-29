import cx_Oracle
import mysql.connector
from settings.credentials import *
from settings.parameters import *
from settings.db import *

# --------------------------- Abrindo conexão com Oracle R12 ---------------------------
conn_R12 = cx_Oracle.connect(user=CRD_USER_DB_R12, password=CRD_PWD_DB_R12, dsn=PAR_R12_TNS)
crR12 = conn_R12.cursor()

# --------------------------- Abrindo conexão com Oracle Somar ---------------------------
conn_Somar = cx_Oracle.connect(user=CRD_USER_DB_SOMAR, password=CRD_PWD_DB_SOMAR, dsn=PAR_SOMAR_TNS)
crSomar = conn_Somar.cursor()


class GetDataBase:
    def __init__(self):
        pass

    def blazon(self):
        # --------------------------- Abrindo conexão com MYSql Blazon ---------------------------
        db = mysql.connector.connect(user=CRD_USER_DB_BLAZON, passwd=CRD_PWD_DB_BLAZON, host=PAR_BLAZON_IP, db=PAR_BLAZON_DB_NAME)
        cursor_blazon = db.cursor()

        # fazendo select para encontrar usuarios no blazon
        cursor_blazon.execute(SELECT_USERS_ACTIVES_BLAZON)
        return cursor_blazon.fetchall()
        db.close()

    def r12(self):
        # fazendo select de contas ativas no R12
        crR12.execute(SELECT_CONTAS_ATIVAS_R12_SOMAR)
        return crR12.fetchall()

    def somar(self):
        # fazendo select de contas ativas no Somar
        crSomar.execute(SELECT_CONTAS_ATIVAS_R12_SOMAR)
        return crSomar.fetchall()

    def closeConnection(self):
        crR12.close()
        crSomar.close()

class UpdateDataBase():
    def __init__(self):
        pass

    def r12(self,key, user):
        # fazendo update no R12
        crR12.execute("UPDATE apps.fnd_user SET FAX = '" + key + "' where user_name = '" + user + "'")
        conn_R12.commit()
        print("R12: " + key + " - " + user)

    def somar(self,key, user):
        # fazendo update no Somar
        crSomar.execute("UPDATE apps.fnd_user SET FAX = '" + key + "' where user_name = '" + user + "'")
        conn_Somar.commit()
        print("SOMAR: " + key + " - " + user)

