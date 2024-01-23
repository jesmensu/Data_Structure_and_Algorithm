# works like two list. takes the element from the original list one by one and insert in the appropriet position 
# in the front side sorted list

lst = [6,7,3,2,9,5,8]
count = 0
for r in range(len(lst)):
    for j in range(0,r):
        if lst[j]>lst[r]:
            temp = lst.pop(r)
            lst.insert(j,temp)
            count += 1

print(lst)
print(count)

lst.insert(5,10)
lst[1] = 30
print(lst)