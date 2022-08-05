# Algoritimo Tarefa 017: Três valores e o maior deles (IF)
# Dev: Lucas Oliveira
# Data: 05.08.2022

print('Entre com as medidas dos lados do triângulo: ')
Lado1 = float(input('Lado 1: '))
Lado2 = float(input('Lado 2: '))
Lado3 = float(input('Lado 3: '))

if Lado1 == Lado2 and Lado2 == Lado3:
    print('Triângulo Equilátero')
elif (Lado1 == Lado2 and Lado1 != Lado3) or (Lado1 == Lado3 and Lado1 != Lado2) or (Lado2 == Lado3 and Lado2 != Lado1):
    print('Triângulo Isóceles')
else:
    print('Triângulo Escaleno')

