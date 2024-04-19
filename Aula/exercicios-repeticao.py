"""
Exercícios resolvido 01
Elaborar uma função conta_pares(min, max) para exibir todos os valores entre min e max,
com um incremento de 2, separando-os com um hífen.
Ex.: 2 - 4 - 6 - 8 - 10 - 12 - 14.
"""

def conta_pares(min, max):
    if min % 2:
        min += 1
    for num in range(min, max + 1, 2):
        if num == max or num == max - 1:
            print(num)
        else:
            print(num, end=' - ')

#conta_pares(2, 8)
#conta_pares(1, 8)
#conta_pares(1, 9)
# conta_pares(2, 9)

"""
Exercício resolvido 04
Faça um programa que calcule o fatorial de um número
inteiro positivo fornecido pelo usuário.
Ex.: 5! = 5 * 4 * 3 * 2 * 1 = 120.

x! = x * (x - 1)
"""

def fatorial(num):
    fat = 1
    for mult in range(1, num + 1):
        fat *= mult

    return fat


def fatorial2(num):
    if num == 1:
        return 1
    return num * fatorial2(num - 1)

print(fatorial2(5))