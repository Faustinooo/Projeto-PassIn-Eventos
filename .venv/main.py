from mysql.connector import connect
import time
from datetime import datetime
from funções import *

data_atual = datetime.now()

while True:
    contador = 0

    linha2(32)
    cabeçalho("ESCOLHA SEU USUÁRIO:")
    print(f'''[0] SAIR
[1] ADMIN
[2] REGISTRAR USUÁRIO''')

    result = buscardados("users")

    for dados in result:
        print(f"[{dados[0]}] {dados[1]}")

    escolha = str(input("\nDigite o ID do Usuário: "))

    #-----------------------------------------------------------------------------------------

    if escolha == "0":
        linha2(31)
        cabeçalho("ENCERRANDO PROGRAMA")
        cabeçalho("ATÉ A PRÓXIMA")
        linha2(31)
        time.sleep(1)
        break

    if escolha == '1':
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

            if escolhaaction != 0 and escolhaaction != 1 and escolhaaction != 2 and escolhaaction != 3:
                linha2(31)
                cabeçalho("ESCOLHA UMA OPÇÃO VÁLIDA")
                linha2(31)
                continue

            if escolhaaction == 0:
                while True:
                    nome = input("Digite o Nome do Evento: ")
                    if nome != "":
                        break
                    else:
                        linha2(31)
                        cabeçalho("\033[31mNOME INVÁLIDO\033[m")
                        linha2(31)

                while True:
                    data = input("Digite a Data do Evento [DD/MM/YYYY]: ").strip("/")
                    verificacao = vefdata(data)
                    if verificacao == True:
                        break
                    else:
                        linha2(31)
                        cabeçalho("\033[31mDATA INVÁLIDA\033[m")
                        linha2(31)
                while True:
                    maximo = input("Digite a Capacidade Máxima: ")
                    if maximo.isalpha() or maximo == "" or int(maximo) <= 0:
                        linha2(31)
                        cabeçalho("\033[31mCAPACIDADE INVÁLIDA\033[m")
                        linha2(31)
                    else:
                        break

                date = f"{data[4:]}-{data[3:4]}-{data[0:2]}"
                date = f"{data[4:]}-{data[3:4]}-{data[0:2]}"
                dato = f"{data[0:2]}/{data[3:4]}/{data[4:]}"
                nume = str(f"{nome}").replace(" ", "")
                name = f"{nome} - {dato} - 0/{maximo}"

                query(comando=f"insert into testeDB.eventos values (default, '{name}', '{date}', '{maximo}', '{nome}','{nume}', '')")

                tabela(nume)
                linha2(34)
                print("\n\033[32mEVENTO CRIADO COM SUCESSO!\033[m\n")
                linha2(34)
                time.sleep(2)

            if escolhaaction == 1:
                eventoscad = buscardados("eventos")

                if len(eventoscad) == 0:
                    linha2(31)
                    cabeçalho("NÃO HÁ EVENTOS DISPONÍVEIS")
                    linha2(31)
                    continue

                ids = ""
                result = buscardados("eventos")
                for i, coluna in enumerate(result):
                    print(f"[{coluna[0]}] {coluna[1]}\n")
                    ids += f"{coluna[0]}"
                while True:
                    inspecionar = str(input("Deseja inspecionar qual evento: "))
                    if inspecionar not in ids:
                        linha2(31)
                        cabeçalho("\033[31mID INVÁLIDO\033[m")
                        linha2(31)
                    else:
                        break

                result = buscardados("eventos")

                instabela = ""
                dataevento = ""
                maximoevento = 0
                numero = 0
                for i, v in enumerate(result):
                    numero = v[0]
                    if numero == int(inspecionar):
                        instabela = v[5]
                        dataevento = v[2]
                        maximoevento = v[3]
                print(f'''
Nome: {instabela}
Data: {dataevento}
Capacidade Máxima: {maximoevento} 
                
Participantes:''')

                result = buscardados(instabela)

                for i in result:
                    print(f"-{i[1]}")
                time.sleep(2)

            if escolhaaction == 2:
                eventoscad = buscardados("eventos")

                if len(eventoscad) == 0:
                    linha2(31)
                    cabeçalho("NÃO HÁ EVENTOS DISPONÍVEIS")
                    linha2(31)
                    continue

                ids = ""
                result = buscardados("eventos")
                for i, coluna in enumerate(result):
                    print(f"[{coluna[0]}] {coluna[1]}\n")
                    ids += f"{coluna[0]}"

                while True:
                    apagar = str(input("Deseja Apagar qual evento: "))
                    if apagar not in ids:
                        linha2(31)
                        cabeçalho("\033[31mID INVÁLIDO\033[m")
                        linha2(31)
                    else:
                        break

                result = buscardados("eventos")
                aptabela = ""
                numero = 0
                for i, v in enumerate(result):
                    numero = v[0]
                    if numero == int(apagar):
                        aptabela = v[5]

                #--------------------------------------------------------------------------------------------------

                query(f'''delete from eventos where (nometabela = '{aptabela}');''')
                query(f'''UPDATE users SET evento = '' WHERE evento = '{aptabela}';''')

                #---------------------------------------------------------------------------------------------------

                query(f'''drop table {aptabela};''')

            if escolhaaction == 3:
                linha2(31)
                cabeçalho("SAINDO DO USUÁRIO...")
                linha2(31)
                time.sleep(2)
                break

    if escolha == '2':
        linha2(33)
        cabeçalho("REGISTRAR NOVO USUARIO:")
        while True:
            nome = str(input("Digite o Nome do Evento: ")).upper()
            if nome != "":
                break
            else:
                linha2(31)
                cabeçalho("\033[31mNOME INVÁLIDO\033[m")
                linha2(31)
        while True:
            data = input("Digite a Data do Evento [DD/MM/YYYY]: ").strip("/")
            verificacao = vefdata(data)
            if verificacao == True:
                break
            else:
                linha2(31)
                cabeçalho("\033[31mDATA INVÁLIDA\033[m")
                linha2(31)
        date = f"{data[4:]}-{data[3:4]}-{data[0:2]}"
        ident = f"{nome[:2]}{data[4:]}{data[3:4]}{data[0:2]}"
        query(f"insert into users (id, nome, nascimento, idade, evento) values ('{ident}', '{nome}','{date}','','')")
        linha2(33)
        continue

    #---------------------------------------------------------------------------------------------------------------------------

    if escolha != 0 and escolha != 1 and escolha != 2:

        result = buscardados("users")

        listaid = []
        for i in result:
            listaid.append(i[0])
        if escolha in listaid:
            pass
        else:
            linha2(31)
            cabeçalho("\033[31mUSUÁRIO INVÁLIDO\033[m")
            linha2(31)
            continue

        while True:

            result = buscardados("users")
            dadosuser = []
            nome = ""
            for i, v in enumerate(result):
                if v[0] == escolha:
                    nome = v[1]
                    dadosuser = v
            linha2(34)
            cabeçalho(f"USUÁRIO: {nome}")
            cabeçalho("OPÇÕES:")
            print(f'''[0] SAIR
[1] REGISTRAR EM UM EVENTO
[2] REALIZAR CHECK IN
[3] VISUALIZAR FICHA DE INSCRIÇÃO
[4] SAIR DO EVENTO REGISTRADO''')
            escolhaaction = int(input("\nDigite o Número da Ação: "))

            if escolhaaction != 0 and escolhaaction != 1 and escolhaaction != 2 and escolhaaction != 3 and escolhaaction != 4:
                linha2(31)
                cabeçalho("ESCOLHA UMA OPÇÃO VÁLIDA")
                linha2(31)
                continue

            if escolhaaction == 0:
                linha2(31)
                cabeçalho("SAINDO DO USUÁRIO...")
                linha2(31)
                time.sleep(2)
                break

            if escolhaaction == 1:
                eventoscad = buscardados("eventos")

                if len(eventoscad) == 0:
                    linha2(31)
                    cabeçalho("NÃO HÁ EVENTOS DISPONÍVEIS")
                    linha2(31)
                    continue

                if dadosuser[4] != "":
                    linha2(31)
                    cabeçalho(f"JÁ ESTÁ REGISTRADO NO EVENTO [{dadosuser[4]}]")
                    linha2(31)
                else:

                    result = buscardados("eventos")
                    ids = ""
                    for i, coluna in enumerate(result):
                        print(f"[{coluna[0]}] {coluna[1]}\n")
                        ids += f"{coluna[0]}"
                    while True:
                        registrar = str(input("Deseja se registrar em qual evento: "))
                        if registrar not in ids:
                            linha2(31)
                            cabeçalho("\033[31mID INVÁLIDO\033[m")
                            linha2(31)
                        else:
                            break

                    #===========================================================================================================

                    result = buscardados("eventos")
                    eventoreg = str("").lower()
                    for i, v in enumerate(result):
                        if v[0] == int(registrar):
                            eventoreg = v[5]
                            maxevento = v[3]
                            dataev = v[2]
                            nomeatual = v[1]
                            nometotal = v[4]
                            inscritoss = v[6]

                    result = buscardados(eventoreg)

                    #CADASTRO DO USUÁRIO
                    inscritoss += 1
                    query(f"update eventos set inscritos = '{inscritoss}' where (titulo = '{nomeatual}');")
                    nomenovo = f"{nometotal} - {dataev} - {inscritoss}/{maxevento}"
                    neme = dadosuser[1]
                    datoi = dadosuser[2]
                    dataatual = data_atual.strftime("%Y-%m-%d")
                    ident = dadosuser[0]
                    query(f"insert into {eventoreg} (id, nome, datacompra, datacheckin) values ('{ident}', '{neme}','{dataatual}','')")
                    nomemin = eventoreg.lower()
                    print(f"{nomemin} e {dadosuser[0]}")
                    query(f"update users set evento = '{nomemin}' where id = '{dadosuser[0]}';")

                    # TROCAR NUMERO DE PESSOAS NO EVENTO

                    query(f'''UPDATE eventos SET titulo = '{nomenovo}' WHERE titulo = '{nomeatual}';''')
                    linha2(33)
                    cabeçalho(f"REGISTRO REALIZADO")
                    linha2(33)

            if escolhaaction == 2:

                result = buscareventos(dadosuser[4])
                checkin = ""
                for i in result:
                    if i[0] == dadosuser[0]:
                        checkin = i[3]

                if checkin != None:
                    linha2(31)
                    cabeçalho(f"CHECK-IN JÁ FOI REALIZADO NO DIA [{checkin}]")
                    linha2(31)

                else:
                    nomeevento = dadosuser[4]
                    datacheck = data_atual.strftime("%Y-%m-%d")
                    query(f'''update {nomeevento} set datacheckin = '{datacheck}' where (id = '{dadosuser[0]}');''')
                    linha2(33)
                    cabeçalho("CHECK-IN REALIZADO COM SUCESSO")
                    linha2(33)

            if escolhaaction == 3:
                linha2(35)
                cabeçalho("FICHA DE INSCRIÇÃO")
                print(f'''ID = {dadosuser[0]}
NOME: {dadosuser[1]}
DATA DE NASCIMENTO: {dadosuser[2]}
IDADE: {idade_now(dadosuser[2])} ANOS''')
                if dadosuser[4] != "":
                    print(f"EVENTO INSCRITO: {dadosuser[4]}")

                linha2(35)
            if escolhaaction == 4:
                if dadosuser[4] != "":
                    query(f'''delete from {dadosuser[4]} where (id = '{dadosuser[0]}')''')

                    result = buscardados("eventos")
                    for v in result:
                        if v[5] == dadosuser[4]:
                            eventoreg = v[5]
                            maxevento = v[3]
                            dataev = v[2]
                            nomeatual = v[1]
                            nometotal = v[4]
                            inscritos = int(v[6])
                            id = v[0]

                    inscritos -= 1
                    query(f"update eventos set inscritos = '{inscritos}' where (id  = '{id}');")
                    nomenovo = f"{nometotal} - {dataev} - {inscritos}/{maxevento}"

                    query(f'''UPDATE eventos SET titulo = '{nomenovo}' WHERE titulo = '{nomeatual}';''')
                    query(f'''update users set evento = "" where (id = '{dadosuser[0]}');''')

                    linha2(32)
                    cabeçalho("INSCRIÇÃO CANCELADA COM SUCESSO")
                    linha(32)
                else:
                    linha2(31)
                    cabeçalho("USUÁRIO NÃO REGISTRADO EM NENHUM EVENTO")
                    linha2(31)