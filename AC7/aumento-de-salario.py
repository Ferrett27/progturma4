salario = float(input())
if 0 < salario <= 400.00:
    percentual = 15
    salarionovo = ((salario * percentual) / 100) + salario
    reajuste = salarionovo - salario
    print("Novo salario: %.2f" %salarionovo)
    print("Reajuste ganho: %.2f" %reajuste)
    print(f"Em percentual: {percentual} %")
elif 400.01 < salario <= 800.00:
    percentual = 12
    salarionovo = ((salario * percentual) / 100) + salario
    reajuste = salarionovo - salario
    print("Novo salario: %.2f" %salarionovo)
    print("Reajuste ganho: %.2f" %reajuste)
    print(f"Em percentual: {percentual} %")
elif 800.01 < salario <= 1200.00:
    percentual = 10
    salarionovo = ((salario * percentual) / 100) + salario
    reajuste = salarionovo - salario
    print("Novo salario: %.2f" %salarionovo)
    print("Reajuste ganho: %.2f" %reajuste)
    print(f"Em percentual: {percentual} %")
elif 1200.01 < salario <= 2000.00:
    percentual = 7
    salarionovo = ((salario * percentual) / 100) + salario
    reajuste = salarionovo - salario
    print("Novo salario: %.2f" %salarionovo)
    print("Reajuste ganho: %.2f" %reajuste)
    print(f"Em percentual: {percentual} %")
elif salario > 2000.0:
    percentual = 4
    salarionovo = ((salario * percentual) / 100) + salario
    reajuste = salarionovo - salario
    print("Novo salario: %.2f" %salarionovo)
    print("Reajuste ganho: %.2f" %reajuste)
    print(f"Em percentual: {percentual} %")
