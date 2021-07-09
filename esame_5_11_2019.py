"""algoritmo efficiente per spostare tutti i numeri dispari prima dei pari"""

def separa_dispari_pari(vettore):

    i = 0 # cursore iniziale
    j = i-1

    while i<len(vettore):

        # mentre itero sul vettore con il cursore i che aumenta ad ogni iteraizone
        # verifico se il valore è dispari
        if(vettore[i] % 2 != 0):
            # se è dispari, aumento j di 1
            # assegno il valore di i nella posizione j
            # la posizione di j aumentata di 1 viene scambiata con i (che sarebbe più avanti)
            j += 1
            tmp = vettore[j]
            vettore[j] = vettore[i]
            vettore[i] = tmp
        
        i += 1

    
if __name__ == "__main__":

    l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    separa_dispari_pari(l)
    print(l)
        