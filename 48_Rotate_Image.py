def rotate(arr):
    m = len(arr)
    if m == 0 : return 
    n = len(arr[0])
    for i in range(m/2):
        arr[i], arr[m-1-i] = arr[m-1-i], arr[i]

    for i in range(m):
        for j in range(i+1, n):
            arr[i][j], arr[j][i] = arr[j][i], arr[i][j]


arr = 

