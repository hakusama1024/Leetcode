def addbinary(a, b):
    sizea = len(a)
    sizeb = len(b)
    if sizea == 0 : return b
    if sizeb == 0 : return a
    car = 0
    res = ""
    while sizea > 0 or sizeb > 0 or car:
        ta = 0
        tb = 0
        if sizea > 0 : 
            ta = int(a[sizea-1])
            sizea -= 1
        if sizeb > 0 : 
            tb = int(b[sizeb-1])
            sizeb -= 1
        res = str((ta + tb + car) % 2) + res
        car = (ta + tb + car) / 2

    print res
    return res

a = "11"
b = "1"

addbinary(a, b)

        
