class Node:
    def __init__(self, item = None):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self, last = None):
        self.last = last

    def insert_at_start(self, item):
        n = Node(item)
        if self.last == None:
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
        
        print("Item", item, "inserted at start")

    def insert_at_end(self, item):
        n = Node(item)
        if self.last == None:
            n.next = n
            self.last = n
        else:
            n.next = self.last.next
            self.last.next = n
            self.last = n

        print("Item", item, "inserted at end")

    def insert_after_item(self, data, item_to_insert):
        if self.last == None:
            raise ValueError("No item to insert after")
        else:
            current = self.last.next
            n = Node(item_to_insert)
            item = ""
            while(current != self.last):
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
                self.last = n
                print("Item", item_to_insert, "inserted after item", item)
            if(item == ""):
                print("Item", data, "is not in the list to insert after")

    def delete_from_start(self):
        if self.last == None:
            print("No element to delete")
        elif self.last == self.last.next:
            item = self.last.next.item
            self.last = None
            print("Item", item, "deleted") 
        else:
            item = self.last.next.item
            self.last.next = self.last.next.next
            print("Item", item, "deleted")

    def delete_from_end(self):
        if self.last == None:
            print("No element to delete")
        elif self.last.next == self.last:
            item = self.last.item
            self.last = None
            print("Item", item, "deleted")
        else:
            current = self.last.next
            while(current.next != self.last):
                current = current.next
            item = self.last.item
            current.next = self.last.next
            self.last = current
            print("Item", item, "deleted")

    def delete_item(self, item):
        if self.last == None:
            raise IndexError("Index out of bound")
        if self.last.next == self.last:   # if one element present
            self.last = None
            return
        if self.last.next.item == item:   # if first item to be delete
            self.last.next = self.last.next.next
            return
        current = self.last.next
        while current.next != self.last:     # for the middle item
            if current.next.item == item:
                current.next = current.next.next
                return
            current = current.next
        if current.next.item == item:      # for the last item to be delete. which the last is pointed
            current.next = current.next.next
            self.last = current
            return

    def populate_from_list(self, listSeq):
        if len(listSeq) == 0:
             print("No item in the list")

        else:
            self.last = Node(listSeq[0])
            self.last.next = self.last
            for item in lst[1:]:
                    n = Node(item)
                    n.next = self.last.next
                    self.last.next = n
                    self.last = n
            print("List", listSeq, "has inserted to the list")

    def print_list(self):
        if self.last == None:
            print("No element in the linked list to print")
        else:
            current = self.last.next
            print("Items in the list are:")
            while current != self.last:
                print(current.item)
                current = current.next
            print(current.item)

    def reverse_linked_list(self):
        current = self.last.next
        last = self.last.next
        prev_node = self.last
        while current != self.last:
            next_node = current.next
            current.next = prev_node
            prev_node = current
            current = next_node
        current.next = prev_node
        self.last = last

    def __iter__(self):
            return SSLIterator(self.last)

class SSLIterator:
    def __init__(self, last):
        self.current = last
        self.last = last
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

