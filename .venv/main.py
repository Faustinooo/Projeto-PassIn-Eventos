from mysql.connector import connect
import time
from datetime import datetime

data_atual = datetime.now()

# FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES

def mysql_connection(host, user, passwd, database=None):
    connection = connect(
        host=host,
        user=user,
        passwd=passwd,
        database=database
    )
    return connection


def linha(a=0):
    print(f"\033[1;{a}m-=\033[m" * 20)


def cabeçalho(a="TEXTO"):
    print(f"\033[1m{a.center(40)}\033[m")


def linha2(a=0):
    print(f"\033[1;{a}m-=\033[m" * 20)


def query(comando=""):
    connection = mysql_connection('localhost', 'root', '', database='testeDB')
    query_string = f'''
                {comando}
                '''
    cursor = connection.cursor()
    cursor.execute(query_string)
    connection.close()


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


# FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES FUNCOES
while True:
    contador = 0

    linha2(32)
    cabeçalho("ESCOLHA SEU USUÁRIO:")
    print(f'''[0] SAIR
[1] ADMIN
[2] REGISTRAR USUÁRIO''')

    connection = mysql_connection('localhost', 'root', '', database='testeDB')
    query_string = '''
                SELECT * FROM users;
                                                    '''
    cursor = connection.cursor()
    cursor.execute(query_string)
    result = cursor.fetchall()
    for dados in result:
        print(f"[{dados[0]}] {dados[1]}")
    connection.close()

    escolha = int(input("\nDigite o ID do Usuário: "))

    #-----------------------------------------------------------------------------------------

    if escolha == 0:
        linha2(31)
        cabeçalho("ENCERRANDO PROGRAMA")
        cabeçalho("ATÉ A PRÓXIMA")
        linha2(31)
        time.sleep(1)
        break

    if escolha == 1:
        while True:
            linha2(32)
            cabeçalho("ADMINISTRADOR")
            cabeçalho("OPÇÕES: ")
            print('''[0] - CRIAR NOVO EVENTO
[1] - VER EVENTOS
[2] - APAGAR EVENTOS
[3] - SAIR DO USUÁRIO''')
            escolhaaction = int(input("\nDigite o Número da Ação: "))
            linha2(32)

            if escolhaaction == 0:
                nome = input("Digite o Nome do Evento: ")
                data = input("Digite a Data do Evento: ")
                maximo = input("Digite a Capacidade Máxima: ")
                date = f"{data[4:]}-{data[3:4]}-{data[0:2]}"
                dato = f"{data[0:2]}/{data[3:4]}/{data[4:]}"
                nume = str(f"{nome}").replace(" ", "")
                name = f"{nume} - {dato} - 0/{maximo}"

                query(comando=f"insert into testeDB.eventos values (default, '{name}', '{date}', '{maximo}', '{nume}')")

                tabela(nome)
                linha2(34)
                print("\n\033[32mEVENTO CRIADO COM SUCESSO!\033[m\n")
                linha2(34)
                time.sleep(2)
            if escolhaaction == 1:
                connection = mysql_connection('localhost', 'root', '', database='testeDB')
                query_string = '''
                    SELECT * FROM eventos;
                '''
                cursor = connection.cursor()
                cursor.execute(query_string)
                result = cursor.fetchall()
                for i, coluna in enumerate(result):
                    print(f"[{coluna[0]}] {coluna[1]}\n")
                connection.close()
                inspecionar = int(input("Deseja inspecionar qual evento: "))

                connection = mysql_connection('localhost', 'root', '', database='testeDB')
                query_string = '''
                                    SELECT * FROM eventos;
                                '''
                cursor = connection.cursor()
                cursor.execute(query_string)
                result = cursor.fetchall()
                instabela = ""
                dataevento = ""
                maximoevento = 0
                numero = 0
                for i, v in enumerate(result):
                    numero = v[0]
                    if numero == inspecionar:
                        instabela = v[4]
                        dataevento = v[2]
                        maximoevento = v[3]
                print(f'''
Nome: {instabela}
Data: {dataevento}
Capacidade Máxima: {maximoevento} 
                
Participantes:''')
                connection.close()

                connection = mysql_connection('localhost', 'root', '', database='testeDB')
                query_string = f'''
                            SELECT * FROM {instabela};
                                                '''
                cursor = connection.cursor()
                cursor.execute(query_string)
                result = cursor.fetchall()
                for i in result:
                    print(f"-{i[1]}")
                time.sleep(2)

            if escolhaaction == 2:
                connection = mysql_connection('localhost', 'root', '', database='testeDB')
                query_string = '''
                                    SELECT * FROM eventos;
                                '''
                cursor = connection.cursor()
                cursor.execute(query_string)
                result = cursor.fetchall()
                for i, coluna in enumerate(result):
                    print(f"[{coluna[0]}] {coluna[1]}\n")
                connection.close()
                inspecionar = int(input("Deseja Apagar qual evento: "))

                connection = mysql_connection('localhost', 'root', '', database='testeDB')
                query_string = '''
                                    SELECT * FROM eventos;
                                                '''
                cursor = connection.cursor()
                cursor.execute(query_string)
                result = cursor.fetchall()
                aptabela = ""
                numero = 0
                for i, v in enumerate(result):
                    numero = v[0]
                    if numero == inspecionar:
                        aptabela = v[4]
                connection.close()

                #--------------------------------------------------------------------------------------------------

                connection = mysql_connection('localhost', 'root', '', database='testeDB')
                query_string = f'''
                        delete from eventos where (nome = '{aptabela}');
                                '''
                cursor = connection.cursor()
                cursor.execute(query_string)
                connection.close()

                #---------------------------------------------------------------------------------------------------

                connection = mysql_connection('localhost', 'root', '', database='testeDB')
                query_string = f'''
                        drop table {aptabela};
                                                '''
                cursor = connection.cursor()
                cursor.execute(query_string)
                connection.close()

            if escolhaaction == 3:
                linha2(31)
                cabeçalho("SAINDO DO USUÁRIO...")
                linha2(31)
                time.sleep(2)
                break

    if escolha == 2:
        linha2(33)
        cabeçalho("REGISTRAR NOVO USUARIO:")
        nome = input("Digite Seu Nome: ").upper()
        data = input("Digite Sua Data de Nascimento: ")
        date = f"{data[4:]}-{data[3:4]}-{data[0:2]}"
        ident = f"`{nome[:2]}{data[4:]}"
        query(f"insert into users (id, nome, nascimento, idade, evento) values ('{ident}', '{nome}','{date}','','')")
        arquivooo = open('user.txt', 'a', encoding='utf8')
        arquivooo.write(f"\n{nome.title()}")
        arquivooo.close()
    #---------------------------------------------------------------------------------------------------------------------------

    if escolha != 0 and escolha != 1 and escolha != 2:
        connection = mysql_connection('localhost', 'root', '', database='testeDB')
        query_string = '''
                                            SELECT * FROM users;
                                                        '''
        cursor = connection.cursor()
        cursor.execute(query_string)
        result = cursor.fetchall()
        dadosuser = []
        nome = ""
        for i, v in enumerate(result):
            if v[0] == escolha:
                nome = v[1]
                dadosuser = v
        connection.close()
        linha2(34)
        cabeçalho(f"USUÁRIO: {nome}")
        cabeçalho("OPÇÕES:")
        print(f'''[0] SAIR
[1] REGISTRAR EM UM EVENTO
[2] REALIZAR CHECK IN
[3] VISUALIZAR FICHA DE INSCRIÇÃO''')
        escolhaaction = int(input("\nDigite o Número da Ação: "))
        if escolha == 0:
            linha2(31)
            cabeçalho("SAINDO DO USUÁRIO...")
            linha2(31)
            time.sleep(2)
            break

        if escolhaaction == 1:
            connection = mysql_connection('localhost', 'root', '', database='testeDB')
            query_string = '''
                                                SELECT * FROM eventos;
                                            '''
            cursor = connection.cursor()
            cursor.execute(query_string)
            result = cursor.fetchall()
            for i, coluna in enumerate(result):
                print(f"[{coluna[0]}] {coluna[1]}\n")
            connection.close()
            registrar = int(input("Deseja se registrar em qual evento: "))

            #===========================================================================================================

            connection = mysql_connection('localhost', 'root', '', database='testeDB')
            query_string = '''
                                                        SELECT * FROM eventos;
                                                                    '''
            cursor = connection.cursor()
            cursor.execute(query_string)
            result = cursor.fetchall()
            eventoreg = str("").lower()
            for i, v in enumerate(result):
                if v[0] == registrar:
                    eventoreg = v[4]
            connection.close()
            neme = dadosuser[1]
            datoi = dadosuser[2]
            dataatual = data_atual.strftime("%Y-%m-%d")
            query(f"insert into {eventoreg} (id, nome, datacompra, datacheckin) values (default, '{neme}','{dataatual}','')")






