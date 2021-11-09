from datos_tablero import pedir_datos_tablero
from jugador import Jugador
from obtener_datos import Obtener_Datos
from generador_tableros import Generador_Tableros
from escritor import Escritor
from palabra import Palabra
from tablero import tablero

obtener_usuario = Obtener_Datos()
p = Palabra()
t = tablero()

class Programa:
    def __init__(self):
        self
    

    def main():

        Obtener_Datos.obtener_datos_tablero()
        Generador_Tableros.generar(pedir_datos_tablero.n, pedir_datos_tablero.palabras)
        Escritor.escribir_tablero()
        Jugador.archivo()
        tablero.imprimir()
        t.encontrar_palabra()


Programa.main()