def test(arr):
    size = len(arr)
    if size == 0 : return arr
    mi =  
    ma = -(1<<32)
    for i in range(size):
        ma = max(ma, cur*arr[i], arr[i])
        mi = min(mi, cur*arr[i], arr[i])
        cur = max(arr[i] * cur, arr[i])

    print ma







arr = [-1, 2,3,  4, -2, -4]
print arr


test(arr)


