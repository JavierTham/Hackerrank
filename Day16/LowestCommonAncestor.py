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

# lowest common ancestor is the node where
# both values are in the left and right sub-tree each
def lca(root, v1, v2):
    # if 1 of them is the root, it is also the lca
    if v1 == root.info or v2 == root.info:
        return root
    
    # 1 value is bigger 1 value is smaller
    elif min(v1, v2) < root.info and max(v1, v2) > root.info:
        return root

    else:
        # both values smaller that root
        if v1 < root.info:
            return lca(root.left, v1, v2)
        # both values bigger than root
        else:
            return lca(root.right, v1, v2)

tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)