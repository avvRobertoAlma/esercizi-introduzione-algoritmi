def partiziona(lista, start, end, pivot):


    i = start
    j = end

    while i < end and j > 0:

        if lista[i] < pivot:
            i += 1
        
        if lista[j] > pivot:
            j -= 1

        
        if i < j:
            print(f"scambiato {lista[j]} con {lista[i]}")
            tmp = lista[j]
            lista[j] = lista[i]
            lista[i] = tmp
        else:
            return j




def partiziona_a_tre(lista, p1, p2):

    medium = partiziona(lista, 0, len(lista)-1, p1)
    partiziona(lista, medium, len(lista)-1, p2)




if __name__ == "__main__":

    v = [100,4, 23, 11, 18, 2, 8, 9, 7, 234, 199, 12, 18, 25]
    partiziona_a_tre(v, 10, 100)
    print(v)