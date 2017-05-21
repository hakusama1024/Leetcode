def test(arr1, arr2):
    m = len(arr1)
    n = len(arr2)
    if m == 0 or n == 0 : return 0
    arr = [[0] * (n+1) for i in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if arr1[i-1] == arr2[j-1]:
                arr[i][j] = arr[i-1][j-1] + 1
            else:
                arr[i][j] = max(arr[i-1][j], arr[i][j-1])

    print arr[m][n]

arr1 = "xinbaihahahaha"
arr2 = "fdsafdsaibha12321"

test(arr1, arr2)



