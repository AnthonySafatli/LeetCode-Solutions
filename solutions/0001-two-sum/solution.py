class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for i1, num in enumerate(nums):
            try:
                i2 = nums[i1 + 1:].index(target - num) + i1 + 1
                return [i1, i2]
            except:
                continue

        
