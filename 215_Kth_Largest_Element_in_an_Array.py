#Given [3,2,1,5,6,4] and k = 2, return 5.


def test(arr, k):
    size = len(arr)
    if size == 0 : return 0
    k = k % size

    pivitvalue = arr[-1]
    storeindex = 0
    for i in range(size-1):
        if arr[i] < pivitvalue:
            arr[storeindex], arr[i] = arr[i], arr[storeindex]
            storeindex += 1
    arr[storeindex], arr[-1] = arr[-1], arr[storeindex]

    print arr

arr = [3, 2, 1, 5, 6, 7, 4]
k = 2
print arr
test(arr, k)

