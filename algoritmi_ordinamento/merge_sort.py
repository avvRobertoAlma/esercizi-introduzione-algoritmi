"""
algoritmo che, nella versione ricorsiva si basa sulla tecnica del divide et impera
"""

def merge_sort(lista, start, end):

    if start < end:

        medium = int((start+end)/2)
        merge_sort(lista, start, medium)
        merge_sort(lista, medium+1, end)
        fondi(lista, start, medium, end)


    return

def fondi(lista, start, medium, end):
    # creo una nuova lista b
    b = list()
    i = start
    j = medium+1

    # finché i è minore o uguale dell'indice medio e j è minore o uguale dell'ultimo indice

    while i <= medium and j <= end:

        # prendo il minimo tra il primo sottovettore e il secondo sottovettore
        if (lista[i] < lista[j]):
            b.append(lista[i])
            # aumento i
            i += 1
        else:
            b.append(lista[j])
            j += 1
    
    # se il primo sottovettore non è terminato
    while i<= medium:
        b.append(lista[i])
        # aumento i
        i += 1

    # se il secondo sottovettore non è terminato
    while j<= end:
        b.append(lista[j])
        j += 1


    ## ricopia i valori di b in lista
    for i in range(len(b)):
        lista[start+i] = b[i]




## versione iterativa merge sort (da fare)







if __name__ == "__main__":
    l = [1, 5, 2, 3, 4, 7, 6, 9, 8, 0, 10]
    merge_sort(l, 0, 10)
    print(l)