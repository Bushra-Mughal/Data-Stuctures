# === Binary Tree ===
# A tree with atmost 2 childs (no rule)

#=== USE CASES ===
# It is most commonly discussed as its category includes:
# BST , heap , AVL trees etc which mimics "natural heirarchy structure" (ie: math equation)

# === Why need a Binary Search Tree? ===
# FAST (searching + insertion + deletion)
# It reduces Time complexity: O(n)--> O( log n )
# BUT..... is not gurantee efficiency as:
#   its worst case:
        # 1
        #  \
        #   2
        #    \
        #     3  → O(n) for all operations!
        #      \
        #       4


#=== USE CASES ===
# Compiler (syntax trees)

# ===== FOR SIMPLICITY: =====
# BST == Binary tree + a rule
# RULE = root.right > root , root.left < root
# Have no duplicates just like 'set' ( in most cases )

# ==== OPERATIONS ====
# BFS:   level order
# DFS:   inorder, preorder, postorder


# ======= Create a Binary Tree + Traversal + Search funtions ========
# Create node class for each "Tree" node:
class node:
    def __init__(self,val,left=None,right=None):
        self.val = val
        self.left = None
        self.right = None
# Create nodes:
A = node(3)
B = node(7)
C = node(1)
D = node(8)
E = node(9)
F = node(8)
# Create connections:
A.left=B
A.right=C
B.left=D
D.right=E
C.right=F

# === Define traversal methods (DFS) ===
# recursion:
def preorder(node):
    if not node:
        return
    print(node.val)
    preorder( node.left )
    preorder( node.right )
    
def inorder(node):
    if not node:
        return
    inorder( node.left )
    print(node.val)
    inorder( node.right )

def postorder(node):
    if not node:
        return
    postorder( node.left )
    postorder( node.right )
    print(node.val)

# iteration:
def Preorder(node):
    stack = [node]
    while stack:
        node = stack.pop()
        print(node.val)
        if node.right:
            stack.append( node.right )
        if node.left:
            stack.append( node.left )

#Task: create logic of inorder traversal using stack iteration
#Task: create logic of postorder traversal using stack iteration

# === Define traversal method (BFS) ===
from collections import deque

def levelorder(node):
    queue = deque()
    queue.append(node)
    while queue:
         node = queue.pop()
         print(node.val)
         if node.left:
             queue.appendleft(node.left)
         if node.right:
             queue.appendleft(node.right)

# levelorder(A)         

## ==== Search using DFS ====
# iteration:  ---> O(n)
def search_DFS(root , target_val):
    if not root:
        return -1
    stack = [root]
    level = 0
    while stack:
        if len(stack)>1:
            level+=1
        node = stack.pop()
        if node.val == target_val:
            return f"Found at: {level}"
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        if len(stack)==1:
            level=1
    return -1

# recursion:  ---> O(n)
def Search_DFS(root , target_val):
    if not root:
        return False
    if root.val == target_val:
        return True
    return Search_DFS(root.left , target_val) or Search_DFS(root.right , target_val)

# result = search_DFS(A , 8)
# print( result )

# result = Search_DFS(A , 8)
# print( result )

# TASK: search using BFS

#===== Create a BST + iteration + Binary search + insertion function =====
#Create nodes:
A1 = node(6)
B1 = node(4)
C1 = node(11)
D1 = node(3)
E1 = node(5)
F1 = node(9)
G1 = node(14)
H1 = node(20)

#Create connections:
A1.left , A1.right = B1 , C1
B1.left , B1.right = D1 , E1
C1.left , C1.right = F1 , G1
G1.right = H1

#===== traversal function (DFS) =====
#recursion:
def inorder(node):
    if not node:
        return 
    inorder(node.left)
    print(node.val)
    inorder(node.right)

# inorder( A1 )

# TASK: do rest of the traversal functions (BFS and DFS)
# TASK: create searching functions for BST (BFS and DFS)--> O(n)

#=== Binary search on BST ===
# TAKS: create binary search for BST --> O(log n)  -------> this is the biggest pros of BST

#=== insertion ===
def insert(root , node):
    if root.val > node.val:
        if root.left:
            insert(root.left , node)
        else:
            root.left = node
    else:
        if root.right:
            insert(root.right , node)
        else:
            root.right = node

insert( A1 , node(1))
inorder( A1 )