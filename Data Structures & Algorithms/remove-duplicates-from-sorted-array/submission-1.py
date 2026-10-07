class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        non_dup = 0
        dup = 1
        
        while (dup < len(nums)):
            if nums[non_dup] != nums[dup]:
                non_dup += 1
                nums[non_dup] = nums[dup]

            dup += 1

        return non_dup + 1