import random

class RandomShuffle(object):
    def __init__(self, nums):
        self.nums = nums

    def reset(self):
        return self.nums
    
    def shuffle(self):
        arr = self.nums[:]
        size = len(arr)
        for i in range(size):
            po = random.randrange(0, i+1)
            arr[i], arr[po] = arr[po], arr[i]
        return arr



nums = [1, 2,3 ,4]

shu = RandomShuffle(nums)
print shu.shuffle()
print shu.shuffle()
print shu.shuffle()
print shu.reset()
