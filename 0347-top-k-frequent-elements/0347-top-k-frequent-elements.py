class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = list(set(nums))
        c = []
        for i in arr:
            n = nums.count(i)
            c.append([n, i])
        c.sort(reverse=True)
        res = []
        for i in range(k):
            res.append(c[i][1])
        return res


