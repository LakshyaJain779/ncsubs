class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {

        }

        for num in nums:
            count[num] = 1 + count.get(num,0)
        #print(count)

        arr = []

        highest = 0

        while k != 0:
            num = max(count, key=count.get)
            arr.append(num)
            del count[num]
            k -= 1
            
        return arr