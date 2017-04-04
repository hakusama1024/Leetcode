def longestconsecutive(nums):
    size = len(nums)
    if size == 0 : return 0
    res = 0
    se = set(nums)
    re = []
    for i in nums:
        t = []
        if i-1 not in nums:
            j = i +1
            t.append(i)
            while j in nums:
                t.append(j)
                j+=1
            if j-i > res:
                re = t[:]

    print re
    print res


nums = [1, 23, 4, 5, 3, 6, 7, 9, 8, 5,10 ]

longestconsecutive(nums)
