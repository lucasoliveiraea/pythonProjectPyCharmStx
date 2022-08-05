# Algoritimo Tarefa 003: Idade de um nadador (IF)
# Dev: Lucas Oliveira
# Data: 01.08.2022

Idade = int(input("Informe a idade do nadador: "))

if Idade < 5:
    print("O nadador ainda não se encaixa em uma categoria para competição")
elif 5 <= Idade <= 7:
    print("Categoria Infantil")
elif 8 <= Idade <= 10:
    print("Categoria Juvenil")
elif 11 <= Idade <= 15:
    print("Categoria Adolescente")
elif 16 <= Idade <= 30:
    print("Categoria Adulto")
else:
    print("Categoria Sênior")

