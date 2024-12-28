def two_point_sum(target_sum, lst1):
    res = []
    lst = lst1.copy()
    lst.sort()
    start = 0
    end = len(lst)-1
    while(start<end):
        sum = lst[start] + lst[end]
        if sum == target_sum:
            res.append((lst[start], lst[end]))
            if lst[end] == lst[end-1]:
                end -= 1
            else:
                start += 1
            
        elif sum < target_sum:
            start += 1
        else:
            end -= 1

    for i in res:

        indx1 = lst1.index(i[0])
        indx2 = lst1.index(i[1])

        print(indx1, indx2)

    return res

def two_point_subs(target_subs, lst):
    result_list = []
    lst.sort()
    start = 0
    end = 1
    while(start<len(lst)-1 and end<len(lst)):
        subs = lst[end] - lst[start]
        if subs == target_subs:
            result_list.append((lst[start], lst[end]))
            if end < len(lst)-1 and lst[start] == lst[start+1]:
                start += 1
            else:
                end += 1
        elif subs < target_subs:
            end += 1
        else:
            start += 1
    return result_list


print(two_point_sum(14, [1, 4, 2, 9,10,10,5,7]))

print(two_point_subs(3, [1, 4, 2, 9,10,5,7]))

l = [1,2,3,2]
print(l.index(2,2))

            
