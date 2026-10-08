class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        total_product = 1
        zero_index = []
        length = len(nums)
        for index in range(length):
            if nums[index] == 0:
                zero_index.append(index)
            else:
                total_product *= nums[index]

        if len(zero_index) > 1 :
            return [0] * len(nums)

        if len(zero_index) == 0:
            for index in range(length):
                nums[index] = total_product // nums[index]
            return nums

        nums = [0] * length
        nums[zero_index[0]] = total_product
        return nums
