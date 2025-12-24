# Dictionary is python implementation of hashmap or hash table (java) 
# Internally:   Dictionary = list/array + hashing 
# Hashing = converting string into an index
# Hash funtion do 'hashing' of the given value

# ===== COLLISION =====
#Collision = overwriting or mdification of the key-value pairs
#Collision happens due to 'same hashing of different keys'

# ===== HASHMAP DEFINITION =====
#A linear datastructure which stores key-value pairs and locate them in O(1) constant time.

# === MOST COMMON USE CASE ===
# When ever occurance of a character or etc is to be calculated 

#=== Implementation of hashmap ===:

# Simple one ====
class Hashmap:
    def __init__(self,size):
        if size<20:
            self.size = 30  
        else:
            self.size = size
        self.hashmap = [[] for x in range(size)]

    def hash_function(self,data):
        sum = 0
        for val in data:
            sum+=ord(val)
        return sum%self.size
    
    def add(self,key,val):
        index = self.hash_function(key)
        if self.hashmap[index]==None:
            self.hashmap[index]=[key,val]
        else:
            self.hashmap[index].append([key,val])

    def search(self,key):
        index = self.hash_function(key)
        if self.hashmap[index]!=[]:
            print(f"Value is: {self.hashmap[index]}\n")
        else:
            print('Key not found\n')

    def delete(self,key):
        index = self.hash_function(key)
        if self.hashmap[index]!=None:
            self.hashmap[index]=[]
            print("Value successfuly deleted\n")
        else:
            print("Key isnt present\n")

    def print_hash_table(self):
        print(f"{'='*6}Your hashtable{'='*6}")
        for val in self.hashmap:
            if val!=[]:
                print(val)
        print(f"{'='*50}\n")

obj = Hashmap(20)
obj.add('march 9',1089)
obj.add('march 10',108)
obj.add('march 11',189)
obj.add('march 12',109)
obj.add('march 13',89)
obj.add('march 14',10)
obj.add('march 15',19)
obj.add('march 16',8)
obj.add('march 17',9)
obj.add('march 18',0)
obj.print_hash_table()

obj.search('march 13')
obj.search('march 2')
obj.print_hash_table()

obj.delete('march 15')
obj.print_hash_table()

    

# Another way of implementation ====
class hashmap:
    def __init__(self,size_of_array):
        self.size = size_of_array    # so that we can use 'size or array' in hashing funtion
        self.arr=[ [] for i in range(self.size)] # this is 'list comprehention'
    
    # Hashing function:
    def hashing(self,key):
        sum=0
        for val in key:
            sum+= ord(val)
        mod= sum % self.size
        return mod

    # Funtion to add key-value pairs like dictionary ( d[key]=val ):
    def __setitem__(self,key,val):
        hash = self.hashing(key)
        found=False
        for sub_list in self.arr[hash]:  # USE ENUMERATE FUNCTION IF: as 'index' gives the 'position' of that key-value pair , 'enumerate' function is used . otherwise no need to use it
            if len(sub_list)==2 and sub_list[0]==key:
                found=True
                sub_list[1]=val
                break
        if found==False:  # or: 'if not found'
            self.arr[hash].append([key,val])
    
    # Funtion to access elements like dictionary ( d[key] ):  ( this works like: d.get(key) )
    def __getitem__(self,key):
        hash=self.hashing(key)
        for tuple in self.arr[hash]:
            if tuple[0]==key:
                return tuple[1]
            
    # To delete the key-value pair like in dictionary (del d[key]):
    def __delitem__(self,key):
        hash= self.hashing(key)
        for sub_list in self.arr[hash]:
            if sub_list[0]==key:
                self.arr[hash].remove(sub_list)

d = hashmap(10)
# when size = 10 , the hash values are:
d['March 10']=900   # hash value = 0
d['March 10']=11111 
d['March 9']=67     # hash value = 0 
d['March 20']=234   # hash value = 1   
d['Dec 7']=177      # hash value = 5
d['April 6']=800    # hash value = 0

print(d['March 9'])
print(d['March 10'])
print(d['April 6'])
print(d['Dec 8'])  # here 'print' function gives me 'None'
print(d.arr)
del d['Dec 7']
print(d.arr)
# COLLISION: It is fetching me same values for 'March 10' and 'March 9' when array size is 10 , not when size is 100.





#####TEST:
## Q1:
# class hashmap:
#     def __init__(self,size):
#         self.arr=[[] for i in range(size)]
#         self.size=size

#     def hashing_function(self,key):
#         sum=0
#         for value in key:
#             sum+=ord(value)
#         return sum % self.size
    
#     def add_to_hashmap(self,file):
#         with open(file,'r') as file:
#             line=file.readline()
#             # time comp: O(n+4)
#             while line:
#                 sub_list=line.split(' ')
#                 key=sub_list[0]
#                 value=sub_list[1]
#                 hash=self.hashing_function(key)
#                 self.arr[hash].append([key,value])
#                 line=file.readline()
#     def find_avg(self):  # as i used no instance method init but , i used it through an object
#         with open('example.txt','r') as file:
#             val=0
#                 # Q: Why use a hashmap while i can directly use the file? If no file , then i will use hashmap right?
#                 # O(28)
#             for iter in range(7):
#                 data=file.readline()
#                 list=data.split(' ')
#                 value=int(list[1])
#                 val+=value
#             avg= val/7
#             return avg
#     def min_value(self):
#         min=10000000000 # why error in: self.arr[0][0][1]?
#         # O(3n)
#         for list in self.arr :
#             if len(list)==1:
#                 if int(list[0][1])<min:
#                     min=int(list[0][1])
#         return min

# obj=hashmap(100)
# obj.add_to_hashmap('example.txt')
# print(obj.find_avg())
# print(obj.min_value())

## Q2:
# class hashmap:
#     def __init__(self,size):
#         self.arr=[None for i in range(size)]
#         self.size=size
#     def hashfunction(self,key):
#         sum=0
#         for letter in key:
#             sum+=ord(letter)
#         mod=sum%self.size  # clear about: Why increasing array size makes less collisions? ( MATH )
#         return mod
#     def add(self,file):
#         with open('example.txt','r') as file:
#             line=file.readline()
#             while line:
#                 list=line.split(' ')
#                 key=list[0]
#                 value=list[1]
#                 hash=self.hashfunction(key)
#                 self.arr[hash]=value
#     def __getitem__(self,key):
#         hash=self.hashfunction(key)
#         return self.arr[hash]
# obj=hashmap(100)
# obj.add('example.txt')
# print(obj['Jan9'])
# print(obj['Jan10'])

## Q3:
# class hashmap:
#     def __init__(self,size):
#         self.arr=[0 for i in range(size)]
#         self.size=size
#     def hasingfunction(self,key):
#         sum=0
#         for l in key:
#             sum+=ord(l)
#         return sum%self.size
#     def add(self):
#         with open('example.txt','r') as file:
#             line=file.readline()
#             while line:
#                 for word in line:
#                     if ',' or ':' or ';' or '!' or '-' or '.' not in word:
#                         hash=self.hasingfunction(word)
#                         self.arr[hash]+=1 # value at that hash becomes ' value+1' for that word
#                 line=file.readline()
#     def __getitem__(self,key):
#         with open('example.txt','r') as file:
#             data=file.read()
#             if key not in data:
#                 return 0  # so that same hash value is not returned
#             else:
#                 hash=self.hasingfunction(key)
#                 return self.arr[hash]
# obj=hashmap(100)
# obj.add()
# print(obj['ko'])    
 
## Q4:
# LINEAR PROBING:
# class hm:
#     def __init__(self,size):
#         self.arr=[None for i in range(size)]
#         self.size=size
#     def hf(self,key):
#         sum=0
#         for l in key:
#             sum+=ord(l)
#         return sum%self.size
    
#     def __setitem__(self,key,value):
#         hash=self.hf(key)
#         if self.arr[hash]!=None:
#             Range=[i for i in range(hash,self.size)]+[i for i in range(0,hash)]
#             for hash in Range:
#                 if self.arr[hash]!=None:
#                     if self.arr[hash][0]==key:
#                         self.arr[hash]=[key,value]
#                         return
#                 elif self.arr[hash]==None:
#                     self.arr[hash]=[key,value]
#                     return
#         else:
#             self.arr[hash]=[key,value]
#     def __getitem__(self,key):
#         for list in self.arr:
#             if list!=None:
#                 if list[0]==key:
#                     return list[1]
# obj=hm(10)
# obj['March 9']=9080
# obj['March 10']=7676
# print(obj['March 9'])
# print(obj.arr)
# obj['March 9']=45
# obj['March 10']=76
# print(obj['March 9'])
# print(obj.arr)
