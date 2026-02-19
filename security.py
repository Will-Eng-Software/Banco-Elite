import hashlib

def gerar_hash_pin(pin):
    """Transforma o PIN em um Hash SHA-256 seguro."""
    # Convertemos o PIN para string e depois para bytes
    pin_bytes = str(pin).encode('utf-8')
    # Geramos o Hash
    hash_objeto = hashlib.sha256(pin_bytes)
    return hash_objeto.hexdigest()

def verificar_pin(pin_digitado, hash_armazenado):
    """Verifica se o PIN digitado corresponde ao Hash no banco."""
    return gerar_hash_pin(pin_digitado) == hash_armazenado

# Teste Rápido
if __name__ == "__main__":
    pin_usuario = "3107"
    hash_para_banco = gerar_hash_pin(pin_usuario)
    
    print(f"PIN Original: {pin_usuario}")
    print(f"O que será salvo no DB: {hash_para_banco}")