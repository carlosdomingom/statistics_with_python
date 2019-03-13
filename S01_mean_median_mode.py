if __name__ == '__main__':
    n = int(input())
    lista = []
    # Ordeno la lista numérica sobre lo que recibo como entrada
    lista = sorted(list(map(float, input().split())))
    # Imprimo la suma entre el total de valores (media)
    print("{0:.1f}".format(sum(lista) / n))
    # Imprimo la mediana. Con valores pares, es la media de los dos
    # del medio. Con valores impares, el valor central
    mediana = lista[(n-1)//2:n//2+1]
    print("{0:.1f}".format(sum(mediana) / len(mediana)))
    modadic = {}
    modalist = []

    # Creo un diccionario e inserto los valores sin repetirlos
    # junto con la cantidad
    for x in lista:
        if x not in modadic:
            modadic[x] = 1
        else:
            modadic[x] += 1

    max = 0

    # Ordeno el diccionario por valor y clave
    for key, value in sorted(modadic.items(), key=lambda kv:(-kv[1], kv[0]), reverse=True):
        # Dejo de insertar en la nueva lista cuando el valor es menor
        if value >= max:
            modalist.append(key)
            max = value

    if(modadic[modalist[0]] == modadic[modalist[1]]):
        print(modalist[-1])
    else:
        print(modalist[0])
