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

print('Conectado ao banco de dados')