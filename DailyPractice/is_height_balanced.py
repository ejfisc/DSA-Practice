#! python3
# Given a tree, find if the binary tree is height balanced or not. 
# A height balanced binary tree is a tree where every node's 2 subtree do not differ in height 
# by more than 1.

from operator import is_


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

# helper function to find height of binary tree
def height(root):
    # base case
    if root is None:
        return 0
        
    # height of tree is maximum of left subtree height and right subtree height + 1
    return max(height(root.left), height(root.right)) + 1

def is_height_balanced(tree):
    # base case
    if tree is None:
        return True

    # store height of right and left subtrees
    left_height = height(tree.left)
    right_height = height(tree.right)

    # check if left and right subtree are balanced
    l = is_height_balanced(tree.left)
    r = is_height_balanced(tree.right)

    # check if height differs by more than one
    if abs(left_height - right_height) <= 1:
        return l and r

    # if we reach this point the tree is not balanced
    return False
    
    pass

#     1
#    / \
#   2   3
#  /
# 4 
n4 = Node(4)
n3 = Node(3)
n2 = Node(2, n4)
n1 = Node(1, n2, n3)
print(is_height_balanced(n1)) # true

#     1
#    / 
#   2   
#  /
# 4  
n1 = Node(1, n2)
print(is_height_balanced(n1)) # false