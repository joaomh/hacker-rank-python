class Node:

    # Constructor to create a new node 
    def __init__(self, data):
        self.data = data # Pointer to data
        self.next = None # Initialize next as null
def getNode(head, position):
    current = head
    result = head
    index = 0
    while current is not None:
        current = current.next
        
        if index > position:
            result = result.next
        index+=1
    
    return result.data  