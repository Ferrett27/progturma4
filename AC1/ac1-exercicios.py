"""
Trabalho AC 1 
02/03/2024

"""
# Exercício 1:

def func1(sep="=" * 35):
    a = float(input("Informe o valor de a da equação: "))
    b = float(input("Informe o valor de b da equação: "))
    c = float(input("Informe o valor de c da equação: "))
    
    delta = b ** 2 - 4 * a * c
    
    x1 = (-b + delta ** 0.5) / (a * 2)
    x2 = (-b - delta ** 0.5) / (a * 2)

    print(sep)
    print("A primeira raiz da equação é", x1)
    print("A segunda raiz da equação é", x2)
    print(sep)
    
 

# Exercício 2:

def func2(sep="-" * 26, sep2=" " * 10):
    ano = int(input("Informe o ano: ")) 

    resultado = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

    print(sep)
    print(sep2, resultado)
    print(sep)
