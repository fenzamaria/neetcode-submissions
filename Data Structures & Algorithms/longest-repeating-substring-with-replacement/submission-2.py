class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxLength = 0

        for ch in set(s):

            left = 0
            changes = 0

            for right in range(len(s)):

                if s[right] != ch:
                    changes += 1

                while changes > k:

                    if s[left] != ch:
                        changes -= 1

                    left += 1

                length = right - left + 1

                if length > maxLength:
                    maxLength = length

        return maxLength