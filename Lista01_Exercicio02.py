r = int(input('Insira a razão da PA: '))
a1 = int(input('Insira o primeiro termo da PA: '))
n = int(input('Quantos elementos devem ser exibidos? '))

print('1 º termo: ', a1)
for i in range(2, n +1):
    print(i,'º termo: ', a1 + (i - 1) * r)
