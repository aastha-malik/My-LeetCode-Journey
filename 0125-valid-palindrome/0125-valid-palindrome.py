class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = ""
        for i in s:
            if i.isalnum():
                strs = strs + str(i.upper())
        
        for i in range(len(strs)//2):
            if strs[i] != strs[len(strs) - 1 - i]:
                return False
        return True
        