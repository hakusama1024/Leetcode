from collections import deque

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST(object):
    def __init__(self):
        self.root = None

    def insert(self, val):
        if not self.root:
            self.root = Node(val)
        else:
            t = self.root
            self._insert(t, val)

    def _insert(self, t, val):
        if t.val < val:
            if t.right : self._insert(t.right, val)
            else: t.right = Node(val)
        else:
            if t.left : self._insert(t.left, val)
            else: t.left = Node(val)
    def preoder(self):
        t = self.root
        stack = [t]
        res = []
        while stack:
            node = stack.pop()
            res.append(node.val)
            if node.right : stack.append(node.right)
            if node.left : stack.append(node.left)
        print res
        return res

    def findrange(self, start, end):
        if start > end : return
        res = []
        stack = []
        t = self.root
        while stack or t:
            while t:
                if end >= t.val >= start:
                    stack.append(t)
                t = t.left
            if stack:
                t = stack.pop()
                res.append(t.val)
                t = t.right
        print res

    def inorder(self):
        t = self.root
        stack = [] 
        res = []
        while stack or t:
            while t : 
                stack.append(t)
                t = t.left
            t = stack.pop()
            res.append(t.val)
            t = t.right
        print res

    def levelprint(self):
        dq = deque()
        t = self.root
        dq.append(t)
        while dq:
            size = len(dq)
            t = []
            for _ in range(size):
                tmp = dq.popleft()
                t.append(tmp.val)
                if tmp.left : dq.append(tmp.left)
                if tmp.right : dq.append(tmp.right)
            print t

    def inorder_from_preorder(self):
        arr = self.preoder()
        stack = []
        res = []
        for i in range(len(arr)):
            if not stack or stack[-1] > arr[i]:
                stack.append(arr[i])
                continue
            else:
                while stack and stack[-1] < arr[i]:
                    res.append(stack.pop())
                stack.append(arr[i])
        while stack : res.append(stack.pop())
        print res

    def construct_tree_from_preorder(self):
        arr = self.preoder()
        if not arr or len(arr) == 0 : return None


    def _construct_tree_from_preorder(self, node, arr, index):
        pass

        

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(1)
bst.insert(5)
bst.insert(6)
bst.insert(9)
bst.insert(3)
bst.insert(7)

#bst.levelprint()

#bst.preoder()
bst.inorder()
bst.findrange(2, 9)

#bst.inorder_from_preorder()


def serialize(node):
    res = [] 
    def se(node):
        if not node : 
            res.append('#')
            return
        res.append(str(node.val))
        se(node.left)
        se(node.right)
    se(node)
    print res



    serialize.index = 0
    def build():
        if serialize.index < len(res):
            if res[serialize.index] == '#' : 
                serialize.index += 1
                return None
            node = Node(int(res[serialize.index]))
            serialize.index += 1
            node.left = build()
            node.right = build()
            return node

    t = build()
    dq = deque()
    dq.append(t)
    while dq:
        size = len(dq)
        tmp = []
        for _ in range(size):
            no = dq.popleft()
            tmp.append(no.val)
            if no.left : dq.append(no.left)
            if no.right : dq.append(no.right)
        print tmp

    
def serial(node):
    if not node : return '{}'
    res = [node]
    index = 0
    while index < len(res):
        if res[index]:
            res.append(res[index].left)
            res.append(res[index].right)
        index += 1
    while res[-1] == None:
        res.pop()

    ret = '{%s}' % ','.join([str(node.val) if node is not None else '#'
                                      for node in res])

    print ret








t = bst.root
#serialize(t)
serial(t)



