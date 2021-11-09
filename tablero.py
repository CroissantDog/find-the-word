import re
from generar_tablero import generar_tablero
from obtener_datos import Obtener_Datos
from palabra import Palabra
from datos_tablero import pedir_datos_tablero
from jugador import Jugador

j = Jugador()
p = Palabra()
o = Obtener_Datos()

class tablero:
    def __init__(self):
        self
    
    def imprimir():
        matriz = str(generar_tablero.matriz)
        matriz = re.sub(r'[-\+!~@#$%^&*()={}\[\:;<.>?/\'"]', "", matriz)
        matriz = re.sub(r'[,]', "", matriz)
        matriz = re.sub(r'[]]', "\n", matriz)
        matriz = matriz.replace(" ", " | ") 
        print(" | " + matriz)

    
    
    def encontrar_palabra(self):
        dic = generar_tablero.dic
        t = tablero()

        p.crear()

        if p.palabra == "fin":
            print(j.imprimir_nombre(), "su puntaje es: ", j.imprimir_puntaje(), "\n", "Las palabras encontradas son: ", j.lista_encontradas(), "\n", "Las palabras que faltaron encontrar son: ", j.lista_no_encontradas())

        elif p.palabra in dic:
            x1 = dic[p.palabra].get("x_inicial")
            x2 = dic[p.palabra].get("x_final")
            y1 = dic[p.palabra].get("y_inicial")
            y2 = dic[p.palabra].get("y_final")

            #Pone la palabra en mayuscula
            txt = p.palabra.upper()
            #La convierte en lista, cada letra es un indice
            mayus = list(txt)
            
            #Se verifica si la palabra es horizontal o vertical
            #Luego, se reemplaza el indice de la matriz, por el indice de la lita
            #que contiene la palabra
            if y1 == y2:
                for i in range(x1, x2):
                    generar_tablero.matriz[y1][i] = mayus[i]
            else:
                for i in range(y1, y2):
                    generar_tablero.matriz[i][x1] = mayus[i]


            j.sumar_punto()

            j.palabras_encontradas.append(p.palabra)

            tablero.imprimir()
            t.encontrar_palabra()
        else:
            print("La palabra ingresada no se encuentra en el tablero")
            t = tablero()
            t.encontrar_palabra()