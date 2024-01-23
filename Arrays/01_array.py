'''Array is created in Python by importing array module to the python program. Then, the array is declared as shown below −

from array import *

arrayName = array(typecode, [Initializers])
Typecode	       Value
    b	    Represents signed integer of size 1 byte
    B	    Represents unsigned integer of size 1 byte
    c	    Represents character of size 1 byte
    i	    Represents signed integer of size 2 bytes
    I	    Represents unsigned integer of size 2 bytes
    f	    Represents floating point of size 4 bytes
    d	    Represents floating point of size 8 bytes
'''

from array import *
import numpy as np

array1 = array('i', [10,20,30,40,50])
# array2 = array("i",[[1,2,3,4,5],[2,3,3,4,5],[1,8,9,5,4]]) # Not working
# accessing element
for x in array1:      
   print(x)

print (array1[0])
# print(array2[0])

# operations
array1.insert(1,60)    #insert
array1.remove(30)
# print (array1.index(40))
array1[2] = 80        #update

T = [[11, 12, 5, 2], [15, 6,10,3], [10, 8, 12, 5], [12,15,8,6]]
S = np.array(T)

a = T[: : -1]
b = S[: : -1]

print(T[0][1])
print(S[0,1])

# print(a)
# print(b)