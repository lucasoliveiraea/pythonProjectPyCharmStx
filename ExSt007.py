# Algoritimo Tarefa 007: Conjunto de valores (While)
# Dev: Lucas Oliveira
# Data: 05.08.2022

import math

Numero = 1

while Numero > 0:
    Numero = float(input("Informe o valor a ser armazenado e calculado: "))
    print('Valor lido :', Numero)

    if Numero > 0:
        print('Valor ao quadrado: ', math.pow(Numero, 2))
        print('Valor ao cubo: ', math.pow(Numero, 3))
        print('Raiz quadrada do valor: ', math.sqrt(Numero))

    print('Informe 0 ou um valor negativo para sair')
