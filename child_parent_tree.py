import collections

arr = [
[15, 20, True],
[19, 80, True],
[17, 20, False],
[16, 80, False],
[80, 50, False],
[50, None, False], 
[20, 50, True],
]

#child, parent, left

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def test(arr):
    size = len(arr)
    if size == 0 : return None
    d = {}
    root = None
    for i in range(size):
        myself = d.get(arr[i][0])
        if not myself:
            myself = Node(arr[i][0])
            d[arr[i][0]] = myself 

        if arr[i][1]:
            parent = d.get(arr[i][1])
            if not parent:
                parent = Node(arr[i][1])
                d[arr[i][1]] = parent
            if arr[i][2]:
                d[arr[i][1]].left = myself 
            else:
                d[arr[i][1]].right = myself 
        else:
            root = myself

    dq = collections.deque()
    dq.append(root)
    while dq:
        s = len(dq)
        l = []
        for _ in range(s):
            t = dq.popleft()
            l.append(t.val)
            if t.left : dq.append(t.left)
            if t.right : dq.append(t.right)
        print l

test(arr)





