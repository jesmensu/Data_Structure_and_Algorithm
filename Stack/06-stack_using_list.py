class Stack:
    def __init__(self, items = []):
        self.items = items

    def isEmpty(self):
        return len(self.items)==0
    
    def push(self, item):
        self.items.append(item)
        print("Item entered: ", item)

    def pop(self):
        item = self.items.pop()
        print ("Item removed: ", item)
        return item

    def peek(self):
        print("Picked item:", self.items[-1])
        return self.items[-1]

    def size(self):
        return len(self.items)
    
    def __iter__(self):
        return self
    
s = Stack([0])
s.push(0)
s.push(1)
s.pop()
print("Size of the stack:", s.size())
