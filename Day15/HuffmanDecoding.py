# don't have left and right child
def is_leaf(node):
    return not node.left and not node.right
    
def decodeHuff(root, s):
    # use list to store decoded characters for faster time complexity
    decoded = []
    curr_node = root
    
    for i in s:
        # i == 1 -> right
        # i == 0 -> left
        if int(i) == 1:
            curr_node = curr_node.right
        else:
            curr_node = curr_node.left      
        
        # if leaf, decode character
        if is_leaf(curr_node):
            # add decoded character to list
            decoded.append(curr_node.data)
            
            # reset curr_node to the root
            curr_node = root
            
    print("".join(decoded))