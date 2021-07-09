"""
quicksort
Algoritmo di ordinamento ricorsivo
	 * Il cuore è costituito dal metodo partiziona che restituisce l'indice medio con cui dividere il vettore
	 * vengono poi effettuate due chiamate ricorsive
	 * @param lista -> il vettore da ordinare
	 * @param indice_iniziale
	 * @param indice_finale
"""
def quick_sort(lista, indice_iniziale, indice_finale):

    if indice_iniziale < indice_finale:
        indice_medio = partiziona(lista, indice_iniziale, indice_finale)
        # indice_medio è un pivot sulla cui base dividere il vettore in due sottovettori
        quick_sort(lista, indice_iniziale, indice_medio-1)
        quick_sort(lista, indice_medio+1, indice_finale)

    return

def partiziona(lista, indice_iniziale, indice_finale):

    ## la prima cosa da fare è trovare l'elemento pivot
    pivot = lista[indice_finale] # posso scegliere anche l'ultimo elemento

    # creo un cursore
    i = indice_iniziale -1 

    """
	 * vado con il cursore in avanti dalla prima posizione del vettore fino alla ultima -1
	 * dato che è l'ultimo elemento il pivot
    """
    j = indice_iniziale
    while j<indice_finale:
        
        if lista[j] <= pivot:
            """
             * se l'elemento corrente è minore o uguale del pivot
			 * aumento la posizione di i di 1;
			 * scambio A[j] con A[i]
			 * In sostanza tramite il cursore j si esaminano tutti gli elementi del vettore				
             * il cursore i separa quelli più grandi da quelli più piccoli o uguali del pivot
			 * se A[j] è minore o uguale del pivot, si sposta di 1 il cursore i e si scambia A[j] con A[i]
			 */	
            """
            i += 1

            ## scambiare lista[j] con lista[i]
            tmp = lista[i]
            lista[i] = lista[j]
            lista[j] = tmp

        j = j + 1

        """
        /* a questo punto abbiamo spostato tutti gli elementi più grandi del pivot a destra
		 * bisogna solo scambiare il pivot con l'ultimo elemento (i + 1)
		 */
        """
    tmp = lista[i+1]
    lista[i+1] = pivot
    lista[indice_finale] = tmp

    print(lista)
    return i+1




if __name__ == "__main__":

    l = [1, 5, 2, 3, 4, 7, 6, 9, 8, 0, 10]
    quick_sort(l, 0, len(l)-1)
    print(l)