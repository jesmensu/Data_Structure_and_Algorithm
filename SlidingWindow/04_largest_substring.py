# Longest substring with unique character
def longest_unique_substring(s):
    char_set = set()
    left = 0
    max_length = 0
    start_index = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        
        # Update max length and start index
        if right - left + 1 > max_length:
            max_length = right - left + 1
            start_index = left

    return s[start_index: start_index + max_length]

# Example Usage
s = "abcabcdbb"
print("Longest unique substring:", longest_unique_substring(s))


def largest_substring(st):
    max_len = 0
    left = 0
    char_set = set()
    char_set.add(st[0])
    for right in range(1,len(st)):
        while st[right] in char_set:
            char_set.remove(st[left])
            left += 1
        char_set.add[right]

        if right - left > max_len:
            max_len = right - left

    return st[left:left+max_len]

print("Longest unique substring:", longest_unique_substring(s))