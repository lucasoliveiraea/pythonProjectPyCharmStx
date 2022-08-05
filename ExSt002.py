# Algoritimo Tarefa 002: Gratificação de natal (IF)
# Dev: Lucas Oliveira
# Data: 01.08.2022

HorasExtras = float(input("Digite o número de horas extras: "))
HorasFaltas = float(input("Digite o número de horas-faltas: "))

TotalMinutos: float = (HorasExtras - (2 / 3 * HorasFaltas)) * 60

if TotalMinutos >= 2401:
    print("Minutos totais: ", TotalMinutos, "com gratificação de R$ 500,00")
elif 1801 <= TotalMinutos < 2401:
    print("Minutos totais: ", TotalMinutos, "com gratificação de R$ 400,00")
elif 1201 <= TotalMinutos < 1801:
    print("Minutos totais: ", TotalMinutos, "com gratificação de R$ 300,00")
elif 600 <= TotalMinutos < 1201:
    print("Minutos totais: ", TotalMinutos, "com gratificação de R$ 200,00")
else:
    print("Minutos totais: ", TotalMinutos, "com gratificação de R$ 100,00")
