def Word_Break_II(s, worddic):
    size = len(worddic)
    if size ==  0 : return []
    res = []
    set = dd
    dp = [False] * (size+1)
    dp[0] = True
    helper(dp, 0, s, dic, res)
    print res



def helper(cur, po, s, dp, res):
    print cur, po
    if po == len(s) : 
        res.append(" ".join(cur))
        return
    for i in range(po, len(s)+1):
        if s[po:i] in dic and dic[s[po:i]]:
            dic[s[po:i]] == False
            helper(cur+[s[po:i]], i, s, dic, res)
            dic[s[po:i]] == True 

            

s = "catsanddog"
worddic = ["cat", "cats", "and", "sand", "dog"]

Word_Break_II(s, worddic)


