class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def set_right_child(self, node):
        self.right = node
        
    def set_left_child(self, node):
        self.left = node

    def __str__(self):
        return str(self.data)