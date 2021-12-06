def reverse(llist):
    # at original tail
    if not llist.next: # tail.next => NULL

        # swap pointers
        llist.next, llist.prev = llist.prev, None

        # return new head
        return llist
        
    # at original head
    if not llist.prev: # head.prev => NULL

        # remember next node for recursion
        next_node = llist.next

        # swap pointers
        llist.next, llist.prev = None, next_node

        # recursively call function on next node
        return reverse(next_node)
    
    # at middle nodes
    next_node = llist.next
    
    # swap pointers
    llist.next, llist.prev = llist.prev, llist.next
    
    return reverse(next_node)