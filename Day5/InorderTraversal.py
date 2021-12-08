# method 1
def inOrder(root):
    # define helper to get output string
    def helper(root):
        # base case (NULL object)
        if not root:
            return ""
        
        # inorder traversal goes left, then mid, then right
        s = helper(root.left) + " " + str(root.info) + " " + helper(root.right)

        # strip excess whitespace
        return s.strip()
        
    s = helper(root)
    print(s)