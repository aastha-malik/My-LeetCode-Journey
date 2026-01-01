class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            s = "".join(sorted(i))
            if s not in d.keys():
                d[s] = [i]
            else:
                d[s].append(i)

            
        res = []
        for i in  d.values():
            res.append(i)
            
        return res
