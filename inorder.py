import heapq
class Heap(object):
    def __init__(self):
        self.l = []
    def push(self, a):
        heapq.heappush(self.l, a)

    def pop(self):
        return heapq.heappop(self.l)
    def printheap(self):
        print self.l


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None
    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            t = self.root
            self._insert(t, val)

    def _insert(self, t, val):
        if val[1] < t.val[1]:
            if t.left:
                self._insert(t.left, val)
            else:
                t.left = Node(val)
        else:
            if t.right:
                self._insert(t.right, val)
            else:
                t.right = Node(val)
    def getroot(self):
        return self.root

def test(arr):
    size = len(arr)
    if size == 0 : return None
    newarr = []
    for i in range(size):
        newarr.append((arr[i], i))

    hp = Heap()
    for i in newarr:
        hp.push(i)


    t = Tree()
    for i in range(size):
        val = hp.pop()
        t.insert(val)
    traver(t.getroot())

def traver(node):
    stack = []
    while node or stack:
        while node:
            stack.append(node)
            node = node.left
        if stack: 
            node = stack.pop()
            print node.val[0]
            if node.right:
                stack.append(node.right)
            node = None




    

arr = [4, 5, 2, 1, 3]
test(arr)





