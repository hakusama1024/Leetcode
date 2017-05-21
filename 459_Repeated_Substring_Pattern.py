s = "abcabcabcabc"


def test(s):
    size = len(s)
    if size == 0 : return 0
    for i in range(1, len(s)/2):
        if helper(s[:i], s, i):
            print s[:i]


def helper(cur, s, po):
    if len(cur) > len(s)/2 or len(s) % len(cur) != 0:
        return False
    for i in range(len(s)/len(cur)):
        for j in range(len(cur)):
            if cur[j] != s[i*len(cur) + j]:
                return False
    return True


test(s)
