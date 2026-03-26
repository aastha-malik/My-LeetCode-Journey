class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d = {}
        res = set()
        for i in arr:
            a = abs(i-x)
            
            if a not in d.keys():
                d[a] = [i]
            else:
                d[a].append(i)
            res.add(a)
        res = list(res)
        res.sort()

        ans = []
        for i in res:
            
            a = d[i]
            for p in a:
                ans.append(p)
                if len(ans) == k:
                    ans.sort()
                    return ans
        ans.sort()
        return ans


        
        
        
        

        