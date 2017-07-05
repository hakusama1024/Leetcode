def test(n):
    if n <= 0 : return 0
    t = 0
    print n
    nn = n
    l = []
    r = []
    while n:
        r.append(n%10)
        n /= 10
    res = []
    helper([], r, 0, 3, res)

    d = {}
    for i in res:
        su = sum(i)
        if su in d:
            d[su].append(i)
        else:
            d[su] = [i]
    print d
        


def helper(cur, arr, po, limit, res):
    if limit == 0:
        if len(cur) == 3:
            res.append(cur[:])
        return
    for i in range(po, len(arr)):
        cur.append(arr[i])
        helper(cur, arr, i+1, limit-1, res)
        cur.pop()








def permutation(arr, po, res):
    if po == len(arr):
        res.append(arr)
        return
    for i in range(po, len(arr)):
        if i > 0 and arr[i] == arr[i-1] : continue
        arr[i], arr[po] = arr[po], arr[i]
        permutation(arr[:], po+1, res)



test(134026)
