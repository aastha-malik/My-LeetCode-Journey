class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        insert = False
        while i < len(intervals):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i,newInterval )
                insert = True
                break
            i += 1
        if insert == False:
            intervals.append(newInterval)
        
        j = 0
        while j < len(intervals)-1:
            
            if intervals[j][1] >= intervals[j + 1][0]:
                intervals[j][1] = max(intervals[j][1], intervals[j + 1][1])
                intervals.pop(j+1)
            
            else:
                j += 1
                
        return intervals
       