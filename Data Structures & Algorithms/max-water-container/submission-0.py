class Solution:
    def maxArea(self, heights):

        maxProduct = 0

        for i in range(len(heights)):

            for j in range(i + 1, len(heights)):

                product = min(heights[i], heights[j]) * (j - i)

                if product > maxProduct:
                    maxProduct = product

        return maxProduct