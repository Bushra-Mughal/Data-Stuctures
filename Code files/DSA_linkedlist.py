# Linkedlist > list/array 
#   O(1)         O(n)       --> for insert/delete at beginning
# Single linked list:

class node:
    def __init__ (self,data,next=None):
        self.data=data
        self.next=next

# Double linked list:
class NODE:
    def __init__(self,data,next=None,pre=None):
        self.data=data
        self.next=next
        self.pre=pre

# All linked list operations:
class linkedlist:
    def __init__ (self):
        self.head=None

    def insert_beginning(self,data):
        self.head=NODE(data,next=self.head,pre=None)

    def insert_end(self,data):
        if self.head==None:
            self.head=NODE(data,next=self.head,pre=None)
            return
        current=self.head        # current is the reference to the orignal node
        while current.next!=None:    # if you remove .next here , the current will become = None when the loop ends
            current=current.next
        current.next = NODE(data,next=None,pre=current)

    def insert_val(self,data):
        for val in data:
            self.insert_end(val)
            
    def insert_at(self,ind,data):
        try:
            current=self.head
            if ind==0:
                self.head=NODE(data,self.head.next,pre=None)
            for val in range(1,ind):
                current=current.next
            next=current.next
            current.next=NODE(data,next=next,pre=current)
        except:
            print("Invalid...")
    
    def insert_after(self,data1,data2):
        current=self.head
        while current:
            if current.data==data1:
                next=current.next
                current.next=NODE(data2,next=next,pre=current)
                return
        print("Such data not found...")

    def remove_at(self,ind):  # 1
        try:
            Node=self.head
            for val in range(ind):   # 0-0
                Node=Node.next
            current=self.head
            for val in range(ind-1):  # 0 - (-1)
                current=current.next
            current.next=Node.next
        except:
            print("Couldn't perform...")
    
    def remove_by_val(self,data):
        current=self.head
        Node=None
        found=False
        while current:
            if current.data==data:
                Node=current
                found=True
            current=current.next
        current=self.head
        if found==False:
            print("Such node not found...")
            return
        while current:
            if current.next==Node:
                current.next=Node.next
            current=current.next
    
    def print_backward(self):
        tail=None
        current=self.head
        while current.next!=None:
            current=current.next
        tail=current
        while tail.pre!=None:
            print(tail.data," --> ",end=" ")
            tail=tail.pre
        print(tail.data)
        
    def print(self):
        current=self.head
        while current.next!=None:
            print(current.data," --> ",end=" ")
            current=current.next
        print(current.data)

ll=linkedlist()
ll.insert_val(["banana","mango","grapes","orange"])
ll.insert_val_after("mango","apple") 
ll.print()    # banana --> mango --> apple --> grapes --> orange
ll.remove_by_val("orange") 
ll.print()    # banana --> mango --> apple --> grapes
ll.remove_by_val("figs")   # Such node not found...
ll.print()    # banana --> mango --> apple --> grapes
ll.print_backward()   # grapes --> apple --> mango --> banana
