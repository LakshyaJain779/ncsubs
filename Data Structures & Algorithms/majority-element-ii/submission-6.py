class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        hashmap = {

        }
        
        for num in nums:
            hashmap[num] = 1 + hashmap.get(num,0)
        
        return [i for i in hashmap if hashmap[i] > len(nums)//3]