def test(arr):
    size = len(arr)
    if size <= 1 : return arr
    print quicksort(arr, 0, size-1, 3)
    print arr


def quicksort(arr, left, right, k):
    if left < right:
        po = partition(arr, left, right)
        quicksort(arr, left, po, k-po)
        quicksort(arr, po+1, right, po+k)


def partition(arr, lo, hi):
    pivot = arr[lo]
    i = lo
    j = hi
    while 1:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j : 
            print arr, arr[j]
            return j
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

arr = [4, 52,2,3 ,5, 64, 4,32,9 ]

test(arr)


