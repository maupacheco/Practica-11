#Incremental
#Uso del Insertion Sort

def insertSort(lista):
    for index in range (1, len(lista)):
        actual = lista[index]
        posicion = index
        #print("valor a ordenar {}".format(actual))
        while posicion>0 and lista[posicion-1]>actual:
            lista[posicion] = lista[posicion-1]
            posicion = posicion-1
        lista[posicion] = actual
        #print(lista)
        #print()
    return lista

lista = [21, 10, 12, 0, 34, 15]
#print(lista)
insertSort(lista)
#print(lista)

