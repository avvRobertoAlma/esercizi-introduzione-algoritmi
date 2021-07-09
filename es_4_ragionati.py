"""
scrivere due funzioni una iterativa e una ricorsiva che restituiscano n^k, dati due interi n e k
"""

def potenza_iterativa(n, k):

    if(k == 0):
        return 1

    result = 1 #c1
    for i in range(k): #k-volte
       result *= n #c2
    
    return result #c3

    #costo = c1 + k(c2) + c3 = Theta(k)



def potenza_ricorsiva(n, k):
    if k == 0: #c1
        return 1 #c2
    else:
        return n * potenza_ricorsiva(n, k-1) #c3 + T(n, k-1)

    #equazione ricorrenza
    # T_n = T(k-1) + c1
    # T(1) = #c'

    #Theta(k)


if __name__ == "__main__":

    print(potenza_iterativa(2, 3))
    print(potenza_ricorsiva(2, 3))