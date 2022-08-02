# Algoritimo Tarefa 004: Empresa com 10 funcionários (While)
# Dev: Lucas Oliveira
# Data: 01.08.2022

Laco1 = 1
Laco2 = True
Laco3 = True

while Laco1 <= 10:
    SalarioMinimo = 450
    SalarioInicial = 0
    SalarioFinal = 0
    AuxilioAlimentacao = 0

    Codigo = input("Digite o código do funcionário: ")
    HoraTrabalhada = float(input("Digite as horas trabalhadas no mês: "))

    while Laco2:
        Categoria = input("Digite a categoria: ")
        if Categoria == 'O' or Categoria == 'G':
            Laco2 = False
        else:
            print("As categorias possíveis são O e G, digite novamente...")
            continue
        break

    while Laco3:
        Turno = input("Digite o turno: ")
        if Turno == 'M' or Turno == 'V' or Turno == 'N':
            Laco3 = False
        else:
            print("Os turnos possíveis são M, V e N, digite novamente...")
            continue
        break

    if Categoria == 'G' and Turno == 'N':
        ValorHora = SalarioMinimo * 0.18
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    elif Categoria == 'G' and Turno == 'M' or Turno == 'V':
        ValorHora = SalarioMinimo * 0.15
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    elif Categoria == 'O' and Turno == 'N':
        ValorHora = SalarioMinimo * 0.13
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
    else:
        ValorHora = SalarioMinimo * 0.10
        SalarioInicial = HoraTrabalhada * ValorHora
        if SalarioInicial <= 300:
            AuxilioAlimentacao = SalarioInicial * 0.20
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        elif SalarioInicial > 300 and SalarioInicial <= 600:
            AuxilioAlimentacao = SalarioInicial * 0.15
            SalarioFinal = SalarioInicial + AuxilioAlimentacao
        else:
            AuxilioAlimentacao = SalarioInicial * 0.05
            SalarioFinal = SalarioInicial + AuxilioAlimentacao

    print("Código: ", Codigo, "Horas Trabalhadas: ", HoraTrabalhada, "Categoria: ", Categoria, "Turno: ", Turno)
    print( "Valor da hora: ", ValorHora, "Salário inicial: ", SalarioInicial, "Auxílio Alimentação: ", AuxilioAlimentacao, "Salário Final: ", SalarioFinal)
    print("Número do Laço Principal ", Laco1 )
    Laco1 += 1
    Laco2 = True
    Laco3 = True
print("Fim")