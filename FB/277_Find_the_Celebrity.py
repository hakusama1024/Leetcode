def find(n):
    if n == 0 : return -1
    can = 0
    for i in range(1, n):
        if knows(can, i):
            can = i

    for i in range(n):
        if i != can:
            if knows(can, i) or not knows(i, can):
                return -1
    return can
