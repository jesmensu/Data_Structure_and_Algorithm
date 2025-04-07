from collections import defaultdict

def zero_sum_subarrays(arr):
    prefix_sum = 0
    sum_map = defaultdict(list)  # Stores prefix sum indices
    result = []

    # Initialize for sum = 0 case
    sum_map[0].append(-1)

    for i, num in enumerate(arr):
        prefix_sum += num  # Compute prefix sum
        # If prefix sum is seen before, subarrays exist
        if prefix_sum in sum_map:
            for start_index in sum_map[prefix_sum]:
                result.append((start_index + 1, i))  # Store (start, end) indices
        
        # Store index of current prefix sum
        sum_map[prefix_sum].append(i)

    return result

# Example Usage
arr = [1, 2, -3, 3, 1, -4, 2, -2]
print("Zero-sum subarrays:", zero_sum_subarrays(arr))


prefix_sum = 0
# prefix_arr = []
prefix_sum_map = {}
prefix_sum_map[0] = [-1]
result = []
res = 0

for i in range(len(arr)):

    prefix_sum += arr[i]
    
    # prefix_arr.append(prefix_sum)
    if prefix_sum not in prefix_sum_map:
        prefix_sum_map[prefix_sum] = [-1]
        continue
    for start_index in prefix_sum_map[prefix_sum]:
        result.append((start_index+1, i))
        # res += prefix_sum_map[prefix_sum] -1
    prefix_sum_map[prefix_sum].append(i)

print(len(result))
print(result)