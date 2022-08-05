# Algoritimo Tarefa 018: Ângulos do triângulo (IF)
# Dev: Lucas Oliveira
# Data: 05.08.2022

print('Entre com as medidas dos ângulos do triângulo: ')
Ang1 = float(input('Ângulo 1: '))
Ang2 = float(input('Ângulo 2: '))
Ang3 = float(input('Ângulo 3: '))

if Ang1 + Ang2 + Ang3 == 180:
    print('Triângulo')
    if Ang1 == 90 or Ang2 == 90 or Ang3 == 90:
        print('Retângulo')
    elif Ang1 < 90 and Ang2 < 90 and Ang3 < 90:
        print('Acutângulo')
    else:
        print('Obtustângulo')
else:
    print('Não é um triângulo')

