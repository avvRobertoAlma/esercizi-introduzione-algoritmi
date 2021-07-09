"""
Dati in input un intero n ed un vettore A=(a 0 , ..., a n-1 ) di n numeri interi, si scrivano due funzioni,
una iterativa ed una ricorsiva, che restituiscano in output la somma a 0 +a 1 +...+a n-1 . Si studi poi il
costo computazionale delle due funzioni.
"""

def somma_iterativa(n, lista):

    somma = 0
    for i in range(len(lista)):
        somma += lista[i]

    return somma

def somma_ricorsiva(n, lista):

    if len(lista) == 1:
        return n
    else:

        return lista[0] + somma_ricorsiva(n, lista[1:])



if __name__ == "__main__":

    print(somma_iterativa(5, [1,2,3,4,5]))
    print(somma_ricorsiva(5, [1,2,3,4,5]))