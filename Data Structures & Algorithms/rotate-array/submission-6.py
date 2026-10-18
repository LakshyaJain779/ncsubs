class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rot(start,end):
            l = start
            r = end - 1
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        
        rot(0,len(nums))
        rot(0,k % len(nums))
        rot(k % len(nums), len(nums))
        
