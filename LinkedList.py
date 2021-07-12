class Node:
    value = None
    next = None

    def __init__(self, value):
        self.value = value

    def addSuccessor(self, p):

        self.next = p


"""
Funzione inserisci in testa
@param pointer -> il puntatore alla testa della lista attuale
@param newPointer -> il puntatore all'elemento da inserire in testa
@return il puntatore alla testa della lista come modificata
"""
def insert_in_testa(pointer, newPointer):

    if newPointer:

        # se il nuovoPuntatore (quello da inserire in testa) non è nullo
        # l'attributo next del nuovoPuntatore diventa il puntatore all'inizio della lista
        newPointer.next = pointer

    pointer = newPointer

    return pointer

"""
funzione printLinkedList ricorsiva
@param pointer -> puntatore alla lista
"""
def printLinkedList(pointer):

    ## caso base
    ## se c'è il puntatore
    ## stampa il valore
    if pointer:
        print(pointer.value)
    
    ## invocazione ricorsiva
    ## se c'è un prossimo elemento
    ## invoca ricorsivamente la funzione sul prossimo elemento
    if pointer.next:
        printLinkedList(pointer.next)

"""
funzione search
restituisce true se è presente un puntatore con il valore passato in input
@param pointer -> il puntatore alla testa della lista
@param value -> il valore da ricercare
@return un valore booleano
"""
def search(pointer, value):


    if not pointer:
        return False
    
    if pointer.value == value:
        return True
    
    ## iterativa
    ## finché c'è un prossimo elemento
    ## il puntatore viene sostituito con un riferimento al prossimo elemento e si ripete il ciclo
    ## costo computazionale O(n) dove n è il numero di elementi della lista
    while pointer.next:

        pointer = pointer.next
        if pointer.value == value:
            return True

    return False

"""
funzione find
restituisce il puntatore a un nodo se è presente un puntatore che ha una determinata chiave
@param pointer -> il puntatore alla testa della lista
@param value -> il valore da ricercare
@return un nodo
"""
def find(pointer, value):


    if not pointer:
        return False
    
    if pointer.value == value:
        return pointer
    
    ## iterativa
    ## finché c'è un prossimo elemento
    ## il puntatore viene sostituito con un riferimento al prossimo elemento e si ripete il ciclo
    ## costo computazionale O(n) dove n è il numero di elementi della lista
    while pointer.next:

        pointer = pointer.next
        if pointer.value == value:
            return pointer

    return None



"""
funzione delete
@param pointer -> il puntatore alla testa della lista
@param node -> il puntatore all'elemento da cancellare
@return pointer
"""
def delete(pointer, node):

    if node: # se il puntatore da cancellare non esiste, non ha senso eseguire alcuna operazione
        
        if pointer == node:
            pointer = node.next # il primo elemento della lista diventa quello puntato dal nodo da cancellare (il successore)
        
        # se non è il primo elemento
        elemento_corrente = pointer
        while elemento_corrente.next != node:
            # finché il successore dell'elemento corrente è diverso dal nodo da cancellare
            # avanzo l'elemento_corrente
            elemento_corrente = elemento_corrente.next

        # esco dal ciclo o quando il successore di elemento corrente è il nodo, o quando non trovo nulla
        if elemento_corrente.next == node:

            elemento_corrente.next = node.next # sostituisco il riferimento all'elemento successivo

    return pointer # restituisco il puntatore
            
"""
funzione delete by key
@param pointer -> il puntatore alla testa della lista
@param value -> il valore da cercare
@return il puntatore alla testa della lista modificata
"""
def delete_by_key(pointer, value):

    node = find(pointer, value) # prima trovo il nodo
    return delete(pointer, node)

if __name__ == "__main__":

    p = Node(100)

    p = insert_in_testa(p, Node(50))
    p = insert_in_testa(p, Node(25))
    p = insert_in_testa(p, Node(12))

    p = delete_by_key(p, 25)

    printLinkedList(p)

    # print(search(p, 15))
