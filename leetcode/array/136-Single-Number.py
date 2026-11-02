class Solution(object):
    def singleNumber(self, nums):
        p = set(nums)
        q = [item for item in p if nums.count(item) == 1]
        return q[0]