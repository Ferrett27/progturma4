"""
AC2
09/03/2024
"""
# Exercício 1:

def eq_seg_grau(a, b, c):
    a | b | c == float
    
    dlt = b ** 2 - 4 * a * c

    x1 = (-b + dlt ** 0.5) / (a * 2)
    x2 = (-b - dlt ** 0.5) / (a * 2)

    return x1, x2

# print(eq_seg_grau(1, -6, 8))
    
def bissexto(ano):
    int(ano)

    resul = ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0

    return resul

# print(bissexto(2012))
        
# Exercício 2:
        
def calcula_salario(valor_hora, num_horas, irpf=0.275):
    valor_hora | num_horas == float

    salario_bruto = valor_hora * num_horas
    
    imposto = salario_bruto * irpf

    salario_liquido = salario_bruto - imposto

    return  salario_liquido

# print(calcula_salario(25, 176))