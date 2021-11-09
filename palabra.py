from obtener_datos import Obtener_Datos

o = Obtener_Datos()

class Palabra:
    def __init__(self):
        self.palabra = ""
    
    def crear(self):
        inp = input("Ingrese una palabra que haya encontrado: ")
        self.palabra = inp

    def obtener_palabra(self):
        return self.palabra