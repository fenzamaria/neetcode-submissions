class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ns=[]
        maxLen =0
        for ch in s:
            if(ch not in ns):
                ns.append(ch)
            else:
                if(len(ns) > maxLen):
                    maxLen = len(ns)
                while ch in ns:
                    ns.pop(0)

                ns.append(ch)

        if len(ns) > maxLen:
            maxLen = len(ns)
        return maxLen
