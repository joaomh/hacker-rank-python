class Node:

    # Constructor to create a new node 
    def __init__(self, data):
        self.data = data # Pointer to data
        self.next = None # Initialize next as null
def reversePrint(head):
    previous_node = None
    current_node = head
    while current_node != None:
         next = current_node.next
         current_node.next = previous_node
         previous_node = current_node
         current_node = next
    head = previous_node
    # now prints contents of linked list
    contents = head 
    if contents is None:
        print("List has no element")
    while contents: 
        print(contents.data)
        contents = contents.next