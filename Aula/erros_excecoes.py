"""
Programação Estruturada
2024.1
12/04/2024

Tratamento de erros e exceções
try / except / else / finally
- Uso quando não souber qual exceção pode subir
- Ou quando sei qual exeção pode subir, mas não sei como o código chega lá
"""

def divisao(a, b):
    try:
        print(a / b)
    except ZeroDivisionError:
        print("Erro! o divisor não pode ser 0.")
    except TypeError:
        print("Erro! Ambos os parâmetros precisam ser numéricos.")

#divisao(10, 2)
#divisao(10, 0)
#divisao("abc", 2)

print("=" * 40)

#Caso não saiba o erro
def terceira_letra():
    nome = input("informe seu nome: ")
    try:
        print(f"A terceira letra do seu nome é {nome[2]}.")
    except Exception as err:
        print(f"Erro desconhecido. Erro: {err}")
        print(type(err))
    else:
        print("Leitura dos dados bem sucedida.") # não e muito utilizada
    finally:
        print("Fim da função")

# terceira_letra()

class TamanhoExcedidoError(Exception):
    pass

def exibe_num(numero):
    if numero > 10:
        raise TamanhoExcedidoError

    print(numero)

#exibe_num(15)

def fun1():
    raise NotImplementedError

def func2():
    raise NotImplementedError

fun1()