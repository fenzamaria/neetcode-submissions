class Solution:
    def trap(self, height):

        amt = 0

        for i in range(1, len(height) - 1):

            leftMax = max(height[:i])

            rightMax = max(height[i+1:])

            water = min(leftMax, rightMax) - height[i]

            if water > 0:
                amt += water

        return amt