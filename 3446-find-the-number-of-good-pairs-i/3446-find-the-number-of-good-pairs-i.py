class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        res = 0
        for i in nums1:
            for j in nums2:
                n = j * k
                if i % n == 0:
                    res += 1
        return res
        