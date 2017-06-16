def test(arr):
    if not arr : return arr
    size = len(arr)
    if size == 0 : return arr
    l = 0
    r = size-1
    while l < r:
        m = l+(r-l)/2
        if arr[m] > arr[r]:
            l = m+1
        if arr[m] < arr[r]:
            r = m
    print arr[l]

arr = [4, 5 ,6, 7, 8,9, 1, 2, 3]
test(arr)
