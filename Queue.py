class Queue:

    def __init__(self):
        self.items = []


    def enqueue(self, element):
        self.items.insert(0, element)

    def dequeue(self):
        self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0
    