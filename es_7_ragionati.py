"""
Dato un vettore A di n interi, progettare un algoritmo ricorsivo che restituisce il massimo ed il
minimo di A in tempo O(n). Verificare tale costo computazionale tramite l’impostazione e la
risoluzione di un’equazione di ricorrenza.
"""

def trova_min_max(min, max, lista):

    current_value = lista[0] #c1

    if current_value > max: #c2
        max = current_value #¢3
    
    if not min or current_value < min: #c4 + c5
        min = current_value #c6

    if (len(lista) == 1): #c7
        return (min, max) #c8


    else:
        return trova_min_max(min, max, lista[1:]) #T(n-1)

#ricorrenza
# T(1) = Theta(1):
# T(n) = T(n-1) + Theta(1)


if __name__ == "__main__":

    print(trova_min_max(None, 0, [1,5,6,12, 56,11]))
    