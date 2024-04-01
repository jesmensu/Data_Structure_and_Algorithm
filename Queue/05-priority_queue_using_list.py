
class Queue:
    def __init__(self, items = []):
        self.items = items  # [(item, prioroty)]

    def isEmpty(self):
        return len(self.items)==0
    
    def push(self, item, priority):
        index = 0
        while(index<len(self.items) and self.items[index][1]< priority):
            index += 1
        self.items.insert(index, (item, priority))
        print("Item entered: ", item)

    def pop(self):
        if self.isEmpty():
            print("Queue is underflow")
            return 
        item, p = self.items.pop(0)
        print ("Item removed: ", item)
        return item

    def get_front(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.items[0][0]
    
    def get_rear(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        return self.items[-1][0]

    def size(self):
        return len(self.items)
    
q = Queue()
q.push(5, 3)
q.push(4,1)
q.push(7,5)

print(q.items)

q.pop()
q.pop()
print(q.items)



print("Size of the Queue:", q.size())
