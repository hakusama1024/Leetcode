def test(arr):
    if not arr : return []
    m = len(arr)
    if m == 0 : return []
    n = len(arr[0])
    if n == 0 : return []
    dp = [[(1<<32)-1] * n for _ in range(m)]
    for i in range(m):
        dp[i][0] = 1
        dp[i][n-1] = 1

    for i in range(n):
        dp[0][i] = 1
        dp[m-1][i] = 1
    res = []

    for i in range(1, m-1):
        for j in range(1, n-1):
            dp[i][j] = min(dp[i-1][j], dp[i+1][j], dp[i][j-1], dp[i][j+1])+1

    for i in range(m):
        for j in range(n):
            if arr[i][j] >= dp[i][j] : res.append((i, j))

    print res
    


arr = [
        [0,3,5,1,3,5,6,1],
        [0,1,5,3,3,2,6,1],
        [0,3,9,1,0,5,9,1],
        [0,3,5,8,3,8,6,1],
        [0,3,5,9,3,5,6,1],
       ]

for i in arr:
    print i
print ""
test(arr)

    


