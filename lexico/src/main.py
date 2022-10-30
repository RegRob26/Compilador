import sys
def creaTabla(archivo):
    """

    :param archivo:
    :return:
    """
    diccionario = {}
    with open(archivo) as f:
        for line in f:
            (k, v) = line.split(',')
            diccionario[str(k)] = int(v)
    return diccionario

def busquedaPaReser(palabra, tablaPalabrasReservadas):
    """

    :param palabra: Contiene la palabra a buscar dentro del diccionario.
    :param tablaPalabrasReservadas: Es el diccionario de las palabras reservadas en el que se buscara la palabra.
    :return: el valor de la palabra(token) como entero o None en caso de estar dentro del diccionario.
    """
    return tablaPalabrasReservadas[palabra]

if __name__ == '__main__':
    archivo = "../entradas/tablaPalabrasReservadas.txt"

    archivoNombre = sys.argv[1]            #Para la lectura por consola del archivo
    tablaPalabrasReservadas = creaTabla(archivo)


    print(tablaPalabrasReservadas)
    print(busquedaPaReser("else", tablaPalabrasReservadas))





