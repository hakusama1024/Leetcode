def test(arr):
    size = len(arr)
    if size == 0 : return 0
    l = 0 
    r = size-1
    while l < r:
        print arr[l], arr[r]
        m = (l+r)/2
        if arr[l] > arr[r]:
            l = m+1
        else:
            r = m
    print arr[l] 

arr = [4, 5, 6,7, 1, 2,3]
arr = [3,1,2]
print arr
test(arr)
