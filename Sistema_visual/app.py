from tkinter import *
from tkinter import messagebox
import DataBaser
from PIL import Image, ImageTk
from tkinter import filedialog

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
    menu_inicial.iconbitmap('Sistema_visual/Imagens/_123034.ico')
    menu_inicial['bg'] = '#00ffee'


    #Funções:


    def fazer_login():
        
        nome_de_login_usuario = text_usuario.get()
        senha_de_login_usuario = text_senha.get()

        #Nesta parte eu verifico se o cadastro de funcionario está salvo no bando de dados
        # Se estiver salvo, quando o funcionario coloar o login de funcionario ele terá acesso a aba de gerenciamento

        if  nome_de_login_usuario == 'funcionario' and senha_de_login_usuario == 'funcionario':
            try:
                    menu_inicial.destroy()
                    janela_funcionario()  

            except:
                pass


#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------


    #Esse código é usado para verificar se o que foi digitado pelo usuário está salvo no banco de dados:
            
        else:        

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

global caminho_arquivo 

def janela_funcionario():
    login_funcionario = Tk()
    login_funcionario.title('Gerenciamento')
    login_funcionario.geometry('500x250+200+200')
    login_funcionario.maxsize(500,500)
    login_funcionario.resizable(True,True)
    login_funcionario['bg'] = '#00ffee'


    #Funções:


    def abrir_imagem():
    
        global caminho_arquivo
        caminho_arquivo = filedialog.askopenfilename(initialdir="/", title="Selecione a imagem",
                                                     filetypes =(("Aquivos de imagem", "*.png;* .jpg;* .gif;* .bmp;* .ppm;* .pgm"),
                                                                 ("Todos os arquivos", "*.*")))
        
        if caminho_arquivo:
            imagem_original = Image.open(caminho_arquivo)
            # Redimensionar a imagem (substitua altura e largura pelos valores desejados)
            altura = 120
            largura = 120
            imagem_redimensionada = imagem_original.resize((largura, altura))
            imagem = ImageTk.PhotoImage(imagem_redimensionada)
            label_imagem.config(image=imagem)
            label_imagem.etiqueta = imagem #Referenciando a imagem
           
    global label_imagem

    def voltar_menu_inicial():
        login_funcionario.destroy()
        menu_inicial_registro()


    def RegistrarProdutos():
        Nome_Produto = text_cadastro_produto.get()
        Descricao_produto = text_descricao_produto.get()
        Preco_produto = text_preco_cadastro_produto.get()
        Quantidade_produto = text_quantidade_produto.get()

        if caminho_arquivo:
            with open(caminho_arquivo, 'rb') as file:
                Imagem_data = file.read()
          

        else:
            Imagem_data = None
        
        
        if  (Nome_Produto == '' and Descricao_produto == '' and Descricao_produto == '' and Preco_produto == '' and Preco_produto == '' and Imagem_data == '' or
            Nome_Produto == '' and Preco_produto == '' or
            Nome_Produto == '' and Quantidade_produto == '' or
            Nome_Produto == '' and Imagem_data == '' or
            Descricao_produto == '' and Preco_produto == '' or
            Descricao_produto == '' and Quantidade_produto == '' or
            Descricao_produto == '' and Imagem_data == '' or
            Preco_produto == '' and Quantidade_produto == '' or
            Preco_produto == '' and Imagem_data == '' or
            Imagem_data == '' or
            Nome_Produto == '' or
            Descricao_produto == '' or
            Preco_produto == '' or
            Imagem_data == ''
            ):
            messagebox.showerror(title= 'Cadastro', message= 'Preencha todos os campos do cadastro!')
         

        else:
            DataBaser.cursor.execute("""
            INSERT INTO CadastroEstoque(Nome, Descricao, Preco, Quantidade, Imagem) VALUES (?,?,?,?,?)
            """, (Nome_Produto, Descricao_produto, Preco_produto, Quantidade_produto, Imagem_data))
            DataBaser.conn.commit()
            messagebox.showinfo(title='Cadastro', message= 'Produto Cadastrado!')

            text_cadastro_produto.delete(0, 'end')
            text_descricao_produto.delete(0, 'end')
            text_preco_cadastro_produto.delete(0, 'end')
            text_quantidade_produto.delete(0, 'end')
            text_cadastro_produto.delete(0, 'end')
            label_imagem.etiqueta = None
            
    

    #Criar widgets:
    nome_cadastro_produto = Label(login_funcionario, text='Nome do produto:', bg='#00ffee')
    text_cadastro_produto = Entry(login_funcionario)
    descricao_cadastro_produto = Label(login_funcionario, text='Descrição:', bg='#00ffee')
    text_descricao_produto = Entry(login_funcionario)
    preco_cadastro_produto = Label(login_funcionario, text='Preço:', bg='#00ffee')
    text_preco_cadastro_produto = Entry(login_funcionario)
    quantidade_cadastro_produto = Label(login_funcionario, text='Quantidade:', bg='#00ffee')
    text_quantidade_produto = Entry(login_funcionario)
    imagem_produto = Label(login_funcionario, text="Carregar imagem:", bg='#00ffee')
    botao_abrir_imagem = Button(login_funcionario, command=abrir_imagem, text="Carregar")
    moldura_imagem_cadastro = Label(login_funcionario, bg="white", padx=60, pady=50)
    label_imagem = Label(login_funcionario)
    botao_voltar_menu_inicial = Button(login_funcionario, text= 'Voltar',command= voltar_menu_inicial , bg = 'yellow', fg = 'blue', width=8)
    botao_registrar_produtos = Button(login_funcionario, text='Registrar', command=RegistrarProdutos, bg = 'yellow', fg = 'blue', width=8)


    #Criar layout:

    nome_cadastro_produto.grid(row=4, column=0, sticky=W, pady=5, )
    text_cadastro_produto.grid(row=4, column=2, sticky=W, pady=5)
    descricao_cadastro_produto.grid(row=5, column=0, sticky=W, pady=5)
    text_descricao_produto.grid(row=5, column=2, sticky=W, pady=5)
    preco_cadastro_produto.grid(row=7, column=0, sticky=W, pady=5)
    text_preco_cadastro_produto.grid(row=7, column=2, sticky=W, pady=5)
    quantidade_cadastro_produto.grid(row=8, column=0, sticky=W, pady=5)
    text_quantidade_produto.grid(row=8, column=2, sticky=W, pady=5)
    imagem_produto.grid(row=9, column=0, sticky=W, pady=5)
    botao_abrir_imagem.grid(row=9, column=1, pady=5)
    moldura_imagem_cadastro.place(x=350, y=10)
    label_imagem.place(x=350, y=10)
    botao_voltar_menu_inicial.place(x=50, y=180)
    botao_registrar_produtos.place(x=150, y=180)



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




#menu_inicial_registro()

janela_funcionario()

#janela_cadastro()

#janela_pagina_de_compras()