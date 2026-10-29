class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1
        most = 0
        while(l < r):
            lower = heights[l]
            if heights[r] < lower:
                lower = heights[r]
            if lower * (r - l) > most:
                most = lower * (r - l)
                print(lower,r,l)
            
            if heights[l] < heights[r]:
                l+=1 
            elif heights[r] < heights[l]:
                r-=1
            else:
                l += 1
                r -= 1
        
        return most
            
            