# Algoritimo Tarefa 002: Idade e Peso (IF)
# Dev: Lucas Oliveira
# Data: 01.08.2022

Idade = int(input("Informe a idade do paciente: "))
Peso = float(input("Informe o peso do paciente: "))

if Idade < 20 and Peso <= 60:
    print("Você está no grau de risco: 9")
elif Idade < 20 and 60 < Peso <= 90:
    print("Você está no grau de risco: 8")
elif Idade < 20 and Peso > 90:
    print("Você está no grau de risco: 7")
elif 20 <= Idade <= 50 and Peso <= 60:
    print("Você está no grau de risco: 6")
elif 20 <= Idade <= 50 and 60 < Peso <= 90:
    print("Você está no grau de risco: 5")
elif 20 <= Idade <= 50 and Peso > 90:
    print("Você está no grau de risco: 4")
elif Idade > 50 and Peso < 60:
    print("Você está no grau de risco: 3")
elif Idade > 50 and 60 < Peso <= 90:
    print("Você está no grau de risco: 2")
elif Idade > 50 and Peso > 90:
    print("Você está no grau de risco: 1")

