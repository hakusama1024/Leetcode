def test(s, k):
    if not s : return s
    size = len(s)
    if size < k : return s
    s = list(s)
    po = 0
    print ''.join(s)
    while po < size:
        if po + k < size:
            for i in range(k/2):
                s[po+i],s[po+k-i-1] = s[po+k-i-1], s[po+i]
            if po + 2*k < size:
                po += 2*k
            else:
                break
        else:
            for i in range((size-po)/2):
                s[po+i],s[size-i-1] = s[size-i-1], s[po+i]
            break

    print ''.join(s)



s = "1234567890" 
k = 4#, output 
print k
test(s, k)
