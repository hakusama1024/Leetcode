'''
recursive
'''

def lowestCommonAncestor(root, p, q):
    if p.val < root.val and q.val < root.val:
        lowestCommonAncestor(root.left, p, q)
    if p.val > root.val and q.val > root.val:
        lowestCommonAncestor(root.right, p, q)
    return root

'''
iterative
'''

#def lowestCommonAncestor(root, p, q):
#    cur = root
#    while 1:
#        if p.val < cur.val and q.val < cur.val:
#            cur = cur.left
#        elif p.val > cur.val and q.val > cur.val:
#            cur = cur.right
#        else:
#            return cur
