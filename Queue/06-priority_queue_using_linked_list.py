class Node:
    def __init__(self, item = None, priority = None):
        self.item = item
        self.priority = priority
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def isEmpty(self):
        return self.front == None

    def push(self, item, priority):
        n = Node(item, priority)
        if self.isEmpty():
            self.front = n
            self.rear = n
        elif self.front.priority>priority:
            n.next = self.front
            self.front = n
        else:
            count = 0
            current = self.front
            while current.next != None:
                if priority>current.priority:
                    n.next = current.next
                    current.next = n
                    break
                current = current.next
                count += 1
            current.next = n

        self.item_count += 1
        print("Item", item, "inserted into Queue")

    def pop(self):
        if self.isEmpty():
            print("Queue is underflow")
            return
        elif self.front.next == None:
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
        
    def size(self):
        return self.item_count

q = Queue()
q.push(10, 1)
print("Size of the queue:", q.size())
q.push(20, 2)
print("Size of the queue:", q.size())
q.push(30, 0)
print("Size of the queue:", q.size())
q.pop()
print("Size of the queue:", q.size())
q.pop()
print("Size of the queue:", q.size())
q.pop()
print("Size of the queue:", q.size())
q.pop()
print("Size of the queue:", q.size())

