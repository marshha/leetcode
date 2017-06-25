class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_target_diff = {}
        index = 0
        for num in nums:
            if num in num_target_diff:
                return [num_target_diff[num], index]

            num_target_diff[target - num] = index

            index += 1

