def pedir_dato(texto, validacion):
    dato = int(input(texto))
    while validacion(dato) is False:
        dato = int(input("ERROR. " + texto))
    return dato