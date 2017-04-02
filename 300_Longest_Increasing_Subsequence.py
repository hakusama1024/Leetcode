 #!/usr/bin/python
  # -*- coding: utf-8 -*-

def max_lengthOfLIS( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    size = len(nums)
    if size == 0 : return 0
    res = 0
    dp = [[1] * size]
    dp.append([[nums[i]] for i in range(size)])
    print dp
    for i in range(1,size):
        t = 0 
        for j in range(i):
            if nums[i] > nums[j]:
                if t < dp[0][j]:
                    t = dp[0][j]
                    dp[1][i] = dp[1][j] + [nums[i]]
        dp[0][i] = t + 1
        res = max(res, dp[0][i])
    print res
    print dp


'''
如果只是求连续Longest Increasing Subsequence的最大长度那么每次回头查时。先看当前i指向的值是不是比指针j的值大.
如果True，就看dp数组这个位置上的值。更新t。
j循环结束后。更新dp[i]的值为t+1。意思就是在i数之前已经有t个长度的序列。现在就再加上1。
然后更新res的值。这样就找到长度最大。
但是如果找的是sum最大。dp里保存的值就要换成sum。

'''
def max_sum_OfLIS( nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    size = len(nums)
    if size == 0 : return 0
    res = 0
    dp = [nums[:]]
    dp.append([[nums[i]] for i in range(size)])
    for i in range(1,size):
        t = -(1<<31) 
        for j in range(i):
            if nums[i] > nums[j]:
                if t < dp[0][j]:
                    t = dp[0][j]
                    dp[1][i] = dp[1][j] + [nums[i]]

        dp[0][i] = max(t + nums[i], nums[i]) 
        res = max(res, dp[0][i])
    print res
    print dp

#a = [10,9,2,5,3,7,101,18, 20]
a = [1, -4, 3, -2, 4]

max_sum_OfLIS(a)
#max_lengthOfLIS(a)

'''
如果还需要返回使用的数组成的数组就需要在dp再加一维。当更新t时候更新dp[1]相应的位置。
'''

