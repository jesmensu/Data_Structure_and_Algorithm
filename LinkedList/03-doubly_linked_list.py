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
        if self.head != None:
            n.next = self.head
        self.head = n
        print("Item", item, "inserted at start")

    def insert_at_end(self, item):
        n = Node(item)
        if self.head == None:
            self.head = n
        else:
            current = self.head
            while(current.next != None): 
                current = current.next
            n.prev = current
            current.next = n
        print("Item", item, "inserted at end")

    def insert_after_item(self, data, item_to_insert):
        current = self.head
        n = Node(item_to_insert)
        item = ""
        while(current != None):
            if(current.item == data):
                item = data
                current.next.prev = n
                n.next = current.next
                current.next = n
                n.prev = current
                print("Item", item, "inserted after item", item_to_insert)
                break
            current = current.next
        if(item == ""):
            print("Item", data, "is not in the list to insert after")

    def delete_from_start(self):
        if self.head == None:
            print("No element to delete")
        elif self.head.next == None:
            item = self.head.item
            self.head = None
            print("Item", item, "deleted")
        else:
            item = self.head.item
            current = self.head.next
            current.prev = None
            self.head = current
            print("Item", item, "deleted")

    def delete_from_end(self):
        if self.head == None:
            print("No element to delete")
        elif self.head.next == None:
            item = self.head.item
            self.head = None
            print("Item", item, "deleted")
        else:
            current = self.head
            while(current.next != None):
                current = current.next
            item = current.item
            current.prev.next = None
            print("Item", item, "deleted")

    def delete_item(self, data):
        if self.head == None:
            print("No element to delete")
        else:
            item = ""
            current = self.head
            while(current != None):
                if current.item == data:
                    item = data
                    if current.next != None:
                        current.next.prev = current.prev 
                    if current.prev != None:
                        current.prev.next = current.next
                    else:
                        self.head = current.next
                    print("Item", data, "deleted")
                    break
                current = current.next
            if item == "":
                print("Item", data, "is not in the list to delete")


    def populate_from_list(self, listSeq):
        if len(listSeq) == 0:
             print("No item in the list")
        else:
            self.head = Node(listSeq[0])
            current = self.head
            for item in lst[1:]:
                    n = Node(item)
                    current.next = n
                    n.prev = current
                    current = current.next
            print("List", listSeq, "has inserted to the list")

    def print_list(self):
        current = self.head
        print("Items in the list are:")
        while current != None:
            print(current.item)
            current = current.next

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


lst = []
linkedList = DoublyLinkedList()
linkedList.populate_from_list(lst)
# linkedList.insert_at_start(0)
linkedList.insert_after_item(1,3)
# linkedList.insert_at_end(5)
# linkedList.delete_item(2)
# linkedList.delete_from_start()
# linkedList.delete_from_end()
# linkedList.delete_from_start()
# linkedList.print_list()
for x in linkedList:
    print(x)

