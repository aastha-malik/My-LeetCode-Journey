class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in d :
                d[s].append(i)
            else:
                d[s] = [i]
        arr = []
        for i in d:
            arr.append(d[i])
        return arr