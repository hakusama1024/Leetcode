def test(arr):
    size = len(arr)
    if size < 2 : return ""
    l = r = pair = 0
    res = []
    for i in range(size):
        if arr[i] == "(":
            l += 1
        elif arr[i] == ")" and l > r:
            r += 1
            pair += 1
    l = r = pair
    for i in range(size):
        if arr[i] == "(" and l > 0:
            res.append(arr[i]) 
            l -= 1
        elif arr[i] == ")" and r > l:
            res.append(arr[i]) 
            r -= 1
            pair -= 1
        if pair == 0 : break
    print "".join(res)


arr = "((()("
print arr
test(arr)




    

