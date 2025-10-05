# Exemplo de criptografia e descriptografia de Vigenère

def cifra_vigenere(texto, chave):
    resultado = ""
    chave = chave.upper()
    chave_len = len(chave)
    chave_idx = 0

    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            k = ord(chave[chave_idx % chave_len]) - ord('A')
            resultado += chr((ord(char) - base + k) % 26 + base)
            chave_idx += 1
        else:
            resultado += char
    return resultado

def decifra_vigenere(texto, chave):
    resultado = ""
    chave = chave.upper()
    chave_len = len(chave)
    chave_idx = 0

    for char in texto:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            k = ord(chave[chave_idx % chave_len]) - ord('A')
            resultado += chr((ord(char) - base - k) % 26 + base)
            chave_idx += 1
        else:
            resultado += char
    return resultado

palavra = "SEGREDO!"
chave = "DACC"

criptografada = cifra_vigenere(palavra, chave)
print(f"Criptografada: {criptografada}")

descriptografada = decifra_vigenere(criptografada, chave)
print(f"Descriptografada: {descriptografada}")