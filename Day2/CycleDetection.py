def has_cycle(head):
    # use a set to keep track of visited nodes
    visited = set()

    # helper function to pass on the set along with the recursion
    def helper(head, visited):
        # if "head" is NULL, we have reached the tail without having a cycle
        if not head:
            return 0

        # add node into set if not yet visited
        if head not in visited:
            visited.add(head)
            # do recursion with next node
            return helper(head.next, visited)

        # return 1 if current node has already been visited
        else:
            return 1

    return helper(head, visited)