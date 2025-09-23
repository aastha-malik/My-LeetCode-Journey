class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = version1.split(".")
        v2 = version2.split(".")
        if len(v1) < len(v2):
            x = len(v2) - len(v1)
            for i in range(x):
                v1.append("0")
        if len(v1) > len(v2):
            x = len(v1) - len(v2)
            for i in range(x):
                v2.append("0")
        i = 0
        l = len(v1)
        while i < l:
            if int(v1[i]) > int(v2[i]) :
                return 1
            elif int(v1[i]) < int(v2[i]) :
                return -1
            else:
                i+= 1
        return 0
        
        