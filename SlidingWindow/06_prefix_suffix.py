# finding the largest matching prefix and sufix from a string
# used KMP algorithm
def largest_prefix_sufix(st):
    lps = []
    pre = 0
    suf = 1
    lps.append(0)
    while(suf<len(st)):
        if st[pre] == st[suf]:
            lps.append(pre+1)
            pre += 1
            suf += 1
        else:
            if pre == 0:
                lps.append(0)
                suf += 1
            else:
                pre = lps[pre -1]
    return lps[-1]

print(largest_prefix_sufix("abaa"))