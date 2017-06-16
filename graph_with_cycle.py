def test(arr):
    if not arr : return False
    size = len(arr)
    if size == 0 : return False
    d = {}
    for i in arr:
        if i[0] in d:
            d[i[0]].append(i[1])
        else:
            d[i[0]] = [i[1]]
    stack = []
    se = set()
    for i in d.keys():
        helper(i, d, se, stack)
    print stack

def helper(node, d, se, stack):
    if node in se : return False
    se.add(node)
    if node in d:
        for i in d[node]:
            helper(i, d, se, stack)
    stack.append(node)

arr = [['a','b'], ['b','e'], ['c','d'], ['a', 'e'], ['c','d'], ['d', 'e'], ['e', 'f'], ['d','f']]
test(arr)



