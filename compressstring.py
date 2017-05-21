def test(s):
    size = len(s)
    if size < 2 : return s
    c = s[0]
    count = 1
    res = ""
    for i in range(1, size):
        if s[i] != c:
            if count == 1:
                res += c
            else:
                res += c+str(count)
                count = 1
            c = s[i]
        else:
            count+=1
    res += s[-1] if count == 1 else s[-1]+str(count)

    print s
    print res


s = "fdsaaadddfdss"

test(s)
        
