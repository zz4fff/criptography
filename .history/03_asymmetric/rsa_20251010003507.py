from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64

# Gerar par de chaves RSA
chave = RSA.generate(2048)
print("Chave privada: ", chave)
chave_publica = chave.publickey()
print("Chave p: ", chave)

# Inicializar cifradores
cifrador = PKCS1_OAEP.new(chave_publica)
decifrador = PKCS1_OAEP.new(chave)

# Mensagem original
mensagem = "SEGREDO!"

# Criptografar (precisa ser bytes)
mensagem_bytes = mensagem.encode('utf-8')
criptografada = cifrador.encrypt(mensagem_bytes)
criptografada_b64 = base64.b64encode(criptografada).decode('utf-8')
print(f"Criptografada (base64): {criptografada_b64}")

# Descriptografar
criptografada_bytes = base64.b64decode(criptografada_b64)
descriptografada = decifrador.decrypt(criptografada_bytes)
print(f"Descriptografada: {descriptografada.decode('utf-8')}")