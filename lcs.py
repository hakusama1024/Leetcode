def lsc(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    if m == 0 or n == 0 : return []
    res = []
    dp = [[0] * (n+1) for i in range(2)]

    ma = 0

    for i in range(1, m+1):
        for j in range(1, n+1):
            if arr1[i-1] == arr2[j-1]:
                dp[i%2][j] = dp[(i-1)%2][j-1]+1
                if ma < dp[i%2][j]:
                    ma = dp[i%2][j]
                    res.append(arr1[i-1])
            else:
                dp[i%2][j] = max(dp[(i-1)%2][j], dp[i%2][j-1])

    for i in dp:
        print i
    print res
    print dp[1][n]

arr1 = ["a", "b", "c", "d", "a", "c", "c"]
arr2 = ["a", "d", "c", "a", "b", "c", "c"]

lsc(arr1, arr2)
