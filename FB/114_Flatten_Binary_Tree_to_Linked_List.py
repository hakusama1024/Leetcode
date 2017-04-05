def flatbinarytreetolinkedlist(root):
    if not root : return
    now = root
    while now:
        if now.left:
            pre = now.left
            while pre.right:
                pre = pre.right
            pre.right = now.right
            now.right = now.left
            now.left = None
        now = now.right


pre = None
def flatbinarytreetolinkedlist(root):
    if not root : return root
    flatbinarytreetolinkedlist(root.right)
    flatbinarytreetolinkedlist(root.left)
    root.right = pre
    root.left = None
    pre = root

