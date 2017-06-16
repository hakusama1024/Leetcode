class BIT(object):
    def __init__(self, arr):
        self.tree = (len(arr)+1) * [0]
        for i in range(len(arr)):
            self.update(i, arr[i])
        print self.tree

    def update(self, i, val):
        i += 1
        while i < len(self.tree):
            self.tree[i] += val
            i += i & (-i)

    def geSum(self, i):
        s = 0
        i += 1
        while i:
            s += self.tree[i]
            i -= i & (-i)
        return s

arr = [2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9]
print arr
bit = BIT(arr)
print bit.geSum(4)




