L = ['a', 'b', 'c', 'd', 's', 'g', 'e' , 'w']
word = "c??"
dic = set(['abc', 'cba', 'dsgs', 'dsgew', 'as cdd'])


def test(L, word, dic):
    res = []
    helper("", 0, L, word, dic, res)
    print res

def helper(cur, po, L, word, dic, res):
    if po == len(word):
        if cur in dic:
            res.append(cur)
        return 
    if word[po] != "?":
        helper(cur+word[po], po+1, L, word, dic, res)
    else:
        for s in L:
            helper(cur+s, po+1, L, word, dic, res)


test(L, word, dic)
