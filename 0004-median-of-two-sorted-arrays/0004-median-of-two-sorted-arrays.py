class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums = nums1 + nums2
        nums.sort()
        if len(nums) == 1:
            return float(nums[0])
        if len(nums) % 2 == 0:
            i = len(nums) // 2
            return (nums[i] + nums[i-1]) / 2
        else:
            i = len(nums) // 2
            return float(nums[i])
        