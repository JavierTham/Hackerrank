import sys, os

CURRENT_DIR = os.path.dirname(__file__)
sys.path.append(os.path.join(os.path.dirname(CURRENT_DIR), 'Data_Structures'))

from Node import Node
from BST import BST

print(Node(3))