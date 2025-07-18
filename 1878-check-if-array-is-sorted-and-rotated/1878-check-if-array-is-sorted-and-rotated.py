class Solution:
    def check(self, nums: List[int]) -> bool:
        arr = []
        for i in nums:
            arr.append(i)
        arr.sort()
        arr = arr + arr
        l = len(nums)
        for i in range(len(arr)):
            if nums == arr[i:i+l]:
                return True
        return False
            