"""
counting sort
ordinamento lineare
c'è un vettore di appoggio C
che conterrà il numero di occorrenze dei valori della lista da ordinare
"""

def counting_sort(lista, max_element):

    C = list()

    # 1. creare un vettore con tutti zeri (Theta(n))
    # si va da 1 all'elemento massimo (non ci devono essere zeri)

    C = [0 for i in range(1, max_element+1)]

    # 2. ogni valore di lista viene inserito in una posizione di C e per ogni occorrenza si aggiunge +1
    # es. se la lista ha 3 volte il valore 5
    # in posizione 5 avremo un valore 3
    for i in range(len(lista)):
        C[lista[i]-1] += 1

    
    # 3. riassegnamo i valori alla lista
    # j è l'indice delal lista (partiamo da zero)
    j = 0

    print(C)

    for i in range(len(C)):

        while C[i] > 0:
            # la prima posizione di i è 0, +1 = 1
            lista[j] = i+1
            j += 1
            C[i] -= 1

    

if __name__ == "__main__":

    lista = [1, 5, 2, 3, 4, 4, 2, 2, 5, 6, 8, 11, 10]
    counting_sort(lista, 11)
    print(lista)
    