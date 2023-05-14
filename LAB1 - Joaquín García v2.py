"""
Laboratorio de Programación Básica en Python para Manejo de Datos
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

No puede utilizar pandas, numpy o scipy. Se debe utilizar solo las funciones de python
básicas.

Utilice el archivo `data.csv` para resolver las preguntas.


"""


def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    suma = 0
    for i in datos:
        suma+=int(i[1])
    return suma

def pregunta_02():
    """
    Retorne la cantidad de registros por cada letra de la primera columna como la lista
    de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [
        ("A", 8),
        ("B", 7),
        ("C", 5),
        ("D", 6),
        ("E", 14),
    ]

    """
    col1 = []

    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    for i in datos:
        col1.append(i[0])

    unicos = list(set(col1))
    unicos.sort()

    lista = []
    for i in unicos: 
        contador = 0
        for j in col1: 
            if i==j:
                contador+=1
        tupla = (i, contador)
        lista.append(tupla)
    return lista

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como una lista
    de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [
        ("A", 53),
        ("B", 36),
        ("C", 27),
        ("D", 31),
        ("E", 67),
    ]

    """
    col1 = []
    col2 = []

    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    for i in datos:
        col1.append(i[0])
        col2.append(i[1])

    unicos = list(set(col1))
    unicos.sort()

    lista = []
    for i in unicos:
        contador = 0
        suma = 0
        for j in col1:
            if i==j:
                suma+=int(col2[contador])
            contador+=1
        tupla = (i,suma)
        lista.append(tupla)
    return lista

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la cantidad de
    registros por cada mes, tal como se muestra a continuación.

    Rta/
    [
        ("01", 3),
        ("02", 4),
        ("03", 2),
        ("04", 4),
        ("05", 3),
        ("06", 3),
        ("07", 5),
        ("08", 6),
        ("09", 3),
        ("10", 2),
        ("11", 2),
        ("12", 3),
    ]

    """
    col3 = []

    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    for i in datos:
        col3.append(i[2])

    meses = []
    for i in col3:
        meses.append(i[i.index("-")+1:i.rindex("-")])

    unicos = list(set(meses))
    unicos.sort()

    lista = []
    for i in unicos: 
        contador = 0
        for j in meses:
            if i == j:
                contador+=1
        tupla = (i, contador)
        lista.append(tupla)
    return lista

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2 por cada
    letra de la columa 1.

    Rta/
    [
        ("A", 9, 2),
        ("B", 9, 1),
        ("C", 9, 0),
        ("D", 8, 3),
        ("E", 9, 1),
    ]

    """

    col1 = []
    col2 = []

    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    for i in datos:
        col1.append(i[0])
        col2.append(i[1])

    unicos = list(set(col1))
    unicos.sort()

    lista = []
    for i in unicos:
        contador = 0
        primer_registro = 0
        for j in col1:
            if i==j:
                num = int(col2[contador])
                if primer_registro == 0:
                    maximo = num
                    minimo = num
                    primer_registro=1
                else:
                    if num>maximo:
                        maximo = num
                    if num<minimo:
                        minimo = num
            contador+=1
        tupla = (i,maximo, minimo)
        lista.append(tupla)
    return(lista)

def pregunta_06():
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras corresponde a
    una clave y el valor despues del caracter `:` corresponde al valor asociado a la
    clave. Por cada clave, obtenga el valor asociado mas pequeño y el valor asociado mas
    grande computados sobre todo el archivo.

    Rta/
    [
        ("aaa", 1, 9),
        ("bbb", 1, 9),
        ("ccc", 1, 10),
        ("ddd", 0, 9),
        ("eee", 1, 7),
        ("fff", 0, 9),
        ("ggg", 3, 10),
        ("hhh", 0, 9),
        ("iii", 0, 9),
        ("jjj", 5, 17),
    ]

    """
    col5 = []
    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    for i in datos:
        linea = i[4].replace("\n", "").split(",")
        for j in linea: 
            col5.append(j)

    registros = []
    numeros = []
    for i in col5:
        dividido = i.split(":")
        registros.append(dividido[0])
        numeros.append(dividido[1])

    lista = []
    unicos = list(set(registros))
    unicos.sort()
    for i in unicos:
            contador = 0
            primer_registro = 0
            for j in registros:
                if i==j:
                    num = int(numeros[contador])
                    if primer_registro == 0:
                        maximo = num
                        minimo = num
                        primer_registro=1
                    else:
                        if num>maximo:
                            maximo = num
                        if num<minimo:
                            minimo = num
                contador+=1
            tupla = (i,minimo, maximo)
            lista.append(tupla)
    return lista
    
def pregunta_07():
    """
    Retorne una lista de tuplas que asocien las columnas 0 y 1. Cada tupla contiene un
    valor posible de la columna 2 y una lista con todas las letras asociadas (columna 1)
    a dicho valor de la columna 2.

    Rta/
    [
        (0, ["C"]),
        (1, ["E", "B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E", "E", "D"]),
        (4, ["E", "B"]),
        (5, ["B", "C", "D", "D", "E", "E", "E"]),
        (6, ["C", "E", "A", "B"]),
        (7, ["A", "C", "E", "D"]),
        (8, ["E", "D", "E", "A", "B"]),
        (9, ["A", "B", "E", "A", "A", "C"]),
    ]

    """

    col1 = []
    col2 = []

    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    for i in datos:
        col1.append(i[0])
        col2.append(i[1])

    unicos = list(set(col2))
    unicos.sort()

    lista = []
    for i in unicos: 
        registros = []
        contador = 0
        for j in col2:
            if i == j:
                registros.append(col1[contador])
            contador+=1
        tupla = (int(i), registros)
        lista.append(tupla)
    return lista

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla contiene  el valor
    de la segunda columna; la segunda parte de la tupla es una lista con las letras
    (ordenadas y sin repetir letra) de la primera  columna que aparecen asociadas a dicho
    valor de la segunda columna.

    Rta/
    [
        (0, ["C"]),
        (1, ["B", "E"]),
        (2, ["A", "E"]),
        (3, ["A", "B", "D", "E"]),
        (4, ["B", "E"]),
        (5, ["B", "C", "D", "E"]),
        (6, ["A", "B", "C", "E"]),
        (7, ["A", "C", "D", "E"]),
        (8, ["A", "B", "D", "E"]),
        (9, ["A", "B", "C", "E"]),
    ]

    """
    col1 = []
    col2 = []

    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    for i in datos:
        col1.append(i[0])
        col2.append(i[1])

    unicos = list(set(col2))
    unicos.sort()

    lista = []
    for i in unicos: 
        registros = []
        contador = 0
        for j in col2:
            if i == j:
                registros.append(col1[contador])
            contador+=1
        registros = list(set(registros))
        registros.sort()
        tupla = (int(i), registros)
        lista.append(tupla)
    return lista

def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que aparece cada
    clave de la columna 5.

    Rta/
    {
        "aaa": 13,
        "bbb": 16,
        "ccc": 23,
        "ddd": 23,
        "eee": 15,
        "fff": 20,
        "ggg": 13,
        "hhh": 16,
        "iii": 18,
        "jjj": 18,
    }

    """
    col5 = []
    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    for i in datos:
        linea = i[4].replace("\n", "").split(",")
        for j in linea: 
            col5.append(j)

    registros = []
    numeros = []
    for i in col5:
        dividido = i.split(":")
        registros.append(dividido[0])
        numeros.append(dividido[1])

    diccionario = {}
    unicos = list(set(registros))
    unicos.sort()
    for i in unicos:
            contador = 0
            num_registros = 0
            for j in registros:
                if i==j:
                    num_registros+=1
                contador+=1
            diccionario[i]=num_registros
    return diccionario

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la columna 1 y la
    cantidad de elementos de las columnas 4 y 5.

    Rta/
    [
        ("E", 3, 5),
        ("A", 3, 4),
        ("B", 4, 4),
        ...
        ("C", 4, 3),
        ("E", 2, 3),
        ("E", 3, 3),
    ]


    """
    col1 = []
    col4 = []
    col5 = []

    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    for i in datos:
        col1.append(i[0])
        info4 = i[3].split(",")
        col4.append(info4)
        info5 = i[4].replace("\n", "").split(",")
        col5.append(info5)

    lista = []
    contador = 0
    for i in col1:
        largo_col4 = len(col4[contador])
        largo_col5 = len(col5[contador])
        tupla = (i, largo_col4, largo_col5)
        lista.append(tupla)
        contador += 1

    return lista

def pregunta_11():
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada letra de la
    columna 4, ordenadas alfabeticamente.

    Rta/
    {
        "a": 122,
        "b": 49,
        "c": 91,
        "d": 73,
        "e": 86,
        "f": 134,
        "g": 35,
    }


    """
    col2 = []
    col4 = []

    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    for i in datos:
        col2.append(i[1])
        info4 = i[3].split(",")
        col4.append(info4)

    registros = []
    for i in col4:
        for j in i:
            registros.append(j)

    registros = list(set(registros))
    registros.sort()


    diccionario = {}
    for i in registros:
        suma = 0
        contador = 0
        for j in col4:
            for k in j:
                if i==k:
                    suma+=int(col2[contador])
            contador+=1
        diccionario[i]=suma

    return diccionario

def pregunta_12():
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor la suma de
    los valores de la columna 5 sobre todo el archivo.

    Rta/
    {
        'A': 177,
        'B': 187,
        'C': 114,
        'D': 136,
        'E': 324
    }

    """
    col1 = []
    col5 = []
    datos = []
    with open('data.csv') as archivo:
        for linea in archivo:
            linea = linea.split("\t")
            datos.append(linea)

    for i in datos:
        col1.append(i[0])
        info5 = i[4].replace("\n", "").split(",")
        col5.append(info5)
        
    sumanumeroscol5 = []
    for i in col5:
        sumanum = 0
        for j in i:
            dividido = j.split(":")
            sumanum+=int(dividido[1])
        sumanumeroscol5.append(sumanum)

    unicos = list(set(col1))
    unicos.sort()

    diccionario = {}
    for i in unicos:
        suma = 0
        contador = 0
        for j in col1:
            if i == j:
                suma+=int(sumanumeroscol5[contador])
            contador+=1
        diccionario[i]=suma
    return diccionario
    
