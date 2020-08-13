#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    current_node = head
    while (current_node is not None):
        result = current_node
        temp_node = current_node.next
        current_node.next = current_node.prev
        current_node.prev = temp_node
        current_node = temp_node
    return result