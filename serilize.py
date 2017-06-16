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
        if not self.root : self.root = Node(val)
        else : 
            t = self.root
            self._insert(t, val)

    def _insert(self, node, val):
        if node.val > val:
            if node.left : self._insert(node.left, val)
            else : node.left = Node(val)
        else:
            if node.right : self._insert(node.right, val)
            else : node.right = Node(val)

    def pre(self):
        t = self.root
        stack = [t]
        res = []
        while stack:
            node = stack.pop()
            if node : 
                res.append(str(node.val))
                if node.right : stack.append(node.right)
                else : stack.append(None)
                if node.left : stack.append(node.left)
                else : stack.append(None)
            else:
                res.append('#')
        return res

    def level(self, node=None):
        if node : t = node
        else : t = self.root
        dq = deque()
        dq.append(t)
        while dq:
            size = len(dq)
            tmp = []
            for _ in range(size):
                t = dq.popleft()
                tmp.append(t.val)
                if t.left : dq.append(t.left)
                if t.right : dq.append(t.right)
            print tmp


    def build(self, arr):
        arr = arr[::-1]
        def helper(arr):
            if arr:
                t = arr.pop()
                if t == '#' : return None
                else : 
                    node = Node(int(t))
                    node.left = helper(arr)
                    node.right = helper(arr)
                return node
        root = helper(arr)
        
        self.level(root)

    def build_index(self, arr):
        arr = arr[::-1]
        self.index = 0
        def helper(arr):
            if self.index < len(arr):
                t = arr[self.index]
                self.index += 1
                if t == '#' : return None
                else : 
                    node = Node(int(t))
                    node.left = helper(arr)
                    node.right = helper(arr)
                return node
        root = helper(arr)
        
        self.level(root)

bst = BST()
bst.insert(4)
bst.insert(2)
bst.insert(1)
bst.insert(3)
bst.insert(6)
bst.insert(7)
bst.insert(5)

arr = bst.pre()
bst.level()

bst.build(arr)
bst.build_index(arr)
