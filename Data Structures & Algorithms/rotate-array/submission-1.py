class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k % len(nums)):
            key = nums[len(nums) - 1]
            for j in range(len(nums) - 2, -1,-1):
                nums[j + 1] = nums[j]
            nums[j] = key
        
