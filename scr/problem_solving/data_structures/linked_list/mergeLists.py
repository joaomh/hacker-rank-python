class Node:

    # Constructor to create a new node 
    def __init__(self, data):
        self.data = data # Pointer to data
        self.next = None # Initialize next as null
def mergeLists(head1, head2): 
    # create a new node to avoid additional checks in loop
    new_list = Node(0)
    current_list = new_list 
    while head1 and head2:
        if head1.data < head2.data:
            current_list.next = head1
            head1 = head1.next
        else:
            current_list.next = head2
            head2 = head2.next
        current_list = current_list.next
    current_list.next = head1 or head2 # add non-empty list
    return new_list.next
