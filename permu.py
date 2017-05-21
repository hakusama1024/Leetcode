def test(arr):
    size = len(arr)
    if size == 0 : return arr
    res = []
    helper(0, arr, res)
    print(res)
    print(len(res))


def helper(po, cur, res):
    if po == len(cur):
        res.append(cur[:])
        return
    for i in range(po, len(cur)):
        cur[po], cur[i] = cur[i], cur[po] 
        helper(po+1, cur, res)


def test2(arr):
    size = len(arr)
    if size == 0 : return []
    res = []
    arr.sort()
    helper2(0, arr, res)
    print(res)
    print(len(res))

def helper2(po, cur, res):
    if po == len(cur)-1:
        res.append(cur[:])
        return
    for i in range(po, len(cur)):
        if i != po and arr[i] == arr[i-1]: continue
        cur[po], cur[i] = cur[i], cur[po] 
        helper2(po+1, cur, res)
        cur[po], cur[i] = cur[i], cur[po] 

def permuteUnique(nums):
    res = []
    nums.sort()
    size = len(nums)
    helper3(0, nums, res)
    print(len(res))
    print(res)
    return res
    
    
def check(start, index, nums):
    for j in range(start, index):
        if nums[j] == nums[index] : return False
    return True
    
def helper3(start, nums, res):
    if start == len(nums)-1:
        res.append(nums[:])
        return
    for i in range(start, len(nums)):
        if check(start, i, nums):
            nums[i], nums[start] = nums[start], nums[i]
            helper3(start+1, nums, res)
            nums[i], nums[start] = nums[start], nums[i]



arr = [1, 2, 2, 4]

test2(arr)

#class Solution {
#public:
#    void recursion(vector<int> num, int i, int j, vector<vector<int> > &res) {
#        if (i == j-1) {
#            res.push_back(num);
#            return;
#        }
#        for (int k = i; k < j; k++) {
#            if (i != k && num[i] == num[k]) continue;
#            swap(num[i], num[k]);
#            recursion(num, i+1, j, res);
#        }
#    }
#
#    vector<vector<int> > permuteUnique(vector<int> &num) {
#        sort(num.begin(), num.end());
#        vector<vector<int> >res;
#        recursion(num, 0, num.size(), res);
#        return res;
#    }
#};
#




