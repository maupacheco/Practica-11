#Estrategia divide y vencerás
#Quick Sort
def quicksort(lista):
    quicksort2(lista, 0, len(lista)-1)

def quicksort2(lista, inicio, fin):
    if inicio < fin:
        pivote = particion(lista, inicio, fin)
        quicksort2(lista, inicio, pivote-1)
        quicksort2(lista, pivote+1, fin)

def particion(lista, inicio, fin):
    pivote = lista[inicio]
    #print("valor del pivote {}".format(pivote))
    izquierda = inicio+1 
    derecha = fin
    #print("indice izquierda {} y indice derecha {}".format(izquierda, derecha))
    bandera = False
    while not bandera:
        while izquierda<= derecha and lista[izquierda] <= pivote:
            izquierda = izquierda+1
        while derecha >= izquierda and lista[derecha] >= pivote:
            derecha = derecha -1
        if derecha < izquierda:
            bandera = True
        else:
            temp = lista[izquierda]
            lista[izquierda] = lista[derecha]
            lista[derecha] = temp
    #print(lista)
    temp = lista[inicio]
    lista[inicio] = lista[derecha]
    lista[derecha] = temp
    return derecha

lista = [18, 13, 10, 14, 0, 5, 15, 1]
#print(lista)
quicksort(lista)
#print(lista) 
