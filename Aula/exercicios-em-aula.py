"""
Programação Estruturada
2024.1
08/03/2024

Exercícios
"""

"""
Excercício resolvidos 02
Implemente um programa que receba dois números e retorne o maior deles
"""
# receba = ter parametros e retorne e o uso de return

def maior(n1, n2):
    if n1 > n2:
        return n1
    return n2

"""
Exercício 04
Faça um programa que verifique se uma letra é vogal ou consoante
"""

def e_vogal(letra):
    match letra:
        case "a" | "e" | "i" | "o" | "u":
            return "É vogal"
    return "É consoante"

"""
Exercício 05
Faça um programa que receba três notas, calcule sua média aritmética simples e
apresente na tela uma das seguintes informações:

A mensagem “Aprovado”, se a média alcançada for maior ou igual a sete;
A mensagem “Reprovado”, se a média for menor do que sete;
A mensagem “Aprovado com Distinção”, se a média for igual a dez;
A mensagem “Nota inválida!” toda vez que for inserido um valor inválido.
"""
def nota_e_valida(nota):
    return 0 <= nota <= 10

def media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    if nota_e_valida(nota1) and nota_e_valida(nota1) and nota_e_valida(nota1):
        if media == 10:
            print("Aprovado com Distinção")
        elif 7 <= media < 10:
            print("Aprovado")
        elif 0<= media < 7:
            print("Reprovado")
    else:
        print("Nota Inválida")

media(10, 10, 10)
media(10, 8, 9)
media(6, 5, 5)
media(11, 9, 10)
media(11, 11, 11)