import csv
import itertools
from generar_tablero import generar_tablero
from datos_tablero import pedir_datos_tablero


def escribir_juego(matriz, dic, nombre_archivo):
    # Se escribe el .csv del juego
    with open(nombre_archivo + ".csv", "w", newline='') as archivo:
        writer = csv.writer(archivo)
        archivo = writer.writerows(generar_tablero.matriz)

    # Se escribe el .csv con la solucion
    columnas = ['palabra', 'x_inicial', 'y_inicial', 'x_final', 'y_final']
    with open(nombre_archivo + "_solucion" + ".csv", "w", newline='') as archivo:
        w = csv.DictWriter(archivo, columnas)
        w.writeheader()
        for key,val in sorted(generar_tablero.dic.items()):
            row = {'palabra': key}
            row.update(val)
            w.writerow(row)