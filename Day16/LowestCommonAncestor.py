# lowest common ancestor is the node where
# both values are in the left and right sub-tree each
def lca(root, v1, v2):
    # if 1 of them is the root, it is also the lca
    if v1 == root.info or v2 == root.info:
        return root
    
    # 1 value is bigger 1 value is smaller
    if min(v1, v2) < root.info and max(v1, v2) > root.info:
        return root
    else:
        # both values smaller that root
        if v1 < root.info:
            lca(root.left, v1, v2)
        # both values bigger than root
        else:
            lca(root.right, v1, v2)