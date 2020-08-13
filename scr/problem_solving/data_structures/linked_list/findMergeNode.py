def findMergeNode(head1, head2):
    point1 = head1
    point2 = head2
    len1 = 0
    len2 = 0
    while point1:
        len1 += 1
        point1 = point1.next
    while point2:
        len2 += 1
        point2 = point2.next
    if len1 > len2:
        for __ in range(len1 - len2):
            head1 = head1.next
    else:
        for __ in range(len2 - len1):
            head2 = head2.next
    while head1 and head2:
        if head1 == head2:
            return head1.data
        head1 = head1.next
        head2 = head2.next 

