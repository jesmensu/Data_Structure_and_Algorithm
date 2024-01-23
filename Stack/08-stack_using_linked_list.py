class Node:
    def __init__(self, item = None):
        self.item = item
        self.next = None

class Stack:
    def __init__(self, head = None):
        self.head = head
        self.item_count = 0

    def isEmpty(self):
        return self.head == None

    def push(self, item):
        n = Node(item)
        if self.head != None:
            n.next = self.head
        self.head = n
        self.item_count += 1
        print("Item", item, "inserted into Stack")

    def pop(self):
        if self.head == None:
            print("No element to remove")
            return
        else:
            item = self.head.item
            self.head = self.head.next
            print("Item", item, "removed")
            self.item_count -= 1
            return item
    
    def peek(self):
        if self.head == None:
            print("No element to pick")
            return
        else:
            item = self.head.item
            print("Item", item, "picked")
            return item
        
    def size(self):
        return self.item_count


s = Stack()
s.push(0)
s.push(1)
s.pop()
s.peek()
print("Size of the stack:", s.size())

