nota = float(input('Escreva a nota da aluna de 1 a 10!: '))

if nota >= 7:
    print('APROVADA')
elif nota < 7 and nota > 6:
    print ('RECUPERACAO')
else:
    print('REPROVADA')
