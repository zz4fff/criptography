def cifra_rail_fence(texto, trilhos):
    texto = ''.join([c for c in texto if c.isalpha()])  # Remove não alfabéticos
    if trilhos == 1:
        return texto
    rail = [''] * trilhos
    trilho = 0
    direcao = 1

    for char in texto:
        rail[trilho] += char
        trilho += direcao
        if trilho == 0 or trilho == trilhos - 1:
            direcao *= -1
    return ''.join(rail)

def decifra_rail_fence(texto_cifrado, trilhos):
    if trilhos == 1:
        return texto_cifrado
    # Cria o padrão de trilhos
    padrao = [0] * len(texto_cifrado)
    trilho = 0
    direcao = 1
    for i in range(len(texto_cifrado)):
        padrao[i] = trilho
        trilho += direcao
        if trilho == 0 or trilho == trilhos - 1:
            direcao *= -1
    # Conta quantas letras em cada trilho
    contagem = [padrao.count(r) for r in range(trilhos)]
    # Preenche os trilhos com as letras cifradas
    rails = []
    idx = 0
    for count in contagem:
        rails.append(list(texto_cifrado[idx:idx+count]))
        idx += count
    # Reconstrói o texto original
    resultado = ''
    trilho_idx = [0] * trilhos
    for r in padrao:
        resultado += rails[r][trilho_idx[r]]
        trilho_idx[r] += 1
    return resultado

palavra = "SEGREDO!"
trilhos = 3

criptografada = cifra_rail_fence(palavra, trilhos)
print(f"Criptografada: {criptografada}")

descriptografada = decifra_rail_fence(criptografada, trilhos)
print(f"Descriptografada: {descriptografada}")