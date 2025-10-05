# coding: utf-8
from pprint import pprint as pp

from click import pause
from numpy import size

tab_alfab = [['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K'],
             ['L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V'],
             ['X', 'W', 'Y', 'Z', '.', ',', '#', '*', '@', '%', ' '],
             ['Á', 'Â', 'À', 'É', 'Ê', 'Í', 'Ó', 'Ô', 'Ú', '?', '!']]
pp(tab_alfab)
r1, r2 = size(tab_alfab)
print(r1)
tab_num = []  # vetor que vai do 1 ao r1 x r2
for i in range(r1):
    tab_num.add(tab_alfab[i]) # transformado vetor em matriz r1 x r2


## 1 ETAPA: ESCREVER A MENSAGEM

msg_in = '*SEGREDO!*'   # " * " inicia e finaliza a frase //
                                         # não pode colocar acento
print('=>> Mensagem de Texto para Codificar:') # imprimir na janela de comando
print(' ')
print(msg_in)
print(' ')
pause(2)  # pause de 2 segundos para facilitar a visualização
[Lin,Cin]= size(msg_in)

msg_cod = [];
msg_erro = 'NÃO EXISTE ESSE CARACTERE NA TABELA, POR FAVOR DIGITE OUTRO';

## 2 ETAPA: TRANSFORMAR MENSAGEM TEXTO EM UMA MENSAGEM DE MATRIZ DE NÚMEROS

for m in range(Lin):
    for n in range(Cin):
        carac_in = msg_in[m, n];
        if carac_in != tab_alfab:
            error(msg_erro)

        s1, s2 = find(tab_alfab == carac_in)
        num_in = tab_num[s1, s2]
        msg_cod = [msg_cod  num_in]


# COMPLETAR A MATRIZ COM ALGUM CARACTERE
aux1 = Cin / 10
if(class(aux1) == 1):
    aux1 = fix(aux1)
    msg_cod = reshape(msg_cod, 10, aux1)
else:
    aux1 = ceil(aux1);
    aux3 = aux1 * 10 - Cin;
        for(i in range(aux3)):
            msg_cod = [msg_cod 32] # caractere escolhido aqui foi " % " (32)

    msg_cod = reshape(msg_cod, 10, aux1)

## 3 ETAPA: CRIAR UMA CHAVE DE CODIFICAÇÃO ALEATÓRIA
chave = 0.1 + (9.9 - 0.1). * rand(aux1, aux1) # número no intervalo de 0,1 ate 9,99
chave = ceil(chave) # arrendodar para inteiro maior

# M1= [13 5 21 29 6 21 20 21 18 15 29 4 5; CHAVE FIXA PARA TESTE DA APOSTILA
#      16 5 14 4 5 29 4 5 29 13 9 13 33];

M3 = msg_cod

## 4 ETAPA: MENSAGEM CODIFICADA EM MATRIZ DE NÚMEROS. PRONTA PARA ENVIO
M2 = chave * M3 # mensagem codificada através da chave

## 5 ETAPA: DECODIFICAR A MENSAGEM RECIBIDA NA MATRIZ DE NÚMEROS
M1 = (inv(chave)) * M2
M1 = round(M1)
[LM1, CM1] = size(M1);

## 6 ETAPA: DECODIFICAR A MENSAGEM NA MATRIZ DE NÚMEROS PARA MENSAGEM DE TEXTO
msg_beta = [];
# mensagem= string(mensagem);
for(m in range(LM1)):
    for(n in range(CM1)):
        num = M1(m, n)
        [s1, s2] = find(tab_num == num)
        carac = tab_alfab(s1, s2)
        msg_beta = [msg_beta  carac]

## 7 ETAPA: MENSAGEM TEXTO RECEBIDA
msg = erase(msg_beta, "%") # formato string


## IMPRIMIR OS DADOS

print('=>> Chave Aleatória Usada:')
print(' ')
print(chave)
pause(2) # pause de 2 segundos para facilitar a visualização

print('=>> Mensagem Transformada em Matriz de Números:')
print(' ')
print(msg_cod)
pause(2) # pause de 2 segundos para facilitar a visualização

print('=>> Mensagem Codificada para Envio:')
print(' ')
print(M2)
pause(2) # pause de 2 segundos para facilitar a visualização

print('=>> Mensagem Recebida Decodificada:')
print(' ')
print(M1)
pause(2) # pause de 2 segundos para facilitar a visualização

print('=>> Mensagem Recebida Decodificada em Texto:')
print(' ')
mensagem = sprintf('%s', msg{:})


print(mensagem)
# print(strrep(mensagem, char(39), ''))

fim = 10
