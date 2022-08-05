# Algoritimo Tarefa 006: Receber nomes e salários (While)
# Dev: Lucas Oliveira
# Data: 05.08.2022

RendaPoupanca = 1.02
RendaFundo = 1.05
SalarioCarlos = float(input('Digite o salário do funcionário: '))
SalarioJoao = (SalarioCarlos/3)

print('Salario Carlos', SalarioCarlos)
print('Salario Joao', SalarioJoao)

Meses = 0
while SalarioJoao < SalarioCarlos:
    SalarioCarlos *= RendaPoupanca
    SalarioJoao *= RendaFundo
    Meses += 1

if SalarioJoao > SalarioCarlos:
    print("Para ultrapassar o valor pertencente à João levou:", Meses, "meses")
elif SalarioJoao == SalarioCarlos:
    print("Para igualar o valor pertencente à Carlos João levou:", Meses, "meses")

