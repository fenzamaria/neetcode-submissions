class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        st = []

        for i in strs:
            temp = []

            for j in strs:
                if len(i) == len(j) and Counter(i) == Counter(j):
                    temp.append(j)

            if temp not in st:
                st.append(temp)

        return st