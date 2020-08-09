class Node:

    # Constructor to create a new node 
    def __init__(self, data):
        self.data = data # Pointer to data
        self.next = None # Initialize next as null

def deleteNode(head, position): 
    if head is None:
        return head
    elif position == 0:
        return head.next
    
    prev_node = head
    current_node = head
    current_position = 0

    while current_position < position:
        current_position = current_position + 1
        prev_node = current_node
        current_node = current_node.next

    prev_node.next = current_node.next
    return head