def letterCombinations(digits):
    size = len(digits)
    if size == 0 : return []
    res = []
    dic = {'2':['a', 'b', 'c'], '3':['d', 'e', 'f'], '4':['g', 'h', 'i'], '5':['j','k','l'], '6':['m','n','o'], '7':['p','q','r','s'], '8':['t','u','v'], '9':['w','x','y','z']}
    helper(digits, 0, "", dic, res)
    print res

def helper(digits, po, cur, dic, res):
    if po == len(digits) : 
        res.append(cur)
        return
    for i in dic[digits[po]]:
        helper(digits, po+1, cur+i, dic, res)

letterCombinations("23")
