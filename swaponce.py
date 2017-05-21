def test(arr):
    size = len(arr)
    if size == 0 : return
    ma = -1
    for i in range(1, size):
        if arr[i-1] < arr[i]:
            if ma == -1:
                ma = i
            else:
                if arr[ma] < arr[i]:
                    ma = i
    if ma == -1 : 
        print "no move"
        print arr
        return 
    start = 0
    for i in range(ma):
        if arr[i] < ma:
            start = i
            break

    arr[start], arr[ma] = arr[ma], arr[start]
    print arr

arr = [9, 8, 7, 6]
print arr
test(arr)
