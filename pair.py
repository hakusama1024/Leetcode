def test(s):
    size = len(s)
    if size == 0 : return ""
    res = ""
    pair = 0
    l = 0
    r = 0
    res = ""
    for c in s:
        if c == "(":
            l += 1
            res += c
        elif c == ")" and l > r:
            r += 1
            pair += 1
            res += c
    print pair

    l = pair
    r = pair
    res = ""
    for c in s:
        if c == "(" and l > 0:
            l -= 1
            res += c
        elif c == ")" and r > l:
            r -= 1
            res += c
            pair -= 1
        if pair == 0 : break
    print res 

s = "((((((())())((()))"

print s
test(s)




