# Brutforce 
#  Time complexity O(n^2)

lst = [6,7,3,2,9,5,8]
for r in range(1,len(lst)):
    for j in range(len(lst)-r):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]

print(lst)

# Modified Bubble sort
#  best case Time complexity O(n) for sorted array

lst = [6,7,3,2,9,5,8]
flag = False
for r in range(1,len(lst)):
    flag = False
    for j in range(len(lst)-r):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1] = lst[j+1],lst[j]
            flag = True
    if flag == False:
        break

print(lst)