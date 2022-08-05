# Algoritimo Tarefa 012: 3 valores em ordem (IF)
# Dev: Lucas Oliveira
# Data: 05.08.2022

Valor1 = float(input('Informe o primeiro valor: '))
Valor2 = float(input('Informe o segundo valor: '))
Valor3 = float(input('Informe o terceiro valor: '))

if Valor1 > Valor2 and Valor1 > Valor3:
    Maior = Valor1
    if Valor2 > Valor3:
        Meio = Valor2
        Menor = Valor3
    else:
        Meio = Valor3
        Menor = Valor2
elif Valor2 > Valor1 and Valor2 > Valor3:
    Maior = Valor2
    if Valor1 > Valor3:
        Meio = Valor1
        Menor = Valor3
    else:
        Meio = Valor3
        Menor = Valor1
else:
    Maior = Valor3
    if Valor1 > Valor2:
        Meio = Valor1
        Menor = Valor2
    else:
        Meio = Valor2
        Menor = Valor1
print('Os valores na ordem crescente são: ', Menor, Meio, Maior)
