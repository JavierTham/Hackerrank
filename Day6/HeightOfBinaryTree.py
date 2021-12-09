def height(root):
    # define helper function to record the height
    def helper(root, h):
        # return the height after leaf node
        if not root:
            return h
        
        # if node exists, increase height by 1 (because an edge exists)
        h += 1

        # recursively move left and right down the tree
        left = helper(root.left, h)
        right = helper(root.right, h)

        # return the max height between each sub-tree
        return max(left, right)
    
    # call helper function on left and right child
    left = helper(root.left, 0)
    right = helper(root.right, 0)

    # return max height between the left and right child
    return max(left, right)

class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

# tests
# got lazy to write the logic for creating a tree
root = Node(5)
root.left = Node(3)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.right = Node(4)
root.right = Node(6)
print(height(root))

root2 = Node(3)
root2.left = Node(2)
root2.left.left = Node(1)
root2.right = Node(4)
print(height(root2))