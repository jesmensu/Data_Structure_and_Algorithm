# def quick_sort(list1):
# Quick sort is inplace algorithm and This is not inplace algorithm. 
#     if len(list1)<=1:
#         return list1
#     else:
#         pivot=list1[0]
#         p = 1
#         q = len(list1)-1
#         while(p<=q):
#             while p<=len(list1)-1 and list1[p] < pivot:
#                 p += 1
#             while q>=0 and list1[q] > pivot:
#                 q -= 1
#             if p<q:
#                 list1[p], list1[q] = list1[q], list1[p]
#         list1[0], list1[q] = list1[q], list1[0]
#         print(id(list1))
#         lesser = quick_sort(list1[:q])
#         # print(lesser)
#         greater = quick_sort(list1[p:])
#         # print(greater)
#         result = lesser + [pivot] + greater
#         # print(pivot)
#         return result

# mylist=[53,11,72,68,41,25,18,37,44,80]
# mylist=quick_sort(mylist)
# print(mylist)




# def partition(array, low, high):
#   pivot = array[high]
#   i = low - 1
#   for j in range(low, high):
#     if array[j] <= pivot:
#       i = i + 1
#       (array[i], array[j]) = (array[j], array[i])
#   (array[i + 1], array[high]) = (array[high], array[i + 1])
#   return i + 1

# def quickSort(array, low, high):
#   print(id(array))
#   if low < high:
#     pi = partition(array, low, high)
#     quickSort(array, low, pi - 1)
#     quickSort(array, pi + 1, high)

# data = [3, 8, 7, 2, 1, 0, 9, 6]
# print("Unsorted Array")
# print(data)
# size = len(data)
# quickSort(data, 0, size - 1)
# print('Sorted Array in Ascending Order:')
# print(data)


def quick_sort(list1, low, high):
    if high>low:
        pivot=list1[low]
        p = low+1
        q = high
        while(p<=q):
            while p<=high and list1[p] <= pivot:
                p += 1
            while q>=low and list1[q] > pivot:
                q -= 1
            if p<q:
                list1[p], list1[q] = list1[q], list1[p]
        list1[low], list1[q] = list1[q], list1[low]
        quick_sort(list1, low, q-1)
        quick_sort(list1, q+1, high)

mylist=[53,11,72,68,41,25,18,37,44,80]
quick_sort(mylist, 0, len(mylist)-1)
print(mylist)