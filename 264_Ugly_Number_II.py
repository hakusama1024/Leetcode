def Ugly_Number_II(n):
    if n < 1 : return 0
    if n == 1 : return 1
    arr = [1] * n
    a = b = c = 0
    for i in range(1, n):
        arr[i] = min(arr[a]*2, arr[b]*3, arr[c]*5)
        if arr[i] == arr[a]*2 : a +=1
        if arr[i] == arr[b]*3 : b +=1
        if arr[i] == arr[c]*5 : c +=1
    print arr[-1]


Ugly_Number_II(100)



