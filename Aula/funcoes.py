"""
Programação Estruturada
2024.1
01/03/2024

Funções
- Encapsular uma informação
- Isolar o comportamento pra facilitar o uso
- Organizar o código
"""

CAMINHO_DO_PROJETO = "C:\\projetos"

def traco(sep, tamanho):
    print(sep * tamanho)

# Declaração / definição de função
def cabecalho(titulo, sep="-", tamanho=30): # E lido na ordem do valor
    traco(sep, tamanho)
    print(titulo)
    traco(sep, tamanho)

# Chamando uma função
cabecalho("Relatório de despesas")
cabecalho("Folha de pagamento", tamanho=25, sep=".")

# Não colocar os parênteses significa que estou
# falando da função, é não chamando
cabecalho
print(cabecalho) # Não funciona tb (apenas fala a indentidade da função)
print(cabecalho("Olá", tamanho=25))

# Toda função tem um retorno
print (print("Olá, mundo"))
# print(input("nome: "))

def soma(a, b):
    return a + b

print(soma(2,5) + soma(4,9))

x = 5
print(x % 2 == 0)

print("-" * 30)
def e_par(num):
    return num % 2 == 0

print(e_par(8))
print(e_par(55))

def troca_valores(a, b):
    return b, a

print(troca_valores(8, 0))
y = 5

x, y = troca_valores(x, y)
print(x, y)

print("-" * 30)
# Escopo de variáveis
def func1():
    a = 10
    print(a) # escopo local
    print(x) # escopo global

def func2(x):
    x = 999
    print(x) # escopo local tem preferência

func2(100)
print(x)

def func3():
    global x # NÃO USAR
    x = 0
    print(x)

func3()
print(x) # 0
