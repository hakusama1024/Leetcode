def test(nums):
    size = len(nums)
    if size == 0 : return nums 
    i = 0
    while i < size:
        if nums[i]-1 != i:
            index = nums[i]-1
            if size > index >= 0 : 
                nums[i], nums[index] = nums[index], nums[i]
            else:
                i += 1
        else:
            i += 1
    print arr
    for i in range(size):
        if nums[i] != i + 1:
            return i + 1
    return -1


arr = [-1, 3, 2, 1]

print test(arr)
