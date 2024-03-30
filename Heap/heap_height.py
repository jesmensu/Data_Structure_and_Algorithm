
from math import log2


arr = [8,6,5,9,3,2,13,10,15,27]

def heapify_rec(arr, pos, n):
    larg_elm_pos = pos
    lchild_pos = 2*pos + 1
    rchild_pos = 2*pos + 2
    if lchild_pos<n and arr[lchild_pos]>arr[larg_elm_pos]:
        larg_elm_pos = lchild_pos
    if rchild_pos<n and arr[rchild_pos]>arr[larg_elm_pos]:
        larg_elm_pos = rchild_pos
    if larg_elm_pos != pos:
        arr[larg_elm_pos], arr[pos] = arr[pos], arr[larg_elm_pos]
        heapify_rec(arr, larg_elm_pos, n)

def build_heap(arr):
    n = len(arr)
    if n == 0:
        raise IndexError("Insufficient value")
    for i in range((n//2)-1,-1,-1):
        	heapify_rec(arr, i, n)
             
def heap_height(arr):
    #  h = int(log2(len(arr)))
    h = 0
    n = len(arr)
    if n == 1:
        return 1
    while n>1:
         n = n//2
         h += 1 
    return h

print(arr)
build_heap(arr)
print(arr)
print(heap_height(arr))
