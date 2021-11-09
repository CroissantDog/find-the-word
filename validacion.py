import os.path
# Funciones de validación
def mayor_a_10(numero):
    return int(numero) > 10

def entero_mayor_a(n, m):
    return n >= m

def entero_mayor_a_15(n):
    return entero_mayor_a(n, 15)

def cantidad_menor_a(n, variable):
    return len(variable) < n / 3

def menor_30_caracteres(n):
    return len(n) > 30

def menor_40_caracteres(n):
    return len(n) > 40

def existe_archivo(n):
    os.path.exists(n)