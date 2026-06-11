class Solution:
    def minWindow(self, s: str, t: str) -> str:

        answer = ""

        for i in range(len(s)):

            stack = list(t)

            for j in range(i, len(s)):

                if s[j] in stack:
                    stack.remove(s[j])

                if not stack:

                    window = s[i:j+1]

                    if answer == "" or len(window) < len(answer):
                        answer = window

                    break

        return answer