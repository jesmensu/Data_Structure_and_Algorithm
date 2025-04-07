def check_string_as_substring(st1, st2):
    lps = [] 
    len_st1 = len(st1)
    len_st2 = len(st2)
    if len_st1 == len_st2:
        for i in range(len_st1):
            if st1[i] != st2[i]:
                return -1,-1
        return 0,len_st1
    if len_st1 < len_st2:
        smaller = st1
        larger = st2
    else:
        smaller = st2
        larger = st1       
    pre = 0
    suf = 1
    lps.append(0)
    while(suf<len(smaller)):
        if smaller[pre] == smaller[suf]:
            lps.append(pre+1)
            pre +=1
            suf +=1
        else:
            if pre == 0:
                lps.append(0)
                suf +=1
            else:
                pre = lps[pre-1]

    # print(lps)
    fp = 0
    sp = 0
    while(sp<len(larger)):
        if (len(larger)-sp) < (len(smaller)-fp):
            return -1
        if smaller[fp] == larger[sp]:
            fp += 1
        elif fp != 0:
            fp = lps[fp- 1]
        sp += 1
        if(fp==len(smaller)):
            return sp-len(smaller)
    return -1

print(check_string_as_substring("ababc", "abcdfeababcrt"))