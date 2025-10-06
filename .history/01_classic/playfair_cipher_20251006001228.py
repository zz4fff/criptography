import string

def gerar_matriz_playfair(chave):
    chave = chave.upper().replace('J', 'I')
    matriz = []
    usado = set()
    for c in chave + string.ascii_uppercase:
        if c not in usado and c.isalpha():
            matriz.append(c)
            usado.add(c)
    return [matriz[i*5:(i+1)*5] for i in range(5)]

def preparar_texto(texto):
    texto = texto.upper().replace('J', 'I')
    texto = ''.join([c for c in texto if c.isalpha()])
    resultado = ""
    i = 0
    while i < len(texto):
        a = texto[i]
        b = texto[i+1] if i+1 < len(texto) else 'X'
        if a == b:
            resultado += a + 'X'
            i += 1
        else:
            resultado += a + b
            i += 2
    if len(resultado) % 2 != 0:
        resultado += 'X'
    return resultado

def encontrar_posicao(matriz, letra):
    for i, linha in enumerate(matriz):
        if letra in linha:
            return i, linha.index(letra)
    return None

def cifra_playfair(texto, chave):
    matriz = gerar_matriz_playfair(chave)
    texto = preparar_texto(texto)
    resultado = ""
    for i in range(0, len(texto), 2):
        a, b = texto[i], texto[i+1]
        linha_a, col_a = encontrar_posicao(matriz, a)
        linha_b, col_b = encontrar_posicao(matriz, b)
        if linha_a == linha_b:
            resultado += matriz[linha_a][(col_a + 1) % 5]
            resultado += matriz[linha_b][(col_b + 1) % 5]
        elif col_a == col_b:
            resultado += matriz[(linha_a + 1) % 5][col_a]
            resultado += matriz[(linha_b + 1) % 5][col_b]
        else:
            resultado += matriz[linha_a][col_b]
            resultado += matriz[linha_b][col_a]
    return resultado

def decifra_playfair(texto, chave):
    matriz = gerar_matriz_playfair(chave)
    resultado = ""
    for i in range(0, len(texto), 2):
        a, b = texto[i], texto[i+1]
        linha_a, col_a = encontrar_posicao(matriz, a)
        linha_b, col_b = encontrar_posicao(matriz, b)
        if linha_a == linha_b:
            resultado += matriz[linha_a][(col_a - 1) % 5]
            resultado += matriz[linha_b][(col_b - 1) % 5]
        elif col_a == col_b:
            resultado += matriz[(linha_a - 1) % 5][col_a]
            resultado += matriz[(linha_b - 1) % 5][col_b]
        else:
            resultado += matriz[linha_a][col_b]
            resultado += matriz[linha_b][col_a]
    return resultado

palavra = "SEGREDO!"
chave = "DACC"

criptografada = cifra_playfair(palavra, chave)
print(f"Criptografada: {criptografada}")

descriptografada = decifra_playfair(criptografada, chave)
print(f"Descriptografada: {descriptografada}")