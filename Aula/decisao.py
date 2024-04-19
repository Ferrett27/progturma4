"""
Programação Estruturada
2024.1
08/03/2024

Estrutura de decisão
- if/elif/else
- match/case
"""

def saudacao(turno):
    if turno == "M":
        print("Bom dia!")
    elif turno == "T":
        print("Boa tarde!")
    elif turno == "N":
        print("Boa noite!")
    else:
        print("Dado inválido!")

def saudacao2(turno):
    if turno == "M":
        return "Bom dia!"
    if turno == "T":
        return "Boa tarde!"
    if turno == "N":
        return "Boa noite!"
    return "Dado inválido!"

saudacao("M")
saudacao("T")
saudacao("N")
saudacao("A")

print("-" * 30)
saudacao2("M")
saudacao2("N")

def le_nome():
    nome = input("Informe o seu nome: ")
    # if nome == "":(da false) seria a mesma coisa do abaixo
    if not nome:
        print("Erro! Entrada inválida")

    return nome

# Ternário
def e_par(num):
    if num % 2 == 0:
        return "é par"
    return "é impar"

# isso é o ternário
def e_par2(num):
    return "é impar" if num % 2 else "é par"

# Match/case
def saudacao3(turno):
    match turno:
        case "M":
            print("Bom dia!")
        case "T":
            print("Boa tarde!")
        case "N":
            print("Boa noite!")
        case _: # Default case, opcional
            print("Dado inválido")

print("-" * 30)
saudacao3("M")
saudacao3("T")
saudacao3("N")
saudacao3("A")

def aprovacao(conceito):
    match conceito:
        case "bom" | "Ótimo" | "Excelente":
            return "Aprovado"
        case _:
            return "Reprovado"