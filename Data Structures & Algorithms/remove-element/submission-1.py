class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        addval = []
        for i in range(len(nums)):
            if nums[i] != val:
                result.append(nums[i])

            else:
                addval.append(val)

        for i in range(len(result)):
            nums[i] = result[i]

        return len(result)

                