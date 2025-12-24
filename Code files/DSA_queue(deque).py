# QUEUE IS A OPEN ENDED LIST FOLLOWING A FIFO PRINCIPLE.
# Queue: A FIFO linear data structure where insertion happens at the rear and deletion at the front.
# USE CASE:  
# . producer --> |queue| --> consumer
#   producer consumer type of architecture where one component is producing information and other components are consuming them. Queue allows us to implement loosely coupled architecture which has many benefits. 
# . in BUFFERING real-time data (storing data in temporary memory space)
#   like in yahoo finance buffering data from NY stock exchange

# Tip: deque have index. slicing is slower than list
# Python’s deque (double-ended queue) is not implemented using a list. Instead, it uses a doubly-linked list.



# # QUEUE USING LIST (but problem is it's 'dynamicity'):
# list=[]
# list.insert(0,'val 1')
# list.insert(0,'val 2')  # made first one to right
# list.insert(0,'val 3')

# list.pop() #--> 'val 1'
# list.pop() #--> 'val 2'
# list.pop() #--> 'val 3'


# # USING DEQUE:
from collections import deque  # --> works as stack | queue
# queue=deque()  # --> double ended queue
# queue.appendleft('val 1')
# queue.appendleft('val 2')  # shifts first one to right
# queue.appendleft('val 3')

# queue.pop() #--> 'val 1'
# queue.pop() #--> 'val 2'
# queue.pop() #--> 'val 3'

# Write a program to print binary numbers from 1 to 10 using Queue. 
    # 1
    # 10
    # 11
    # 100
    # 101
    # 110
    # 111
    # 1000
    # 1001
    # 1010
q = deque()
q.append('1')
for val in range(1,11):
    q.appendleft(q[-1]+'0')
    q.appendleft(q[-1]+'1')
    
    print(q[-1])
    q.pop()

print(q)






