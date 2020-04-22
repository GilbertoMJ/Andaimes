import sqlite3

connection = sqlite3.connect('databaseDados.db')
c = connection.cursor()

def CREATE():
    # CLIENTE #
    c.execute('CREATE TABLE IF NOT EXISTS CLIENTE (\
        `nome` VARCHAR (60) NOT NULL,\
        `endereco` VARCHAR (50),\
        `bairro` VARCHAR(20),\
        `cep` VARCHAR(9),\
        `cidade` VARCHAR(20),\
        `estado` VARCHAR(2),\
        `contato` VARCHAR(30),\
        `cpf` VARCHAR(14) NOT NULL,\
        `rg` VARCHAR(14),\
        `tipo` VARCHAR(1),\
        PRIMARY KEY(`cpf`));')
    # PEÇA #
    c.execute('CREATE TABLE IF NOT EXISTS PECA (\
        `codigo` VARCHAR(5) NOT NULL,\
        `nomeSingular` VARCHAR(25) NOT NULL,\
        `nomePlural` VARCHAR(25) NOT NULL,\
        `genero` VARCHAR(1) NOT NULL,\
        `preco` VARCHAR(8),\
        PRIMARY KEY(`codigo`));')
    # DOCUMENTO #
    c.execute('CREATE TABLE IF NOT EXISTS DOCUMENTO (\
        `nome` VARCHAR(20) NOT NULL,\
        `codigoDocumentoVBA` TEXT,\
        `codigoDocumentoPython` TEXT,\
        PRIMARY KEY(`nome`));')
    connection.commit()
    
CREATE()