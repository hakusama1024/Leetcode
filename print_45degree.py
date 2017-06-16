def printDiag(M):
    m = len(M)
    n = len(M[0])
    i, j = m - 1, 0
    while j < n:
        k, l = i, j
        while k < m and l < n:
            print(M[k][l], end=" ")
            l += 1
            k += 1
        if i > 0:
            i -= 1
        else:
            j += 1
        print("")
# Test
A = [[1, 2, 3, 4],
     [5, 6, 7, 8],
     [9,10,11,12]]

printDiag(A)
