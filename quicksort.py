def test(arr):
    size = len(arr)
    if size <= 1 : return arr
    quicksort(arr, 0, size-1)
    print arr


def quicksort(arr, left, right):
    if left < right:
        po = partition(arr, left, right)
        quicksort(arr, left, po)
        quicksort(arr, po+1, right)

def partition(arr, lo, hi):
    pivot = arr[lo]
    i = lo
    j = hi
    while 1:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1
        if i >= j : return j
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1

arr = [4, 52,2,3 ,5, 64, 4,32,9 ]

test(arr)


