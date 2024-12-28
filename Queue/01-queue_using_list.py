# the front is the end of the line where elements are removed, and the rear is the end where elements are added

class Queue:
    def __init__(self, items = []):
        self.items = items

    def isEmpty(self):
        return len(self.items)==0
    
    def enqueue(self, item):
        self.items.append(item)
        print("Item entered: ", item)

    def dequeue(self):
        if self.isEmpty():
            print("Queue is underflow")
            return 
        item = self.items.pop(0)
        print ("Item removed: ", item)
        return item

    def get_front(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.items[0]
    
    def get_rear(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.items[-1]

    def size(self):
        return len(self.items)
    
    def __iter__(self):
        return self
    
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.dequeue()

print("Size of the Queue:", q.size())
