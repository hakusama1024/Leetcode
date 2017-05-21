def lengthOfLongestSubstringKDistinct(s, k):
    """
    :type s: str
    :type k: int
    :rtype: int
    """
    size = len(s)
    if size == 0 : return 0
    if k >= size : return size
    dic = {}
    for i in range(k):
        if s[i] in dic:
            dic[s[i]] += 1
        else:
            dic[s[i]] = 1
    res = k
    l = 0
    print dic
    for i in range(k, size):
        if s[i] not in dic:
            dic[s[i]] = 1
        else:
            dic[s[i]] += 1
        while len(dic) > k:
            if dic[s[l]] == 1:
                dic.pop(s[l])
            else:
                dic[s[l]] -= 1
            l += 1
        print dic, i, l

        res = max(res, i-l+1)
    
            
    print res

s = "ababffzzeee"
k = 3
lengthOfLongestSubstringKDistinct(s, k)
