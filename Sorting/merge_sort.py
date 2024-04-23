lst = [2,3,4,7,5,4,1,7]

def merge(left_list,right_list):
        lst_merge = []
        i = 0
        j = 0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]< right_list[j]:
                lst_merge.append(left_list[i])
                i += 1
            else:
                lst_merge.append(right_list[j])
                j += 1
        if i<len(left_list):
            lst_merge.extend(left_list[i:])
        elif j<len(right_list):
            lst_merge.extend(right_list[j:])

        return lst_merge


def merge_sort(lst):
    mid = len(lst)//2
    if len(lst)<=1: 
        return lst
    left_list = lst[:mid]
    right_list = lst[mid:]
    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    merged_list = merge(left_list,right_list)
    return merged_list
        

    

print(merge_sort(lst))