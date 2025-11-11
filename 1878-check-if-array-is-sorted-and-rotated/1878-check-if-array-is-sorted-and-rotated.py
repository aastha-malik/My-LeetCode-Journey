class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = nums.copy()
        arr.sort()
        for i in range(len(nums)+1):
            n = arr[0]
            arr.pop(0)
            arr.append(n)
            if arr == nums:
                return True
        return False
