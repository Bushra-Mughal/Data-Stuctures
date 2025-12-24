# Tree is a non-linear data structure( heirarchical + no order/no index )
#💮It is the sub-category of "Directed Graph "
#◾ ORDER TYPES: 
# 1) ORDERED   (like 'permutation' where order matters)
# 2) UNORDERED (swapping doesnt matter)
#◾ MANY TYPES :
# General, 
# Binary (BST, HEAP, AVL ...),  
# Trie  ETC

# Memorize these simple lines: 
#⏳ 1)EVERY CHILD IS A root ITSELF
#⏳ 2)TREE IS a RECURSIVE DATA STRUCTURE



#===== EASY STEPS TO CREATE A TREE =====
#Start with a simple class:
class Tree_node:
    def __init__(self,data):
        self.data = data
        self.child = []
        self.parent = None

#Funtion to add child:
    def add_child(self , child_node):
        child_node.parent = self       #-->this will add the 'current object' in parent of child_tree
        self.child.append(child_node)

#Function to print tree (level wise):
    def print_tree_from_this_node(self,level = 0):
        print(f"{' '*level}{self.data}")
        for child in self.child:        #--> for loop will end when there is no child
            child.print_tree(level+1)   #-->recursion
        

#Create a simple heirarchy (level 0)
root = Tree_node( 'ROOT' )

#Create level 1 nodes
parent1 = Tree_node ( 'PARENT1')
parent2 = Tree_node ( 'PARENT2')

#Connect to root
root.add_child( parent1 )
root.add_child( parent2 )

#Create level 2
child1 = Tree_node( 'CHILD1')
child2 = Tree_node( 'CHILD2')

child3 = Tree_node( 'CHILD3')
child4 = Tree_node( 'CHILD4')

#Connect to level 1
parent1.add_child( child1 )
parent1.add_child( child2 )

parent2.add_child( child3 )
parent2.add_child( child4 )

root.print_tree_from_this_node()

# WE BUILT THIS TREE:
#
#                  ROOT
#              /           \
#        PARENT1           PARENT2
#       /     \           /      \
#   CHILD1   CHILD2    CHILD3    CHILD4