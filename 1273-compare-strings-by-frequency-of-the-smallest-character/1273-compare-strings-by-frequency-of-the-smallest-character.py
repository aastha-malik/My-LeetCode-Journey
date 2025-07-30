class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        l = len(queries)
        for i in range(l):
            queries[i] = sorted(queries[i])
        
        n = len(words)
        for i in range(n):
            words[i] = sorted(words[i])
        
        res = []
        for i in queries:
            c = i.count(i[0])
            num = 0
            for j in words:
                con = j.count(j[0])
                if c < con:
                    num += 1
            res.append(num)
        return res
        