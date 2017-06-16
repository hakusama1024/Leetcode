def test(arr):
    size = len(arr)
    if size == 0 : return False
    l = 0
    r = 0 
    for i in range(size):
        if arr[i] == '(':
            l += 1
        elif arr[i] == ')':
            if l > r :
                r += 1
            else:
                print False
                return
    print l == r

arr = "()()()()"
arr = "(+1^$#)(#$)"
arr = ")("
arr = "(()#%33"


test(arr)



