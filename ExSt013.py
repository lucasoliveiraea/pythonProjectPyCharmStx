# Algoritimo Tarefa 013: Altura e sexo (IF)
# Dev: Lucas Oliveira
# Data: 05.08.2022

Sexo = int(input('Informe o sexo (Digite 1 para Feminino ou 2 para Masculino): '))
Altura = float(input('Informe a altura: '))

if Sexo == 1:
    PesoIdeal = (62.1 * Altura) - 44.7
else:
    PesoIdeal = (72.7 * Altura) - 58

print('O peso ideal é: ', PesoIdeal)
