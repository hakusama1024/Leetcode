import collections

def test(arr):
    if not arr : return 0
    size = len(arr)
    if size == 0 : return 0
    d1 = {}
    d2 = {}
    for i in arr:
        d1[i[0]] = 0
        d1[i[1]] = 0
        d2[i[0]] = []
        d2[i[1]] = []

    for i in arr:
        d1[i[1]] += 1
        d2[i[0]].append(i[1])

    time = {'a' : 3, 'b' : 4, 'c' : 5, 'd' : 6, 'e': 7, 'f':9}
    
    res = 0
    for i in d1:
        if d1[i] == 0:
            dq = collections.deque()
            dq.append(i)
            tres = 0
            while dq:
                size = len(dq)
                tmp = 0 
                for _ in range(size):
                    t = dq.popleft()
                    tmp = max(tmp, time[t])
                    if len(d2[t]) :
                        for j in d2[t]:
                            dq.append(j)
                tres += tmp
            res = max(res, tres)
    print res

arr = [['a', 'b'], ['b', 'c'], ['b', 'd'], ['a', 'e'], ['e', 'f']]
test(arr)


