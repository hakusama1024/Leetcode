class Node(object):
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

class Iter(object):
    def __init__(self, root):
        self.stack = []
        self.findleft(root)

    def hasNext(self):
        if len(self.stack) == 0 :
            return False
        return True

    def next(self):
        node = self.stack.pop()
        if node.right:
            self.findleft(node.right)
        return node.val

    def findleft(self, node):
        t = node
        while t:
            self.stack.append(t)
            t = t.left


root = Node(6)
root.left = Node(4)
root.left.left = Node(3)
root.left.left.left = Node(2)
root.left.left.left.left = Node(1)
root.left.right = Node(5)
root.right = Node(8)
root.right.right = Node(9)
root.right.left = Node(7)

root1 = Node(9)
root1.left = Node(7)
root1.left.left = Node(6)
root1.left.left.left = Node(5)
root1.left.left.left.left = Node(4)
root1.left.right = Node(8)
root1.right = Node(11)
root1.right.right = Node(12)
root1.right.left = Node(10)



a = Iter(root)
b = Iter(root1)
t1 = None
t2 = None
while a.hasNext() or b.hasNext():
    if not t1 and a.hasNext():
        t1 = a.next()
    if not t2 and b.hasNext():
        t2 = b.next()
    if t1 and t2:
        if t1 < t2:
            print t1
            t1 = None
        else:
            print t2
            t2 = None
    else:
        if t1: 
            print t1
            t1 = None
        else:
            print t2
            t2 = None








