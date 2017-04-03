def threesum(nums):
    size = len(arr)
    if size < 3 : return []
    nums.sort()
    res = []
    for i in range(size-2):
        if i > 0 and nums[i] == nums[i-1] : continue
        tar = -nums[i]
        l = i+1
        r = size-1
        while l < r:
            if nums[l] + nums[r] == tar:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif nums[l] + nums[r] < tar:
                l += 1
            else:
                r -= 1
    print res
    return res




arr = [-1,0,1,2,-1,-4]

threesum(arr)
