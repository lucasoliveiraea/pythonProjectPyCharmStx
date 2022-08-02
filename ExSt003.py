# Algoritimo Tarefa 003: Idade de um nadador (IF)
# Dev: Lucas Oliveira
# Data: 01.08.2022

Idade = int(input("Informe a idade do nadador: "))

if Idade < 5:
    print("O nadador ainda não se encaixa em uma categoria para competição")
elif Idade >= 5 and Idade <= 7:
    print("Categoria Infantil")
elif Idade >= 8 and Idade <= 10:
    print("Categoria Juvenil")
elif Idade >= 11 and Idade <= 15:
    print("Categoria Adolescente")
elif Idade >= 16 and Idade <= 30:
    print("Categoria Adulto")
else:
    print("Categoria Sênior")

