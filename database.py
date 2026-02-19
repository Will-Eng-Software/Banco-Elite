import sqlite3
import hashlib

# Configurações do Banco
NOME_BANCO = 'banco_elite.db'

def conectar():
    """Cria uma conexão com o banco de dados SQLite."""
    return sqlite3.connect(NOME_BANCO)

def inicializar_sistema():
    """Cria a tabela de contas se ela ainda não existir."""
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS contas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titular TEXT NOT NULL,
            pin_hash TEXT NOT NULL,
            saldo REAL DEFAULT 0.0
        )
    ''')
    conn.commit()
    conn.close()
    print("✅ Sistema de Dados Inicializado (Tabela 'contas' pronta).")

def cadastrar_cliente(nome, pin):
    """Gera o hash do PIN e salva o novo cliente no banco."""
    # 1. Gerar Segurança (Hashing)
    pin_hash = hashlib.sha256(str(pin).encode('utf-8')).hexdigest()
    
    conn = conectar()
    cursor = conn.cursor()
    
    try:
        cursor.execute('''
            INSERT INTO contas (titular, pin_hash, saldo) 
            VALUES (?, ?, ?)
        ''', (nome, pin_hash, 0.0))
        conn.commit()
        print(f"✅ Cliente '{nome}' cadastrado com sucesso e PIN protegido!")
    except Exception as e:
        print(f"❌ Erro ao cadastrar cliente: {e}")
    finally:
        conn.close()

# Bloco de Execução (Teste do Engenheiro)
if __name__ == "__main__":
    # 1. Garantir que a tabela existe
    inicializar_sistema()
    
    # 2. Testar um cadastro real
    nome_input = input("Nome do novo cliente: ")
    pin_input = input("Defina um PIN de 4 dígitos: ")
    
    cadastrar_cliente(nome_input, pin_input)