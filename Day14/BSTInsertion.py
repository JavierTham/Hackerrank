class Node:
    def __init__(self, info):
        self.info = info  
        self.left = None  
        self.right = None 
        self.level = None 

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):
        new_node = Node(val)

        # if tree is empty
        if not self.root:
            self.root = new_node
            return self.root

        curr_node = self.root

        # loop till node is inserted
        while True:
            # new node has smaller value, go left
            if new_node.info < curr_node.info:
                # current node has left child
                if curr_node.left:
                    curr_node = curr_node.left
                else:
                    curr_node.left = new_node
                    return self.root

            # new node has larger value, go right
            else:
                # current node has right child
                if curr_node.right:
                    curr_node = curr_node.right
                else:
                    curr_node.right = new_node
                    return self.root