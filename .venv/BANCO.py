from mysql.connector import connect
from funções import *

query(f'''CREATE TABLE eventos(
    `id` int auto_increment primary key,
    `titulo` varchar(100) not null,
    `data` date,
    `Maximo` int not null ,
    `nome` varchar(40),
    `nometabela` VARCHAR(40),
    `inscritos` int
);''')

query(f'''create table users(
    `id` varchar(10) not null primary key,
    `nome` varchar(40) not null,
    `nascimento` date not null,
    `idade` tinyint,
    `evento` varchar(40)
);''')

print("BANCO DE DADOS ATUALIZADO COM SUCESSO")
