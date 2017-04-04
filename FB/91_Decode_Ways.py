

def decodeways(s):
    size = len(s)
    if size == 0 or s[0] == '0' : return 0
    res = 0
    dp = [0] * (size+1)
    dp[0] = 1
    dp[1] = 1 if s[0] != '0' else 0
    

    for i in range(1, size):
        s1 = int(s[i-1])
        s2 = int(s[i])
        if s2 == 0:
            if s1 == 1 or s1 == 2:
                dp[i] = dp[i-1]
            else:
                return dp[i-1]
        elif 10 < s1*10+s2 < 20 or 20 < s1*10 + s2 < 27:
            dp[i] += dp[i-1]
        else:
            dp[i] = dp[i-1]
    print dp
    return dp[size-1]
        


s = "1210123"
print decodeways(s)
