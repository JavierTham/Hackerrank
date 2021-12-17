def levelOrder(root):
    if not root:
        return

    # use queue to store next node to go to
    queue = []
    queue.append(root)

    # while queue still has items, all nodes haven't been visited yet
    while queue:
        curr_node = queue.pop(0)
        print(curr_node.info, end = " ")

        # if have left child, append into queue
        if curr_node.left:
            queue.append(curr_node.left)
        # if have right child, append into queue
        if curr_node.right:
            queue.append(curr_node.right)