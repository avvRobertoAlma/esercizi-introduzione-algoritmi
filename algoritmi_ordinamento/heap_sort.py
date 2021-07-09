"""HEAP SORT"""

"""per prima cosa definisco la funzione heapify"""

"""
@param A -> vettore
@param i -> l'indice del nodo radice considerato
@param n -> la grandezza dell'heap (heap_size)
"""
def heapify(A, i, n):

    ## la prima cosa da fare è calcolare i valori di LEFT e RIGHT
    ## LEFT = 2*i
    ## RIGHT = 2*i +1
    ## NB in python le liste partono da zero (per cui a left e right si deve aggiungere 1)

    massimo = i
    left = 2*i +1
    right = 2*i +2

    if left < n and A[left] > A[massimo]:

        # se sto costruendo un max heap
        # il massimo è l
        massimo = left

    if right < n and A[right] > A[massimo]:

        # se sto costruendo un max heap
        # il massimo è A[l]
        massimo = right
    
    # se il massimo è diverso da i
    if massimo != i:
        tmp = A[massimo]
        A[massimo] = A[i]
        A[i] = tmp

        # ho scambiato A[massimo] con A[i]
        # rieseguo heapify sul nuovo nodo radice

        heapify(A, massimo, n)

def build_heap(A):

    # n è la lunghezza del vettore
    n = len(A)
  
    # costruisce il maxheap
    # Since last parent will be at ((n//2)-1) we can start at that location.
    for i in range(n // 2 - 1, -1, -1):
        heapify(A, i, n)

def heap_sort(A):
    build_heap(A)

    for i in range(len(A)-1, 0, -1):
        # scambia A[i] con A[0]
        A[i], A[0] = A[0], A[i]
        heapify(A, 0, i)

if __name__ == "__main__":

    v = [2, 1, 5, 3, 4, 7]
    heap_sort(v)
    print(v)

    
    