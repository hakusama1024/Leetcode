def test(arr):
    size = len(arr)
    if size == 0 : return 0
    j = 0
    for i in range(size):
        if arr[j] == 0 and arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j] 
            j += 1
        elif arr[j] != 0:
            j += 1
    print arr
    print j

arr = [1, 2, 4, 0, 3, 21, 0, 4,2 ,1 ,0]
print arr

test(arr)


