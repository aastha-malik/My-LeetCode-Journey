class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        s = "".join(nums)
        arr = list(s)
        for i in range(len(arr)):
            arr[i] = int(arr[i])
        return arr