# Algoritimo Tarefa 016: Complemento ao Polígono da tarefa 14 (IF)
# Dev: Lucas Oliveira
# Data: 05.08.2022

Valor1 = int(input('Digite o primeiro valor: '))
Valor2 = int(input('Digite o segundo valor: '))
Valor3 = int(input('Digite o terceiro valor: '))

if Valor1 > Valor2 and Valor1 > Valor3:
    print('O maior valor dentre os 3 é o ', Valor1)
elif Valor2 > Valor1 and Valor2 > Valor3:
    print('O maior valor dentre os 3 é o ', Valor2)
else:
    print('O maior valor dentre os 3 é o', Valor3)

