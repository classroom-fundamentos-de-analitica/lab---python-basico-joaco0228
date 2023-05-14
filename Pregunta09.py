def pregunta_09():
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
    unicos = []
    for i in registros: 
        if i not in unicos:
            unicos.append(i)
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