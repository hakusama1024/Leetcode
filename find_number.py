def test(arr):
    if not arr : return None
    size = len(arr)
    if size == 0 : return None

    l = 0 
    r = size-1
    po = -1
    while l < r:
        m = l + (r-l)/2
        if arr[m] == target:
            po = m
            break
        elif arr[m] > target:
            r = m-1
        else:
            l = m+1
    if po == -1 : return None
    print po, arr[po]


