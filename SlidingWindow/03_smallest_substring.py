# find the shortest substring that contains all distinct characters present in the string

def smallest_substring(st):
    fp = 0
    char_set = set(st)
    counter = {k:0 for k in char_set}

    char_set_diff = len(char_set)
    min_len = len(st)
    substring = ""

    for sp in range(len(st)):
        if char_set_diff > 0:
            counter[st[sp]] += 1
            if counter[st[sp]] == 1:
                char_set_diff -= 1

        while char_set_diff == 0:
            min_len = min(sp - fp + 1 , min_len)
            substring = st[fp:sp+1]

            counter[st[fp]] -= 1
            if counter[st[fp]] == 0:
                char_set_diff += 1    
            fp += 1
                
    return min_len, substring

# print(smallest_substring("abcdd"))


def smallest_substring1(st):
    fp = 0
    sp = 0
    char_set = set(st)
    counter = {k:0 for k in char_set}

    char_set_diff = len(char_set)
    min_len = len(st)
    substring = ""

    while sp < len(st):
        if char_set_diff > 0:
            counter[st[sp]] += 1
            if counter[st[sp]] == 1:
                char_set_diff -= 1

        while char_set_diff == 0:
            min_len = min(sp - fp + 1, min_len)
            substring = st[fp:sp+1]

            counter[st[fp]] -= 1
            if counter[st[fp]] == 0:
                char_set_diff += 1    
            fp += 1
        sp += 1  
    return min_len, substring

print(smallest_substring1("abcdd"))