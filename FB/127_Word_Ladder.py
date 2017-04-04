import collections

arr = ["hot","dot","dog","lot","log","cog"]

beginWord = "hit"
endWord = "cog"

def wordladder(beginWord, endWord, arr):
    dq = collections.deque()
    dic = set(arr)
    res = []
    helper(beginWord, 0, dic, [], endWord, res)
    print res

def helper(cur, po, dic, curlist, endWord, res):
    if cur == endWord:
        res.append(curlist)
        return
    for i in range(len(cur)):
        l = cur[:i]
        r = cur[i+1:]
        for j in "abcdefghijklmnopqrstuz":
            if cur[i] != j:
                new = l + j + r
                if new in dic:
                    dic.remove(new)
                    helper(new, po+1, dic, curlist+[new], endWord, res)

wordladder(beginWord, endWord, arr)
