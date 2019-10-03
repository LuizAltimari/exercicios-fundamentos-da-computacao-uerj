somaP = 0
contP = 0
contI = 0
numero = 1

while numero > 0:
    numero = int(input('Informe um número inteiro: '))
    if numero > 0:
        if numero % 2 == 0:
            somaP += numero
            contP += 1
        else:            
            contI += 1
    

print('Quantidade de pares: ', contP)
print('Quantidade de ímpares: ', contI)
if contP == 0:
        contP = 1
print('Média dos número pares: ', somaP/contP) 
