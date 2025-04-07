def get_lps(st):
    lps = []
    lps.append(0)
    fp = 0
    sp = 1
    while(sp<len(st)):
        if st[fp] == st[sp]:
            lps.append(fp + 1)
            fp += 1
            sp += 1
        else:
            if fp == 0:
                lps.append(0)
                sp += 1
            else:
                fp = lps[fp-1]
    return lps

def make_palindrome(st):
    new_string = st + "$" + st[::-1]
    lps = get_lps(new_string)
    pre_suf_len = lps[-1]
    palindrme_string = st[pre_suf_len+1::-1]+ st
    return palindrme_string

print(make_palindrome("aabaart"))