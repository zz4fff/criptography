import secrets

password = secrets.token_hex(8)  # Gera uma senha de 16 caracteres hexadecimais (128 bits)
print(password)
