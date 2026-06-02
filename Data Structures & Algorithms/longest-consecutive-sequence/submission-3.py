class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        num = sorted(set(nums))

        length = 1
        longest = 1

        for i in range(len(num) - 1):

            if num[i+1] - num[i] == 1:
                length = length + 1

            else:
                length = 1

            if length > longest:
                longest = length

        return longest