def test(root):
    if not root or not root.left and not root.right: return None
    mi = (1<<31)-1
    while root and root.left and root.right:
        if root.val == root.left.val:
            mi = min(mi, root.right.val)
            root = root.left
        else:
            mi = min(mi, root.left.val)
            root = root.right

    return mi


