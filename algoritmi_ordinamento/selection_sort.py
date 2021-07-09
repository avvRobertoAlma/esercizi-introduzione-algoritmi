"""
selection sort, per ogni elemento della lista scambia quello in prima posizione con il minimo
"""

def selection_sort(lista):

    ## deve scambiare l'elemento in prima posizione con il minimo
    ## e poi via via con i successivi minimi

    for i in range(len(lista)):
        current = lista[i]

        # m è il minimo ?
        m = i


        for j in range(i+1, len(lista)):
            if lista[j] < lista[m]:
                m = j

        # uscito dal ciclo lista[j] è il minimo
        tmp = lista[i]
        lista[i] = lista[m]
        lista[m] = tmp
    
    return lista

if __name__ == "__main__":

    print(selection_sort([4, 7, 1, 2, 9, 12, 5, 99, 65]))