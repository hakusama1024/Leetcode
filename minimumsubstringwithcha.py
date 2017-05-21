def test(s, dic):
    size = len(s)
    if size == 0 : return 0
    sized = len(dic)
    if sized == 0 : return s
    if size < sized : return 0
    print sized
    d = {}
    l = 0
    res = "a" * (size+1)
    for i in range(size):
        if s[i] in dic:
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
                while d[s[i]] != 1:
                    if s[l] in dic:
                        d[s[l]]-=1
                        if d[s[l]] == 0:
                            del d[s[l]]
                    l += 1
        print d
        if len(d) == sized:
            if i-l+1 < len(res):
                res = s[l:i+1]
    print res

s = "bcdfsafdsafewrsafdsac"
dic = {"a":1, "b":1, "c":1}

test(s, dic)




