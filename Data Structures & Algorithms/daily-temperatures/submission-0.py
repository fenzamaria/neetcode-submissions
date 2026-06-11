class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ls = []
        for i in range(len(temperatures)):
            c = 0
            for j in range(i+1,len(temperatures)):
                if(temperatures[j]>temperatures[i]):
                    c = j-i
                    break
            ls.append(c)
        return ls
                    

