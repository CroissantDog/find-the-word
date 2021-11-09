from pedir_dato import pedir_dato
from validacion import cantidad_menor_a, menor_30_caracteres, entero_mayor_a_15

def pedir_datos_tablero():
    pedir_datos_tablero.n = pedir_dato("Ingrese un numero igual o mayor a 15: ", entero_mayor_a_15)

    pedir_datos_tablero.palabras = []
    while cantidad_menor_a(pedir_datos_tablero.n, pedir_datos_tablero.palabras):
        palabra = input("Ingrese una palabra: ")
        if palabra == "fin":
            break
        elif cantidad_menor_a(pedir_datos_tablero.n, palabra):
            pedir_datos_tablero.palabras.append(palabra)
        else:
            print("ERROR. La longitud de la palabra debe ser menor a " + str(pedir_datos_tablero.n/3) + " caracteres.")
    
    pedir_datos_tablero.nombre_archivo = input("Ingrese el nombre del archivo: ")
    while menor_30_caracteres(pedir_datos_tablero.nombre_archivo):
        print("ERROR. El nombre del archivo no puede ser mayor a 30 caracteres.")
        pedir_datos_tablero.nombre_archivo = input("Ingrese el nombre del archivo: ")
    tupla = (pedir_datos_tablero.n, pedir_datos_tablero.palabras, pedir_datos_tablero.nombre_archivo)
    return tupla