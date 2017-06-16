import collections

def test(arr):
    if not arr : return 0
    m = len(arr)
    if m == 0 : return 0
    n = len(arr[0])
    if n == 0 : return 0
    dq = collections.deque()
    dq.append((0, 0, 1))
    res = 0
    while dq:
        i, j, num = dq.popleft()
        res = max(res, num)
        if i > 0 and arr[i-1][j] > arr[i][j]:
            dq.append((i-1, j, num+1))
        if i < m-1 and arr[i+1][j] > arr[i][j]:
            dq.append((i+1, j, num+1))
        if j > 0 and arr[i][j-1] > arr[i][j]:
            dq.append((i, j-1, num+1))
        if j < n-1 and arr[i][j+1] > arr[i][j]:
            dq.append((i, j+1, num+1))

    print res

arr = [[1, 2, 3, 4, 5], [16, 17, 24, 23, 6], [15, 18, 25, 22, 7], [14, 19, 20, 21, 8], [13, 12, 11, 10, 9]]
test(arr)
        
        

