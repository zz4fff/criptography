import string

def gerar_tabela_polialfabetica():
    alfabeto = string.ascii_uppercase
    tabela = []
    for i in range(26):
        linha = alfabeto[i:] + alfabeto[:i]
        tabela.append(linha)
    return tabela

def cifra_polialfabetica(texto, chave):
    tabela = gerar_tabela_polialfabetica()
    texto = texto.upper()
    chave = chave.upper()
    resultado = ""
    chave_idx = 0
    for c in texto:
        if c.isalpha():
            linha = ord(chave[chave_idx % len(chave)]) - ord('A')
            coluna = ord(c) - ord('A')
            resultado += tabela[linha][coluna]
            chave_idx += 1
        else:
            resultado += c
    return resultado

def decifra_polialfabetica(texto, chave):
    tabela = gerar_tabela_polialfabetica()
    texto = texto.upper()
    chave = chave.upper()
    resultado = ""
    chave_idx = 0
    for c in texto:
        if c.isalpha():
            linha = ord(chave[chave_idx % len(chave)]) - ord('A')
            coluna = tabela[linha].index(c)
            resultado += chr(coluna + ord('A'))
            chave_idx += 1
        else:
            resultado += c
    return resultado

palavra = "SEGREDO!"
chave = "POLI"

criptografada = cifra_polialfabetica(palavra, chave)
print(f"Criptografada: {criptografada}")

descriptografada = decifra_polialfabetica(criptografada, chave)
print(f"Descriptografada: {descriptografada}")