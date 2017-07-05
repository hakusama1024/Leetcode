def test(arr):
    if not arr : return []
    size = len(arr)
    if size < 2 : return []
    t1 = t2 = (1<<31)-1
    for i in range(size):
        if arr[i] < t1:
            t1 = arr[i]
            if t1 < t2:
                t1, t2 = t2, t1

    print t1, t2
arr = [2, 5,1, 3,2 ,1, 5,3 ,6,9 , 3, 32, 6, 19]
test(arr)
            
