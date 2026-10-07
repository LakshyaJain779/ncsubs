class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        total = 0
        hashmap = {
            0: 1
            }

        for num in nums:
            total += num

            if total - k in hashmap:
                count += hashmap[total - k]

            hashmap[total] = hashmap.get(total, 0) + 1

        return count