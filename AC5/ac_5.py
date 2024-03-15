"""
Programação Estruturada
2024.1
15/03/2024

AC5
"""
import random

def main():
    "Aventureiro"
    va = 100
    atk1 = random.randint(10, 20)
    defesa1 = random.randint(1, 5)

    "Monstro"
    vm = random.randint(60, 80)
    atkm = random.randint(20, 30)

    "Rodada"
    rodada = 0

    "Rodada 0"
    print("Rodada", rodada)
    print("Aventureiro:", "vida",va,"-","att",atk1,"-","def",defesa1)
    print("Monstro:", "vida",vm,"-","att",atkm)

    "Jogo:"
    while va > 0 and vm > 0:
            rodada = rodada + 1

            dano_a = random.randint(1, atk1)
            vm = vm - dano_a

            dano_m0 = random.randint(1, atkm)
            dano_m = dano_m0 - defesa1
            va = va - dano_m

            if va <= 0:
                print("Rodada", rodada)
                print("Você morreu!")
                break

            elif vm <= 0:
                print("Rodada", rodada)
                print("O monstro morreu!")
                break

            print("Rodada", rodada)
            print("Aventureiro:", "vida",va,"-","att",atk1,"-","def",defesa1)
            print("Monstro:", "vida",vm,"-","att",atkm)







main()
