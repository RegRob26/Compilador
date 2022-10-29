import sys


def creaTabla(archivo):
    a = {}
    with open(archivo) as f:
        for line in f:
            (k, v) = line.split(',')
            a[str(k)] = int(v)
    return a

def busquedaPaReser(palabra, tablaPalabrasReservadas):
    return tablaPalabrasReservadas[palabra]

if __name__ == '__main__':
    """

    :return: valor de salida del programa principal
    """
    archivo = "../entradas/tablaPalabrasReservadas.txt"

    archivoNombre = sys.argv[1]            #Para la lectura por consola del archivo
    tablaPalabrasReservadas = creaTabla(archivo)
    print(tablaPalabrasReservadas)
    print(busquedaPaReser("else", tablaPalabrasReservadas))





