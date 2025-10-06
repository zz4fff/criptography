import numpy as np
import string

def texto_para_numeros(texto):
    texto = texto.upper()
    return [ord(c) - ord('A') for c in texto if c.isalpha()]

def numeros_para_texto(nums):
    return ''.join([chr(n % 26 + ord('A')) for n in nums])

def ajustar_texto(texto, tamanho_bloco):
    texto = ''.join([c for c in texto.upper() if c.isalpha()])
    while len(texto) % tamanho_bloco != 0:
        texto += 'X'
    return texto

def cifra_hill(texto, chave):
    tamanho_bloco = chave.shape[0]
    texto = ajustar_texto(texto, tamanho_bloco)
    nums = texto_para_numeros(texto)
    resultado = []
    for i in range(0, len(nums), tamanho_bloco):
        bloco = np.array(nums[i:i+tamanho_bloco])
        cifrado = np.dot(chave, bloco) % 26
        resultado.extend(cifrado)
    return numeros_para_texto(resultado)

def inversa_modular(matriz, modulo):
    det = int(round(np.linalg.det(matriz)))
    det_inv = pow(det, -1, modulo)
    matriz_adj = np.round(det * np.linalg.inv(matriz)).astype(int) % modulo
    return (det_inv * matriz_adj) % modulo

def decifra_hill(texto, chave):
    tamanho_bloco = chave.shape[0]
    nums = texto_para_numeros(texto)
    chave_inv = inversa_modular(chave, 26)
    resultado = []
    for i in range(0, len(nums), tamanho_bloco):
        bloco = np.array(nums[i:i+tamanho_bloco])
        decifrado = np.dot(chave_inv, bloco) % 26
        resultado.extend(decifrado)
    return numeros_para_texto(resultado)

# Exemplo de chave 3x3 (deve ser invertível módulo 26)
chave = np.array([[6, 24, 1],
                  [13, 16, 10],
                  [20, 17, 15]])

palavra = "SEGREDO!"
criptografada = cifra_hill(palavra, chave)
print(f"Criptografada: {criptografada}")

descriptografada = decifra_hill(criptografada, chave)
print(f"Descriptografada: {descriptografada}")