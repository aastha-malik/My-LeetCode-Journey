class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        d = {}
        res = []
        ind = {}
        for i in arr:
            a = abs(i-x)
            ind[a] = 0
            if a not in d.keys():
                d[a] = [i]
            else:
                d[a].append(i)
            res.append(a)
        res.sort()

        ans = []
        for i in res[:k]:
            p = ind[i]
            a = d[i]
            ans.append(a[p])
            ind[i] += 1
         
        ans.sort()
        return ans


        
        
        
        

        