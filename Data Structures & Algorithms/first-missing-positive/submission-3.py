class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 1 
        if len(nums) == 1 and nums[0] > 1:
            return 1
        
        for i in range(1,len(nums) + 2):
            if i not in nums:
                return i
        return 2