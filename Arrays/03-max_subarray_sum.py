
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

def largestContiguousSum(arr) -> int:
		# add your logic here
		start = 0
		new_start = 0
		end = 0
		curr = 0
		max_sum = arr[0]
		curr_sum = 0
		while curr<len(arr):
			if curr_sum>max_sum:
				max_sum = curr_sum
				end = curr-1
				start = new_start
			if curr_sum<=0:
				curr_sum = 0
				new_start = curr
			curr_sum = curr_sum + arr[curr]
			curr = curr + 1
		return max_sum, start, end

print(largestContiguousSum(arr))



max_sum_current = 0
max_sum_total = 0
for i in arr:
    max_sum_current = max_sum_current + i
    if max_sum_current < 0:
        max_sum_current = 0

    if max_sum_total< max_sum_current:
        max_sum_total = max_sum_current

print(max_sum_total)
