from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding
import os

# Gerar chave de 8 bytes (64 bits, DES usa 56)
chave = os.urandom(8)
texto_plano = b"SENHA"
padder = padding.PKCS7(64).padder()
texto_padded = padder.update(texto_plano) + padder.finalize()

cipher = Cipher(algorithms.TripleDES(chave), modes.ECB(), backend=default_backend())
encryptor = cipher.encryptor()
cifrado = encryptor.update(texto_padded) + encryptor.finalize()
print(f"Cifrado: {cifrado.hex()}")

decryptor = cipher.decryptor()
decifrado_padded = decryptor.update(cifrado) + decryptor.finalize()
unpadder = padding.PKCS7(64).unpadder()
decifrado = unpadder.update(decifrado_padded) + unpadder.finalize()
print(f"Decifrado: {decifrado}")