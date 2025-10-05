# Exemplo de criptografia e descriptografia de César


def cifra_cesar(texto, chave):
    resultado = ""
    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            resultado += chr((ord(char) - base + chave) % 26 + base)
        else:
            resultado += char
    return resultado


def decifra_cesar(texto, chave):
    return cifra_cesar(texto, -chave)

# Testando a cifra de César
palavra = "SEGREDO!"
chave = 3

criptografada = cifra_cesar(palavra, chave)
print(f"Criptografada: {criptografada}")

descriptografada = decifra_cesar(criptografada, chave)
print(f"Descriptografada: {descriptografada}")
