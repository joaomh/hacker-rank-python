def printLinkedList(head):
    if head:
        current = head
        while current:
            print(current.data)
            current = current.next
