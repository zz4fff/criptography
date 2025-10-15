import string

def atbash(texto):
    alfabeto = string.ascii_uppercase
    atbash_map = {c: alfabeto[::-1][i] for i, c in enumerate(alfabeto)}
    resultado = ""
    for c in texto.upper():
        if c.isalpha():
            resultado += atbash_map[c]
        else:
            resultado += c
    return resultado

palavra = "SEGREDO!"
criptografada = atbash(palavra)
print(f"Criptografada: {criptografada}")

descriptografada = atbash(criptografada)
print(f"Descriptografada: {descriptografada}")