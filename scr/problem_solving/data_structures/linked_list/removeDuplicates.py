class Node:

    # Constructor to create a new node 
    def __init__(self, data):
        self.data = data # Pointer to data
        self.next = None # Initialize next as null

def removeDuplicates(head):
    if head is None:
        return None

    current = head
    while current.next:
        if current.data == current.next.data:
            nextNext = current.next.next
            current.next = nextNext
        else:
            current = current.next 
    return head