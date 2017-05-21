def test(arr):
    size = len(arr)
    if size == 0 : return 0
    res = 0
    dic  = {}
    for i in range(size):
        dic[i] = {}
        for j in range(i):
            diff = arr[i]  - arr[j]
            c1 = dic[i].get(diff) or 1
            c2 = dic[j].get(diff) or 1
            l = max(c2+1, c1)
            res = max(res, l)
            dic[i][diff] = l
    print res 

arr =  [1, 3, 9, 5, 7, 21, 4, 4, 21, 2,3, 5,4, 6, 3,2, 1, 13, 3, 6,4, 5, 2,4, 13]
test(arr)
