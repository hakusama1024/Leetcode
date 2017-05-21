class RandomNode(object):
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None

def copyrandomlist(root):
    if not root : return root
    tmp = root
    while tmp:
        node = RandomNode(tmp.val)
        node.next = tmp.next
        tmp.next = node
        tmp = tmp.next.next

    tmp = root
    while tmp:
        if tmp.random:
            tmp.next.random = tmp.random.next
        tmp = tmp.next.next
        




    dum = RandomNode(0)
    d = dum
    tmp = root
    while tmp:
        d.next = tmp.next
        tmp.next = tmp.next.next
        tmp = tmp.next
        d= d.next

    tmp = dum.next
    while tmp:
        print tmp.val
        tmp = tmp.next
        




root = RandomNode(1)
root.next = RandomNode(2)
root.next.next = RandomNode(3)
root.next.next.next = RandomNode(4)

copyrandomlist(root)

