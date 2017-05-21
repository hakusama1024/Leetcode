import heapq
def test(arr, k):
    print arr
    size = len(arr)
    for i in range(k, size):
        heapq.heapify(arr[:k+1])
        arr[k] = arr[i]
    print arr

arr = [2, 5, 2,3,13, 54, 7,45, 32 ,5,6, 6, 5 ,53,243, 3,2,31, 4,4326, 342,543,]
test(arr, 5)

