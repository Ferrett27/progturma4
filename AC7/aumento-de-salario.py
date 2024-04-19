salario = float(input())

if 0 < salario <= 400:
    per = 15
    salarionovo = salario + ((salario * per) / 100)
    reajs = salarionovo - salario
    print("Novo salario: %.2f" %salarionovo)
    print("Reajuste ganho: %.2f" %reajs)
    print(f"Em percentual: {per} %")

elif 400.01 <= salario <= 800:
    per = 12
    salarionovo = salario + ((salario * per) / 100)
    reajs = salarionovo - salario
    print("Novo salario: %.2f" %salarionovo)
    print("Reajuste ganho: %.2f" %reajs)
    print(f"Em percentual: {per} %")

elif 800.01 <= salario <= 1200:
    per = 10
    salarionovo = salario + ((salario * per) / 100)
    reajs = salarionovo - salario
    print("Novo salario: %.2f" %salarionovo)
    print("Reajuste ganho: %.2f" %reajs)
    print(f"Em percentual: {per} %")

elif 1200.01 <= salario <= 2000.00:
    per = 7
    salarionovo = salario + ((salario * per) / 100)
    reajs = salarionovo - salario
    print("Novo salario: %.2f" %salarionovo)
    print("Reajuste ganho: %.2f" %reajs)
    print(f"Em percentual: {per} %")

elif salario > 2000.01:
    per = 4
    salarionovo = salario + ((salario * per) / 100)
    reajs = salarionovo - salario
    print("Novo salario: %.2f" %salarionovo)
    print("Reajuste ganho: %.2f" %reajs)
    print(f"Em percentual: {per} %")
