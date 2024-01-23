class Deque:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0
    
    def insert_front(self,data):
        self.items.insert(0,data)

    def insert_rear(self,data):
        self.items.append(data)
    def delete_front(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            self.items.pop(0)
    def delete_rear(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            self.items.pop()
    def get_front(self):
        if self.is_empty():
            print("Deque is empty")
        else:
            return self.items[0]
    def get_rear(self):
        if self.is_empty():
            print("Deque is empty")
            return
        else:
            return self.items[-1]
    def size(self):
        return len(self.items)
d1=Deque()
d1.insert_front(10)
d1.insert_front(20)
d1.insert_rear(30)
d1.insert_rear(40)
print(d1.get_front(), d1.get_rear())
