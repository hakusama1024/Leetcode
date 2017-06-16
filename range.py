def test(arr):
    size = len(arr)
    if size == 0 : return ''
    res = []
    arr.append(arr[-1]+2)
    t = 0
    for i in range(1, len(arr)):
        if arr[i] > arr[i-1]+1:
            if i-1 == t:
                res.append(str(arr[t]))
            else:
                res.append(str(arr[t]) + '-' + str(arr[i-1]))
            t = i
    print res

arr = [1, 2, 3, 5, 7, 8, 9, 10,15]
test(arr)

