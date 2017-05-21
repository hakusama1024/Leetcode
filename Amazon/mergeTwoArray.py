def test(A, B):
    lena = len(A)
    lenb = len(B)
    a = 0
    b = 0
    while a < lena and b < lenb:
        print A, B
        if A[a] > B[b] :
            A[a], B[b] = B[b], A[a]
            t = b
            while t+1 < lenb and B[t] > B[t+1] : 
                B[t], B[t+1] = B[t+1], B[t]
                t+= 1
        a += 1

    print A
    print B

A = [1, 2, 5, 9, 20, 30]
B = [3, 4, 6, 10]

test(A, B)

