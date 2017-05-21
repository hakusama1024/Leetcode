i = 0
def decodeString(s):
    """
    :type s: str
    :rtype: str
    """
    global i
    size = len(s)
    if size == 0 : return ""
    return helper(s)

def helper(s):
    global i
    res = ""
    while i < len(s) and s[i] != ']':
        if s[i] not in "0123456789":
            res += s[i] 
            i+=1
        else:
            n = 0
            while i < len(s) and s[i] in "0123456789":
                n = n * 10 + int(s[i])
                i += 1
            i += 1
            t = helper(s)
            i += 1

            while n > 0:
                res += t
                n -= 1
    return res


           

s = "3[a]2[bc]"
r = "aaabcbc"
s = "2[abc]3[cd]ef"
r = "abcabccdcdcdef"


print decodeString(s)
print r
