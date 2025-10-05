from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

key = os.urandom(32)  # Chave de 256 bits
iv: bytes = os.urandom(16)   # Vetor de inicialização
cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
encryptor = cipher.encryptor()
mensagem = b"Texto secreto para teste"

# Adiciona padding
padder = padding.PKCS7(128).padder()
mensagem_padded = padder.update(mensagem) + padder.finalize()

ciphertext = encryptor.update(mensagem_padded) + encryptor.finalize()

# Descriptografar
decryptor = cipher.decryptor()
plaintext = decryptor.update(ciphertext) + decryptor.finalize()

print(mensagem)
print(mensagem_padded)
print(ciphertext.hex())
print(plaintext.decode('utf-8'))