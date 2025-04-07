def get_lps(st):
    lps = []
    pre = 0
    suf = 1
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
                pre = lps[pre-1]
    return lps

def circular_pattern_matching(substring, st):
    new_st = st + st
    lps = get_lps(substring)
    fp = 0
    sp = 0
    while(sp<len(new_st)):
        if new_st[sp] == substring[fp]:
            fp+=1
        elif fp != 0:
            fp = lps[fp-1]
        sp += 1
        if fp == len(substring):
            return sp - len(substring)
        
    return -1

print(circular_pattern_matching("ababc", "abcdfeababcrt"))