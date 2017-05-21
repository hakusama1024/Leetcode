def rangesum(matrix, r1, c1, r2, c2):
    m = len(matrix)
    if m == 0 : return 0
    n = len(matrix[0])

    for i in range(1, m):
        matrix[i][0] += matrix[i-1][0]

    for i in range(1, n):
        matrix[0][i] += matrix[0][i-1]

    for i in range(1, m):
        for j in range(1, n):
            matrix[i][j] = matrix[i][j] + matrix[i-1][j] + matrix[i][j-1] - matrix[i-1][j-1]




    

matrix = [
          [3, 0, 1, 4, 2],
          [5, 6, 3, 2, 1],
          [1, 2, 0, 1, 5],
          [4, 1, 0, 1, 7],
          [1, 0, 3, 0, 5]
         ]


rangesum(matrix, 0, 0, 0, 0)



