import collections


def test(s):
    size = len(s)
    if size == 0 : return ''
    l = s.split()
    d = collections.Counter(l)
    for i in l:
        if d[i] > 1 : 
            print i
            return

s = "python java java python"

test(s)
