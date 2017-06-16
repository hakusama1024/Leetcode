def test(a, b):
    sizea = len(a)
    sizeb = len(b)
    l = 0
    r = 0
    res = []
    while l < sizea and r < sizeb:
        t = 0
        if a[l] < b[r]:
            t = a[l]
            l += 1
        else:
            t = b[r]
            res.append(b[r])
            r += 1
        if not res or res[-1] != t : res.append(t)
        while l < sizea and a[l] == a[l-1]:
            l += 1
        while r < sizeb and b[r] == b[r-1]:
            r += 1


    while l < sizea:
        if not res or res[-1] != a[l] : res.append(a[l])
        l += 1
    while r < sizeb:
        if not res or res[-1] != b[r] : res.append(b[r])
        r += 1
    print res


def test1(a, b):
    res = []
    sizea = len(a)
    sizeb = len(b)
    l = 0
    r = 0
    while l < sizea and r < sizeb:
        if a[l] < b[r]:
            l += 1
        elif a[l] > b[r]:
            r += 1
        else:
            res.append(a[l])
            l += 1
            r += 1

        while l < sizea and a[l] == a[l-1]:
            l += 1
        while r < sizeb and b[r] == b[r-1]:
            r += 1

    print res


a = [1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8]
b = [2, 2, 2, 3,3, 3, 3,4, 5]

test(a, b)

test1(a, b)
            
       
