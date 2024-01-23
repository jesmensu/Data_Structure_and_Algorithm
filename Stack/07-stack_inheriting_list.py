class Stack(list):
    def isEmpty(self):
        return len(self)==0
    
    def push(self, item):
        self.append(item)
        print("Item entered: ", item)

    def pop(self):
        if not self.isEmpty():
            item = super().pop()
            print ("Item removed: ", item)
            return item
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.isEmpty():
            print("Picked item:", self[-1])
            return self[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self)
    
    def insert(self, index, data):
        raise AttributeError("No attribute 'insert' in Stack")
    
s = Stack([0])
s.push(0)
s.push(1)
s.pop()
s.peek()
s.insert(0,3)
print("Size of the stack:", s.size())
