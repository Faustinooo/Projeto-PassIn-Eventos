from mysql.connector import connect

import time
from datetime import datetime

def idade_now(data_nascimento):
    data_atual1 = datetime.now()
    ano_atual = data_atual1.year
    mes_atual = data_atual1.month
    dia_atual = data_atual1.day

    data_nascimento = str(data_nascimento)

    ano_nascimento = int(data_nascimento[:4])
    mes_nascimento = int(data_nascimento[5:7]) #2006-08-24
    dia_nascimento = int(data_nascimento[8:])  #0123456789

    idade = ano_atual - ano_nascimento

    # Verificar se ainda não fez aniversário este ano
    if mes_atual < mes_nascimento or (mes_atual == mes_nascimento and dia_atual < dia_nascimento):
        idade -= 1

    return idade

def linha(a=0):
    print(f"\033[1;{a}m-=\033[m" * 20)


def cabeçalho(a="TEXTO"):
    print(f"\033[1m{a.center(40)}\033[m")


def linha2(a=0):
    print(f"\033[1;{a}m-=\033[m" * 20)



# TROQUE AS INFORMÇÕES DA VARIÁVEL CONNECTION DE ACORDO COM A SUA CONEXÃO
def query(comando=""):
    connection = mysql_connection('localhost', 'root', '', database='testeDB')
    query_string = f'''
                {comando}
                '''
    cursor = connection.cursor()
    cursor.execute(query_string)
    connection.close()



# TROQUE AS INFORMÇÕES DA VARIÁVEL CONNECTION DE ACORDO COM A SUA CONEXÃO
def tabela(a=""):
    connection = mysql_connection('localhost', 'root', '', database='testeDB')
    query_string = f'''
                create table {a.strip()}(
                `id` varchar(10) primary key not null,
                `nome` varchar(100) not null,
                `datacompra` date,
                `datacheckin` date
                 );
                '''
    cursor = connection.cursor()
    cursor.execute(query_string)
    connection.close()

def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host=host,
        user=user,
        passwd=passwd,
        database=database
    )
    return connection

# FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES