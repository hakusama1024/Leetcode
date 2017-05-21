mi = (1<<31) -1

def test(nums):
    size = len(nums)
    if size == 0 : return 0
    helper(0, 0, 0, nums)
    print mi



def helper(po, step, rem, nums):
    print po, step, rem
    global mi
    if po == len(nums)-1:
        mi = min(mi, step)
        print mi
        return
    ma = max(nums[po], rem)
    for i in range(1, ma+1):
        if po+i <= len(nums):
            helper(po+i, step+1, ma-i, nums)

nums = [2,3,1,1,4]
test(nums)
