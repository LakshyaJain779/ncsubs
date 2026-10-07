class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num = sorted(nums)
        arr = []
        left = 0 
        print(num)
        while left < len(nums) - 2:
            l = left + 1
            r = len(num) - 1
            while l < r:
                total = num[left] + num[l] + num[r]
                if total > 0:
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    if [num[left], num[l], num[r]] not in arr:
                        arr.append([num[left], num[l], num[r]])
                    r -= 1
                    l += 1

            left += 1

        return arr
