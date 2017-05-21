def test(s):
    size = len(s)
    if size == 0 : return []
    dic = {'1':'abc', '2':'def', '3':'ghi', '4':'jkl', '5':'mno', '6':'pqr', '7':'stu', '8':'vwx','9':'yz'}
    res = []
    helper(s, 0, [], dic, res)
    print res

def helper(s, po, cur, dic, res):
    if po ==  len(s) : 
        res.append(''.join(cur))
        return
    for i in dic[s[po]]:
        helper(s, po+1, cur+[i], dic, res)


test('1234')
