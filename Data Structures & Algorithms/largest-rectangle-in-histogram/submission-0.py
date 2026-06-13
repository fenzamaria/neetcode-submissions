class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack = []
        maxArea = 0

        for i in range(len(heights)):

            start = i

            while stack and stack[-1][1] > heights[i]:

                index, height = stack.pop()

                area = height * (i - index)

                maxArea = max(maxArea, area)

                start = index

            stack.append((start, heights[i]))

        for index, height in stack:

            area = height * (len(heights) - index)

            maxArea = max(maxArea, area)

        return maxArea