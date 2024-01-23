class Node:
    def __init__(self, item = None):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert_at_start(self, item):
        n = Node(item)
        if self.head == None:
            n.next = n
            self.head = n
        else:
            n.next = self.head.next
            self.head.next = n
        
        print("Item", item, "inserted at start")

    def insert_at_end(self, item):
        n = Node(item)
        if self.head == None:
            n.next = n
            self.head = n
        else:
            n.next = self.head.next
            self.head.next = n
            self.head = n

        print("Item", item, "inserted at end")

    def insert_after_item(self, data, item_to_insert):
        if self.head == None:
            raise ValueError("No item to insert after")
        else:
            current = self.head.next
            n = Node(item_to_insert)
            item = ""
            while(current != self.head):
                if(current.item == data):
                    item = data
                    n.next = current.next
                    current.next = n
                    print("Item", item_to_insert, "inserted after item", item)
                    return
                current = current.next
            if(current.item == data):
                item = data
                n.next = current.next
                current.next = n
                self.head = n
                print("Item", item_to_insert, "inserted after item", item)
            if(item == ""):
                print("Item", data, "is not in the list to insert after")

    def delete_from_start(self):
        if self.head == None:
            print("No element to delete")
        elif self.head == self.head.next:
            item = self.head.next.item
            self.head = None
            print("Item", item, "deleted") 
        else:
            item = self.head.next.item
            self.head.next = self.head.next.next
            print("Item", item, "deleted")

    def delete_from_end(self):
        if self.head == None:
            print("No element to delete")
        elif self.head.next == self.head:
            item = self.head.item
            self.head = None
            print("Item", item, "deleted")
        else:
            current = self.head.next
            while(current.next != self.head):
                current = current.next
            item = self.head.item
            current.next = self.head.next
            self.head = current
            print("Item", item, "deleted")

    def delete_item(self, data):
        if self.head == None:
            print("No element to delete")
        elif self.head.next == self.head and self.head.item == data:
            item = self.head.item
            self.head = None
            print("Item", item, "deleted")
        else:
            current = self.head.next
            if current.item == data:
                self.head.next = current.next
                print("Item", data, "deleted")
            else:
                while(current.next != self.head):
                    if current.next.item == data:
                        current.next = current.next.next
                        print("Item", data, "deleted")
                        return
                    current = current.next
                if current.next.item == data:
                    current.next = current.next.next
                    self.head = current
                    print("Item", data, "deleted")
                    return
                print("Item", data, "is not in the list to delete")


    def populate_from_list(self, listSeq):
        if len(listSeq) == 0:
             print("No item in the list")

        else:
            self.head = Node(listSeq[0])
            self.head.next = self.head
            for item in lst[1:]:
                    n = Node(item)
                    n.next = self.head.next
                    self.head.next = n
                    self.head = n
            print("List", listSeq, "has inserted to the list")

    def print_list(self):
        if self.head == None:
            print("No element in the linked list to print")
        else:
            current = self.head.next
            print("Items in the list are:")
            while current != self.head:
                print(current.item)
                current = current.next
            print(current.item)

    def __iter__(self):
            return SSLIterator(self.head)

class SSLIterator:
    def __init__(self, head):
        self.current = head
        self.last = head
        self.count = 0
        
    def __iter__(self):

            return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        if self.current == self.last and self.count == 1:
            raise StopIteration
        else:
            self.count = 1
        data = self.current.next.item
        self.current = self.current.next
        return data





lst = [2,3,4]
linkedList = LinkedList()
linkedList.populate_from_list(lst)
# linkedList.insert_at_start(3)
# linkedList.insert_at_start(2)
# linkedList.insert_at_start(1)
# linkedList.insert_at_start(0)
# try:
#     linkedList.insert_after_item(3,4)
# except Exception as e:
#     # pass
#     print(e)
# linkedList.insert_at_end(5)
# linkedList.insert_at_end(7)
# linkedList.delete_item(2)
# linkedList.delete_from_start()
# linkedList.delete_from_end()
# linkedList.delete_from_start()
# linkedList.print_list()
for x in linkedList:
    print(x)

