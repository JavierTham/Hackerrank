class Node:
    def __init__(self, info): 
        self.info = info  
        self.left = None  
        self.right = None 
        self.dist = None # to store horizontal distance from center. 
                         # root.dist = 0, root.left.dist = -1, root.right.dist = 1

    def __str__(self):
        return str(self.info) 

class BinarySearchTree:
    def __init__(self): 
        self.root = None

    def create(self, val):  
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root
         
            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

def topView(root):
    # do a level order traversal down the tree
    # take note of horizontal distance from center

    if not root:
        return 

    # queue for level order traversal, child nodes are put into the queue
    queue = []
    root.dist = 0
    queue.append(root)

    # dictionary to store first node at that horizontal distance
    # key - horizontal distance from center
    # value - node.info
    top_nodes_dist = {}

    # keep track of distance of node that is furthest left
    max_left_dist = 0

    # level order traversal, keep going down tree
    while(queue):
        curr_node = queue.pop(0)

        # first time a node reaches this distance from center (this node can be viewed from the top)
        if curr_node.dist not in top_nodes_dist:
            top_nodes_dist[curr_node.dist] = curr_node.info
            max_left_dist = min(max_left_dist, curr_node.dist)

        # already have another node at this distance (this node cannot be viewed from top)
        # if have left child
        if curr_node.left:
            # update child's distance from center
            curr_node.left.dist = curr_node.dist - 1
            queue.append(curr_node.left)
        
        # if have right child
        if curr_node.right:
            # update child's distance from center
            curr_node.right.dist = curr_node.dist + 1
            queue.append(curr_node.right)

    # iterate through the dictionary storing values of node's which can be viewed from top
    # starting from the furthest left
    curr_dist = max_left_dist
    while curr_dist in top_nodes_dist:
        print(top_nodes_dist[curr_dist], end = " ")
        curr_dist += 1
        
    




tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)