class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {

        }
        
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num,0)

        if len(nums) < 3:
            return list(set(nums))
        
        print(hashmap)
        nums2 = []
        for key,val in hashmap.items():
            if val > len(nums) // 3:
                nums2.append(key)

        return nums2