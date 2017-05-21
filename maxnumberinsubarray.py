import collections
def test(arr, k):
    size = len(arr)
    if size == 0 : return []
    res = []
    dq = collections.deque()
    for i in range(size):
        if len(dq) >= k : dq.popleft() 
        while dq and arr[dq[-1]] > arr[i]:
            dq.pop()
        dq.append(i)
        if i + 1 - k >= 0:
            res.append(arr[dq[0]])
    print res

arr = [4, 2, 1, 6, -3, 1, 6 ,8, 4]
print arr
k = 3

test(arr, k)
