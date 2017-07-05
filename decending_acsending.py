def test(arr, target):
    if not arr : return -1
    size = len(arr)
    l = 0 
    r = size-1
    while l < r:
        m = l + (r-l)/2
        if arr[m] < arr[m+1]:
            r = m
        else:
            l = m+1
    if arr[l] == target : return l
    mid = l
    l = 0
    r = mid
    while l <= r:
        m = l + (r-l)/2
        if arr[m] > target:
            l = m+1
        elif arr[m] < target:
            r = m-1
        else: return m

    l = mid
    r = size-1
    while l <= r:
        m = l + (r-l)/2
        if arr[m] > target:
            r = m
        elif arr[m] < target:
            l = m+1
        else : return m
    return -1
    




arr = [5,4, 3, 2, 1, 5, 6, 7, 8, 9]
print test(arr, 5)
