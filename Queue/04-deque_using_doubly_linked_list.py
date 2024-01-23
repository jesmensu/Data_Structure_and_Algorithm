class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None
        self.item_count = 0

    def isEmpty(self):
        return self.item_count == 0
    
    def insert_front(self, item):
        n = Node(item)
        if self.isEmpty():
            self.rear = n
        else:
            n.next = self.front
            self.front.prev = n
        self.front = n
        self.item_count += 1
        print("Item inserted", item)

    def insert_rear(self, item):
        n = Node(item)
        if self.isEmpty():
            self.front = n
        else:
            n.prev = self.rear
            self.rear.next = n
        self.rear = n
        self.item_count += 1
        print("Item inserted", item)

    def delete_front(self):
        if self.isEmpty():
            print("Queue is underflow")
        elif self.front == self.rear:
            item = self.front.item
            self.front = None
            self.rear = None
            self.item_count -= 1
            print("Item deleted", item)
        else:
            item = self.front.item
            self.front= self.front.next
            self.front.prev =None
            self.item_count -= 1
            print("Item deleted", item)

    def delete_rear(self):
        if self.isEmpty():
            print("Queue is underflow")
        elif self.front == self.rear:
            item = self.rear.item
            self.front = None
            self.rear = None
            self.item_count -= 1
            print("Item deleted", item)
        else:
            item = self.rear.item
            self.rear = self.rear.prev
            self.rear.next = None
            self.item_count -= 1
            print("Item deleted", item)

    def get_front(self):
        if not self.isEmpty():
            return self.front.item
        
    def get_rear(self):
        if not self.isEmpty():
            return self.rear.item

    def size(self):
        return self.item_count

d1=Deque()
d1.insert_front(10)
# d1.delete_front()
d1.insert_front(20)
d1.delete_front()
# d1.insert_rear(30)
d1.insert_rear(40)
# d1.delete_front()
# d1.delete_rear()
print(d1.size())
print(d1.get_front(), d1.get_rear())
