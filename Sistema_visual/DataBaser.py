import sqlite3

conn = sqlite3.connect('RegistroData.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS Cadastro (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Email TEXT NOT NULL,
    Senha TEXT NOT NULL
);
""")


cursor.execute("""
CREATE TABLE IF NOT EXISTS CadastroEstoque (
    Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Descricao TEXT NOT NULL,
    Preco REAL NOT NULL,
    Quantidade INTEGER NOT NULL,
    Imagem BLOB
);
""")

print('Conectado ao banco de dados')