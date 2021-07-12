from helpers import alberoBinario


"""
implementazione della Coda per python
"""
class Queue:

    def __init__(self):
        self.items = []


    def enqueue(self, element):
        self.items.insert(0, element)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

"""
la visita a livelli
è un algoritmo che non ha spiegato ma potrebbe chiedere
dato un albero
                1

            2       3
        4       5       6
deve stampare 1    23    456 (sostanzialmente ogni livello)
Per l'implementazione si usa la Coda (Queue)
@param tree -> l'albero da visitare
"""
def visita_albero_livelli(tree):

    # si inizializza una coda vuota
    queue = Queue()

    if tree.valore:
        # se il nodo radice ha un valore si aggiunge alla coda
        queue.enqueue(tree)

    # finché la coda non è vuota
    while not queue.isEmpty():

        # si processa il primo elemento della coda
        # la funzione dequeue estrae il primo elemento e lo restituisce
         t = queue.dequeue()

         # stampa il valore del primo elemento estratto dalla coda
         print(t.valore)
         
         # se il nodo ha un figlio sinistro si aggiunge alla coda
         if t.sx:
             queue.enqueue(t.sx)

        # se il nodo ha un figlio destro si aggiunge alla coda
         if t.dx:
             queue.enqueue(t.dx)


    # finché il nodo avrà un figlio sinistro e destro si andrà avanti con il ciclo


if __name__ == "__main__":

    tree = alberoBinario.crea(2)
    visita_albero_livelli(tree)