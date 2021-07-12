"""
class BST (Binary Search Tree)
"""


class BST:

    key = None
    sx = None
    dx = None
    parent = None

    def __init__(self, key):
        self.key = key

    def __str__(self):

        return f"[key]:{self.key}\n[parent.key]:{self.parent.key if self.parent else None}"

    


        

"""
Funzione inserimento

@param tree -> l'albero di ricerca in cui inserire il nodo
@param node -> il nodo da inserire
@returns l'albero modificato
"""
def insert(tree, node):

    y = None # è il padre del puntatore x (all'inizio deve essere null, perché la radice non può avere un padre)
    x = tree # è il puntatore alla radice

    while x and x.key: # finché x non è nullo (ossia il puntatore esiste)

        y = x # il padre diventa il nodo x

        if node.key < x.key:

            # devo andare a sx
            x = x.sx
        
        else:

            # devo andare a destra
            x = x.dx

    # a questo punto esco dal ciclo perché ho trovato una x che è null

    if y == None: # se anche y è null ossia è un albero vuoto e non siamo mai scesi

        tree = node # l'albero è formato dal solo nodo passato in input
    
    else:

        if node.key < y.key:
            node.parent = y
            
            y.sx = node
        else:
            node.parent = y
            y.dx = node

    return tree

"""
funzione ricorsiva hasElement
@param tree -> il puntatore al nodo radice
@param key -> la chiave da ricercare
@returns True se esiste un nodo con quella chiave
"""
def hasElement(tree, key):
    if not tree:
        return
    else:
        if tree.key == key:
            return True
        
        if key < tree.key:
            return hasElement(tree.sx, key)
        else:
            return hasElement(tree.dx, key)

"""
funzione ricorsiva search
@param tree -> il puntatore al nodo radice
@param key -> la chiave da ricercare
@returns il nodo corrispondente alla chiave passata in input (se esiste)
"""
def search(tree, key):

    if not tree:
        return None
    if tree:
        if tree.key == key:
            return tree
        else:
            result = search(tree.sx, key)
            if result:
                return result
            else:
                return search(tree.dx, key)

"""
funzione predecessore:
ci sono due casi da considerare
primo caso: il nodo ha un sottoalbero sinistro (allora il predecessore è il massimo dei nodi del sottoalbero sinistro)
"""
def predecessor(tree, key):
    
    p = search(tree, key)

    if not p:
        return None

    x = None
    if p.sx: # 1) caso - ha un sottalbero sx
        x = p.sx
        

        while x and x.dx:
            x = x.dx

        return x.key
    else:
        # devo salire a destra
        # devo prendere le informazioni del padre
        x = p.parent
        print(x.key)
        while x.parent and x.parent.key > p.key:
            # finché è maggiore di p.key sto salendo a sinistra
            # il ciclo termina quando trova un parent che ha una key che non è più grande di p.key
            x = x.parent
            print(x.key)
        
        return x.parent.key


"""
funzione minimum
@param tree -> il puntatore al nodo radice
@returns il valore minimo
"""
def minimum(tree):

    x = tree
    # finché esiste un sottoalbero sinistro, va sempre a sinistra
    while x.sx:
        x = x.sx
    # esce dal ciclo quando non c'è più un sottoalbero sinistro
    return x.key

"""
funzione maximum
@param tree -> il puntatore al nodo radice
@returns il valore massimo
"""
def maximum(tree):
    x = tree
    # finché esiste un sottalbero destro
    while x.dx:
        x = x.dx
    # esce dal ciclo quando non c'è più un sottoalbero dx
    return x.key

"""
funzione delete
@param key -> la chiave da eliminare
@param tree -> l'albero in cui effettuare l'eliminazione
"""
def delete(tree, key):

    # 1) verificare che esista un elemento con quella chiave
    p = search(tree, key)

    # se non c'è il nodo -> restituire None
    if not p: return None

    # se il nodo esiste e non ha figli
    # posso impostare a None il puntatore
    if not p.sx and not p.dx:
        print("non ci sono figli")
        p = None

    elif p.sx and not p.dx:
        
       # se ha solo un figlio sinistro
       # collego il figlio sinistro al genitore
       if p.key < p.parent.key:
           # se p è un figlio sx di parent
           p.parent.sx = p.sx
       else:
           p.parent.dx = p.sx

    elif p.dx and not p.sx:
        if p.key < p.parent.key:
            p.parent.sx = p.dx
        else:
            p.parent.dx = p.dx

    return tree



def pre_order(tree):
    if not tree:
        return
    else:
        if tree.key:
            print(str(tree) + " ")
        if tree.sx:
            pre_order(tree.sx)
        if tree.dx:
            pre_order(tree.dx)


def in_order(tree):

    if not tree:
        return
    if tree.key and not tree.sx and not tree.dx:
        print(tree)
    else:
        if tree.sx:
            in_order(tree.sx)
        if tree.dx:
            in_order(tree.dx)
        print(tree)

if __name__ == "__main__":

    # crea un nuovo nodo 
    p = BST(10)

    # crea un alberto vuoto
    tree = BST(None)

    # vettore con gli elementi da inserire
    v = [15, 3, 2, 9, 10, 23, 99, 101, 4, 69, 44, 55, 66]

    # popola l'alberto di ricerca con tutti gli elementi del vettore
    for num in v:
        tree = insert(tree, BST(num))

    # stampa il valore minimo
    print(f"Il valore minimo è: {minimum(tree)}")

    # stampa il valore massimo
    print(f"Il valore massimo è: {maximum(tree)}")
    
    # visita in preordine
    print("Visita in preordine: ")
    pre_order(tree)
    print("\n--------------\n")
    print("Visita in ordine")
    in_order(tree)
    print("\n-------------------\n")

    # predecessore 
    print(f"Il predecessore di 3 è: {predecessor(tree, 3)}")

    tree = delete(tree, 101)
    print(maximum(tree))