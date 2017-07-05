def test(arr):
    if not arr : return
    m = len(arr)
    if m == 0 : return 
    n = len(arr[0]) 
    if n == 0 : return

    i = j = 0
    index = 0
    res = [0] * (m*n)
    for su in range(m+n-1):
        if su%2:
            j = min(su, n-1)
            i = su - j
            print i, j
            while j >= 0 and i < m:
                res[index] = arr[i][j]
                i += 1
                j -= 1
                index += 1
        else:
            i = min(su, m-1)
            j = su - i
            print i, j
            while i >= 0 and j < n:
                res[index] = arr[i][j]
                i -= 1
                j += 1
                index += 1

    print res


arr = [[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
[13, 14, 15, 16],
[17, 18, 19, 20]]

test(arr)

