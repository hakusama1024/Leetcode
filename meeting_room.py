from heapq import *
def test(arr):
    if not arr : return []
    size = len(arr)
    res = []
    l = []
    for i in arr:
        l.append((i[0], 0, i))
        l.append((i[1],1, i))
    l.sort(key=lambda x: x[0])

    d = {}
    roommap = {}
    hp = []
    room = 1
    for i in l:
        if i[1] == 0 :
            if not hp:
                n = room
                room += 1
                d[n] = [i[2]]
            else:
                n = heappop(hp)
                d[n].append(i[2])
            roommap[','.join([str(j) for j in i[2]])] = n 
        else:
            n = roommap[','.join([str(j) for j in i[2]])]
            heappush(hp, n)

    res = []
    ma = 0
    count = 0
    sta = 0
    for i in l:
        if i[1] == 0:
            count += 1
            if ma == count:
                sta = i[2][0]
            elif count > ma:
                res = []
                sta = i[2][0]
                ma = count
        else:
            count -= 1
            if count+1 == ma:
                res.append((ma, sta, i[2][1]))

    print "most", res

    a = d.keys()
    a.sort()
    for i in a:
        print i, d[i]









arr = [[3, 5], [5, 7], [2, 5], [3, 4], [2, 7], [1, 9], [6, 7], [5, 8]]
test(arr)

