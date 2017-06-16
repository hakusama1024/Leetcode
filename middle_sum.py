def test(arr):
    size = len(arr)
    if size <= 1 : return False
    su = sum(arr)
    dp = [False] * (su+1)
    dp[0] = True
    for i in arr:
        for j in range(su, 0, -1):
            if j >= i:
                dp[j] = dp[j] or dp[j-i]
    print dp[su/2]
    for i in range(len(dp)):
        print i, dp[i]

arr = [4, 2, 5, 4]
test(arr)
