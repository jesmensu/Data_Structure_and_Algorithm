class Node:
    def __init__(self, item = None):
        self.item = item
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert_at_start(self, item):
        n = Node(item)
        if self.head == None:
            n.next = n
            n.prev = n
            self.head = n
        else:
            n.next = self.head
            n.prev = self.head.prev
            self.head.prev.next = n
            self.head.prev = n
            self.head = n
        print("Item", item, "inserted at start")

    def insert_at_end(self, item):           
        n = Node(item)
        if self.head == None:
            n.next = n
            n.prev = n
            self.head = n
        else:
            n.next = self.head
            n.prev = self.head.prev
            self.head.prev.next = n
            self.head.prev = n
        print("Item", item, "inserted at end")

    def insert_after_item(self, data, item_to_insert):
        if self.head == None:
            print("No element to insert after")
            return
        current = self.head
        n = Node(item_to_insert)
        while(current != self.head.prev):
            if(current.item == data):
                n.next = current.next
                n.prev = current
                current.next.prev = n
                current.next = n
                print("Item", item_to_insert, "inserted after item", data)
                return
            current = current.next
        if(current.item == data):
            n.next = current.next
            n.prev = current
            current.next.prev = n
            current.next = n
            print("Item", item_to_insert, "inserted after item", data)
            return
        print("Item", data, "is not in the list to insert after")

    def delete_from_start(self):
        if self.head == None:
            print("No element to delete")
        elif self.head.next == self.head:
            item = self.head.item
            self.head = None
            print("Item", item, "deleted from start")
        else:
            item = self.head.item
            self.head.next.prev = self.head.prev
            self.head.prev.next = self.head.next
            self.head = self.head.next
            print("Item", item, "deleted from start")

    def delete_from_end(self):
        if self.head == None:
            print("No element to delete")
        elif self.head.next == self.head:
            item = self.head.item
            self.head = None
            print("Item", item, "deleted from end")
        else:
            item = self.head.prev.item
            self.head.prev.prev.next = self.head
            self.head.prev = self.head.prev.prev
            print("Item", item, "deleted from end")

    def delete_item(self, data):
        if self.head == None:
            print("No element to delete")
        else:
            current = self.head
            while(current != self.head.prev):
                if current.item == data:
                    if current == self.head:
                        self.delete_from_start()
                    else:
                        current.next.prev = current.prev 
                        current.prev.next = current.next
                    return
                current = current.next
            if current.item == data:
                self.delete_from_end()
                return
            print("Item", data, "is not in the list to delete")


    def populate_from_list(self, listSeq):
        if len(listSeq) == 0:
             print("No item in the list")
        else:
            self.head = Node(listSeq[0])
            self.head.next = self.head
            self.head.prev = self.head
            for item in lst[1:]:
                    n = Node(item)
                    n.next = self.head
                    n.prev = self.head.prev
                    self.head.prev.next = n
                    self.head.prev = n
            print("List", listSeq, "has inserted to the list")

    def print_list(self):
        if self.head == None:
            print("No element in the list")
            return
        current = self.head
        print("Items in the list are:")
        while current != self.head.prev:
            print(current.item)
            current = current.next
        print(current.item)

    def __iter__(self):
            return SSLIterator(self.head)

class SSLIterator:
    def __init__(self, head):
        self.current = head
        
    def __iter__(self):
            return self
    
    def __next__(self):
        if self.current == None:
            raise StopIteration
        data = self.current.item
        self.current = self.current.next
        return data


lst = [0,1,2]
linkedList = DoublyLinkedList()
linkedList.populate_from_list(lst)
# linkedList.insert_at_start(1)
# linkedList.insert_at_start(0)
# linkedList.insert_after_item(1,3)
linkedList.insert_at_end(5)
# linkedList.insert_at_end(6)
# linkedList.insert_after_item(5,7)
linkedList.delete_item(5)
# linkedList.insert_at_start(1)
linkedList.insert_at_end(6)
# linkedList.delete_from_start()
# linkedList.delete_from_end()
# linkedList.delete_from_end()
# linkedList.delete_from_start()
linkedList.print_list()
# for x in linkedList:
#     print(x)

