"""
dati A e B due vettori di interi
sia C la loro intersezione
MIGLIORABILE
"""

def stampa_unione(A, B):

    C = list()

    i = 0
    j = 0

    while i < len(A) and j<len(B):

        if (A[i] < B[j]):
            C.append(A[i])
            print(C)
            i += 1

        elif (A[i] > B[j]):
            C.append(B[j])
            print(C)
            j += 1
        
        elif (A[i] == B[j]):
            if (A[i] > C[len(C)-1]):
                print(C)
                C.append(A[i])
            i += 1
            j += 1

    while i < len(A):
        if(A[i] > C[len(C)-1]):
            print(C)
            C.append(A[i])
        i += 1
    
    while j < len(B):
        if(B[j] > C[len(C)-1]):
            print(C)
            C.append(B[j])
        j += 1
    
    print(C)



if __name__ == "__main__":
    stampa_unione([1,3,4, 6], [2,3,4,7])
        