def pares_5():
    pares = 0
    for i in range(5):
        num = int(input())
        if num % 2 == 0:
            pares += 1
    return pares

pares = pares_5()

print(f"{pares} valores pares")
