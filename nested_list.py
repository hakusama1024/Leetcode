arr = [1, [2, 3], [[1]]]

def test(arr):
    size = len(arr)
    if size == 0 : return 0
    d = depth(arr)
    print helper(arr, d)

def helper(arr, depth):
    res = 0
    for i in arr:
        if type(i) == int:
            res += i * depth
        else:
            res += helper(i, depth-1)
    return res

def depth(arr):
    if type(arr) == int:
        return 0
    else:
        ma = 0
        for i in arr:
            ma = max(ma, depth(i)+1)
        return ma
        

test(arr)





