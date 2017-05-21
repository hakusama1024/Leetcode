def test(arr):
    size = len(arr)
    if size <= 1 : return size
    res = 0
    t = 1
    for i in range(1, size):
        if arr[i] > arr[i-1]:
            t += 1
        else:
            t = 1
        res = max(res, t)
    print res



def test1(arr):
    size = len(arr)
    if size <= 1 : return size
    dp = [1] * size
    for i in range(1, size):
        for j in range(i-1, 0, -1):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j]+1)
    print dp 






arr = [2, 2, 52, 1, 2, 36, 2, 1, 4, 5]


print arr
#test(arr)
test1(arr)



