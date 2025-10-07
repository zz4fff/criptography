def cifra_transposicao(texto, chave):
    texto = ''.join([c for c in texto if c.isalpha()])  # Remove caracteres não alfabéticos
    colunas = chave
    linhas = (len(texto) + colunas - 1) // colunas
    matriz = [''] * colunas

    for idx, char in enumerate(texto):
        coluna = idx % colunas
        matriz[coluna] += char

    return ''.join(matriz)

def decifra_transposicao(texto_cifrado, chave):
    colunas = chave
    linhas = (len(texto_cifrado) + colunas - 1) // colunas
    num_cheias = len(texto_cifrado) % colunas
    if num_cheias == 0:
        num_cheias = colunas

    matriz = []
    idx = 0
    for c in range(colunas):
        tam_col = linhas if c < num_cheias else linhas - 1
        matriz.append(texto_cifrado[idx:idx+tam_col])
        idx += tam_col

    resultado = ''
    for l in range(linhas):
        for c in range(colunas):
            if l < len(matriz[c]):
                resultado += matriz[c][l]
    return resultado

palavra = "SEGREDO!"
chave = 4  # Número de colunas

criptografada = cifra_transposicao(palavra, chave)
print(f"Criptografada: {criptografada}")

descriptografada = decifra_transposicao(criptografada, chave)
print(f"Descriptografada: {descriptografada}")