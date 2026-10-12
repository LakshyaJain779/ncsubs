class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        arr = []
        nums.sort()

        LEFT = 0
        while(LEFT < len(nums) - 3):
            LEFT2 = LEFT + 1
            while (LEFT2 < len(nums) - 2):
                l = LEFT2 + 1
                r = len(nums) - 1
                while(l < r):
                    total = nums[LEFT] + nums[LEFT2] + nums[l] + nums[r]

                    if total > target:
                        r -= 1
                    elif total < target:
                        l += 1
                    else:
                        if [nums[LEFT], nums[LEFT2] , nums[l] , nums[r]] not in arr:
                            arr.append([nums[LEFT], nums[LEFT2] , nums[l] , nums[r]])
                        l += 1
                        r -= 1
                LEFT2 += 1
            LEFT += 1

        return arr
