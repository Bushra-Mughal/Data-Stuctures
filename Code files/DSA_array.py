#==== What is array ====
#Array is linear data structure
#Array have ordered collection of elements

#===== Array occupy =====
# elements
# index
# and memory location

#===== ARRAY TYPES =====
# static (user gives size) 
# dynamic (user dont give size, RAM does(using geometric series pattern (ele*n)))

#===== To implement static array =====
#  1.list comprehention  2.NUMPY library

#===== To implement dynamic array =====
#  1.use list😊  (in python) 

#===== its operations ======
# INSERTION:  
# O(n) --> insert front, O(1)--> insert back
array=[None for val in range(1,6)]
for i in range(0,len(array)):
    array[i]=input(f"Enter val {i+1}: ")
for val in array:
    print(val)

#DELETION:
#  O(n) --> remove front, O(1)--> remove back
array=[12,23,24,26,2,3]
del_at = 2
for i in range(del_at,len(array)-1):
    array[i]=array[i+1]
del array[len(array)-1]
for val in array:
    print(val)

#SEARCH:
array=['a','b','g','y','x','y','j']
search='y'
found=False
for j in range(0,len(array)):
    if array[j]==search:                
        print(f"Found: '{array[j]}' AT: {array.index(array[j])}")
        found=True
        break
if found==False:
    print("Not found")

#ITERATION:
array=['a','b','g','y','x','y','j']
for i in range(0,len(array)):
    print(array[i])

#UPDATE:
array=[10,20,30,35,50,60]
update_at=3
update_val=40
array[update_at]=update_val


