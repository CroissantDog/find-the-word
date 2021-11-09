from generar_tablero import generar_tablero
from validacion import menor_40_caracteres
from datos_tablero import pedir_datos_tablero
import os



class Jugador:
    def __init__(self):
        self.puntaje = 0
        self.nombre_jugador = self.crear()
        self.palabras_encontradas = []
        self.palabras_no_encontradas = []
    
    def crear(self):
        inp = input("Ingrese su nombre: ")
        while menor_40_caracteres(inp) is True:
            inp = input("Su nombre debe contener menos de 40 caracteres. Introduza su nombre: ")
        return inp
    
    def archivo():
        if os.path.exists(pedir_datos_tablero.nombre_archivo + '.csv') is True:
            pass
        else:
            print("El archivo de juego no existe, reinicie el programa para crearlo.")
        
    def sumar_punto(self):
        self.puntaje += 1
    
    def imprimir_puntaje(self):
        return self.puntaje

    def imprimir_nombre(self):
        return self.nombre_jugador
    
    def lista_encontradas(self):
        return self.palabras_encontradas

    def lista_no_encontradas(self):
        for i in generar_tablero.dic:
            if i in self.palabras_encontradas:
                continue
            else:
                self.palabras_no_encontradas.append(i)
        return self.palabras_no_encontradas