def Factor_Combinations(n):

    if n < 2 : return []
    res = []
    helper([], 2, n, res)
    print res

def helper(cur, po, rem, res):
    if rem == 1 : 
        res.append(cur[:])
        return
    for i in range(po, rem+1):
        if rem % i == 0:
            cur.append(i)
            helper(cur, i, rem/i, res)
            cur.pop()


Factor_Combinations(18)

