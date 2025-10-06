def rot13(texto):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + 13) % 26 + base)
        else:
            resultado += char
    return resultado

palavra = "SEGREDO!"
criptografada = rot13(palavra)
print(f"Criptografada: {criptografada}")

descriptografada = rot13(criptografada)
print(f"Descriptografada: {descriptografada}")