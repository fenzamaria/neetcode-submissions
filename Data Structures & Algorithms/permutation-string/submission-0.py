class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        for i in range(len(s2) - len(s1) + 1):

            stack = list(s1)

            for j in range(i, i + len(s1)):

                if s2[j] in stack:
                    stack.remove(s2[j])

                else:
                    break

            if not stack:
                return True

        return False