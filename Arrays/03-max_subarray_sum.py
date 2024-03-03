
# Largest Sum Contiguous Subarray (Kadane’s Algorithm)
arr = [-1,-2,1,4,-2,-1,3,-1,5,-17,6]

max_sum_current = 0
max_sum_total = 0
start = 0
new_start = 0
end = 0
for i in range(len(arr)):
    max_sum_current = max_sum_current + arr[i]
    if max_sum_current < 0:
        max_sum_current = 0
        new_start = i + 1

    if max_sum_total< max_sum_current:
        max_sum_total = max_sum_current
        end = i
        start = new_start
print(max_sum_total)
print(start, end)