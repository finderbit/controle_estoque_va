import sqlite3


querys_sqls = {
    "crete_table": """CREATE TABLE clientes (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        fone TEXT,
        bairro TEXT);""",

}


def receber_dados(*args):
    return args


conn = sqlite3.connect("clientes.db")
cursor = conn.cursor()
try:    
    cursor.execute(querys_sqls["crete_table"])
    conn.commit()
    print("Tabela criada")
    cursor.close()
    conn.close()
except:
    conn.close()
cursor.executemany("""
INSERT INTO clientes (nome, idade, cpf, email, fone, cidade, uf, criado_em)
VALUES (?,?,?,?,?,?,?,?)
""", )
