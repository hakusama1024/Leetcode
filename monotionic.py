def test(arr):
    size = len(arr)
    if size < 2 : return True
    flag =0
    for i in range(1, size):
        if arr[i] > arr[i-1]:
            flag = 1
            break
        if arr[i] < arr[i-1]:
            flag = -1
            break
    
    if flag == 0 : return True
    for i in range(1, size):
        if arr[i] * flag < arr[i-1] * flag:
            return False
    return True

arr = [ 1, 2, 3, 4, 5]
arr = [1, 1, 1, 1, 2]
print arr

print test(arr)


