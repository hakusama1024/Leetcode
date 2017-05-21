import random
def test(m, n, k):
    if m == 0 or n == 0 or k > m*n : return
    arr = [[0] * n for _ in range(m)]
    while k > 0:
        print("here")
        a = random.randint(0, m-1)
        b = random.randint(0, n-1)
        if arr[a][b] == 1:
            continue
        else:
            arr[a][b] = 1
            k-=1

test(3, 5, 3)
