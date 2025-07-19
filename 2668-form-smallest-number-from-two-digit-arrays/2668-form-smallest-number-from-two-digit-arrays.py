class Solution:
    def minNumber(self, nums1: List[int], nums2: List[int]) -> int:
        arr = []
        for i in nums1:
            if i in set(nums2):
                arr.append(i)
        if len(arr) == 0  :
            a = str(min(nums1))
            b = str(min(nums2))
            num = [a, b]
            num.sort()
            s = "".join(num)
            return int(s)
        else:
            return min(arr)

        