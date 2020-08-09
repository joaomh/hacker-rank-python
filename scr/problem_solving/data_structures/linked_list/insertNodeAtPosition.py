class Node:

    # Constructor to create a new node 
    def __init__(self, data):
        self.data = data # Pointer to data
        self.next = None # Initialize next as null

def insertNodeAtPosition(head, data, position):
    i = 0
    current_head = head
    previous_head = head
    while i <= position:
        if i == position:
            new_head = Node(data)
            previous_head.next = new_head
            new_head.next = current_head
            return head
        else:
            i += 1
            previous_head = current_head
            current_head = current_head.next
    return head