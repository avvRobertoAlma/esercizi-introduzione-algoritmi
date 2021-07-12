"""
counting sort

"""

def counting_sort(lista, elemento_massimo):

    """
    ordinamento lineare (Theta(n)
    si crea una lista A di appoggio
    in cui ogni posizione corrisponde a un elemento della lista input
    es. la posizione 1 della lista A corrisponde al valore "1" contenuto nella lista input
    se A[1] = 3 significa che ci sono 3 occorrenza di 1 nella lista input
    
    """

    A = [0 for i in range(1, elemento_massimo+1)]

    for i in range(len(lista)):

        """
        per ogni indice della lista
        si prende il valore lista[i]
        qquesto valore è la posizione in A
        si aumenta di 1 il valore corrispondente in A
        """
        A[lista[i]-1] += 1

    """
    utilizzo un cursore j
    che servirà per scorrere la lista A e aggiornare i valori
        
    """
    j=0

    """
    ciclo for che viene eseguito per ogni valore della lista di Appoggio
        
    """
    for i in range(len(A)):
        while A[i] > 0:
            print(i)
            lista[j] = i+1
            A[i] -= 1
            j += 1



if __name__ == "__main__":

    v = [3, 1, 3, 9, 11, 8, 23, 6, 3, 4]
    counting_sort(v, 23)
    print(v)
