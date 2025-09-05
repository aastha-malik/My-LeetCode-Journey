class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        l = len(s1)
        new_s1 = sorted(s1)
        for i in range(len(s2)):
            sub_str = sorted(s2[i:i+l])
            if new_s1 == sub_str :
                return True
        return False
        