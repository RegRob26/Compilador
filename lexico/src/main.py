import sys
import re
def creaTablaReserv(archivo):
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

def creaTablaTransiciones(archivo):
    transiciones = []
    with open(archivo) as f:
        for line in f:
            i = 0
            temp = line.strip()
            temp2 = [int(ele) for ele in temp.split()]
            transiciones.append(temp2)

    #print(transiciones[0][0])

    return transiciones

def busquedaPaReser(palabra, tablaPalabrasReservadas):
    """

    :param palabra: Contiene la palabra a buscar dentro del diccionario.
    :param tablaPalabrasReservadas: Es el diccionario de las palabras reservadas en el que se buscara la palabra.
    :return: el valor de la palabra(token) como entero o None en caso de estar dentro del diccionario.
    """
    token = None
    try:
        token = tablaPalabrasReservadas[palabra]
    except:
        pass
    return token

def leerArchivo(fichero, lineas):
    linea = fichero.readline()
    lineas = lineas + 1
    return linea

def leerLinea(linea, archivo):
    linea = linea + 1
    return archivo.readline()

def casosComprobar(simbolo):
    entrada = 0
    notConjunto = "[^*^a-zA-z^\s^/^\d^=^<^>^_^+^-^(^)^{^}^;^\"^,^.^E^-]"

    if simbolo == '/':
        entrada = 0
    elif simbolo == '*':
        entrada = 1
    elif re.findall(notConjunto, simbolo):
        entrada = 2
    elif re.findall(notConjunto, simbolo):
        entrada = 3
    elif re.findall(notConjunto, simbolo):
        entrada = 4
    elif simbolo == '/n':
        entrada = 5
    elif simbolo == '"':
        entrada = 6
    elif simbolo == 'CR':
        entrada = 7
    elif re.findall("[a-zA-z]", simbolo):
        entrada = 8
    elif simbolo == '_':
        entrada = 9
    elif re.findall("[0-9]", simbolo):
        entrada = 10
    elif simbolo == '\t' or simbolo == '\n' or simbolo == ' ':
        entrada = 11
    elif simbolo == '+':
        entrada = 12
    elif simbolo == '-':
        entrada = 13
    elif simbolo == '(':
        entrada = 14
    elif simbolo == ')':
        entrada = 15
    elif simbolo == '{':
        entrada = 16
    elif simbolo == '}':
        entrada = 17
    elif simbolo == ';':
        entrada = 18
    elif simbolo == '<':
        entrada = 19
    elif simbolo == '>':
        entrada = 20
    elif simbolo == '=':
        entrada = 21
    elif simbolo == ',':
        entrada = 22
    elif simbolo == '.':
        entrada = 23
    elif simbolo == 'E':
        entrada = 24
    elif simbolo == '-':
        entrada = 25

    return entrada

def tablaTransiciones(linea, lexema, tt, palabrasReservadas,  cant, error):
    estadoActual = 1
    simbolo = 0
    entrada = 0
    lexemas = []
    estadoAnterior = 0

    lexemasValues = []
    entradaAnterior = 0

    for simbolo in linea:
        vistazo = linea[1:2]
        if estadoActual != 2630:
            entrada = casosComprobar(simbolo)
            if tt[estadoActual][entrada] == -1:
                error.append("Error caracter no identificado en linea " + str(cant) + ' ' + simbolo)
                return -1
            if (estadoActual == 1 or estadoActual == 11) and entrada == 11:
                pass
            elif tt[estadoActual][entrada] != -1:
                lexema = lexema + simbolo
                estadoAnterior = estadoActual
                estadoActual = tt[estadoActual][entrada]

            if tt[estadoActual][len(tt[estadoActual])-2] == 2630 and tt[estadoActual][casosComprobar(vistazo)] == -1:
                lexemas.append(lexema)
                corroboraClave = tt[estadoActual][len(tt[estadoActual])-1]
                if corroboraClave == 301:
                    newToken = busquedaPaReser(lexema, palabrasReservadas)
                    if newToken is not None:
                        lexemas.append(newToken)
                    else:
                        lexemas.append(tt[estadoActual][len(tt[estadoActual])-1])
                else:
                    lexemas.append(tt[estadoActual][len(tt[estadoActual]) - 1])
                lexemas.append(cant)
                lexemasValues.append(lexemas)
                lexemas = []
                lexema = ""
                estadoAnterior = estadoActual
                estadoActual = 1
                entrada = 0

            linea = linea[1:]
            entradaAnterior = entrada

    return lexemasValues

def analizador(transiciones, palabrasReservadas, fichero, tablaSimbolos, tablaErrores):
    cant = 1
    lexema = ""
    linea = leerArchivo(fichero, cant)
    token = 0
    while linea != '':
        error = []
        token = tablaTransiciones(linea, lexema, transiciones, palabrasReservadas, cant, error)
        if token == -1:
            linea = leerArchivo(fichero, cant)
            for dato in error:
                print(dato)
                tablaErrores.write(dato)
                tablaErrores.write('\n')
        cant = cant + 1
        if token != -1:
            linea = leerArchivo(fichero, cant)
            if len(token) >= 1:
                #tablaSimbolos.write("\n".join(token))
                for dato in token:
                    for entrada in dato:
                        tablaSimbolos.write(str(str(entrada)))
                        tablaSimbolos.write('\t')
                    tablaSimbolos.write('\n')

if __name__ == '__main__':
    archivo = "../entradas/tablaPalabrasReservadas.txt"

    #archivoNombre = sys.argv[1]            #Para la lectura por consola del archivo
    archivoNombre = "../entradas/prueba.c"
    tablaPalabrasReservadas = creaTablaReserv(archivo)
    archivoAnalizar = open(archivoNombre, 'r')

    archivoNombreTransi = "../entradas/tablaTransiciones.txt"
    archivoEscribir = "../salidas/tablaSimbolos.txt"
    tablaSimbolos = open(archivoEscribir, 'w')

    archivoErrores = "../salidas/errores.txt"
    tablaErrores = open(archivoErrores, 'w')

    tablaTransicion = creaTablaTransiciones(archivoNombreTransi)

    linea = 0

    analizador(tablaTransicion, tablaPalabrasReservadas, archivoAnalizar, tablaSimbolos, tablaErrores)





