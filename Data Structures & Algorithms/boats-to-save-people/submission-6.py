class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        l = 0
        r = len(people) - 1
        count = 0
        print(people)
        while l <= r:
            total_weight_remaining = limit - people[r]
            r -= 1
            count += 1
            if l <= r and total_weight_remaining >= people[l]:
                l += 1
        return count