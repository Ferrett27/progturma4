def camisetas():
    while True:
        n = int(input())
        if n == 0:
            break
        lista = []
        for i in range(n):
            nome = input()
            cor_tamanho = input().split(" ")
            cor_tamanho.append(nome)
            lista.append(cor_tamanho)
        lista.sort()
        lista[1].sort(reverse=True)
        print(lista)

camisetas()

