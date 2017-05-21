def test(arr):
    size = len(arr)
    if size == 0 : return 
    l = 0
    for i in range(size):
        if arr[l] != 0 :
            l += 1
        elif arr[l] == 0 and arr[i] != 0:
            arr[l], arr[i] = arr[i], arr[l]
            print "swap", arr[l], arr[i]
            l+=1
    print arr


def twopointer(arr):
    size = len(arr)
    if size == 0 : return 
    l = 0 
    r = size -1
    while l < r:
        while l < r and arr[l] != 0:
            l += 1
        while l < r and arr[r] == 0 : 
            r -= 1
        if arr[l] == 0 and arr[r] != 0 :
            arr[l], arr[r] = arr[r], arr[l]
            print "swap"
    print arr


def copy(arr):
    size = len(arr)
    if size == 0 : return
    l = 0
    for i in range(size):
        if arr[i] != 0 and i != l:
            arr[l] = arr[i]
            print "herer"
            l += 1
        elif arr[l] != 0 and i == l:
            l += 1

    print l
    print arr
    while l < size:
        arr[l] = 0
        l += 1
    print arr



arr = [1, 0, 3, 1, 0, 0, 2, 1, 9]
#arr = [1, 9, 3, 1, 1, 0, 2, 1, 9]




print arr
#twopointer(arr)
copy(arr)
arr = [1, 0, 3, 1, 0, 0, 2, 1, 9]
print arr
test(arr)

