from Queue import PriorityQueue

def test(s, k):
    size = len(s) 
    if size == 0 : return ""
    res = []
    dic = {}
    for i in range(size):
        if s[i] not in dic:
            dic[s[i]] = -1
    for i in range(size):
        if dic[s[i]] == -1:
            res.append(s[i])
            dic[s[i]] = len(res)-1
        else:
            while len(res) - dic[s[i]] < k:
                res.append('_')
            res.append(s[i])
            dic[s[i]] = len(res)-1
    print res




def test1(s, k):






s = "BAACDCBBAA"
print s
k = 3

test(s, k)
