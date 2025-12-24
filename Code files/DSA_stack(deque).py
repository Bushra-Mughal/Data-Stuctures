# Stack ds is also called 'deque'. From 'collections' library we get 'deque' class
# Problem with: 
# dynamic array: O(1) but, copying of all values to new memory space
# linked list: O(n) for last element
# hash map: O(n) but, only key-value pairs

# Stack = A stack is a LIFO linear data structure allowing insertion and deletion only at the top
# USED IN: undo command, recursion in programming, browser previous tab, function call stack etc
#TIP: use stack when: balanced braces --> syntax parsing (analyzing sequence of symbols)

# stack is like this:
# | val1 , val2 , val3  --> last element out <--  (container)
# queue is like this:
#--> val3 , val2 , val1 --> first element out      (line)


# Note: DEQUE WORKS SAME AS LIST:
from collections import deque
stack=deque()
stack.append(11)
stack.append(22)
stack.append(33)

stack.pop() #--> 33

# BALANCING PARENTHESIS:
def match(val1,val2):
    dic={
        '(': ')',
        '{': '}',
        '[': ']'
    }
    return dic[val1]==val2
def order_of_braces(string):
    s=deque()
    for val in string:
        if val in ['(','{','[']:
            s.append(val)   # --> | [ |
        elif val in [')','}',']']:
            if len(s)==0:   # --> | ] |  
                return False
            elif not match(s.pop(),val):
                return False
    return len(s)==0  # --> | [ | 

print(order_of_braces("))((a+b}{"))  # if len(s)==0: False
print(order_of_braces("[a+b]*(x+2y)*{gg+kk}"))  # len(s)==0: True
print(order_of_braces("[{( a+b )}]")) #len(s)==0: True
print(order_of_braces("[{( a+b }}]")) # if not match: False
print(order_of_braces("{a+b"))  #len(s)==0: False

    