class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = []
        one = []
        two = []
        for i in nums:
            if i == 0:
                zero.append(i)
            elif i == 1:
                one.append(i)
            elif i == 2:
                two.append(i)
        arr = zero + one + two
        for i in range(len(nums)):
            nums[i] = arr[i]

        



        