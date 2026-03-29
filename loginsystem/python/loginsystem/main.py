# main.py
"""
==========================================
SISTEMA DE LOGIN COMPLETO
Desenvolvido por: kauê henrique pereira da silva
Idade: 16 anos
GitHub: [https://github.com/godkaue4]
==========================================
"""

import sys
import os
from interface import tela_de_login

def verificar_dependencias():
    """Verifica se todas as dependências estão instaladas"""
    try:
        import tkinter
        import sqlite3
        import hashlib
        return True
    except ImportError as e:
        print(f"❌ Erro: {e}")
        print("Instale as dependências com: pip install -r requirements.txt")
        return False

def criar_arquivo_requirements():
    """Cria arquivo requirements.txt se não existir"""
    if not os.path.exists("requirements.txt"):
        with open("requirements.txt", "w", encoding="utf-8") as f:
            f.write("# Dependências do Sistema de Login\n")
            f.write("# Python 3.x já inclui tudo necessário\n")
            f.write("# Nenhum pacote extra necessário!\n")
            f.write("\n")
            f.write("# Para desenvolvimento:\n")
            f.write("# pip install pyinstaller  # Para criar executável\n")
        print("📄 Arquivo requirements.txt criado")

def main():
    """Função principal"""
    print("\n" + "="*60)
    print("        🔐 SISTEMA DE LOGIN - INICIANDO")
    print("="*60)
    
    # Verifica dependências
    if not verificar_dependencias():
        input("Pressione Enter para sair...")
        sys.exit(1)
    
    # Cria arquivo de requirements
    criar_arquivo_requirements()
    
    # Mostra informações
    print("\n📋 INFORMAÇÕES DO SISTEMA:")
    print(f"   • Diretório atual: {os.getcwd()}")
    print(f"   • Banco de dados: usuarios.db")
    print(f"   • Interface: Tkinter")
    print(f"   • Autor: Kauê henrique")
    
    print("\n⏳ Inicializando interface gráfica...")
    
    try:
        # Cria e executa a aplicação
        app = tela_de_login()
        print("✅ Sistema executado com sucesso!")
        
    except Exception as e:
        print(f"\n❌ ERRO CRÍTICO: {e}")
        print("\nSolução de problemas:")
        print("1. Verifique se o Python está instalado corretamente")
        print("2. Execute como administrador se necessário")
        print("3. Tente reinstalar o Python")
        input("\nPressione Enter para sair...")
    
    print("\n👋 Programa finalizado. Até mais!")

# Ponto de entrada
if __name__ == "__main__":
    main()