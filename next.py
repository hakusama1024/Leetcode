def next(s):
    size = len(s)
    if size == 0 : return s
    res = list(s)
    left = 0
    right = size-1

    print(res)
    for i in range(size-1, 0, -1):
       if res[i-1] < res[i]:
           left = i-1
           break
    for i in range(size-1, left, -1):
        if res[i] > res[left]:
            right = i
            break
    res[left], res[right] = res[right], res[left]
    right = size-1
    left += 1 
    if left != right:
        for i in range(int((right-left)/2)):
            res[left+i], res[right-i] = res[right-i], res[left+i]

    print(res)

s = "1325678943"

print(s)
next(s)
    

        

