class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        l = len(nums)
        low = 0
        high = l-1
        while low <= high:
            mid = (low + high) // 2
            if mid  >= nums[mid]:
                if mid == nums[mid-1]:
                    return nums[mid]
                else:
                    high = mid - 1
            else:
                if mid != l-1 and mid == nums[mid+1]:
                    return nums[mid]
                else:
                    low = mid + 1
