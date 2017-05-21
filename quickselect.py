def test(arr, k):
    size = len(arr)
    if size < k : return 
    print quickslect(arr, 0, size-1, k-1)
    arr.sort()
    print arr

def quickslect(arr, l, r, k):
    piv = arr[r]
    po = l
    for i in range(l, r):
        if arr[i] < piv:
            arr[i], arr[po] = arr[po], arr[i]
            po+=1
    arr[po], arr[r] = arr[r], arr[po]
    if po == k : return arr[po]
    elif po < k : return quickslect(arr, po+1, r, k)
    else: return quickslect(arr, l, po-1, k)


arr = [2, 5, 2,3,13, 54, 7,45, 32 ,5,6, 6, 5 ,53,243, 3,2,31, 4,4326, 342,543,]
print arr

test(arr, 5)

