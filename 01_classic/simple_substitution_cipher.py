import string

def gerar_mapa_substituicao(chave):
    alfabeto = string.ascii_uppercase
    chave = chave.upper()
    mapa = {}
    usado = set()
    idx = 0
    for c in chave:
        if c not in usado and c.isalpha():
            mapa[alfabeto[idx]] = c
            usado.add(c)
            idx += 1
    for c in alfabeto:
        if c not in usado:
            mapa[alfabeto[idx]] = c
            idx += 1
    return mapa

def cifra_substituicao(texto, chave):
    mapa = gerar_mapa_substituicao(chave)
    resultado = ""
    for c in texto.upper():
        if c.isalpha():
            resultado += mapa[c]
        else:
            resultado += c
    return resultado

def decifra_substituicao(texto, chave):
    mapa = gerar_mapa_substituicao(chave)
    inverso = {v: k for k, v in mapa.items()}
    resultado = ""
    for c in texto.upper():
        if c.isalpha():
            resultado += inverso[c]
        else:
            resultado += c
    return resultado

palavra = "SEGREDO!"
chave = "CHAVE"

criptografada = cifra_substituicao(palavra, chave)
print(f"Criptografada: {criptografada}")

descriptografada = decifra_substituicao(criptografada, chave)
print(f"Descriptografada: {descriptografada}")