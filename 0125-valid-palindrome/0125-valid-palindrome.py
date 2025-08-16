class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []
        for i in s:
            if i.isalnum() == True  :
                arr.append(i.lower())
        s = "".join(arr)
        n = len(s)
        for i in range(n):
            if s[i] != s[n - i - 1]:
                return False
        return True
        