def test(arr):
    if not arr : return arr
    size = len(arr)
    if size < 2 : return arr
    l = 0
    r = size-1
    po = 0
    while arr[po] < 0: 
        po += 1
    if po > 0 : po -= 1
    print po

    l = po
    r = size-1

    for i in range(po/2+1):
        arr[i], arr[po-i] = arr[po-i], arr[i]
    print arr
    
    while l < r:
        if arr[l]*arr[l] > arr[r]*arr[r]:
            arr[r], arr[l] = arr[l], arr[r]
            r -= 1
        else: l -=1
    print arr



arr = [-9,-4 , -2, -1, 1, 3, 5, 7]


print arr
test(arr)


