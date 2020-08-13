class Node:
    # Constructor to create a new node 
    def __init__(self, data):
        self.data     = data 
        self.next     = None # Reference to next node
        self.previous = None # Reference to the previous node
def sortedInsert(head, data):
    node = Node(data)
    if head == None:
        return node
    if data <= head.data:
        node.next, head.prev = head, node
        return node
    current = head
    while current.next != None and data >= current.next.data:
        current = current.next
    node.prev = current
    node.next = current.next
    current.next = node
    current.next.prev = node
    return head