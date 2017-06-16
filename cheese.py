import collections
def test(arr):
    if not arr : return False
    m = len(arr)
    if m == 0 : return False
    n = len(arr[0])
    if n == 0 : return False
    dq = collections.deque()
    dq.append((0, 0))
    flag = True
    while dq and flag:
        flag = False
        size = len(dq)
        for _ in range(size):
            i, j = dq.popleft()
            if arr[i][j] == 'C' :
                print "cheese", i, j
                return True
            for a, b in [[0, 1], [1, 0]]:
                ii = i + a
                jj = j + b
                if ii < 0 or ii >= m or jj < 0 or jj >= n or arr[ii][jj] == 'X' : continue
                dq.append((ii, jj))
                flag = True
    return False

arr = [
        ['O', 'X', 'O', 'O', 'O', 'O'],
        ['O', 'X', 'X', 'X', 'O', 'O'],
        ['O', 'O', 'O', 'X', 'O', 'O'],
        ['O', 'X', 'O', 'X', 'O', 'O'],
        ['O', 'X', 'O', 'X', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'X', 'X'],
        ['O', 'O', 'X', 'O', 'O', 'C']
        ]
        

print test(arr)
                
