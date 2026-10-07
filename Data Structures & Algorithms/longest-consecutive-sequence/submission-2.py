class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sort_nums = sorted(nums)
        count = highest = 0
        print(sort_nums)
        if len(nums) == 0:
            return 0
        for num in range(len(sort_nums) - 1):
            

            if sort_nums[num] == sort_nums[num + 1]:
                pass

            elif sort_nums[num] + 1 == sort_nums[num + 1]:
                count += 1

            else:
                count = 0

            if highest < count:
                    highest = count 
        return highest + 1