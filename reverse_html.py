def test(s):
    size = len(s)
    if size == 0 : return ''
    res = []
    l = 0
    for i in range(size):
        if s[i] == '&':
            res.append(r(s[l:i]))
            l = i
        elif s[i] == ';':
            res.append(s[l:i+1])
            l = i+1
        if i == size-1 and l < i:
            res.append(r(s[l:i+1]))
    print res
    
    res = res[::-1]
    res = ''.join(res)
    print res


def r(ss):
    l = list(ss)
    size = len(l)
    for i in range(size/2):
        l[i], l[size-1-i] = l[size-1-i], l[i]
    s = ''.join(l)
    return s


#"1234&euro;" => &euro;4321"
#"1234&euro" => "orue&4321"
#"1234&euro;567" => "765&euro;4321"
s = "1234&euro;"
s = "1234&euro;567"
s = "1234&euro"
test(s)

