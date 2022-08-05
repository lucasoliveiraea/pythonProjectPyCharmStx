# Algoritimo Tarefa 004: Salário bruto (IF)
# Dev: Lucas Oliveira
# Data: 01.08.2022

salarioBruto = float(input("Informe o salário do funcionário: "))
imposto = float(salarioBruto * 7/100)

if salarioBruto <= 350:
    gratificacao = float(100)
    totalReceber = float(salarioBruto - imposto + gratificacao)
elif 350 < salarioBruto <= 600:
    gratificacao = float(75)
    totalReceber = float(salarioBruto - imposto + gratificacao)
elif 601 < salarioBruto <= 900:
    gratificacao = float(50)
    totalReceber = float(salarioBruto - imposto + gratificacao)
else:
    gratificacao = float(35)
    totalReceber = float(salarioBruto - imposto + gratificacao)

print("O total a receber pelo funcionário é de: ", totalReceber)

