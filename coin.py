import random
def test():
    arr = []
    for i in range(10):
        arr.append(random.randint(0, 20))
    su = sum(arr)
    dp = [[] for i in range(su+1)]

    for i in range(1, su):
        for j in arr:
            if i >= j and (dp[j] == [] or len(dp[j-i])+1 > len(dp[j])):
                dp[j] = dp[j-i] + [j]
    print dp






            

test()
