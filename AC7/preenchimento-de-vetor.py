def preenchimento_de_vetor():
    v = int(input())
    if v > 50:
        print("O número tem que ser menor que 50.")
    else:
        for i in range(10):
            print(f"N[{i}] = {v}")
            v *= 2