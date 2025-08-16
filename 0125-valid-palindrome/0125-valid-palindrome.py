class Solution:
    def isPalindrome(self, s: str) -> bool:
        for i in s:
            if i.isalnum() == False  :
                s = s.replace(i, "")
        s = s.lower()
        n = len(s)
        for i in range(n):
            if s[i] != s[n - i - 1]:
                return False
        return True
        