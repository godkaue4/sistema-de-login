import tkinter as tk
from tkinter import messagebox
import interface
class cadastro():
    def __init__(self):
        self.janela_de_cadastro=tk.Tk()
        self.janela_de_cadastro.config(bg='#65AEF7')
        self.config_interface()
        self.widget()
        self.iniciar()
    def config_interface(self):
        self.janela_de_cadastro.title('system login')
        self.janela_de_cadastro.geometry('300x400')
    def widget(self):
        self.frame_principal=tk.Frame(self.janela_de_cadastro,bg='#65AEF7',)
        self.frame_principal.pack(expand=True,fill='both',pady=20,padx=20)
        tk.Label(self.frame_principal,
                 text='cadastrar',
                 bg='#65AEF7',
                 fg="#5928CC",
                 anchor='e',
                 font=('Arial',12,'bold')).pack(pady=(0,30),side='top')
        self.novo_user()
        self.new_senha()
        self.botao()
    def novo_user(self):
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
    def new_senha(self):
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
    def botao(self):
        frame_cadastro=tk.Frame(self.frame_principal,bg='#65AEF7')
        frame_cadastro.place(x=100,y=200)
        cadastro_button=tk.Button(frame_cadastro,text='cadastrar',width=5,height=1,font=('Arial',12),command=self.verificação,padx=10,pady=3)
        cadastro_button.pack(pady=5)
    def verificação(self):
        erro=False
        while erro==False:
            usuario=self.entry_new_usuario.get()
            senha=self.entry_new_senha.get()
            if not usuario or not senha:
                messagebox.showwarning('ATENÇÂO!','complete todos os campos pedidos')
                return erro
            if len(usuario) <3:
                messagebox.showinfo('INfO','O USUARIO DEVE TER NO MINIMO 3 CARACTERE!')
                return erro
            if len(senha)<3:
                messagebox.showinfo('INFO','A SENHA DEVE TER NO MINIMO 3 CARACTERE!')
                return erro
            else:
                erro=True
        self.janela_de_cadastro.destroy()
        interface.login()
    def iniciar(self):
        self.janela_de_cadastro.mainloop()

cadastrar=cadastro()