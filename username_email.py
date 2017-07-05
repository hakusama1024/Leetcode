arr = {'a1' : ['a1@gmail.com', 'a2@gmail.com'], 
       'a2' : ['b1@gmail.com', 'a2@gmail.com'], 
       'a3' : ['c1@gmail.com'], 
       'a4' : ['c1@gmail.com', 'd1@gmail.com'],
       'a5' : ['b1@gmail.com','b1@gmail.com']
      }

class UF(object):
    def __init__(self, arr):
        self.dic = {}
        for i in arr.keys():
            self.dic[i] = i

    def find(self, a):
        if self.dic[a] == a : return a
        self.dic[a] = self.find(self.dic[a])
        return self.dic[a]

    def union(self, a, b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a != parent_b:
            self.dic[parent_a] = parent_b

def test(arr):
    d = {}
    for i in arr:
        for j in arr[i]:
            if j in d:
                d[j].add(i)
            else:
                d[j] = set()
                d[j].add(i)

    uf = UF(arr)


    for i in d:
        if len(d[i]) <= 1 : continue
        l = list(d[i])
        for j in range(1, len(l)):
            uf.union(l[0], l[j])

    resd = {}
    for i in uf.dic:
        if uf.dic[i] not in resd:
            resd[uf.dic[i]] = [i]
        else:
            resd[uf.dic[i]].append(i)

    print resd.values()

            





test(arr)

