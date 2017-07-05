def test(arr, target):
    if not arr or not target : return 0
    size = len(arr)
    dp = (target+1) * [0]
    for i in range(size):
        if arr[i] <= target:
            dp[arr[i]] = 1


    for i in arr:
        for j in range(target, -1, -1):
            if j >= i : 
                if dp[j-i] == 0 : dp[j] = 1
                else : dp[j] = dp[j-i] + 1

    print dp[target]

arr = [1, 2, 3, 4, 5, 6]
target = 33

test(arr, target)



    
