"""
AC8
"""
import math
# Figurinhas (Exercício 1)
def figurinhas():
    n = int(input())
    if 1 <= n <= 3000:  
        for i in range(n):
            fig = list(map(int, input().split(" ")))
            f1 = fig[0]
            f2 = fig[1]

            if 1 <= f1 <= 1000 and 1 <= f2 <= 1000:
                print(math.gcd(f1, f2))
            else:
                print("Erro! o numero de figurinhas tem que ser entre 1 e 1000.")
    else:
        print("Erro! o número de casos tem que ser entre 1 e 3000.")

# figurinhas()

# Dama (Exercício 2)
def dama():
    while True:
        coord = list(map(int, input().split(" ")))
        if len(coord) == 4:
            x1 = coord[0]
            y1 = coord[1]
            x2 = coord[2]
            y2 = coord[3]
            if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
                if x1 == x2 and y1 == y2:
                    print("0")
                elif math.fabs(x1 - x2) == math.fabs(y1 - y2):
                    print("1")
                elif x1 == x2 and y1 != y2 or x1 != x2 and y1 == y2:
                    print("1")
                else:
                    print("2")
            else:
                if x1 == 0 and y1 == 0 and x2 == 0 and y2 == 0:
                    break
                else:
                    print("Erro! o tabuleiro não é tão grande assim! apenas coordenadas de 1 a 8.")
        else:
            print("Erro! apenas 4 coordenadas! duas da posição inicial e duas da posição que deseja chegar.")

# dama()

# Soma de Fatoriais (Exercício 3)
def soma_fatoriais():
    while True:
        try:
            valores = list(map(int, input().split(" ")))
            if len(valores) == 2:
                m = valores[0]
                n = valores[1]
                m1 = 1
                n1 = 1
                if n == 0:
                    n = 1
                if m == 0:
                    m = 1
                if 0 <= m <= 20 and 0 <= n <= 20:

                    for i in range(1, m+1):
                        m1 *= i
                    for i in range(1, n+1):
                        n1 *= i
                
                    print(n1 + m1)

                else:
                    print("Erro! o número tem que ser entre 0 a 20.")
            else:
                print("Erro! apenas dois valores.")
        except EOFError:
            break   

# soma_fatoriais()

# Blobs (Exercício 4)
def blobs():
    dias = []
    n = int(input())
    if 1 <= n <= 1000:
        for i in range(n):
            c = float(input())
            if 1 <= c <= 1000:
                d = 0
                while c > 1:
                    c = c / 2
                    d += 1
            
                dias.append(d)
            else:
                print("Erro! a comida tem que ser entre 1 a 1000 kg")
        i = 0
        for _ in range(len(dias)):
            print(f"{dias[i]} dias")
            i += 1
    else:
        print("O número de casos tem que ser entre 1 e 1000")

# blobs()

# Frequência de Números (Exercício 5)
def frequencia():
    lista = []
    n = int(input())
    for i in range(n):
        x = int(input())
        if 1 <= x <= 2000:
            lista.append(x)
        else:
            print("O número tem que ser entre 1 a 2000.")

    unicos = sorted(set(lista))

    for i in range(len(unicos)):
        print(f"{unicos[i]} aparece {lista.count(unicos[i])} vez(es)")

# frequencia()

# Primo Rápido (Exercício 6)
def e_primo(x):
    for i in range(2, int(x ** 0.5)+1):
        if x % i == 0:
            return True

def primo_rapido():
    n = int(input())
    if 1 <= n <= 200:
        for i in range(n):
            x = int(input())
            if x > 1:
                if e_primo(x) == True:
                    print("Not Prime")
                else:
                    print("Prime")        
            else:
                print("Not Prime") 
    else:
        print("Erro! apenas de 1 a 200 números de casos.")

# primo_rapido()
        
# Cara ou Coroa (Exercício 7)
def cara_ou_coroa():
    while True:
        n = int(input())
        if n == 0:
            break

        jogadas = list(map(int, input().split(" ")))
        resul = sorted(set(jogadas))
        if n > 2:
            print(f"Mary won {jogadas.count(resul[0])} times and John won {jogadas.count(resul[1])} times")
        else:
            if jogadas[0] == 1:
                print("Mary won 0 times and John won 1 times")
            elif jogadas[0] == 0:
                print("Mary won 1 times and John won 0 times")

# cara_ou_coroa()

# Funções (Exercício 8)
def funcoes():
    n = int(input())
    for i in range(n):
        valores = list(map(int, input().split(" ")))
        x = valores[0]
        y = valores[1]
        if 1 <= x <= 100 and 1 <= y <= 100:
            r = ((3 * x)** 2) + y ** 2
            b = ((x ** 2)* 2) + ((5 * y)** 2)
            c = -100 * x + y ** 3
            if r > b and r > c:
                print("Rafael ganhou")
            elif b > r and b > c:
                print("Beto ganhou")
            elif c > b and c > r:
                print("Carlos ganhou")
        else:
            print("Erro! o número tem que ser entre 1 a 100")

# funcoes()