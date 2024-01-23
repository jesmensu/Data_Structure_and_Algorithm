lst = [6,7,3,2,9,5,8]
for r in range(len(lst)-1):
    min_index = r
    for j in range(r+1,len(lst)):
        if lst[j]<lst[min_index]:
            min_index = j
    lst[r], lst[min_index] = lst[min_index], lst[r]

print(lst)
