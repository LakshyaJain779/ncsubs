class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {

        }

        for i,num in enumerate(nums):
            print (i , num)
            if target - num not in seen:
                seen[num] = i

            elif target - num in seen:
                return [seen[target - num], i]
            



        