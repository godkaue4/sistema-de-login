import sqlite3 as bd
import bcrypt as hash
class banco_de_dados():
    def __init__(self,nome_banco="usuarios.db"):
        self.nome_banco=nome_banco
        self.conxão=None
        self.cursor=None
        self.conectar()
        self.criar_tabela()

    def conectar(self):
      try:
         self.conexao=bd.connect(self.nome_banco)
         self.cursor=self.conexao.cursor()
         print('conexao realizada com sucesso')
      except:
         print('erro ao conectar com o banco de dados')
    def criar_tabela(self):
      sql="""
        CREATE TABLE IF NOT EXISTS usuarios(
          id  INTEGER PRIMARY KEY AUTOINCREMENT,
          usuario TEXT UNIQUE NOT NULL,           
          senha_hash TEXT NOT NULL,
          data TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
      try:
        self.cursor.execute(sql)
        self.conexao.commit()
        print('tabela criada com sucesso ')
      except bd.Error as erro:
         print(f"erro ao criar a tabela {erro}")
    def criar_hash(self,senha):
      return hash.hashpw(senha.encode('utf-8'), hash.gensalt())
    def verificar_senha(self,senha_digitada,hash_senha):
      senha_bytes=senha_digitada.encode('utf-8')
      if isinstance(hash_senha, str):
        hash_bytes=hash_senha.encode('utf-8')
      else:
        hash_bytes=hash_senha
      return hash.checkpw(senha_bytes,hash_bytes)

    def cadastrar(self, usuario, senha):
        try:
            hash_senha = self.criar_hash(senha).decode('utf-8')
            self.cursor.execute(
                "INSERT INTO usuarios (usuario, senha_hash) VALUES (?, ?)",
                (usuario, hash_senha)
            )
            self.conexao.commit()
            return True, "Cadastrado!"
        except bd.IntegrityError:
            return False, "Usuário já existe"
   #  def cadastrar_usuario(self,usuario,senha):
   #    if self.usuario_existe(usuario):
   #       return False,'usuario ja existe'
   #    senha_hash=self.criar_hash(senha)
   #    sql="INSERT INTO usuarios (usuario,senha_hash) VALUES (?,?)"
   #    try:
   #       self.cursor.execute(sql(usuario,senha_hash))
   #       self.conxão.commit()
   #       return True ,'usuario cadastrado com sucesso!'
   #    except sql.Error as erro:
   #      return False,f'ERRO! ao cadastrar o usuario:{erro}'
    def usuario_existe(self, usuario):
      sql_query = "SELECT id FROM usuarios WHERE usuario = ?"
      self.cursor.execute(sql_query, (usuario,))
      return self.cursor.fetchone() is not None
    def verificar_login(self,usuario,senha):
      sql_query="SELECT senha_hash FROM usuarios WHERE usuario=?" 
      self.cursor.execute(sql_query,(usuario,)) 
      resultado=self.cursor.fetchone()
      if resultado==None:
         return False,'usuarios não encontrado'
      senha_hash_banco=resultado[0]
      if self.verificar_senha(senha,senha_hash_banco):
         return True,'login feito com sucesso'
      else:
         return False,'senha incorreta'
       