"""
AC3
09/03/2024
"""
# Exercício 1:

def determina_tipo_triangulo(l1, l2, l3):
    if l1 == l2 == l3:
        return "Equilátero"
    elif l1 != l2 == l3:
        return "Isóceles"
    elif l1 != l2 != l3:
        return "Escaleno"
    else:
        return "Não é um triangulo"

def testa_triangulo():
    print(determina_tipo_triangulo(4, 4, 4)) # Equilátero
    print(determina_tipo_triangulo(3, 5, 5)) # Isósceles
    print(determina_tipo_triangulo(5, 8, 5)) # Escaleno
    print(determina_tipo_triangulo(2, 2, 4)) # Não é um triângulo

# testa_triangulo()

# Exercício 2:

def dia_semana(dia):
    if 1 <= dia <= 7:
        match dia:
            case 1:
                return "Domingo"
            case 2:
                return "Segunda-feira"
            case 3:
                return "Terça-feira"
            case 4:
                return "Quarta-feira"
            case 5:
                return "Quinta-feira"
            case 6:
                return "Sexta-feira"
            case 7:
                return "Sábado"
    else:
        return ""

def testa_dia_semana():
    print(dia_semana(2)) # segunda-feira
    print(dia_semana(6)) # sexta-feira
    print(dia_semana(7)) # sábado
    print(dia_semana(9)) # string vazia
    
# testa_dia_semana()
    
# Exercício 3:

def inserir_numeros():
    """Retorna o número inserido pelo usuário."""
    x = float(input("Insira um número: "))
    y = float(input("Insira outro número: "))
    return x, y

def operacao():
    """Retorna a operação inserida pelo usuário."""
    opr = input("Informe a operação: ")
    return opr

def calculadora():
    x, y = inserir_numeros()
    opr = operacao()
    
    match opr:
        case "soma":
            resul = x + y
        case "subtracao":
            resul = x - y
        case "multiplicacao":
            resul = x * y
        case "divisao":
            resul = x / y
        case _:
            resul = "Operação inválida"
    
    print("Resultado:", resul)


# calculadora()
