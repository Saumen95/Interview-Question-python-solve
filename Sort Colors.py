class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = [0] * 3
        for num in nums:
            count[num] += 1
        i = 0
        for j in range(3):
            for _ in range(count[j]):
                nums[i] = j
