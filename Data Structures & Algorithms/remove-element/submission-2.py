class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        r = len(nums) - 1
        chking = 0

        def swap(a,b):
            nums[a],nums[b] = nums[b], nums[a]

        while chking <= r:
            if nums[chking] == val:
                swap(chking,r)
                chking -= 1
                r -= 1

            chking +=1

        return chking

                