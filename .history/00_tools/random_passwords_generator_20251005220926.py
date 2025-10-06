import secrets

password = secrets.token_hex(8)  # Gera uma senha de 16 caracteres hexadecimais (64 bits)
print(password)
print(len(password))  # Deve ser 16

password = secrets.token_urlsafe(12)  # Gera uma senha de aproximadamente 16 caracteres
print(password)
print(len(password))

alfabeto = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alfabeto) for _ in range(16))
print(password)
print(len(password))