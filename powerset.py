def test(arr):
    size = len(arr)
    if size == 0 : return []
    res = []
    res.append([])
    print res
    for i in range(size):
        t = len(res)
        for _ in range(t):
            if _ == 0 : 
                res.append([arr[i]])
            else:
                tmp = res[_][:]
                tmp.append(arr[i])
                res.append(tmp)
    print res


arr = [1, 2, 3]
test(arr)

