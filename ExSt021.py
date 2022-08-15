# Algoritimo Tarefa 021: Estruturas condicionais e de repetição: Tabuada com entrada do usuário (FOR)
# Dev: Lucas Oliveira
# Data: 15.08.2022

i_s = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numero = int(input('Entre com o valor a ser criada a tabuada: '))
for i in i_s:
    produto = i * numero
    print(i, "x", numero, "=", produto)