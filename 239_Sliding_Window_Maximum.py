import collections as c
def Sliding_Window_Maximum(nums, k):
    size = len(nums)
    if size == 0 : return []
    res = []
    dq = c.deque()
    for i in range(size):
        if dq and dq[0] == i-k : dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k-1 : res.append(nums[dq[0]])
    print res

nums = [1,3,-1,-3,5,3,6,7]
k = 3



print nums
Sliding_Window_Maximum(nums, k)
