def read(buf, n):
    count = 0
    buf4 = [""] * 4
    while count < n:
        t = read4(buf4)
        rem = n - count
        t = min(t, rem)
        for i in range(t):
            buf[count] = buf4[i]
            count += 1
        if t < 4 : break
    return count

