def longestOnes(nums: list, k: int) -> int:
        # max_no_1 = 0
        no_0 = 0
        max_consec_one = 0
        window_size = 0
        first = 0
        last = 0
        while last<len(nums):
            if nums[last] == 1:
                last += 1
                window_size += 1
            else:
                last += 1
                no_0 += 1
                if no_0 <= k:
                    window_size += 1 
                else:
                    while nums[first] != 0:
                        first += 1
                        window_size -= 1 
                    first += 1
                    window_size -= 1

            if window_size > max_consec_one:
                max_consec_one = window_size
        return max_consec_one

print(longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))