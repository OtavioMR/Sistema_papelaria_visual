import sqlite3

def delete_tabela():
    conn = sqlite3.connect('RegistroData.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Usuario")
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='Usuario'")
    conn.commit()
    conn.close()



def delete_linha():
    conn = sqlite3.connect('RegistroData.db')
    cursor = conn.cursor()
    usuario_id_para_apagar = ####
    sql = f"DELETE FROM Cadastro WHERE id = {usuario_id_para_apagar}"
    try:
        cursor.execute(sql)
        conn.commit()
        print("Registro excluído com sucesso!")
    except sqlite3.Error as e:
        print("Erro ao excluir o registro:")
    finally:
        cursor.close()
        conn.close()


#delete_linha()
        
#delete_tabela()