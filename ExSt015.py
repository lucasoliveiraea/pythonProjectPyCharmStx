# Algoritimo Tarefa 015: Complemento ao Polígono da tarefa 14 (IF)
# Dev: Lucas Oliveira
# Data: 05.08.2022

Lados = int(input('Digite o número de lados de um polígono: '))

if Lados == 3:
    Base = float(input('Digite a medida da base: '))
    Altura = float(input('Digite a medida da altura: '))
    Area = (Base * Altura) / 2
    print('A figura é um Triângulo com área de: ', Area, 'cm²')
elif Lados == 4:
    Lado = float(input('Digite a medida do lado do quadrado: '))
    Area = Lado * Lado
    print('A figura é um Quadrado com área de: ', Area, 'cm²')
elif Lados == 5:
    Lado = float(input('Digite a medida do lado do pentágono: '))
    Apotema = float(input('Digite a medida do apótema do pentágono: '))
    Area = 5/2 * Lado * Apotema
    print('A figura é um Pentágono com área de: ', Area, 'cm²')
elif Lados < 3:
    print('Não é um polígono')
else:
    print('Polígono não identificado')

