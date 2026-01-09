class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        low = 0
        high = len(nums) - 1
        res = nums[0]
        while low <= high :
            mid = (low + high) // 2
            if nums[mid] <= nums[high]:
                if nums[mid] <= res:
                    res = nums[mid]
                    i = mid
                high = mid - 1
            else:
                low = mid + 1

        #nums[i] is min(nums)
        if target >= nums[0]:
            #left = nums[:i]
            l = 0
            h = i-1
            while l <= h:
                m = (l + h)//2
                if l == h and target != nums[m]:
                    break
                if target == nums[m]:
                    return m
                elif target < nums[m]:
                    h = m-1
                else:
                    l = m + 1

        if target <= nums[-1]:
            #right = nums[i:]
            l = i
            h = len(nums) - 1
            while l <= h:
                m = (l + h)//2
                if l == h and target != nums[m]:
                    break
                if target == nums[m]:
                    return m
                elif target < nums[m]:
                    h = m-1
                else:
                    l = m + 1
                
        return -1
        


        