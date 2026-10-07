class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = []
        addval = []
        for i in range(len(nums)):
            if nums[i] != val:
                result.append(nums[i])

            else:
                addval.append(val)

        lenth = len(result)

        while(len(addval) != 0):
            result.append(addval.pop())

        for i in range(len(nums)):
            nums[i] = result[i]

        return lenth

                