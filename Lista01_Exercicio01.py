idade = 0
cont = 0
cont30 = 0
somaM = 0
contM = 0
somaF = 0
contF = 0
maiorSalario = 0
sexo = ''

while idade >= 0:
    idade = int(input('Insira sua idade: '))
    if idade >= 0:
        sexo = input('Insira seu sexo (M ou F): ')    
        salario = float(input('Insira seu salário: '))

        if idade < 30 and salario > maiorSalario:        
            maiorSalario = salario        

        if sexo == 'F':
            somaF += salario
            contF+=1
        else:
            somaM += salario
            contM+=1
        cont+=1

if cont == 0:
    contM = contF = 1
    
media = somaM/contM
print('Média salarial dos homens: R$', media)
media = somaF/contF
print('Média salarial das mulheres: R$', media)
print('Maior salário entre as pessoas abaixo de 30 anos: ', maiorSalario)

        
    
