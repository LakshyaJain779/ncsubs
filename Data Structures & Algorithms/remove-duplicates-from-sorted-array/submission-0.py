class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        hmap = {

        }

        index = 0

        for num in nums:
            if num not in hmap:
                hmap[num] = 1
                nums[index] = num
                index += 1

        return len(hmap)
            
