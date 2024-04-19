"""
Programação Estruturada
2024.1
15/03/2024

Estrutura de Repetição
- while -> quando não sei quantas vezes eu vou precisar repetir as operações.
- for -> quando o números de vezes que o bloco será repetido é limitado, ou
quando quero percorrer uma coleção de dados.
"""

def contagem_regressiva(num):
    while num >= 0:
        print(num)
        num -= 1 # Loop infinito sem isso

    print("Acabou")

contagem_regressiva(5)
print("-" * 30)

print(list(range(5)))
print(list(range(5, 10)))
print(list(range(5, 10, 2)))
print(list(range(5, 10, -2)))
print(list(range(10, 2, 1)))
print("-" * 30)

def contagem_regressiva2(num):
    for cont in range(num, -1, -1):
        print(cont)

contagem_regressiva2(5)
print("-" * 30)

def ola_varias_vezes(num_vezes):
    for _ in range(num_vezes):
        print("olá")

ola_varias_vezes(3)
print("-" * 30)

def pula_mult_3(max):
    """
    Escreve na tela os números de 1 a max (inclusive),
    exceto os múltiplos de três.
    """

    for num in range(1, max +1):
        if not num % 3: # ou tb num % 3 == 0
            continue # pula para a próxima iteração
        print(num)

pula_mult_3(15)
print("-" * 30)

def para_antes_de_10(max):
    """
    Imprime todos os números de 1 a max, até o número 10 (exc.).
    """
    for num in range(1, max + 1):
        if num >= 10:
            break # Interrompe por completo a estrutura
        print(num)

para_antes_de_10(11)

def le_nome():
    """
    Continua pedindo por um nome, até não receber uma string vazia.
    """
    while True:
        nome = input("Informe o nome: ")
        if nome:
            break

    print(nome)

# le_nome()

def e_primo(num):
    """
    Escrever na tela se um número é primo ou não.
    """
    for div in range(2, num):
        if num % div == 0:
            print(num, "Não é primo.")
            break
    else: # executar o bloco apenas se não tiver entrado no break
        print(num, "é primo")

e_primo(7)
e_primo(15)
e_primo(31)
e_primo(49)