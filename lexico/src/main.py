import sys
import re


def creaTablaReserv(archivo):
    """
    Crea un diccionario apartir de los elementos del archivo dado que contiene las palabras reservadas con su respectivo
    token
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

    return transiciones


def busquedaPaReser(palabra, tablaPalabrasReservadas):
    """
    Busca en el diccionario de palabras reservadas el valor de un lexema dado

    :param palabra: Contiene la palabra a buscar dentro del diccionario.
    :param tablaPalabrasReservadas: Es el diccionario de las palabras reservadas en el que se buscara la palabra.
    :return: el valor de la palabra(token) como entero o None en caso de no estar dentro del diccionario.
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


def tablaTransiciones(linea, lexema, tt, palabrasReservadas, cant, error):
    """
    Esta funcion contiene en si las comprobaciones de los estados con sus entradas mediante diversos condiconales, pero
    funciona con una cadena dada por una funcion superior, es decir solo recibe una linea del programa fuente y va determinando
    tokens segun las entradas.

    :param linea:
    :param lexema:
    :param tt:
    :param palabrasReservadas:
    :param cant:
    :param error:
    :return:
    """
    estadoActual = 1
    simbolo = 0
    entrada = 0
    lexemas = []
    estadoAnterior = 0

    lexemasValues = []
    entradaAnterior = 0

    for simbolo in linea:
        # El 'vistazo' sera nuestra forma de saber si seguir leyendo la cadena o se puede ya almacenar el lexema con su
        # valores encontrados. Por lo que es el caracter de comprobacion.
        vistazo = linea[1:2]
        if estadoActual != 2630:
            entrada = casosComprobar(simbolo)

            if tt[estadoActual][entrada] == -1:
                error.append("Error caracter no identificado en linea " + str(cant) + ' ' + simbolo)
                return -1

            # Nos permite realizar la omision para delimitadores y comentarios con pass para dicha accion
            if ((estadoActual == 1 or estadoActual == 11) and entrada == 11) or tt[estadoActual][
                len(tt[estadoActual]) - 1] == 1:
                pass
            # si nuestro estado actual tiene transicion con la entrada dada, es decir, es diferente de -1 entonces almacenara
            # el lexema con lo previamente guardado en pasos anteriores y cambiaara de estado
            elif tt[estadoActual][entrada] != -1:
                lexema = lexema + simbolo
                estadoAnterior = estadoActual
                estadoActual = tt[estadoActual][entrada]
            # Si nuestro estado es de aceptacion y el 'vistazo' ya no corresponde al lenguaje del automata en ejecucion,
            # entonces almacenara el lexema junto con su token y la linea en la que aparece
            if tt[estadoActual][len(tt[estadoActual]) - 2] == 2630 and tt[estadoActual][casosComprobar(vistazo)] == -1:
                lexemas.append(lexema)
                corroboraClave = tt[estadoActual][len(tt[estadoActual]) - 1]
                if corroboraClave == 1:
                    pass
                else:
                    # Como las palabras reservadas son tambien id, antes de almacenar un id se comprueba que no sea una
                    # palabra reservada
                    if corroboraClave == 301:
                        newToken = busquedaPaReser(lexema, palabrasReservadas)
                        if newToken is not None:
                            lexemas.append(newToken)
                        else:
                            lexemas.append(tt[estadoActual][len(tt[estadoActual]) - 1])
                    else:
                        lexemas.append(tt[estadoActual][len(tt[estadoActual]) - 1])
                    lexemas.append(cant)
                    lexemasValues.append(lexemas)
                    lexemas = []
                    lexema = ""
                    estadoAnterior = estadoActual
                    estadoActual = 1
                    entrada = 0

            # Eliminamos el caracter del buffer de entrada para mejor manejo
            linea = linea[1:]
            entradaAnterior = entrada
    # Se retorna la lista de valores con los tokens encontrados
    return lexemasValues


def analizador(transiciones, palabrasReservadas, fichero, tablaSimbolos, tablaErrores):
    """
    La funcion principal del analizador Lexico, de manera general se encarga de leer linea a linea el archivo fuente y
    comprobar los valores de salida de la tabla de transiciones con cada caracter dado, almacenando los resultados en dos
    archivos diferentes, uno para los errores y otro que tiene la tabla de simbolos encontrados

    Para detalle, la tabla de simbolos contiene los datos en el siguiente orden:
        lexema, tipoToken,  #Linea.

    :param transiciones:
    :param palabrasReservadas:
    :param fichero:
    :param tablaSimbolos:
    :param tablaErrores:
    :return: sin retorno
    """
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
                for dato in token:
                    for entrada in dato:
                        tablaSimbolos.write(str(str(entrada)))
                        tablaSimbolos.write('\t')
                    tablaSimbolos.write('\n')


if __name__ == '__main__':
    archivo = "../entradas/tablaPalabrasReservadas.txt"

    archivoNombre = sys.argv[1]            #Para la lectura por consola del archivo
    #archivoNombre = "../entradas/prueba.c"
    tablaPalabrasReservadas = creaTablaReserv(archivo)
    archivoAnalizar = open(archivoNombre, 'r')

    archivoNombreTransi = "../entradas/tablaTransiciones.txt"
    archivoEscribir = sys.argv[2]
   # archivoEscribir = "../salidas/tablaSimbolos.txt"
    tablaSimbolos = open(archivoEscribir, 'w')

    archivoErrores = sys.argv[3]
    #archivoErrores = "../salidas/errores.txt"
    tablaErrores = open(archivoErrores, 'w')

    tablaTransicion = creaTablaTransiciones(archivoNombreTransi)


    print(tablaPalabrasReservadas)
    analizador(tablaTransicion, tablaPalabrasReservadas, archivoAnalizar, tablaSimbolos, tablaErrores)
