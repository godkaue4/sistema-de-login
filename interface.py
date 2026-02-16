#importações
import tkinter as tk
from tkinter import messagebox
from banco import banco_de_dados
#cria a tela do login
class tela_de_login():
    """
    Docstring para tela_de_login
    a classe tela_de_login cria a interface de login
    metodo __init__:onde é criada a janela ,e o banco de dados, e tudo que é fundamental para o progama
    metodo frame_principal:cria o local na janela  onde sera colocados os widgets
    metodo criar_tela_login: cria tudo da tela login como botões ,caixa de texto e mais ,apartir de outros metodos
    metodo config_interface: cofigura a interface
    metodo iniciar :cria o loop da janela
    metodo criar_usuario:serve para criar o label e caixa de texto para o usuario
    metodo criar_senha:serve para criar o laebel e caixa de texto para a senha
    metodo login:serve para criar o botao de logar ,e ao clicar faz a verificações
    metodo cadastro_button:serve para criar o botao cadastrar e para reredicionar para tela de cadastro
    metodo fazer_login:serve para fazer as verificaçoes basicas e caso tudo esteja correto fara login
    metodo cadastrar: criar a tela de cadastro ,que é chamada apos clicar no botão cadastrar,e tambem cadastra o usuario no banco de dados
    metodo verifivar:submetodo de cadastro verifica se tudo esta correto e cadastra no bd caso esteja correto
    metodo voltar_para_login:fecha a tela de cadastro e  volta para a de login
    """
    def __init__(self):
        self.janela=tk.Tk()
        self.banco=banco_de_dados()
        self.janela.config(bg="#65AEF7")
        self.frame_pricipal()
        self.cria_tela_login()
        self.config_interface()
        self.cria_eventos()
        self.iniciar()

    def config_interface(self):
        self.janela.resizable(False,False)
        self.janela.title('system login')
        self.janela.geometry('300x400')
    def limpar_tela(self):
        for widget in self.frame_principal.winfo_children():
            widget.destroy()
    def frame_pricipal(self):
        self.frame_principal=tk.Frame(self.janela,bg="#65AEF7")
        self.frame_principal.pack(expand=True,fill='both',padx=20,pady=20)
    def cria_tela_login(self):
        self.limpar_tela()
        tk.Label(self.frame_principal,
                 text='login',
                 bg='#65AEF7',
                 fg="#5928CC",
                 anchor='e',
                 font=('Arial',12,'bold')).pack(pady=(0,30),side='top')
        self.criar_usuario()
        self.criar_senha()
        self.login()
        self.cadastro_button()
    def criar_usuario(self):
        frame_usuario=tk.Frame(self.frame_principal,bg='#65AEF7')
        frame_usuario.pack(pady=10)
        
        tk.Label(frame_usuario,
                                fg='black',
                                width=10,
                                font=('Arial',12),
                                anchor='n',
                                text='usuario',).pack(side='left',padx=(0,10))
        
        self.entry_usuario=tk.Entry(frame_usuario,width=19,font=('Arial',10))
        self.entry_usuario.pack(side='left')
        self.entry_usuario.focus()
    def criar_senha(self):
        frame_senha=tk.Frame(self.frame_principal,bg='#65AEF7')
        frame_senha.pack(pady=10)
        tk.Label(frame_senha,
                 text='senha',
                 fg='black',
                 width=10,
                 font=('Arial',12),
                 anchor='n').pack(side='left',padx=(0,10))
        self.entry_senha=tk.Entry(frame_senha,width=19,font=('Arial',10),show='*')
        self.entry_senha.pack(side='left')
    def login(self):
        frame_login=tk.Frame(self.frame_principal,bg='#65AEF7')
        frame_login.place(x=85,y=190)
        login_button=tk.Button(frame_login,text='login',
                               width=5,
                               height=1,
                               font=('Arial',12),
                               command=self.fazer_login,
                               padx=10,
                               pady=3)
        login_button.pack(pady=5)
    def cadastro_button(self):
        frame_cadastro=tk.Frame(self.frame_principal,bg='#65AEF7')
        frame_cadastro.place(x=165,y=190)
        cadastro_button=tk.Button(frame_cadastro,
                                  text='cadastrar',
                                  width=5,
                                  height=1,
                                  font=('Arial',12)
                                  ,command=self.cadastro,
                                  padx=10,pady=3)
        cadastro_button.pack(pady=5)
    
    def cria_eventos(self):
         self.janela.bind('<Return>',lambda e: self.fazer_login())
    def fazer_login(self):
        usuario=self.entry_usuario.get().strip()
        senha=self.entry_senha.get().strip()
        sucesso, mensagem=self.banco.verificar_login(usuario,senha)
        if not usuario or not senha:
                messagebox.showwarning('ATENÇÂO!','complete todos os campos pedidos')
                return 
        elif len(usuario) <3 or len(senha)<3:
                messagebox.showinfo('INfO','O USUARIO E SENHA  DEVE TER NO MINIMO 3 CARACTERE!')
                return
        if sucesso:
             messagebox.showinfo('INFO','login realizado com sucesso')
             return
        if mensagem:
             messagebox.showinfo('INFO',mensagem)
             return
    def iniciar(self):
        self.janela.mainloop()
    def cadastro(self):
        self.limpar_tela()
            # self.janela.config(bg='#65AEF7')
            # self.janela.title('system login')
            # self.janela.geometry('300x400')
            # self.frame_principal=tk.Frame(self.janela,bg='#65AEF7',)
            # self.frame_principal.pack(expand=True,fill='both',pady=20,padx=20)
        tk.Label(self.frame_principal,
                    text='cadastrar',
                    bg='#65AEF7',
                    fg="#5928CC",
                    anchor='e',
                    font=('Arial',12,'bold')).pack(pady=(0,30),side='top')
        frame_new_usuario=tk.Frame(self.frame_principal,bg='#65AEF7')
        frame_new_usuario.pack(pady=10)
            
        tk.Label(frame_new_usuario,
                                    fg='black',
                                    width=10,
                                    font=('Arial',12),
                                    anchor='n',
                                    text='usuario',).pack(side='left',padx=(0,10))
            
        self.entry_new_usuario=tk.Entry(frame_new_usuario,width=19,font=('Arial',10))
        self.entry_new_usuario.pack(side='left')
        self.entry_new_usuario.focus()
        frame_new_senha=tk.Frame(self.frame_principal,bg='#65AEF7')
        frame_new_senha.pack(pady=10)
        tk.Label(frame_new_senha,
                    text='senha',
                    fg='black',
                    width=10,
                    font=('Arial',12),
                    anchor='n').pack(side='left',padx=(0,10))
        self.entry_new_senha=tk.Entry(frame_new_senha,width=19,font=('Arial',10),show='*')
        self.entry_new_senha.pack(side='left')
        def verificar_cadastro():
                usuario=self.entry_new_usuario.get()
                senha=self.entry_new_senha.get()
                if not usuario or not senha:
                    messagebox.showwarning('ATENÇÂO!','complete todos os campos pedidos')
                    
                    return 
                if len(usuario) <3:
                    messagebox.showinfo('INfO','O USUARIO DEVE TER NO MINIMO 3 CARACTERE!')
                    self.entry_new_usuario.focus()
                    return 
                if len(senha)<3:
                    messagebox.showinfo('INFO','A SENHA DEVE TER NO MINIMO 3 CARACTERE!')
                    self.entry_new_senha.focus()
                    return 
                sucesso, mensagem= self.banco.cadastrar(usuario,senha)
                if sucesso:
                     messagebox.showinfo('INFO',f'usuario {usuario} cadastrado com sucesso')
                     self.voltar_para_login()   
                if mensagem:
                     messagebox.showinfo('INFO',mensagem)
        frame_cadastrar=tk.Frame(self.frame_principal,bg='#65AEF7')
        frame_cadastrar.pack(pady=30)
        cadastro_botao=tk.Button(frame_cadastrar,
                                     text='cadastrar',
                                     width=5,
                                     height=1,
                                     font=('Arial',12),
                                     command=verificar_cadastro,
                                     padx=10,pady=3)
        cadastro_botao.pack(pady=5) 
        
        frame_cancelar=tk.Frame(self.frame_principal,bg='#65AEF7')
        frame_cancelar.pack(pady=25,padx=30)
        botao_cancelar=tk.Button(frame_cancelar,text='cancelar',
                                 width=5,
                                 height=1,
                                 fg='red',
                                 command=self.voltar_para_login,
                                 padx=10,
                                 pady=3)
        botao_cancelar.pack(pady=5)
    def voltar_para_login(self):
             self.limpar_tela()
             self.cria_tela_login()
if __name__=="__main__":
     login=tela_de_login()
