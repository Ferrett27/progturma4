n = int(input())
if 1 > n or n > 1000:
    print("Erro!, O número tem que ser maior que 1 e menor que 1000")

lista = list(map(int, input().split(" ")))

menor = min(lista)
posicao = 0

for i in range(n):
    if lista[i] == menor:
        posicao = i

print("Menor valor: %d" %menor)
print("Posicao: %d" %posicao)
