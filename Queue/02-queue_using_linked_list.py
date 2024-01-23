class Node:
    def __init__(self, item = None):
        self.item = item
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def isEmpty(self):
        return self.front == None

    def enqueue(self, item):
        n = Node(item)
        if self.isEmpty():
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n
        self.item_count += 1
        print("Item", item, "inserted into Queue")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is underflow")
            return
        elif self.front == self.rear:
            item = self.front.item
            self.rear = None
            self.front = None
        else:
            item = self.front.item
            self.front = self.front.next
        print("Item", item, "removed")
        self.item_count -= 1
        return item
    
    def get_front(self):
        if self.isEmpty():
            print("No element to pick")
            return
        else:
            item = self.front.item
            print("Front:", item)
            return item
        
    def get_rear(self):
        if self.isEmpty():
            print("No element to pick")
            return
        else:
            item = self.rear.item
            print("Rear:", item)
            return item
        
    def size(self):
        return self.item_count

q = Queue()
q.enqueue(10)
print("Size of the queue:", q.size())
q.enqueue(20)
print("Size of the queue:", q.size())
q.enqueue(30)
print("Size of the queue:", q.size())
q.dequeue()
print("Size of the queue:", q.size())
q.dequeue()
print("Size of the queue:", q.size())
q.dequeue()
print("Size of the queue:", q.size())
q.dequeue()
print("Size of the queue:", q.size())

