def strstr(hay, nee):
    if len(hay) == 0 and len(nee) == 0 : return -1
    if len(nee) == 0 : return 0
    l = [0] * len(nee)
    j = 0
    for i in range(1, len(nee)):
        while j > 0 and nee[i] != nee[j]:
            j = l[j-1]
        if nee[i] == nee[j]:
            j += 1
            l[i] = j
    print l

    j = 0
    res = []
    for i in range(len(hay)):
        while j > 0  and nee[j] != hay[i]:
            j = l[j-1]
        if nee[j] == hay[i]:
            j += 1
        if j == len(nee):
            res.append(i - j + 1)
            j = 0
    print res

hay = "basjslfksjsjfds"
nee = "ababcabcabcabc"
print hay
print nee
strstr(hay, nee)
