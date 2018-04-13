#russel john cortez
#QUEUES AND DEQUEUES

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        self.items.pop()

    def size(self):
        return len(self.items)

    def printqueue(self):
        for items in self.items:
            print (items)

q = Queue()
print(q.isEmpty())
q.enqueue(10)
q.enqueue(30)
q.enqueue(50)
q.enqueue(70)
q.enqueue(90)
q.enqueue(110)
q.printqueue()
q.dequeue()
print("\n")
q.printqueue()
