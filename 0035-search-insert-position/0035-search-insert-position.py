class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return 0
        if target > nums[-1]:
            return len(nums)
        less = 0
        less_ind = 0
        low = 0
        high = len(nums)-1
        while low <= high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                less = nums[mid]
                less_ind = mid
                low = mid +1
            else:
                high = mid - 1
                
        return less_ind+1

        