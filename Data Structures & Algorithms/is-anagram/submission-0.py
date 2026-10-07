class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = {

        }

        if len(s) != len(t):
            return False

        for ls in s:
            if ls not in count:
                count[ls] = 1
            else:
                count[ls] += 1

        for lt in t:
            if lt not in count:
                return False
            
            elif count[lt] == 1:
                del count[lt]

            else:
                count[lt] -= 1
        
        if len(count) == 0:
            return True

        return False