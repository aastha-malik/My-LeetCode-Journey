class Solution:
    def hasSpecialSubstring(self, s: str, k: int) -> bool:
        if len(s) <= 1:
            return True
        for i in range(len(s)-k+1):
            sub_s = list(set(s[i:i+k]))
            if len(sub_s) == 1 :
                if i == 0:
                    if i + k < len(s) and s[i+k] != s[i]:
                        return True
                    elif i + k == len(s): 
                        return True
                elif i+k == len(s):
                    if s[i-1] != s[i]:
                        return True
                else:
                    if s[i+k] != s[i] and s[i-1] != s[i]:
                        return True
        return False
            
                

                