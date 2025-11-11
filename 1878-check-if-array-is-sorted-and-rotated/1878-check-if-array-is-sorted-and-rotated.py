class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = nums.copy()
        arr.sort()
        if nums == arr:
            return True
        else:
            l = len(nums)
            arr = arr + arr
            for i in range(l):
                if arr[i:i+l] == nums:
                    return True
            return False