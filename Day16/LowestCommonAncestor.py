import sys, os

CURRENT_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(os.path.dirname(CURRENT_DIR), 'Data_Structures'))

from Node import Node
from BST import BST

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

tree = BST()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

v = list(map(int, input().split()))

ans = lca(tree.root, v[0], v[1])
print(ans.info)