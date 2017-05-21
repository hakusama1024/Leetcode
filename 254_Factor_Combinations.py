def Factor_Combinations(n):

    if n < 2 : return []
    res = []
    #helper([], 2, n, res)
    res = test(n)
    return res

def test(n):
    start = 2
    res = []
    while n != 1:
        if n % start == 0 :
            res.append(start)
            n /= start
        else:
            start += 1
        

    print res

def helper(cur, po, rem, res):
    print po, rem
    if rem == 1 : 
        res.append(cur)
        return
    for i in range(po, rem+1):
        if rem % i == 0:
            helper(cur+[i], i, rem/i, res)


Factor_Combinations(32)

