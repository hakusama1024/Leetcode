import collections
import heapq
class Heap(object):
    def __init__(self):
        self.l = []

    def push(self, item):
        if item:
            heapq.heappush(self.l, item)

    def pop(self):
        if self.l:
            return heapq.heappop(self.l)
        return -1

    def peek(self):
        if self.l:
            return self.l[0]
        return -1

    def size(self):
        return len(self.l)



def test(s, k):
    size = len(s)
    if size == 0 : return ""
    hp = Heap()
    counter = collections.Counter(s)
    for k in counter:
        hp.push((-counter[k], k))
    res = ""

    print hp.peek()
    while hp.size()!= 0:
        count = hp.peek()[0]
        t = []
        while count == hp.peek()[0]:
            t.append(hp.pop())
        print t
        for i in t:
            length = len(res)
            tmpl = min(k, length)
            if i[1] not in res[length-tmpl:]:
                res += i[1]
            if i[0] +1 < 0:
                hp.push((i[0]+1, i[1]))
        print res

       
s = "AABBBCA"
k = 3

test(s, k)


