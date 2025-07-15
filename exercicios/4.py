# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

entrada = input('Vamos começar?')

print("Me informe suas notas de:")

n1 = int (input(' Matemática: '))
n2 = int (input('Português: '))
n3 = int (input('Inglês: '))
n4 = int (input('Física: ' ))

nota = (n1 + n2 + n3 + n4) // 4

print('Nota',nota)

if nota >= 7:
    print('Passou de ano')
elif nota < 7 and nota > 4:
    print('Recuperação')