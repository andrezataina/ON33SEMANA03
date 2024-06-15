nota = float(input('Escreva a nota da aluna de 1 a 10: '))
presenca = float(input('Escreva a presença da aluna de 0 a 100: '))

if nota >= 7 or presenca >= 75:
    print('APROVADA')
else:
    print('REPROVADA')