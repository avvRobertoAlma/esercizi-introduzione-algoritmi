"""dato un vettore di n numeri reali non nulli,
progettare un algoritmo efficiente che posizioni tutti gli elementi negativi prima dei positivi
"""

def posiziona_numeri(lista, start, end):

    pivot = 0 # c1
    j = start # c2
    i = start -1 #c3

    while j < end: # la lista è di n numeri, quindi n-volte

        if lista[j] <= pivot: #c4
            i += 1 #c5
            tmp = lista[j] #c6
            lista[j] = lista[i] #c7
            lista[i] = tmp #c8
        
        j += 1 #c9

    # Theta(n)




if __name__ == "__main__":

    l = [-5, 4, 2, 3, 7, 1, 18, -2, -9, -3, -234, 0]
    posiziona_numeri(l, 0, len(l)-1)
    print(l)



