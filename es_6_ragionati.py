"""
Dati in input un intero n ed un vettore A=(a 0 , ..., a n-1 ) di n numeri reali, si scrivano due funzioni,
una iterativa ed una ricorsiva, che restituiscano il valore 1 se il vettore è palindromo, il valore 0
altrimenti.
"""

## NB n è la lunghezza della lista 
def is_palindrome_iterativa(n, lista):
    i = 0
    
    while lista[i] == lista[n-1]:

        if i == n-1:
            return 1
        
        i += 1
        n -= 1

    return 0

# n ultimo elemento
# m primo elemento da considerare
def is_palindrome_recursive(n,m, lista):

    if n<m: # c1
        return 1 #c2

    else:
        if lista[n-1] == lista[m]: #c3
            return is_palindrome_recursive(n-1, m+1, lista) # T(n-2)
        else:
            return 0 # c4

    """
    
    
    """


        

    


if __name__ == "__main__":

    print(is_palindrome_iterativa(5, [1,2,3,4,1]))
    print(is_palindrome_recursive(5, 0, [1,2,3,2,1]))