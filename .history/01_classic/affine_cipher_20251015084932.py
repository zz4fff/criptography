import string
from math import gcd

def modinv(a, m):
    # Calcula o inverso modular de a mod m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise Exception('Inverso modular não existe')

def cifra_affine(texto, a, b):
    alfabeto = string.ascii_uppercase
    resultado = ""
    for c in texto.upper():
        if c.isalpha():
            x = ord(c) - ord('A')
            y = (a * x + b) % 26
            resultado += chr(y + ord('A'))
        else:
            resultado += c
    return resultado

def decifra_affine(texto, a, b):
    alfabeto = string.ascii_uppercase
    a_inv = modinv(a, 26)
    resultado = ""
    for c in texto.upper():
        if c.isalpha():
            y = ord(c) - ord('A')
            x = (a_inv * (y - b)) % 26
            resultado += chr(x + ord('A'))
        else:
            resultado += c
    return resultado

# Parâmetros: a e b (a deve ser coprimo de 26)
a = 5
b = 8
if gcd(a, 26) != 1:
    raise Exception("O valor de 'a' deve ser coprimo de 26.")

palavra = "SEGREDO!"
criptografada = cifra_affine(palavra, a, b)
print(f"Criptografada: {criptografada}")

descriptografada = decifra_affine(criptografada, a, b)
print(f"Descriptografada: {descriptografada}")