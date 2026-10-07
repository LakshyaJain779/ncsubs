class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(a,b):
            nums[a], nums[b] = nums[b], nums[a]


        l = 0
        r = len(nums) - 1
        chking = 0

        while chking <= r:
            if nums[chking] == 0:
                swap(chking,l)
                l += 1
                
            elif nums[chking] == 2:
                swap(chking,r)
                r -= 1
                chking -= 1

            chking += 1


            
