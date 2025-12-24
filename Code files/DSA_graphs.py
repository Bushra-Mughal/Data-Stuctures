# Interesting facts: TREE & LINKLIST are GRAPHS!
# 1
#  \
#   2
#    \
#     3 
# A TREE is CONNECTED ACYCLIC graph: Nodes=4 then Edges=4-1 

#==== What are graph ====
# Its a non-hierarchical ds having nodes connected using edges.

#==== types ====
# directed graph (uni directional) (ie: tree , cyclic graph)
# undirected graph (bi directional/not one direction) <-->

#==== uses ====
# Its used in "space state" in ML
# used in path finding algorithms (dijkstra, A*)

#===== TRAVERSE =====
#( we create a 'SEEN SET' to track visited nodes )
# DFS  
# BFS 

#==== COMPLEXITY =====
#Using ADJACENCY LIST (most common):
# traversal  O(V+E)
# add edge    O(1)
# add vertex  O(1)

#==== WAYS OF DEFINING EDGES (first step of creating graph)=====
#💠we create EDGE LIST:  
# edges =[ [0,1], [0,2], [1,2] ] 
#       but its IRRITATING SO
#💠we create an ADJACENCY MATRIX:
#  ____________________________
# |Row 1 (for node 0): 0 1 1  |
# |Row 2 (for node 1): 0 0 1  |
# |Row 3 (for node 2): 0 0 0  |
#       but we had a whole row 3 having no connection (ITS SO EXTRA) SO
#💠we create an ADJACENCY LIST: (most common) -->its a dictionary
# { 0: [1,2], 1: [2], 2:[] } 
#💠we can also create a CLASS NODE



# ==== Create a directed graph =====
#An EDGE LIST is given to us:
n = 3
A = [ [0,1], [0,2], [1,2] ]  # --> ie: [0,2] from 0 NODE to 1 NODE

# For creating an edge-defining format (ADJACENCY MATRIX):
m = []          
#To make 'm' a 2D 'zeros' array :
for i in range(n):
    m.append( [0]*n )
#Make vth column in uth row = 1:
for u,v in A:
    m[u][v] = 1

#NOTE: if the graph is undirected then m will be symmetric matrix. m(ij)=m(ji)

# For creating a common edge-defining format (ADJACENCY LIST):
from collections import defaultdict
#Pass a list() (instead of []) to get NEW empty list for each new key:
edges = defaultdict( list )
for u,v in A:
    edges[u].append(v)

#Q: Which one do you find more efficient?
print(edges[0])
print( m[0] )

#==== Create DFS traversal function =====
source = 0        #-> this is our fisrt node
seen=set()        #-->this set will make sure no node is visited twice
seen.add(source)  #->add first node in set

# DFS - O(N+E)
#recursion:
def dfs_recursion(source):
    print(source)
    for nei in edges[source]:
        if nei not in seen:
            seen.add( nei )
            dfs_recursion(nei)
#iteration:
def dfs_iteration(source):
    stack = [source]
    while stack:
        node = stack.pop()
        print( node )
        if edges[node]!=None:
            for n in edges[node]:
                if n not in seen:
                    stack.append(n)
                    seen.add(n)

#NOTE: for how the function knows 'seen'&'edges' while they arent pass as an argument, see last of this file

#==== Create BFS traversal function =====
# BFS - O(N+E)
#iteration:
from collections import deque

def bfs_iteration(source):
    queue = deque()
    queue.appendleft(source)
    while queue:
        node = queue.pop()
        print(node)
        if edges[node]:
            for n in edges[node]:
                if n not in seen:
                    queue.appendleft(n)
                    seen.add(n)
#Call the functions:
dfs_recursion(source)
dfs_iteration(source)
bfs_iteration(source)



###NOTES:
#Q: How my function knows the variables outside it?
#A: Its python! Python checks for LEGB
    # Is 'edges' local to this function? ❌
    # Is it in an enclosing function? ❌
    # Is it global (defined outside)? ✅
    # Built-in? (not needed)
#   And you can only MODIFY that global variable: edges[0]={}




 