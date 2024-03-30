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
             
def heap_sort(arr, reverse = False):
    n = len(arr)-1
    while(n>=0):
        if reverse == True:
            element = arr.pop(0)
            arr.append(element)
        else:
            arr[0],arr[n] = arr[n], arr[0]
        heapify_rec(arr, 0, n)
        n -= 1


print(arr)
print(id(arr))
build_heap(arr)
print(arr)
print(id(arr))
heap_sort(arr, reverse = True)
print(arr)
print(id(arr))
