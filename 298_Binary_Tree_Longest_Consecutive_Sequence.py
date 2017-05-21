class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def Binary_Tree_Longest_Consecutive_Sequence(root):
    if not root : return 0
    print helper(0, root, root.val, 0)


def helper(cur, node, target, ma):
    if not node : return ma 
    print node.val, target
    if node.val == target:
        cur += 1
    else: cur = 1
    ma = max(ma, cur)
    return max(helper(cur, node.left, node.val+1, ma), helper(cur, node.right, node.val, ma))




root = Node(1)
root.right = Node(3)
root.right.left = Node(2)
root.right.right = Node(4)
root.right.right.right = Node(5)

#
#dp = [root]
#while dp:
#    size = len(dp)
#    tmp = []
#    for i in range(size):
#        t = dp.pop(0)
#        tmp.append(t.val)
#        if t.left: dp.append(t.left)
#        if t.right: dp.append(t.right)
#    print tmp
#        

Binary_Tree_Longest_Consecutive_Sequence(root)






