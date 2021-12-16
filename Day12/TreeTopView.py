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

def topView(root):
    #Write your code here
    def helper(root, direction):
        if not root:
            return ""
        if direction == "left":
            print(root.info, end = " ")
            helper(root.left, "left")
            
        if direction == "right":
            print(root.info, end = " ")
            helper(root.right, "right")
    
    helper(root.left, "left")
    print(root.info, end = " ")
    helper(root.right, "right")
        



tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

topView(tree.root)