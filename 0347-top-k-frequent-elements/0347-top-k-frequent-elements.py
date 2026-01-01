class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d.keys():
                d[i] = 1
            else:
                d[i] += 1
        bucket = []
        for i in range(len(nums) + 1):
            bucket.append([])
        
        for i, v in d.items():
            bucket[v].append(i)
        
        res = []
        i = len(bucket)-1
        while i > 0:
            if len(bucket[i]) != 0:
                for j in bucket[i]:
                    res.append(j)
            i -= 1
            
        return res[:k]
        