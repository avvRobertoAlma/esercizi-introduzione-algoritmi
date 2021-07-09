"""
funzione partiziona
@param lista -> il vettore da partizionare
@param start -> indice iniziale
@param end -> indice finale
@param pivot -> il pivot (se è None, si prende ultimo elemento della lista)
"""
def partiziona(lista, start, end, pivot=None):

    # se il pivot non è definito
    # prende in automatico ultimo elemento della lista
    # scelta arbitraria
    if not pivot:
        pivot = lista[end]

    

    # i e j sono i cursori
    # i parte dall'inizio e deve aumentare
    # j parte dalla fine e deve diminuire
    i = start
    j = end

    while i <= end and j >= start: # calamoneri utilizza while true -> deve scorrere tutta la lista

        if lista[i] <= pivot:

            # se l'elemento lista[i] è minore del pivot
            # aumenta i di 1
            i += 1

        if lista[j] > pivot:
            # se lista j è maggiore del pivot
            # diminuisce j di 1
            j -= 1

        # i si ferma quando trova un elemento lista[i] > del pivot
        # j si ferma quando trova un elemento lista[j] < del pivot

        if i < j:
            # se i è minore di j quindi la lista non è stata esaminata tutta
            tmp = lista[j]
            lista[j] = lista[i]
            lista[i] = tmp
            # scambio di posizione lista[i] e lista[j]
            # ricordiamo che prima del pivot ci devono essere elementi minori o uguali del pivot

        # se i >= j:
        else:
            return j
            # significa che il partizionamento è completato 
            # e posso restituire il valore di j alla funzione chiamante
            # j è il cursore che separa gli elementi <= del pivot da quelli più grandi


if __name__ == "__main__":

    A = [12, 2, 45, 7, 17, 8, 3, 1, 9, 55]
    partiziona(A, 0, len(A)-1, 10)
    print(A)

