class UF(object):
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.count = n

    def union(self, a, b):
        print "union : ", a, b
        root_a = self.find(a)
        root_b = self.find(b)
        if root_a != root_b:
            self.parent[root_a] = root_b
            self.count -= 1

    def find(self, a):
        print 'find : ', a
        if self.parent[a] == a:
            return self.parent[a]
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    

uf = UF(10)
print uf.find(9)
uf.union(1, 2)
print uf.parent
print uf.count
uf.union(1, 8)
print uf.parent
print uf.count
uf.union(2, 7)
print uf.parent
print uf.find(2)
print uf.count
uf.union(3, 7)
print uf.parent
print uf.count
