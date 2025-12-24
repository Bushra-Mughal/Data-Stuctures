#==== What is heap? ====
# Also called "priority queue" js a type of Binary Tree 
#NOTE: it is common is leetcode problems

#==== Its orientation ====
# (Min heap , Max heap ) --> all heap types fall under this

#====== types ======
# it has many variants: 
# fibonacci (tree internally),
# binary (array internally)--> what we discussed,
# pairing (tree internally) etc

#===== Operations =====
# build heap O(n) --> heapify()
# sift down O(logn)  --> internally its ensuring the heap rule
# pop , insert ,delete_at_index O(logn) -->due to sifting
# insert tuples O(nlogn)

#===== sifting directions in different operations =====
# heappush ---> bottom-up  so:
# build heap --> bottom-up
# heappop ---> top-down

#===== Cons =====
# searching takes O(n) in worst case as no left-right relation

#==== Common usecase ====
# prioritizing, Heap sort O(nlogn), storing tuples ie:(2:A)

#==== In simple words ====
# Heap = BT + a rule
# Min heap rule:   root <= root.left and root.right
# Max heap rule:   root >= root.left and root.right

#NOTE: see the end of file for more clearity on heapify,heappop etc



# ===== Use built-in lib =======
import heapq  #----> works on ARRAY+INDEX math. depicts MIN HEAP 

#===== Heapify an array O(n) (apply the rule and make it a heap)
array = [-3,0,9,-4,9,2,1,5]
heapq.heapify(array)        #---> rearrange the array -->NOTE: not a heap sort
## print( array )          #---> now is this array satisfies 'heap' rule

#==== PEAK min value in heap O(1)====
#==== POP min value in heap O(log n)====
heap = array.copy()
min_val_1 = heapq.heappop( heap )
min_val_2 = heapq.heappop( heap )
min_val_3 = heapq.heappop( heap )
min_val_4 = heapq.heappop( heap )
min_val_5 = heapq.heappop( heap )
min_val_6 = heapq.heappop( heap )
min_val_7 = heapq.heappop( heap )
min_val_8 = heapq.heappop( heap )
## print( heap , min_val_8 )

# TASK: create logic for finding max value and insert third largest value
## HINT: To make MAX-heap: push negative values

#=== Insertion O(log n) ===
heapq.heappush(array , 4)
## print( array )

#=== Heap sort O(n log n) NOTE: space: O(n) as O(1) is more complex to create ====
# Heap sort requiement: A heapified array
def heap_sort( array ):
    if array:
        heapq.heapify( array )
        n = len(array)
        sorted_array =  [heapq.heappop(array) for i in range(n)]
        return sorted_array

Array = heap_sort( array )
## print( Array )

#=== Add tuples (key-val) in a heap O(nlogn)====
from collections import Counter
list = ['A','B','C','A','D','A','D','E','E']
tuples = Counter(list)
# print (tuples)  --->this is a dic now
array = []

# for k in tuples:  #---> this will give each dic item ('A':3)
#     print(k , tuples[k])
     
for k,v in tuples.items():
    heapq.heappush(array, (v,k))
print(array)
#NOTE: heap will sort acc to 'v' then 'k' -->similar to 'group-by' in SQL


##### NOTES:
#Q: Does an array converts to a heap during all these operations using heapq?
#A: So Python doesn't convert array to a tree – it rearranges the existing array and uses index math to treat it like a tree conceptually.
# That's why it's so efficient: O(n) time, O(1) space for heapify operations!

#Q: How to Heapify an Array (Bottom-Up Approach)
#A: We use the heapify function starting from the last non-leaf node and move upwards to the root.
# Key Insight: All leaf nodes are already valid heaps (single element). So we only need to fix non-leaf nodes.
# Java// This method builds a max-heap from an unsorted array
# public static void buildMaxHeap(int[] arr) {
#     int n = arr.length;

#     // Start from the last non-leaf node
#     // Index of last non-leaf node = (n/2) - 1
#     for (int i = n / 2 - 1; i >= 0; i--) {
#         heapify(arr, n, i);  // Fix the subtree rooted at i
#     }
# }