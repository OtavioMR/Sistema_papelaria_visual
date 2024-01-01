from tkinter import *
from tkinter import messagebox
import DataBaser

#Variável global:
menu_inicial = ''



#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#--------------------------JANELA DO MENU INICIAL-----------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


def menu_inicial_registro():
    
    global menu_inicial
    menu_inicial = Tk()
    menu_inicial.title('Papelaria Otávio')
    menu_inicial.geometry('500x250+200+200')
    menu_inicial.maxsize(500,500)
    menu_inicial.resizable(True,True)
    menu_inicial.iconbitmap('Sistema_visual\Imagens\_123034.ico')
    menu_inicial['bg'] = '#00ffee'


    #Funções:

    #Esse código é usado para verificar se o que foi digitado pelo usuário está salvo no banco de dados:
    
    def fazer_login():
        nome_de_login_usuario = text_usuario.get()
        senha_de_login_usuario = text_senha.get()

        DataBaser.cursor.execute("""
        SELECT * FROM Cadastro
        WHERE (Nome = ? and Senha = ?)
        """,(nome_de_login_usuario, senha_de_login_usuario))
        print('Selecionou')
        verificar_login = DataBaser.cursor.fetchone()
        try:

            if (nome_de_login_usuario in verificar_login and senha_de_login_usuario in verificar_login):
                messagebox.showinfo(title='Login', message= 'Login confirmado!')
                menu_inicial.destroy()
                janela_pagina_de_compras()
                

        except:
            messagebox.showinfo(title= 'Login', message= 'Conta não localizada')

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------


        #Nesta parte eu verifico se o cadastro de funcionario está salvo no bando de dados
        # Se estiver salvo, quando o funcionario coloar o login de funcionario ele terá acesso a aba de gerenciamento
        
        DataBaser.cursor.execute("""
        SELECT * FROM Cadastro
        WHERE (Nome = ? and Senha = ?)
        """,('funcionario', 'funcionario'))
        print('Selecionou')
        verificar_login = DataBaser.cursor.fetchone()
        try:

            if (nome_de_login_usuario in verificar_login and senha_de_login_usuario in verificar_login):
                menu_inicial.destroy()
                janela_funcionario()
                

        except:
            pass


#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------


    #Criar widgets:

    label_1 = Label(menu_inicial, text = 'Entre na sua conta', bg = '#00ffee', font = 'Arial 20')
    login_usuario = Label(menu_inicial, text = 'Usuário:', bg =  '#00ffee')
    login_senha = Label(menu_inicial, text = 'Senha:', bg =  '#00ffee')
    text_usuario = Entry(menu_inicial)
    text_senha = Entry(menu_inicial, show='*')
    botao_cadastrar = Button(menu_inicial, text = 'Criar conta', command= janela_cadastro, bg = 'yellow', fg = 'blue', width=8)
    botao_login = Button(menu_inicial, text= 'Login', bg = 'yellow', fg = 'blue', width=8, command= fazer_login)




    #Criar layout:

    label_1.grid(row = 0, column = 1, pady=20)
    login_usuario.grid(row = 2, column = 0, sticky = W)
    login_senha.grid(row = 3, column = 0, sticky = W)
    #Para usar focus, precisa ser escrito tudo separado!
    text_usuario.grid(row = 2, column = 1, sticky= 'w')
    text_usuario.focus()
    text_senha.grid(row = 3, column = 1, sticky= 'w')
    botao_cadastrar.grid(row = 5, column = 1, sticky=W, pady=15)
    botao_login.grid(row = 5, column = 1)

    menu_inicial.mainloop()


#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#------------------------JANELA DE LOGIN FUNCIONÁRIO--------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
    

def janela_funcionario():
    login_funcionario = Tk()
    login_funcionario.title('Gerenciamento')
    login_funcionario.geometry('500x250+200+200')
    login_funcionario.maxsize(500,500)
    login_funcionario.resizable(True,True)
    login_funcionario['bg'] = '#00ffee'

    #Funções:
    

    #Criar widgets:
    botao_voltar_menu_inicial = Button(login_funcionario, text='Voltar para menu inicial')

    #Criar layout:
    botao_voltar_menu_inicial.pack()

    login_funcionario.mainloop()


#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#------------------------JANELA DE CADASTRO DE CONTA--------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------


def janela_cadastro():
    menu_inicial.destroy()
    cadastro_de_conta = Tk()
    cadastro_de_conta.title('Cadastre sua conta')
    cadastro_de_conta.geometry('500x250+200+200')
    cadastro_de_conta.maxsize(500,500)
    cadastro_de_conta.resizable(True,True)
    cadastro_de_conta['bg'] = '#00ffee'

    #Funções:

    def voltar_menu_inicial():
        cadastro_de_conta.destroy()
        menu_inicial_registro()    


    def RegistrarBancoDeDados():

        Nome_usuario = text_cadastramento_usuario.get()
        Email_usuario = text_cadastramento_email.get()
        Senha_usuario = text_cadastramento_senha.get()

        if (Nome_usuario == '' and Email_usuario == '' and Senha_usuario == '' or
            Nome_usuario == '' and Email_usuario == '' or
            Nome_usuario == '' and Senha_usuario == '' or
            Email_usuario == '' and Senha_usuario == '' or
            Nome_usuario == '' or 
            Email_usuario == '' or
            Senha_usuario == ''
            ):
            messagebox.showerror(title= 'Cadastro', message= 'Preencha todos os campos do cadastro!')

        else:
            DataBaser.cursor.execute("""
            INSERT INTO Cadastro(Nome, Email, Senha) VALUES(?,?,?)
            """, (Nome_usuario, Email_usuario, Senha_usuario))
            DataBaser.conn.commit()
            messagebox.showinfo(title='Cadastro', message= 'Conta cadastrada!')

        

    #Criar widgets:

    Letreiro_01 = Label(cadastro_de_conta, text= 'Cadastre seus dados', bg= '#00ffee', font= 'Arial 20')
    cadastramento_usuario = Label(cadastro_de_conta, text= 'Usuário:', bg= '#00ffee')
    cadastramento_email = Label(cadastro_de_conta, text= 'Email:', bg= '#00ffee')
    cadastramento_senha = Label(cadastro_de_conta, text= 'Senha:', bg= '#00ffee')
    text_cadastramento_usuario = Entry(cadastro_de_conta)
    text_cadastramento_email = Entry(cadastro_de_conta)
    text_cadastramento_senha = Entry(cadastro_de_conta)
    botao_voltar_menu_inicial = Button(cadastro_de_conta, text= 'Voltar',command= voltar_menu_inicial , bg = 'yellow', fg = 'blue', width=8)
    botao_finalizar_cadastro = Button(cadastro_de_conta, text= 'Cadastrar',  bg = 'yellow', fg = 'blue', width=8, command= RegistrarBancoDeDados)


    #Criar layout:

    Letreiro_01.grid(row=0, column=1, pady= 20)
    cadastramento_usuario.grid(row=1, column=0, sticky= W) 
    cadastramento_email.grid(row=2, column=0, sticky= W)
    cadastramento_senha.grid(row=3, column=0, sticky= W)
    text_cadastramento_usuario.grid(row=1, column=1, sticky= W)
    text_cadastramento_usuario.focus()
    text_cadastramento_email.grid(row=2, column=1, sticky= W)
    text_cadastramento_senha.grid(row=3, column=1, sticky= W)
    botao_voltar_menu_inicial.grid(row=4, column=1, sticky= W, pady=15)
    botao_finalizar_cadastro.grid(row=4, column=1)
    


    cadastro_de_conta.mainloop()


#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
#-----------------------------JANELA DE COMPRAS-------------------------------
#-----------------------------------------------------------------------------
#-----------------------------------------------------------------------------
    

def janela_pagina_de_compras():
    #menu_inicial.destroy()
    pagina_de_compras = Tk()
    pagina_de_compras.title('Papelaria Otávio')
    pagina_de_compras.geometry('500x250+200+200')
    pagina_de_compras.maxsize(500,500)
    pagina_de_compras.resizable(True,True)
    pagina_de_compras['bg'] = '#00ffee'

    #Funções:

    #Criar widgets:

    #Criar layout:

    pagina_de_compras.mainloop()




menu_inicial_registro()

#janela_funcionario()

#janela_cadastro()

#janela_pagina_de_compras()