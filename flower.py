def test(arr):
    size = len(arr)
    if size == 0 : return False
    if size == 1 : return 1 - arr[0]
    count = 0
    for i in range(size):
        if arr[i] == 0:
            if (i == 0 and arr[i+1] == 0) or (i == size-1 and arr[i-1] == 0) or (arr[i-1] == 0 and arr[i+1] == 0):
                arr[i] = 1
                count += 1

    print count, ""
    print arr


arr = [0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1,0, 1,0, 1]
print arr

test(arr)

