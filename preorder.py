class Node(object):
    def __init__(self, val):
        self.val = val 
        self.left = None
        self.right = None

def preorder(root):
    if not root : return []
    res = []
    stack = []
    while root:
        res.append(root.val)
        if root.right:
            stack.append(root.right)
        root = root.left
        if not root and stack:
            root = stack.pop()
    print res

root = Node(5)
root.left = Node(3)
root.left.left = Node(1)
root.left.right = Node(4)
root.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(9)

preorder(root)

