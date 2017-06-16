import collections
def test(arr):
    size = len(arr)
    if size == 0 : return False
    d = {}
    for i in arr:
        k, v = i
        if k in d:
            d[k].append(v)
        else:
            d[k] = [v]


    for i in d:
        if dfs([], i, d) : return True
    return False




def dfs(se, k, d):
    if k not in d : return False
    if k in se:
        print k
        return True
    for i in d[k]:
        se.append(i)
        dfs(se, i, d)
        se.pop()



#    for i in k:
#        se = set()
#        dq = collections.deque()
#        dq.append(i)
#        while dq:
#            size = len(dq)
#            for _ in range(size):
#                t = dq.popleft()
#                if t in d:
#                    if t in se : return True 
#                   se.add(t)
#                    if d[t]:
#                        for i in d[t]:
#                            dq.append(i)





arr = [['A', 'B'], ['A', 'C'], ['A', 'D'], ['B', 'C'], ['C', 'A']]
print test(arr)
