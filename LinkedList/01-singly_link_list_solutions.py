class Node:
    def __init__(self, item = None):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self, head = None):
        self.head = head

    def insert_at_start(self, item):
        n = Node(item)
        if self.head != None:
            n.next = self.head
        self.head = n
        print("Item", item, "inserted at start")

    def delete_from_start(self):
        if self.head == None:
            print("No element to delete")
        else:
            item = self.head.item
            self.head = self.head.next
            print("Item", item, "deleted")

    def populate_from_list(self, listSeq):
        if len(listSeq) == 0:
             print("No item in the list")

        else:
            while(listSeq):
                item = listSeq.pop()
                self.insert_at_start(item)
            print("List", listSeq, "has inserted to the list")

    def print_list(self):
        current = self.head
        print("Items in the list are:")
        while current != None:
            print(current.item)
            current = current.next

    def oddEvenList(self):
        # All the even item will go last
        if not self.head or not self.head.next:
            return self.head
        new_list = Node(0)
        dummy = new_list
        current = self.head
        while current != None and current.next != None and current.next.next != None:
            n = Node(current.next.item)
            dummy.next = n
            dummy = dummy.next
            current.next = current.next.next
            current = current.next
        if current.next != None:
            n = Node(current.next.item)
            dummy.next = n
        current.next = new_list.next
        return self.head
    
    def oddEvenList2(self, head):
        if not head or not head.next:
            return head
        new_list = Node()
        dummy = new_list
        current = head
        while current != None and current.next != None and current.next.next != None:
            dummy.next = current.next
            dummy = dummy.next
            current.next = current.next.next
            current = current.next
        if current.next != None:
            dummy.next = current.next
            current.next = None
        current.next = new_list.next
        return head
    
    def reverseList(self, head):
        if head == None:
            return []
        reverse_list_head = Node(head.item)
        head = head.next
        while head != None:
            n = Node(head.item)
            n.next = reverse_list_head
            reverse_list_head = n
            head = head.next
        return reverse_list_head
    
    def reverseList2(self, head):
        if head == None:
            return None
        current_node = head
        prev_node = None
        while current_node != None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        return prev_node


lst = [1,2,3,4,5,6]
linkedList = LinkedList()
linkedList.populate_from_list(lst)
# linkedList.insert_at_start(0)
# linkedList.insert_after_item(2,3)
# linkedList.insert_at_end(5)
# linkedList.delete_item(0)
# linkedList.delete_from_start()
# linkedList.delete_from_end()
# linkedList.delete_from_start()
linkedList.print_list()
reverse_list = linkedList.oddEvenList2(linkedList.head)
linkedList.head = reverse_list
linkedList.print_list()
# for x in linkedList:
#     print(x)

