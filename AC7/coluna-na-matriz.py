c = int(input())
if not 0 <= c <= 11:
    print("Erro!, apenas números de 0 a 11")

t = input()
if t != "S" and t != "M":
    print('Erro!, apenas soma("S") ou media("M")')

matriz = []
v = []
s = 0

for x in range(12):
    for y in range(12):
        val = float(input())
        v.append(val)
        if y == c:
            s = s + val
    matriz.append(v)
    v = []

if t == "S":
    print("%.1f" %s)
if t == "M":
    s = s / 12
    print("%.1f" %s)
