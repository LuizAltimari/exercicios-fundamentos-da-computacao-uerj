soma = 0
notas = []
for i in range(0,10):
    notas.append(int(input('nota: ')))
print('VETOR: ', notas)
for i in range(0, 10):
    if notas[i] % 2 == 0:
        soma += notas[i]
    if i % 2 == 1:
        soma -= notas[i]

print('SOMA: ', soma)
    
