class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        out = []
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if(numbers[i]+numbers[j]==target):
                    out.append(i+1)
                    out.append(j+1)
        return out 