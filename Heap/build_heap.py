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

def heapify_itr(arr, pos, n):
    larg_elm_pos = pos
    lchild_pos = 2*pos +1
    rchild_pos = 2*pos + 2
    # while((lchild_pos<n) and arr[lchild_pos]>arr[pos]) or ((rchild_pos<n) and arr[rchild_pos]>arr[pos]):
    while(rchild_pos<n or lchild_pos<n-1):
        
        if (lchild_pos<n) and arr[lchild_pos]>arr[larg_elm_pos]:
            larg_elm_pos = lchild_pos
        if (rchild_pos<n) and arr[rchild_pos]>arr[larg_elm_pos]:
            larg_elm_pos = rchild_pos
        if  larg_elm_pos != pos:
             arr[larg_elm_pos], arr[pos] = arr[pos], arr[larg_elm_pos]
             pos = larg_elm_pos
        lchild_pos = 2*pos + 1
        rchild_pos = 2*pos + 2

    if (lchild_pos<n) and arr[lchild_pos]>arr[larg_elm_pos]:
        larg_elm_pos = lchild_pos
    if (rchild_pos<n) and arr[rchild_pos]>arr[larg_elm_pos]:
        larg_elm_pos = rchild_pos
    if  larg_elm_pos != pos:
            arr[larg_elm_pos], arr[pos] = arr[pos], arr[larg_elm_pos]


def is_max_heap(arr):
    if arr:
        for i in range(int(len(arr)/2)):
            if arr[i]< arr[2*i + 1]:
                return False
            elif (2*i + 2)<len(arr) and arr[i]< arr[2*i + 2]:
                 return False
                 
        else:
            return True


	
	

def build_heap(arr):
    n = len(arr)
    if n == 0:
        raise IndexError("Insufficient value")
    for i in range((n//2)-1,-1,-1):
        	heapify_itr(arr, i, n)

print(arr)
build_heap(arr)
print(arr)
print(is_max_heap(arr))