# method 1
def preOrder(root):
    # define helper function to create the string to be printed
    def helper(root):
        # base case, reached a NULL object
        if not root:
            return ""
        
        # preorder traversal looks at the root first, goes left, then right
        # recurse in that order
        mid = str(root.info) + helper(root.left) + helper(root.right)

        # concatenate each string with a space in front
        return " " + mid

    s = helper(root)

    # remove extra space at the front
    print(s[1:])

# method 2
def preOrder(root):
    # if node exists
    if root:
        # print mid
        print(root.info, end = " ")

        # go left
        preOrder(root.left)

        # go right
        preOrder(root.right)