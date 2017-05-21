import collections

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def test(root):
    if not root : return []
    res = []
    helper([root.val], root, res) 
    print res

def helper(cur, node, res):
    if not node.left and not node.right : 
        res.append(cur)
        return
    if node.left:
        helper(cur+[node.left.val], node.left, res)
    if node.right:
        helper(cur+[node.right.val], node.right, res)

def iterativea(root):
    if not root : return []
    res = []
    dq = collections.deque()
    dq.append([root])
    while dq:
        size = len(dq)
        for i in range(size):
            t = dq.popleft()
            tmpnode = t[-1]
            if not tmpnode.left and not tmpnode.right:
                res.append(t[:])
                continue
            if tmpnode.left:
                dq.append(t+[tmpnode.left])
            if tmpnode.right:
                dq.append(t+[tmpnode.right])
    print res

    resu = []
    for i in res:
        t = []
        print i
        for j in i:
            t.append(j.val)
        resu.append(t)

    print resu





root = Node(6)
root.left = Node(3)
root.left.left = Node(2)
root.left.left.left = Node(1)
root.left.rihgt  = Node(4)
root.right = Node(9)
root.right.left = Node(7)
root.right.right = Node(10)

test(root)


iterativea(root)



