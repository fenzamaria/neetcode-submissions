class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        list2 = []
        for i in range(len(nums)-k+1):
            list1 = []
            for j in range(i, i + k):
                list1.append(nums[j])
            list2.append(max(list1))
        return list2