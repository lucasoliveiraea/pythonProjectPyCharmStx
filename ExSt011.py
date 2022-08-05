# Algoritimo Tarefa 011: Compra de maçãs (IF)
# Dev: Lucas Oliveira
# Data: 05.08.2022

Quantidade = int(input('Quantas maçãs gostaria de comprar? Fala pra gente: '))

if Quantidade <= 11:
    Total = Quantidade * 0.30
else:
    Total = Quantidade * 0.25

print('Total a ser pago é de R$ ', Total)

