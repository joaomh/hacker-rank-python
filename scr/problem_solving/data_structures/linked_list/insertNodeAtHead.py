def insertNodeAtHead(llist, data):
    if not llist:
        return SinglyLinkedListNode(data)
    head = SinglyLinkedListNode(data)
    head.next = llist
    return head
