class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Iter(object):
    def __init__(self, root):
        self.stack = []
        self.findleft(root)

    def findleft(self, node):
        t = node
        while t:
            self.stack.append(t)
            t = t.left
    def hasNext(self):
        return len(self.stack) != 0

    def next(self):
        if self.hasNext():
            t = self.stack.pop()
            v = t.val
            if t.right:
                self.findleft(t.right)
            return v
        else:
            return None



def test(root1, root2):
    a = Iter(root1)
    b = Iter(root2)

    one = None
    two = None
    while a.hasNext() or b.hasNext():
        if not one and a.hasNext():
            one = a.next()
        if not two and b.hasNext():
            two = b.next()
        if one and two:
            if one< two:
                print one
                one = None
            else:
                print two
                two = None
        else:
            if one:
                print one
                one = None
            else:
                print two
                two = None



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


test(root, root1)



