"""
insertion sort è un algoritmo in cui si scorre una lista dalla posizione i+1 (con i che parte da 0)
e si spostano tutti gli elementi da j=i-1 a destra se maggiori di lista[i]

"""


def insertion_sort(lista):
    
    for i in range(1, len(lista)):

        # estrazione elemento corrente:
        current = lista[i]

        # sposto tutti gli elementi del vettore precedente [1...i-1] a dx di una unità se current
        # è minore
        j = i-1
        while j>=0 and lista[j] > current:
            lista[j+1] = lista[j]
            j -= 1

        # a questo punto so che current è minore di lista[j]
        lista[j+1] = current

    return lista


if __name__ == "__main__":

    l = [4, 2, 6, 1, 9, 12, 5]
    print(insertion_sort(l))
