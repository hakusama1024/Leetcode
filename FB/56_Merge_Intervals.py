
def mergeinterval(arr):
    size = len(arr)
    if size == 0 : return arr
    arr.sort(key=lambda x:(x[0], x[1]))
    res = []
    res.append(arr[0])
    for i in range(1, size):
        if arr[i][0] <= res[-1][1]:
            t = res.pop()
            res.append([t[0], max(t[1], arr[i][1])])
        else:
            res.append(arr[i])
    print res


arr = [[1,3],[2,6],[8,10],[15,18]]

mergeinterval(arr)







