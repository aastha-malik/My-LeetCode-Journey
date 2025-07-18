class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        x1 = points[0][0]
        x2 = points[1][0]
        x3 = points[2][0]

        y1 = points[0][1]
        y2 = points[1][1]
        y3 = points[2][1]

        arr = []
        for i in points:
            if i not in arr:
                arr.append(i)
        if len(arr) != len(points):
            return False
        else:
        
            if 0.5 * (x1*(y2 - y3) + x2*(y3 - y1) + x3*(y1 - y2) ) == 0:
                return False
            else:
                return True