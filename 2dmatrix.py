def test(arr):
    m = len(arr)
    if m == 0 : return 0
    n = len(arr[0])
    m -= 1
    while m >= 0 and n >=0 :
        if arr[m][n-1] == 0:
            m -= 1
        else:
            if n-1 >= 0 and arr[m][n-1] == 1:
                n -= 1
            else:
                m -= 1

    if n == len(arr[0]) : return 0
    return len(arr[0]) - n 
arr = [
       # [1, 1, 1, 1],
        [0, 0, 0, 1], 
       # [0, 1, 1, 1],
       # [0, 1, 1, 1],
       # [0, 0, 0, 0]
      ]


print test(arr)
