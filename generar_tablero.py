import random
import string


def generar_tablero(n, palabras):
    # Crear la matriz que represente al tablero
    generar_tablero.matriz = []
    # Crear listas dentro de listas
    for i in range(0, n):
        generar_tablero.matriz.append([])
    # Agrega caracteres aleatorios a cada lista
    for i in range(0, n):
        for j in range(0, n):
            generar_tablero.matriz[i].append(random.choice(string.ascii_letters).lower())

    # Se crea el diccionario que contendrá la solución
    generar_tablero.dic = {}

    for palabra in palabras:
        #Se inserta la palabra en el diccionario, creando otro diccionario dentro
        generar_tablero.dic.update({palabra: {}})
        # Se situa el indice en 0,0 y se asigna una direccion aleatoria
        x = 0
        y = 0

        direccion = random.randint(0, 1)

        # Si direccion es igual a 0, la palabra se pone en vertical
        # y se agregan los ejes iniciales y finales al diccionario
        if direccion == 0:
            x = random.randint(0, n - 1)
            y = 0
            generar_tablero.dic[palabra].update({'x_inicial': x})
            generar_tablero.dic[palabra].update({'y_inicial': y})
            for letra in palabra:
                generar_tablero.matriz[y][x] = letra
                y += 1
                generar_tablero.dic[palabra].update({'x_final': x})
                generar_tablero.dic[palabra].update({'y_final': y})

        # Caso contrario, horizontal
        # tambien se guardan los ejes iniciales y finales en el diccionario
        else:
            y = random.randint(0, n - 1)
            x = 0
            generar_tablero.dic[palabra].update({'x_inicial': x})
            generar_tablero.dic[palabra].update({'y_inicial': y})
            for letra in palabra:
                generar_tablero.matriz[y][x] = letra
                x += 1
                generar_tablero.dic[palabra].update({'x_final': x})
                generar_tablero.dic[palabra].update({'y_final': y})
 
        
     
    return generar_tablero.matriz