class Node:

    # Constructor to create a new node 
    def __init__(self, data):
        self.data = data # Pointer to data
        self.next = None # Initialize next as null
def compare_lists(llist1, llist2):
    while (llist1 and llist2 and llist1.data == llist2.data):
        llist1 = llist1.next
        llist2 = llist2.next
    
    if not llist1 and not llist2: 
        return 1
    return 0