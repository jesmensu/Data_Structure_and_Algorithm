from copy import deepcopy

link_list = {}

def insert_at_start(head, data):
    Node = {
        "item" : data,
        "next" : {}
    }
    Node["item"] = data
    Node["next"] = head
    head = Node
    return head

def insert_at_end(head, data):
    Node = {
        "item" : data,
        "next" : {}
    }
    Node["item"] = data
    if head == {}:
        head = Node
    else:
        current = head
        while (current["next"] != {}):
            current = current["next"]
        current["next"] = Node
    return head

# link_list = insert_at_start(link_list, 2)
# link_list = insert_at_start(link_list, 1)
link_list = insert_at_end(link_list, 3)

print(link_list)

