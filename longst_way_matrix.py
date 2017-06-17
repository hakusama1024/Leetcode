def test(arr):
    if not arr : return 0
    m = len(arr)
    if m == 0 : return 0
    n = len(arr[0])
    if n == 0 : return 0
    visit = [[False]*n for i in range(m)]
    res = [[]]
    for i in range(m):
        for j in range(n):
            helper(i, j, visit, arr, [], res)
    print res
            

def helper(i, j, visit, arr, cur, res):
    if len(cur) > len(res[0]):
        res.pop()
        res.append(cur[:])
    if i < 0 or i >= len(visit) or j < 0 or j >= len(visit[0]) or visit[i][j] or (cur and cur[-1] <= arr[i][j]) : return
    for a, b in [[0, 1], [0, -1], [1, 0], [-1,0]]:
        visit[i][j] = True
        cur.append(arr[i][j])
        helper(i+a, j+b, visit, arr, cur, res)
        cur.pop()
        visit[i][j] = False 

arr = [
[1,2,4,5],
[3,4,5,8], 
[7,5,2,1],
[8,6,4,2]
]

test(arr)
