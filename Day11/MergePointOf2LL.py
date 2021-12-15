def findMergeNode(head1, head2):
    # maintain a set to record all visited nodes
    nodes = set()

    # add all nodes from LL1
    while head1:
        nodes.add(head1)
        head1 = head1.next
        
    # find 1st common node, which is the merge point
    while head2:
        if head2 in nodes:
            return head2.data
        head2 = head2.next