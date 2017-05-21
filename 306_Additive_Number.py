def Additive_Number(s):
    size = len(s)
    if size < 2 : return False
    for i in range(size-2):
        for j in range(i+1, size-1):
            print int(s[:i+1]), int(s[i+1:j+1])





s = "199100199"
Additive_Number(s)

