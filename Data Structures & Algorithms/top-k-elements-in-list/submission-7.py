class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {

        }

        for num in nums:
            count[num] = 1 + count.get(num,0)
        #print(count)

        arr = []

        for i in range(k):
            num = max(count, key=count.get)
            arr.append(num)
            del count[num]

        return arr