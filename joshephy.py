from collections import deque
def test(arr, k):
    dq = deque()
    for i in arr:
        dq.append(i)

    while dq:
        for i in range(k):
            dq.append(dq.popleft())
        print dq.popleft()

arr = [1, 2, 3,4 , 5, 6, 7, 8, 9]
test(arr, 3)

