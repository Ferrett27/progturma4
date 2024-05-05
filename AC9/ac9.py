"""
AC9
"""
# Distância (Exercício 1)
def distancia():
    n = int(input())
    tempo = int((60 * n) / 30)
    print(f"{tempo} minutos")

# distancia()

# Fatorial Simples (Exercício 2)
def fatorial_simples():
    n = int(input())
    resul = 1
    for i in range(n, 1, -1):
        resul *= i
    print(resul)

# fatorial_simples()

# Ida à Feira (Exercício 3)
def feira():
    n = int(input())
    for i in range(n):
        compras = {}
        m = int(input())
        for i in range(m):
            item = input().split(" ")
            compras[item[0]] = float(item[1])

        p = int(input())
        total = 0.0
        for i in range(p):
            quant = input().split(" ")
            total += compras[quant[0]] * int(quant[1])

        print("R$ %.2f" %total)

# feira()

# Identificando o Chá (Exercício 4)
def identificar_cha():
    t = int(input())
    cha = list(map(int, input().split(" ")))

    print(cha.count(t))

# identificar_cha()

# Aviões de Papel (Exercício 5)
def avioes():
    n = list(map(int, input().split(" ")))
    if n[1] - (n[0] * n[2]) >= 0:
        print("S")
    else:
        print("N")

# avioes()

# Tocógrafo (Exercício 6)
def tacografo():
    n = int(input())
    resul = 0
    for i in range(n):
        m = list(map(int, input().split(" ")))
        resul += m[0] * m[1]
    print(resul)

# tacografo()

# Busca na internet (Exercício 7)
def busca():
    t = int(input())
    quanti = t * 4
    print(quanti)

# busca()

# Sequência Secreta (Exercício 8)
def sequencia():
    lista = []
    n = int(input())
    for i in range(n):
        v = int(input())
        lista.append(v)
    marca = 0
    for i in range(len(lista)):
        if i == len(lista)-1:
            marca += 1
            break
        elif lista[i] != lista[i+1]:
            marca += 1

    print(marca)

# sequencia()