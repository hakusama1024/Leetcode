def reverse_integer(n):
    if n <= 0 : return 0
    res = 0
    size = 1
    t = n
    while t>10:
        size *= 10
        t /= 10
    print n
    print size

reverse_integer(123456)
