import collections
def test(s):
    size =  len(s)
    if size == 0 : return []
    dic = {"1":['a','b','c'], "2":['d','e','f'],"3":['g','h','i'],'4':['j','k','l'], '5':['m','n','o'],'6':['p','q','r'],'6':['s','t','u'],'7':['v','w','x'],8:['y','z']}
    dq = collections.deque()
    po = 0
    while po < size:
        if po == 0:
            for i in dic[s[po]]:
                dq.append([i])
        else:
            l = len(dq)
            for i in range(l):
                t = dq.popleft()
                for j in dic[s[po]]:
                    tmp = t[:]
                    tmp.append(j)
                    dq.append(tmp)
        po+=1
    print dq



def test1(s):
    res = []
    dic = {"1":['a','b','c'], "2":['d','e','f'],"3":['g','h','i'],'4':['j','k','l'], '5':['m','n','o'],'6':['p','q','r'],'6':['s','t','u'],'7':['v','w','x'],8:['y','z']}
    helper([], 0, s, dic, res)
    print res

def helper(cur, po, s, dic, res):
    if po == len(s) :
        res.append(cur)
        return
    for i in dic[s[po]]:
        helper(cur+[i], po+1, s, dic, res)







s = '123'
test1(s)









