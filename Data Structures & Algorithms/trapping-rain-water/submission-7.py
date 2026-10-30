class Solution:
    def trap(self, height: List[int]) -> int:
        length = len(height)
        water = 0

        leftMax = [0]
        rightMax = [0]
        highest = height[0]
        for i in range(1,length):
            if height[i - 1] > highest:
                highest = height[i - 1]
            leftMax.append(highest)
        highest = height[length - 1]
        for i in range(length - 2, -1 , -1):
            if height[i + 1] > highest:
                highest = height[i + 1]
            rightMax.append(highest)

        rightMax = rightMax[::-1]
        #print(leftMax)
        #print(rightMax)

        for i in range(len(leftMax)):
            if min(leftMax[i],rightMax[i]) - height[i] >= 0:
                water += min(leftMax[i],rightMax[i]) - height[i]
        return water