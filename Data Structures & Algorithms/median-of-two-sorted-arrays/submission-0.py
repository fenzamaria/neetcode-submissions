class Solution:
        def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
                nums = []
                for num in nums1:
                    nums.append(num)
                for num in nums2:
                    nums.append(num)
                nums.sort()
                length = len(nums)
                if length % 2 == 0:
                    return (nums[length//2 - 1] + nums[length//2]) / 2
                return nums[length//2]
                                                                                                    
